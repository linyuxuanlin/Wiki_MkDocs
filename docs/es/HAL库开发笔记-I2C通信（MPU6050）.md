```markdown
# Notas de desarrollo de la biblioteca HAL - Comunicación I2C (MPU6050)

En este artículo, basado en el kit de desarrollo RobotCtrl de desarrollo propio, con un núcleo de microcontrolador STM32F407ZET6, se describirá la forma de comunicación I2C utilizando el módulo MPU6050 y la biblioteca HAL. Para obtener información detallada sobre el esquema del kit de desarrollo, consulte [**RobotCtrl - Kit de desarrollo STM32 universal**](to_be_replace[3]).

## Principios básicos

### Comunicación I2C

![Imagen](https://img.wiki-power.com/d/wiki-media/img/20211026174634.png)

Los principios básicos de la comunicación I2C se pueden encontrar en el artículo [**Protocolo de comunicación - I2C**](to_be_replace[3]).

### Módulo MPU6050

![Imagen](https://img.wiki-power.com/d/wiki-media/img/20220404145145.png)

Definición de pines del módulo:

- VCC: 3.3V~5V
- GND: Tierra
- SCL: Reloj I2C / Reloj SPI
- SDA: Datos I2C / Entrada de datos SPI
- XDA: Genera el reloj principal para dispositivos I2C
- AD0: Bit de selección de dirección del dispositivo I2C / Salida de datos SPI
- INT: Pin de interrupción

### Biblioteca MPU6050 con filtro de Kalman

En este caso, utilizaremos la biblioteca MPU6050 con filtro de Kalman, disponible en [**leech001/MPU6050**](https://github.com/leech001/MPU6050). Debe descargar los archivos `mpu6050.c` y `mpu6050.h` y copiarlos en la carpeta de su proyecto. Luego, agréguelos al proyecto en STM32CubeIDE/Keil:

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

void MPU6050_Read_Temp(I2C_HandleTypeDef *I2Cx, MPU6050_t *DataStruct);
```

```

Nota: Por favor, reemplace `to_be_replace[3]` con el enlace correcto a la documentación del kit de desarrollo RobotCtrl.

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

// Configuración de MPU6050
#define MPU6050_ADDR 0xD0
const uint16_t i2c_timeout = 100;
const double Accel_Z_corrector = 14418.0;

uint32_t timer;

Kalman_t KalmanX = {
    .Q_angle = 0.001f,
    .Q_bias = 0.003f,
    .R_measure = 0.03f};

Kalman_t KalmanY = {
    .Q_angle = 0.001f,
    .Q_bias = 0.003f,
    .R_measure = 0.03f,
};

uint8_t MPU6050_Init(I2C_HandleTypeDef *I2Cx)
{
    uint8_t check;
    uint8_t Data;

    // Comprobar la identificación del dispositivo WHO_AM_I

    HAL_I2C_Mem_Read(I2Cx, MPU6050_ADDR, WHO_AM_I_REG, 1, &check, 1, i2c_timeout);

    if (check == 104) // Se devolverá 0x68 si todo va bien
    {
        // Registro de administración de energía 0X6B, debemos escribir todo 0's para despertar el sensor
        Data = 0;
        HAL_I2C_Mem_Write(I2Cx, MPU6050_ADDR, PWR_MGMT_1_REG, 1, &Data, 1, i2c_timeout);

        // Configurar la VELOCIDAD DE DATOS a 1KHz escribiendo el registro SMPLRT_DIV
        Data = 0x07;
        HAL_I2C_Mem_Write(I2Cx, MPU6050_ADDR, SMPLRT_DIV_REG, 1, &Data, 1, i2c_timeout);

        // Configurar la aceleración en el registro ACCEL_CONFIG
        // XA_ST=0, YA_ST=0, ZA_ST=0, FS_SEL=0 -> ± 2g
        Data = 0x00;
        HAL_I2C_Mem_Write(I2Cx, MPU6050_ADDR, ACCEL_CONFIG_REG, 1, &Data, 1, i2c_timeout);
```

```markdown
```c
        // Configurar el giroscopio en el Registro GYRO_CONFIG
        // XG_ST=0, YG_ST=0, ZG_ST=0, FS_SEL=0 -> ± 250 °/s
        Data = 0x00;
        HAL_I2C_Mem_Write(I2Cx, MPU6050_ADDR, GYRO_CONFIG_REG, 1, &Data, 1, i2c_timeout);
        return 0;
    }
    return 1;
}

void MPU6050_Read_Accel(I2C_HandleTypeDef *I2Cx, MPU6050_t *DataStruct)
{
    uint8_t Rec_Data[6];

    // Leer 6 BYTES de datos comenzando desde el registro ACCEL_XOUT_H

    HAL_I2C_Mem_Read(I2Cx, MPU6050_ADDR, ACCEL_XOUT_H_REG, 1, Rec_Data, 6, i2c_timeout);

    DataStruct->Accel_X_RAW = (int16_t)(Rec_Data[0] << 8 | Rec_Data[1]);
    DataStruct->Accel_Y_RAW = (int16_t)(Rec_Data[2] << 8 | Rec_Data[3]);
    DataStruct->Accel_Z_RAW = (int16_t)(Rec_Data[4] << 8 | Rec_Data[5]);

    /*** Convertir los valores RAW en aceleración en 'g'
         Hay que dividir según el valor de escala completa establecido en FS_SEL
         He configurado FS_SEL = 0. Así que estoy dividiendo por 16384.0
         Para más detalles, consulte el Registro ACCEL_CONFIG
         ****/

    DataStruct->Ax = DataStruct->Accel_X_RAW / 16384.0;
    DataStruct->Ay = DataStruct->Accel_Y_RAW / 16384.0;
    DataStruct->Az = DataStruct->Accel_Z_RAW / Accel_Z_corrector;
}

