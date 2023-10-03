# Notas de desarrollo de la biblioteca HAL - Comunicación I2C (MPU6050)

Este artículo se basa en el kit de desarrollo RobotCtrl de desarrollo propio, con un núcleo de microcontrolador STM32F407ZET6, y utiliza el módulo MPU6050 para explicar el método de comunicación I2C de la biblioteca HAL. Para obtener información detallada sobre el esquema del kit de desarrollo y una introducción detallada, consulte [**RobotCtrl - STM32 Kit de desarrollo universal**](https://wiki-power.com/es/RobotCtrl-STM32%E9%80%9A%E7%94%A8%E5%BC%80%E5%8F%91%E5%A5%97%E4%BB%B6).

## Principios básicos

### Comunicación I2C

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20211026174634.png)

Para obtener información sobre los principios básicos de la comunicación I2C, consulte el artículo [**Protocolo de comunicación - I2C**](https://wiki-power.com/es/%E9%80%9A%E4%BF%A1%E5%8D%8F%E8%AE%AE-I2C).

### Módulo MPU6050

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220404145145.png)

Definición de pines del módulo:

- VCC: 3.3V~5V
- GND: Tierra
- SCL: Reloj I2C / Reloj SPI
- SDA: Datos I2C / Entrada de datos SPI
- XDA: Proporciona un reloj principal para el dispositivo I2C
- AD0: Bit de selección de dirección del dispositivo I2C / Salida de datos SPI
- INT: Pin de interrupción

### Biblioteca MPU6050 con filtro de Kalman

