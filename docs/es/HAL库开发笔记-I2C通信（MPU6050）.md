# Notas de desarrollo de la biblioteca HAL - Comunicación I2C (MPU6050)

En esta entrada, basada en el kit de desarrollo RobotCtrl de desarrollo propio, con un núcleo de microcontrolador STM32F407ZET6, se explicará el método de comunicación I2C utilizando el módulo MPU6050 y la biblioteca HAL. Para obtener el esquema del kit de desarrollo y una descripción detallada, por favor visite [**RobotCtrl - STM32 Kit de Desarrollo Universal**](https://wiki-power.com/RobotCtrl-STM32%E9%80%9A%E7%94%A8%E5%BC%80%E5%8F%91%E5%A5%97%E4%BB%B6).

## Principios Básicos

### Comunicación I2C

![Diagrama de la comunicación I2C](https://media.wiki-power.com/img/20211026174634.png)

Puede encontrar los principios básicos de la comunicación I2C en el artículo [**Protocolo de Comunicación - I2C**](https://wiki-power.com/%E9%80%9A%E4%BF%A1%E5%8D%8F%E8%AE%AE-I2C).

### Módulo MPU6050

![Módulo MPU6050](https://media.wiki-power.com/img/20220404145145.png)

Definición de los pines del módulo:

- VCC: 3.3V~5V
- GND: Conexión a tierra
- SCL: Reloj I2C / Reloj SPI
- SDA: Datos I2C / Entrada de datos SPI
- XDA: Generador de reloj principal para dispositivos I2C
- AD0: Bit de selección de dirección del dispositivo I2C / Salida de datos SPI
- INT: Pin de interrupción

### Biblioteca MPU6050 con filtro de Kalman

En este caso, estamos utilizando la biblioteca MPU6050 con filtro de Kalman, que se encuentra en el siguiente enlace: [**leech001/MPU6050**](https://github.com/leech001/MPU6050). Debe descargar los archivos `mpu6050.c` y `mpu6050.h` y copiarlos en la carpeta de su proyecto. Luego, agréguelos al proyecto en STM32CubeIDE/Keil de la siguiente manera:

```c title="mpu6050.h"

#ifndef INC_GY521_H_
#define INC_GY521_H_

#endif /* INC_GY521_H_ */

#include <stdint.h>
#include "i2c.h"

// Estructura de MPU6050
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

// Estructura de Kalman
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

void MPU6050_Read_Temp(I2C_HandleTypeDef *I2Cx, MPU6050_t *DataStruct);
```

```c title="mpu6050.c"
#include <math.h>
#include "mpu6050.h"

#define RAD_TO_DEG 57.295779513082320876798154814105

#define WHO_AM_I_REG 0x75
#define PWR_MGMT_1_REG 0x6B
#define SMPLRT_DIV_REG 0x19
#define ACCEL_CONFIG_REG 0x1C
#define ACCEL_XOUT_H_REG 0x3B
#define TEMP_OUT_H_REG 0x41
#define GYRO_CONFIG_REG 0x1B
#define GYRO_XOUT_H_REG 0x43

// Configurar MPU6050
#define MPU6050_ADDR 0xD0
const uint16_t i2c_timeout = 100;
const double Accel_Z_corrector = 14418.0;

uint32_t timer;

Kalman_t KalmanX = {
    .Q_angle = 0.001f,
    .Q_bias = 0.003f,
    .R_measure = 0.03f
};

Kalman_t KalmanY = {
    .Q_angle = 0.001f,
    .Q_bias = 0.003f,
    .R_measure = 0.03f
};

uint8_t MPU6050_Init(I2C_HandleTypeDef *I2Cx)
{
    uint8_t check;
    uint8_t Data;

    // Comprobar el ID del dispositivo WHO_AM_I

    HAL_I2C_Mem_Read(I2Cx, MPU6050_ADDR, WHO_AM_I_REG, 1, &check, 1, i2c_timeout);

    if (check == 104) // El valor 0x68 será devuelto por el sensor si todo va bien
    {
        // Registro de gestión de energía 0X6B, debemos escribir todos los 0's para despertar el sensor
        Data = 0;
        HAL_I2C_Mem_Write(I2Cx, MPU6050_ADDR, PWR_MGMT_1_REG, 1, &Data, 1, i2c_timeout);

        // Configurar la TASA DE DATOS a 1KHz escribiendo en el registro SMPLRT_DIV
        Data = 0x07;
        HAL_I2C_Mem_Write(I2Cx, MPU6050_ADDR, SMPLRT_DIV_REG, 1, &Data, 1, i2c_timeout);

        // Configurar la aceleración en el Registro ACCEL_CONFIG
        // XA_ST=0, YA_ST=0, ZA_ST=0, FS_SEL=0 -> ± 2g
        Data = 0x00;
        HAL_I2C_Mem_Write(I2Cx, MPU6050_ADDR, ACCEL_CONFIG_REG, 1, &Data, 1, i2c_timeout);
```

````markdown
```markdown
// Establecer la configuración giroscópica en el registro GYRO_CONFIG
// XG_ST=0, YG_ST=0, ZG_ST=0, FS_SEL=0 -> ± 250 °/s
Datos = 0x00;
HAL_I2C_Mem_Write(I2Cx, MPU6050_ADDR, GYRO_CONFIG_REG, 1, &Datos, 1, i2c_timeout);
return 0;
}
return 1;
}

void MPU6050_Leer_Aceleracion(I2C_HandleTypeDef *I2Cx, MPU6050_t *EstructuraDatos)
{
uint8_t DatosRecibidos[6];

    // Leer 6 BYTES de datos a partir del registro ACCEL_XOUT_H

    HAL_I2C_Mem_Read(I2Cx, MPU6050_ADDR, ACCEL_XOUT_H_REG, 1, DatosRecibidos, 6, i2c_timeout);

    EstructuraDatos->Accel_X_RAW = (int16_t)(DatosRecibidos[0] << 8 | DatosRecibidos[1]);
    EstructuraDatos->Accel_Y_RAW = (int16_t)(DatosRecibidos[2] << 8 | DatosRecibidos[3]);
    EstructuraDatos->Accel_Z_RAW = (int16_t)(DatosRecibidos[4] << 8 | DatosRecibidos[5]);

    /*** Convertir los valores RAW en aceleración en 'g'
         Debemos dividir según el valor de escala completa configurado en FS_SEL
         He configurado FS_SEL = 0. Por lo tanto, estoy dividiendo por 16384.0
         Para obtener más detalles, consulte el registro ACCEL_CONFIG       ****/

    EstructuraDatos->Ax = EstructuraDatos->Accel_X_RAW / 16384.0;
    EstructuraDatos->Ay = EstructuraDatos->Accel_Y_RAW / 16384.0;
    EstructuraDatos->Az = EstructuraDatos->Accel_Z_RAW / Accel_Z_corrector;

}

void MPU6050_Leer_Giroscopio(I2C_HandleTypeDef *I2Cx, MPU6050_t *EstructuraDatos)
{
uint8_t DatosRecibidos[6];

    // Leer 6 BYTES de datos a partir del registro GYRO_XOUT_H

    HAL_I2C_Mem_Read(I2Cx, MPU6050_ADDR, GYRO_XOUT_H_REG, 1, DatosRecibidos, 6, i2c_timeout);

    EstructuraDatos->Gyro_X_RAW = (int16_t)(DatosRecibidos[0] << 8 | DatosRecibidos[1]);
    EstructuraDatos->Gyro_Y_RAW = (int16_t)(DatosRecibidos[2] << 8 | DatosRecibidos[3]);
    EstructuraDatos->Gyro_Z_RAW = (int16_t)(DatosRecibidos[4] << 8 | DatosRecibidos[5]);
```
````

```markdown
/**_ Convierte los valores RAW en grados por segundo (°/s)
Debemos dividirlos según el valor de escala completo configurado en FS_SEL.
He configurado FS_SEL = 0. Por lo tanto, estoy dividiendo por 131.0.
Para obtener más detalles, consulta el registro de configuración GYRO_CONFIG.
_**/

DataStruct->Gx = DataStruct->Gyro_X_RAW / 131.0;
DataStruct->Gy = DataStruct->Gyro_Y_RAW / 131.0;
DataStruct->Gz = DataStruct->Gyro_Z_RAW / 131.0;
}

void MPU6050_Read_Temp(I2C_HandleTypeDef *I2Cx, MPU6050_t *DataStruct)
{
uint8_t Rec_Data[2];
int16_t temp;

    // Lee 2 BYTES de datos comenzando desde el registro TEMP_OUT_H_REG

    HAL_I2C_Mem_Read(I2Cx, MPU6050_ADDR, TEMP_OUT_H_REG, 1, Rec_Data, 2, i2c_timeout);

    temp = (int16_t)(Rec_Data[0] << 8 | Rec_Data[1]);
    DataStruct->Temperature = (float)((int16_t)temp / (float)340.0 + (float)36.53);

}

void MPU6050_Read_All(I2C_HandleTypeDef *I2Cx, MPU6050_t *DataStruct)
{
uint8_t Rec_Data[14];
int16_t temp;

    // Lee 14 BYTES de datos comenzando desde el registro ACCEL_XOUT_H

    HAL_I2C_Mem_Read(I2Cx, MPU6050_ADDR, ACCEL_XOUT_H_REG, 1, Rec_Data, 14, i2c_timeout);

    DataStruct->Accel_X_RAW = (int16_t)(Rec_Data[0] << 8 | Rec_Data[1]);
    DataStruct->Accel_Y_RAW = (int16_t)(Rec_Data[2] << 8 | Rec_Data[3]);
    DataStruct->Accel_Z_RAW = (int16_t)(Rec_Data[4] << 8 | Rec_Data[5]);
    temp = (int16_t)(Rec_Data[6] << 8 | Rec_Data[7]);
    DataStruct->Gyro_X_RAW = (int16_t)(Rec_Data[8] << 8 | Rec_Data[9]);
    DataStruct->Gyro_Y_RAW = (int16_t)(Rec_Data[10] << 8 | Rec_Data[11]);
    DataStruct->Gyro_Z_RAW = (int16_t)(Rec_Data[12] << 8 | Rec_Data[13]);

}
```

````markdown
```spanish
    DataStruct->Ax = DataStruct->Accel_X_RAW / 16384.0;
    DataStruct->Ay = DataStruct->Accel_Y_RAW / 16384.0;
    DataStruct->Az = DataStruct->Accel_Z_RAW / Accel_Z_corrector;
    DataStruct->Temperature = (float)((int16_t)temp / (float)340.0 + (float)36.53);
    DataStruct->Gx = DataStruct->Gyro_X_RAW / 131.0;
    DataStruct->Gy = DataStruct->Gyro_Y_RAW / 131.0;
    DataStruct->Gz = DataStruct->Gyro_Z_RAW / 131.0;

    // Resolución del ángulo de Kalman
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
```
````

```c
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

    Kalman->P[0][0] -= K[0] * P00_temp;
    Kalman->P[0][1] -= K[0] * P01_temp;
    Kalman->P[1][0] -= K[1] * P00_temp;
    Kalman->P[1][1] -= K[1] * P01_temp;

    return Kalman->angle;
};
```

Puedes observar que en este código se están realizando operaciones matriciales y cálculos relacionados con el filtro de Kalman para estimar un ángulo. Además, se utilizan diversas variables y matrices, como `Kalman`, `dt`, `S`, `K`, `y`, `newAngle`, etc.

El código también incluye una función `MPU6050_Read_All` que se utiliza para leer datos de un sensor MPU6050 a través de una interfaz I2C.

Por favor, házme saber si necesitas alguna aclaración adicional o si deseas que traduzca alguna parte específica del código.

````markdown
```c
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
```
````

Una vez que hayas configurado la comunicación serie, puedes utilizar la siguiente instrucción para mostrar los valores de las variables:

```c
printf("Ángulo X: %.2f°\t", MPU6050.KalmanAngleX);
```

## Referencias y Agradecimientos

- [leech001/MPU6050](https://github.com/leech001/MPU6050)
- [Protocolo de Comunicación - I2C](https://wiki-power.com/%E9%80%9A%E4%BF%A1%E5%8D%8F%E8%AE%AE-I2C)

> Dirección original del artículo: <https://wiki-power.com/>
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

```

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
```