void MPU6050_Read_Gyro(I2C_HandleTypeDef *I2Cx, MPU6050_t *DataStruct)
{
    uint8_t Rec_Data[6];

    // Leer 6 BYTES de datos comenzando desde el registro GYRO_XOUT_H

    HAL_I2C_Mem_Read(I2Cx, MPU6050_ADDR, GYRO_XOUT_H_REG, 1, Rec_Data, 6, i2c_timeout);

    DataStruct->Gyro_X_RAW = (int16_t)(Rec_Data[0] << 8 | Rec_Data[1]);
    DataStruct->Gyro_Y_RAW = (int16_t)(Rec_Data[2] << 8 | Rec_Data[3]);
    DataStruct->Gyro_Z_RAW = (int16_t)(Rec_Data[4] << 8 | Rec_Data[5]);
}
```

```c
/*** Convierte los valores RAW en grados por segundo (°/s).
     Debemos dividir de acuerdo al valor de Full Scale (FS_SEL) establecido en FS_SEL.
     He configurado FS_SEL = 0. Así que estoy dividiendo por 131.0.
     Para obtener más detalles, consulta el registro de configuración GYRO_CONFIG.  ****/

DataStruct->Gx = DataStruct->Gyro_X_RAW / 131.0;
DataStruct->Gy = DataStruct->Gyro_Y_RAW / 131.0;
DataStruct->Gz = DataStruct->Gyro_Z_RAW / 131.0;
}

void MPU6050_Read_Temp(I2C_HandleTypeDef *I2Cx, MPU6050_t *DataStruct)
{
    uint8_t Rec_Data[2];
    int16_t temp;

    // Lee 2 BYTES de datos a partir del registro TEMP_OUT_H_REG

    HAL_I2C_Mem_Read(I2Cx, MPU6050_ADDR, TEMP_OUT_H_REG, 1, Rec_Data, 2, i2c_timeout);

    temp = (int16_t)(Rec_Data[0] << 8 | Rec_Data[1]);
    DataStruct->Temperature = (float)((int16_t)temp / (float)340.0 + (float)36.53);
}

void MPU6050_Read_All(I2C_HandleTypeDef *I2Cx, MPU6050_t *DataStruct)
{
    uint8_t Rec_Data[14];
    int16_t temp;

    // Lee 14 BYTES de datos a partir del registro ACCEL_XOUT_H

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

```markdown
```markdown
```markdown
```markdown
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

```markdown
Here's the translation of the provided code into Spanish:

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
```

Puedes observar que se están realizando cálculos en el código para el filtro de Kalman y para la lectura de datos del sensor MPU6050 a través de I2C.

## Lectura de información del MPU6050 utilizando I2C

### Configuración del bus I2C en CubeMX

En la categoría de funciones en el panel izquierdo de CubeMX, selecciona "Comunicación" - "I2Cx". Cambia la opción de I2C de "disable" a "I2C" y configura los parámetros en la ventana de configuración (los valores por defecto son adecuados):

![Imagen](https://img.wiki-power.com/d/wiki-media/img/20220403190116.png)

### Configuración en el código para leer la información del MPU6050 a través de I2C

En primer lugar, incluye la biblioteca del MPU6050 en el archivo "main.c":

```c
/* USER CODE BEGIN Includes */

#include "mpu6050.h"

/* USER CODE END Includes */
```

Luego, instancia un objeto para el MPU6050:

```c
/* USER CODE BEGIN PV */

MPU6050_t MPU6050;

/* USER CODE END PV */
```

Dentro de la función principal, inicializa el sensor y asegúrate de que la inicialización sea exitosa antes de continuar con el programa:

```c
/* USER CODE BEGIN 2 */

while (MPU6050_Init(&hi2c1) == 1);

/* USER CODE END 2 */
```

Dentro de un bucle while, puedes leer los datos calculados por la biblioteca y agregar un retraso para la sincronización:

```c
/* USER CODE BEGIN 3 */

while (1) {
    MPU6050_Read_All(&hi2c1, &MPU6050);
    HAL_Delay(100);
}

/* USER CODE END 3 */
```

Con esta línea de código, podrás leer las variables almacenadas en la estructura `MPU6050`, como `MPU6050.KalmanAngleX` (ángulo filtrado en el eje X). Los elementos y tipos de datos de la estructura `MPU6050` son los siguientes:

```c
```

```markdown
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

Una vez configurada la comunicación serie, puedes imprimir las variables con la siguiente declaración:

```c
printf("Ángulo X: %.2f°\t", MPU6050.KalmanAngleX);
```

## Referencias y Agradecimientos

- [leech001/MPU6050](https://github.com/leech001/MPU6050)
- [Protocolo de Comunicación - I2C](enlace_a_tu_referencia_1)
- [Otra Referencia Importante](enlace_a_tu_referencia_2)
```

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.