Aquí utilizamos la biblioteca MPU6050 con filtro de Kalman: [**leech001/MPU6050**](https://github.com/leech001/MPU6050). Copie los archivos `mpu6050.c` y `mpu6050.h` descargados en la carpeta del proyecto y agréguelos al proyecto en STM32CubeIDE/Keil:

```c title="mpu6050.h"

#ifndef INC_GY521_H_
#define INC_GY521_H_

#endif /* INC_GY521_H_ */

#include <stdint.h>
#include "i2c.h"

// Estructura MPU6050
typedef struct
{

    int16_t Accel_X_RAW;
    int16_t Accel_Y_RAW;
    int16_t Accel_Z_RAW;
    double Ax;
    double Ay;
    double Az;

    int16_t Gyro_X_RAW;
    int16_t Gyro_Y_RAW;
    int16_t Gyro_Z_RAW;
    double Gx;
    double Gy;
    double Gz;

    float Temperature;

    double KalmanAngleX;
    double KalmanAngleY;
} MPU6050_t;

// Estructura Kalman
typedef struct
{
    double Q_angle;
    double Q_bias;
    double R_measure;
    double angle;
    double bias;
    double P[2][2];
} Kalman_t;

uint8_t MPU6050_Init(I2C_HandleTypeDef *I2Cx);

void MPU6050_Read_Accel(I2C_HandleTypeDef *I2Cx, MPU6050_t *DataStruct);

void MPU6050_Read_Gyro(I2C_HandleTypeDef *I2Cx, MPU6050_t *DataStruct);

La función `MPU6050_Read_Temp` lee la temperatura del sensor MPU6050 y la almacena en la estructura `DataStruct`. La función `MPU6050_Read_All` lee los valores de aceleración, giroscopio y temperatura del sensor MPU6050 y los almacena en la estructura `DataStruct`. La función `Kalman_getAngle` utiliza el filtro de Kalman para calcular el ángulo a partir de los valores de ángulo, velocidad y tiempo. 

El archivo `mpu6050.c` contiene las definiciones de las constantes y variables utilizadas en el código. También se define la dirección del sensor MPU6050 y se inicializan las variables del filtro de Kalman. La función `MPU6050_Init` inicializa el sensor MPU6050 y configura la tasa de datos y el registro de gestión de energía.

void MPU6050_Init(I2C_HandleTypeDef *I2Cx)
{
    uint8_t Data;

    // Configuración del acelerómetro en el registro ACCEL_CONFIG
    // XA_ST=0, YA_ST=0, ZA_ST=0, FS_SEL=0 -> ±2g
    Data = 0x00;
    HAL_I2C_Mem_Write(I2Cx, MPU6050_ADDR, ACCEL_CONFIG_REG, 1, &Data, 1, i2c_timeout);

    // Configuración del giroscopio en el registro GYRO_CONFIG
    // XG_ST=0, YG_ST=0, ZG_ST=0, FS_SEL=0 -> ±250 °/s
    Data = 0x00;
    HAL_I2C_Mem_Write(I2Cx, MPU6050_ADDR, GYRO_CONFIG_REG, 1, &Data, 1, i2c_timeout);
    return 0;
    }
    return 1;
}

void MPU6050_Read_Accel(I2C_HandleTypeDef *I2Cx, MPU6050_t *DataStruct)
{
    uint8_t Rec_Data[6];

    // Leer 6 BYTES de datos a partir del registro ACCEL_XOUT_H

    HAL_I2C_Mem_Read(I2Cx, MPU6050_ADDR, ACCEL_XOUT_H_REG, 1, Rec_Data, 6, i2c_timeout);

    DataStruct->Accel_X_RAW = (int16_t)(Rec_Data[0] << 8 | Rec_Data[1]);
    DataStruct->Accel_Y_RAW = (int16_t)(Rec_Data[2] << 8 | Rec_Data[3]);
    DataStruct->Accel_Z_RAW = (int16_t)(Rec_Data[4] << 8 | Rec_Data[5]);

    /*** convertir los valores RAW en aceleración en 'g'
         tenemos que dividir según el valor de escala completa establecido en FS_SEL
         He configurado FS_SEL = 0. Así que estoy dividiendo por 16384.0
         para más detalles, consulte el registro ACCEL_CONFIG              ****/

    DataStruct->Ax = DataStruct->Accel_X_RAW / 16384.0;
    DataStruct->Ay = DataStruct->Accel_Y_RAW / 16384.0;
    DataStruct->Az = DataStruct->Accel_Z_RAW / Accel_Z_corrector;
}

void MPU6050_Read_Gyro(I2C_HandleTypeDef *I2Cx, MPU6050_t *DataStruct)
{
    uint8_t Rec_Data[6];

    // Leer 6 BYTES de datos a partir del registro GYRO_XOUT_H

    HAL_I2C_Mem_Read(I2Cx, MPU6050_ADDR, GYRO_XOUT_H_REG, 1, Rec_Data, 6, i2c_timeout);

DataStruct->Gyro_X_RAW = (int16_t)(Rec_Data[0] << 8 | Rec_Data[1]);
DataStruct->Gyro_Y_RAW = (int16_t)(Rec_Data[2] << 8 | Rec_Data[3]);
DataStruct->Gyro_Z_RAW = (int16_t)(Rec_Data[4] << 8 | Rec_Data[5]);

/*** convertir los valores RAW en dps (�/s)
     tenemos que dividir según el valor de escala completa establecido en FS_SEL
     He configurado FS_SEL = 0. Así que estoy dividiendo por 131.0
     para más detalles, consulte el registro GYRO_CONFIG              ****/

DataStruct->Gx = DataStruct->Gyro_X_RAW / 131.0;
DataStruct->Gy = DataStruct->Gyro_Y_RAW / 131.0;
DataStruct->Gz = DataStruct->Gyro_Z_RAW / 131.0;
}

void MPU6050_Read_Temp(I2C_HandleTypeDef *I2Cx, MPU6050_t *DataStruct)
{
    uint8_t Rec_Data[2];
    int16_t temp;

    // Leer 2 BYTES de datos a partir del registro TEMP_OUT_H_REG

    HAL_I2C_Mem_Read(I2Cx, MPU6050_ADDR, TEMP_OUT_H_REG, 1, Rec_Data, 2, i2c_timeout);

    temp = (int16_t)(Rec_Data[0] << 8 | Rec_Data[1]);
    DataStruct->Temperature = (float)((int16_t)temp / (float)340.0 + (float)36.53);
}

void MPU6050_Read_All(I2C_HandleTypeDef *I2Cx, MPU6050_t *DataStruct)
{
    uint8_t Rec_Data[14];
    int16_t temp;

    // Leer 14 BYTES de datos a partir del registro ACCEL_XOUT_H

    HAL_I2C_Mem_Read(I2Cx, MPU6050_ADDR, ACCEL_XOUT_H_REG, 1, Rec_Data, 14, i2c_timeout);

DataStruct->Accel_X_RAW = (int16_t)(Rec_Data[0] << 8 | Rec_Data[1]);
DataStruct->Accel_Y_RAW = (int16_t)(Rec_Data[2] << 8 | Rec_Data[3]);
DataStruct->Accel_Z_RAW = (int16_t)(Rec_Data[4] << 8 | Rec_Data[5]);
temp = (int16_t)(Rec_Data[6] << 8 | Rec_Data[7]);
DataStruct->Gyro_X_RAW = (int16_t)(Rec_Data[8] << 8 | Rec_Data[9]);
DataStruct->Gyro_Y_RAW = (int16_t)(Rec_Data[10] << 8 | Rec_Data[11]);
DataStruct->Gyro_Z_RAW = (int16_t)(Rec_Data[12] << 8 | Rec_Data[13]);

DataStruct->Ax = DataStruct->Accel_X_RAW / 16384.0;
DataStruct->Ay = DataStruct->Accel_Y_RAW / 16384.0;
DataStruct->Az = DataStruct->Accel_Z_RAW / Accel_Z_corrector;
DataStruct->Temperature = (float)((int16_t)temp / (float)340.0 + (float)36.53);
DataStruct->Gx = DataStruct->Gyro_X_RAW / 131.0;
DataStruct->Gy = DataStruct->Gyro_Y_RAW / 131.0;
DataStruct->Gz = DataStruct->Gyro_Z_RAW / 131.0;

// Solución del ángulo de Kalman
double dt = (double)(HAL_GetTick() - timer) / 1000;
timer = HAL_GetTick();
double roll;
double roll_sqrt = sqrt(
    DataStruct->Accel_X_RAW * DataStruct->Accel_X_RAW + DataStruct->Accel_Z_RAW * DataStruct->Accel_Z_RAW);
if (roll_sqrt != 0.0)
{
    roll = atan(DataStruct->Accel_Y_RAW / roll_sqrt) * RAD_TO_DEG;
}
else
{
    roll = 0.0;
}
double pitch = atan2(-DataStruct->Accel_X_RAW, DataStruct->Accel_Z_RAW) * RAD_TO_DEG;
if ((pitch < -90 && DataStruct->KalmanAngleY > 90) || (pitch > 90 && DataStruct->KalmanAngleY < -90))
{
    KalmanY.angle = pitch;
    DataStruct->KalmanAngleY = pitch;
}
else
{
    DataStruct->KalmanAngleY = Kalman_getAngle(&KalmanY, pitch, DataStruct->Gy, dt);
}
if (fabs(DataStruct->KalmanAngleY) > 90)
    DataStruct->Gx = -DataStruct->Gx;
DataStruct->KalmanAngleX = Kalman_getAngle(&KalmanX, roll, DataStruct->Gx, dt);
}

double Kalman_getAngle(Kalman_t *Kalman, double newAngle, double newRate, double dt)
{
    double rate = newRate - Kalman->bias;
    Kalman->angle += dt * rate;

    Kalman->P[0][0] += dt * (dt * Kalman->P[1][1] - Kalman->P[0][1] - Kalman->P[1][0] + Kalman->Q_angle);
    Kalman->P[0][1] -= dt * Kalman->P[1][1];
    Kalman->P[1][0] -= dt * Kalman->P[1][1];
    Kalman->P[1][1] += Kalman->Q_bias * dt;

    double S = Kalman->P[0][0] + Kalman->R_measure;
    double K[2];
    K[0] = Kalman->P[0][0] / S;
    K[1] = Kalman->P[1][0] / S;

    double y = newAngle - Kalman->angle;
    Kalman->angle += K[0] * y;
    Kalman->bias += K[1] * y;

    double P00_temp = Kalman->P[0][0];
    double P01_temp = Kalman->P[0][1];

Cómo usar el MPU6050 con I2C en STM32

El MPU6050 es un sensor de movimiento de seis ejes que combina un acelerómetro de tres ejes y un giroscopio de tres ejes en un solo chip. En este tutorial, aprenderás cómo usar el MPU6050 con I2C en STM32.

## Conexión del MPU6050 con STM32

La conexión del MPU6050 con STM32 se realiza mediante el protocolo I2C. Los pines SDA y SCL del MPU6050 se conectan a los pines SDA y SCL del STM32, respectivamente. Además, se debe conectar la alimentación y la tierra.

## Configuración del MPU6050 en STM32

Para configurar el MPU6050 en STM32, se puede utilizar una biblioteca de terceros. En este tutorial, utilizaremos la biblioteca de [leech001/MPU6050](https://github.com/leech001/MPU6050).

Primero, descarga la biblioteca y agrega los archivos `mpu6050.c` y `mpu6050.h` a tu proyecto STM32. Luego, incluye el archivo `mpu6050.h` en tu archivo `main.c`.

A continuación, inicializa el MPU6050 en la función `main()` de la siguiente manera:

```c
while (MPU6050_Init(&hi2c1) == 1);
```

Esta función inicializa el MPU6050 y devuelve `1` si hay un error.

Después de inicializar el MPU6050, puedes leer los valores del acelerómetro y el giroscopio utilizando la función `MPU6050_Read_All()`. Por ejemplo:

```c
MPU6050_Read_All(&hi2c1, &MPU6050);
```

Esta función lee los valores del acelerómetro y el giroscopio y los guarda en la estructura `MPU6050_t`.

## Filtro de Kalman

El filtro de Kalman es un algoritmo utilizado para estimar el estado de un sistema dinámico a partir de una serie de mediciones incompletas y ruidosas. En este tutorial, utilizaremos el filtro de Kalman para filtrar los valores del MPU6050.

La biblioteca de [leech001/MPU6050](https://github.com/leech001/MPU6050) ya incluye el filtro de Kalman. Puedes obtener el ángulo filtrado utilizando la función `MPU6050_GetAngle()`. Por ejemplo:

```c
double angle = MPU6050_GetAngle(&MPU6050, dt);
```

Esta función devuelve el ángulo filtrado y toma como argumento el tiempo transcurrido desde la última llamada a la función.

## Uso de I2C para leer la información devuelta por el MPU6050

Para leer la información devuelta por el MPU6050 utilizando I2C, primero debes configurar el bus I2C en CubeMX. Luego, en tu código, inicializa el objeto MPU6050 y lee sus valores utilizando la función `MPU6050_Read_All()`.

```c
MPU6050_t MPU6050;

while (MPU6050_Init(&hi2c1) == 1);

while (1)
{
    MPU6050_Read_All(&hi2c1, &MPU6050);
    HAL_Delay(100);
}
```

Después de leer los valores, puedes acceder a ellos a través de la estructura `MPU6050_t`. Por ejemplo:

```c
printf("XAngle: %.2f°\t", MPU6050.KalmanAngleX);
```

## Referencias y agradecimientos

- [leech001/MPU6050](https://github.com/leech001/MPU6050)
- [I2C Communication Protocol](https://wiki-power.com/es/%E9%80%9A%E4%BF%A1%E5%8D%8F%E8%AE%AE-I2C)

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.