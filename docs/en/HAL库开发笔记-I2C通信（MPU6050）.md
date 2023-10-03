# HAL Library Development Notes - I2C Communication (MPU6050)

This article is based on the self-developed RobotCtrl development kit, with the STM32F407ZET6 microcontroller core, and uses the MPU6050 module to explain the HAL library's I2C communication method. For the development kit's schematic and detailed introduction, please refer to [**RobotCtrl - STM32 Universal Development Kit**](https://wiki-power.com/en/RobotCtrl-STM32%E9%80%9A%E7%94%A8%E5%BC%80%E5%8F%91%E5%A5%97%E4%BB%B6).

## Basic Principles

### I2C Communication

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20211026174634.png)

The basic principle of I2C communication can be found in the article [**Communication Protocol - I2C**](https://wiki-power.com/en/%E9%80%9A%E4%BF%A1%E5%8D%8F%E8%AE%AE-I2C).

### MPU6050 Module

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220404145145.png)

Pin definitions for the module:

- VCC: 3.3V~5V
- GND: Ground
- SCL: I2C Clock / SPI Clock
- SDA: I2C Data / SPI Data Input
- XDA: Provides the main clock to the I2C device
- AD0: I2C device address selection bit / SPI data output
- INT: Interrupt pin

### MPU6050 Library with Kalman Filter

Here, we use the MPU6050 library with Kalman filter: [**leech001/MPU6050**](https://github.com/leech001/MPU6050). Copy the downloaded `mpu6050.c` and `mpu6050.h` files to the project folder, and add them to the project in STM32CubeIDE/Keil:

```c title="mpu6050.h"

#ifndef INC_GY521_H_
#define INC_GY521_H_

#endif /* INC_GY521_H_ */

The following code defines structures and functions for interfacing with the MPU6050 accelerometer and gyroscope sensor, as well as a Kalman filter for angle estimation. The MPU6050 structure contains raw sensor data and calculated values for acceleration, angular velocity, and temperature. The Kalman structure contains parameters and variables for the Kalman filter algorithm, which is used to estimate the angle of the sensor based on the raw data. The functions provided include initialization, reading of raw sensor data, reading of temperature, reading of all data, and angle estimation using the Kalman filter.

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

// Setup MPU6050
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

    // check device ID WHO_AM_I

    HAL_I2C_Mem_Read(I2Cx, MPU6050_ADDR, WHO_AM_I_REG, 1, &check, 1, i2c_timeout);

    // MPU6050 initialization
    Data = 0;
    HAL_I2C_Mem_Write(I2Cx, MPU6050_ADDR, PWR_MGMT_1_REG, 1, &Data, 1, i2c_timeout);
    Data = 0x07;
    HAL_I2C_Mem_Write(I2Cx, MPU6050_ADDR, SMPLRT_DIV_REG, 1, &Data, 1, i2c_timeout);
    Data = 0x00;
    HAL_I2C_Mem_Write(I2Cx, MPU6050_ADDR, ACCEL_CONFIG_REG, 1, &Data, 1, i2c_timeout);
    Data = 0x00;
    HAL_I2C_Mem_Write(I2Cx, MPU6050_ADDR, GYRO_CONFIG_REG, 1, &Data, 1, i2c_timeout);

    return check == 0x68 ? 1 : 0;
}

void MPU6050_Read_Accel(I2C_HandleTypeDef *I2Cx, int16_t *Accel)
{
    uint8_t buffer[6];
    HAL_I2C_Mem_Read(I2Cx, MPU6050_ADDR, ACCEL_XOUT_H_REG, 1, buffer, 6, i2c_timeout);
    Accel[0] = (int16_t)(buffer[0] << 8 | buffer[1]);
    Accel[1] = (int16_t)(buffer[2] << 8 | buffer[3]);
    Accel[2] = (int16_t)(buffer[4] << 8 | buffer[5]);
}

void MPU6050_Read_Gyro(I2C_HandleTypeDef *I2Cx, int16_t *Gyro)
{
    uint8_t buffer[6];
    HAL_I2C_Mem_Read(I2Cx, MPU6050_ADDR, GYRO_XOUT_H_REG, 1, buffer, 6, i2c_timeout);
    Gyro[0] = (int16_t)(buffer[0] << 8 | buffer[1]);
    Gyro[1] = (int16_t)(buffer[2] << 8 | buffer[3]);
    Gyro[2] = (int16_t)(buffer[4] << 8 | buffer[5]);
}

void MPU6050_Read_Temp(I2C_HandleTypeDef *I2Cx, float *Temp)
{
    uint8_t buffer[2];
    int16_t temp;
    HAL_I2C_Mem_Read(I2Cx, MPU6050_ADDR, TEMP_OUT_H_REG, 1, buffer, 2, i2c_timeout);
    temp = (int16_t)(buffer[0] << 8 | buffer[1]);
    *Temp = (float)temp / 340.0f + 36.53f;
}

void Complementary_Filter(float Accel[3], float Gyro[3], float *Roll, float *Pitch)
{
    float Accel_Roll = atan2f(Accel[1], Accel[2]) * RAD_TO_DEG;
    float Accel_Pitch = atan2f(-Accel[0], sqrtf(Accel[1] * Accel[1] + Accel[2] * Accel[2])) * RAD_TO_DEG;

    float Gyro_Roll = *Roll + Gyro[0] * 0.0001f;
    float Gyro_Pitch = *Pitch + Gyro[1] * 0.0001f;

    *Roll = 0.98f * Gyro_Roll + 0.02f * Accel_Roll;
    *Pitch = 0.98f * Gyro_Pitch + 0.02f * Accel_Pitch;
}

void Kalman_Filter(Kalman_t *Kalman, float Accel, float Gyro, float *Angle)
{
    float y, S;
    float K[2];

    Kalman->x_angle += Kalman->dt * (Gyro - Kalman->x_bias);
    Kalman->P_00 += -Kalman->dt * (Kalman->P_10 + Kalman->P_01) + Kalman->Q_angle * Kalman->dt;
    Kalman->P_01 += -Kalman->dt * Kalman->P_11;
    Kalman->P_10 += -Kalman->dt * Kalman->P_11;
    Kalman->P_11 += +Kalman->Q_bias * Kalman->dt;

    y = Accel - Kalman->x_angle;
    S = Kalman->P_00 + Kalman->R_measure;
    K[0] = Kalman->P_00 / S;
    K[1] = Kalman->P_10 / S;

    Kalman->x_angle += K[0] * y;
    Kalman->x_bias += K[1] * y;
    Kalman->P_00 -= K[0] * Kalman->P_00;
    Kalman->P_01 -= K[0] * Kalman->P_01;
    Kalman->P_10 -= K[1] * Kalman->P_00;
    Kalman->P_11 -= K[1] * Kalman->P_01;

    *Angle = Kalman->x_angle;
}

float Get_Angle(I2C_HandleTypeDef *I2Cx, float *Roll, float *Pitch)
{
    int16_t Accel[3], Gyro[3];
    float Accel_f[3], Gyro_f[3], Temp;
    float AccelX, AccelY, AccelZ, GyroX, GyroY, GyroZ;
    float AccelX_corrected, AccelY_corrected, AccelZ_corrected;

    MPU6050_Read_Accel(I2Cx, Accel);
    MPU6050_Read_Gyro(I2Cx, Gyro);
    MPU6050_Read_Temp(I2Cx, &Temp);

    AccelX = (float)Accel[0];
    AccelY = (float)Accel[1];
    AccelZ = (float)Accel[2];
    GyroX = (float)Gyro[0];
    GyroY = (float)Gyro[1];
    GyroZ = (float)Gyro[2];

    AccelX_corrected = AccelX / Accel_Z_corrector;
    AccelY_corrected = AccelY / Accel_Z_corrector;
    AccelZ_corrected = AccelZ / Accel_Z_corrector;

    Accel_f[0] = AccelX_corrected;
    Accel_f[1] = AccelY_corrected;
    Accel_f[2] = AccelZ_corrected;
    Gyro_f[0] = GyroX / 131.0f;
    Gyro_f[1] = GyroY / 131.0f;
    Gyro_f[2] = GyroZ / 131.0f;

    Complementary_Filter(Accel_f, Gyro_f, Roll, Pitch);
    Kalman_Filter(&KalmanX, *Roll, Gyro_f[0], Roll);
    Kalman_Filter(&KalmanY, *Pitch, Gyro_f[1], Pitch);

    return *Pitch;
}

The code above is written in C language and is configuring a MPU6050 sensor. The check variable is checking if the sensor is working properly and returning a value of 104 (0x68 in hexadecimal) if everything is okay. If the check variable returns 104, the code will proceed to configure the sensor by writing values to specific registers using the HAL_I2C_Mem_Write function. 

First, the power management register (PWR_MGMT_1_REG) is written with all 0's to wake up the sensor. Then, the sample rate divider register (SMPLRT_DIV_REG) is set to a data rate of 1KHz. 

Next, the accelerometer configuration is set in the ACCEL_CONFIG_REG register. The XA_ST, YA_ST, and ZA_ST bits are set to 0, and the FS_SEL bits are set to 0, which corresponds to a range of +/- 2g. 

Finally, the gyroscopic configuration is set in the GYRO_CONFIG_REG register. The XG_ST, YG_ST, and ZG_ST bits are set to 0, and the FS_SEL bits are set to 0, which corresponds to a range of +/- 250 degrees per second. 

If the check variable does not return 104, the code will return a value of 1.

The following code is for reading accelerometer data from the MPU6050 sensor using I2C communication. The function takes in the I2C handle and a pointer to a MPU6050 data structure as arguments. 

```c
void MPU6050_Read_Accel(I2C_HandleTypeDef *I2Cx, MPU6050_t *DataStruct)
{
    uint8_t Rec_Data[6];

    // Read 6 BYTES of data starting from ACCEL_XOUT_H register

    HAL_I2C_Mem_Read(I2Cx, MPU6050_ADDR, ACCEL_XOUT_H_REG, 1, Rec_Data, 6, i2c_timeout);

    DataStruct->Accel_X_RAW = (int16_t)(Rec_Data[0] << 8 | Rec_Data[1]);
    DataStruct->Accel_Y_RAW = (int16_t)(Rec_Data[2] << 8 | Rec_Data[3]);
    DataStruct->Accel_Z_RAW = (int16_t)(Rec_Data[4] << 8 | Rec_Data[5]);

    /*** convert the RAW values into acceleration in 'g'
         we have to divide according to the Full scale value set in FS_SEL
         I have configured FS_SEL = 0. So I am dividing by 16384.0
         for more details check ACCEL_CONFIG Register              ****/

    DataStruct->Ax = DataStruct->Accel_X_RAW / 16384.0;
    DataStruct->Ay = DataStruct->Accel_Y_RAW / 16384.0;
    DataStruct->Az = DataStruct->Accel_Z_RAW / Accel_Z_corrector;
}
```

The function first declares an array of 6 bytes to store the received data. It then uses the HAL_I2C_Mem_Read function to read 6 bytes of data starting from the ACCEL_XOUT_H register of the MPU6050 sensor. The received data is stored in the Rec_Data array. 

The function then converts the received raw data into acceleration values in 'g' units. This is done by dividing the raw data by a scaling factor. The scaling factor depends on the full scale value set in the ACCEL_CONFIG register. In this case, the full scale value is set to 0, so the scaling factor is 16384.0. The resulting acceleration values are stored in the MPU6050 data structure.

The following code is for reading gyro data from the MPU6050 sensor using I2C communication. The function takes in the I2C handle and a data structure as parameters. The function reads 6 bytes of data starting from the GYRO_XOUT_H register using the HAL_I2C_Mem_Read function. The received data is then converted from raw values to degrees per second (dps) using the full scale value set in FS_SEL. In this case, FS_SEL is set to 0, so the raw values are divided by 131.0. The converted values are then stored in the data structure.

The following code is written in C and is used to read temperature and all data from an MPU6050 sensor using I2C communication protocol. The code uses the HAL library for I2C communication.

```c
void MPU6050_Read_Temp(I2C_HandleTypeDef *I2Cx, MPU6050_t *DataStruct)
{
    uint8_t Rec_Data[2];
    int16_t temp;

    // Read 2 BYTES of data starting from TEMP_OUT_H_REG register

    HAL_I2C_Mem_Read(I2Cx, MPU6050_ADDR, TEMP_OUT_H_REG, 1, Rec_Data, 2, i2c_timeout);

    temp = (int16_t)(Rec_Data[0] << 8 | Rec_Data[1]);
    DataStruct->Temperature = (float)((int16_t)temp / (float)340.0 + (float)36.53);
}

void MPU6050_Read_All(I2C_HandleTypeDef *I2Cx, MPU6050_t *DataStruct)
{
    uint8_t Rec_Data[14];
    int16_t temp;

    // Read 14 BYTES of data starting from ACCEL_XOUT_H register

    HAL_I2C_Mem_Read(I2Cx, MPU6050_ADDR, ACCEL_XOUT_H_REG, 1, Rec_Data, 14, i2c_timeout);
```

The `MPU6050_Read_Temp` function reads the temperature data from the sensor and stores it in the `Temperature` field of the `MPU6050_t` struct. The function first reads 2 bytes of data starting from the `TEMP_OUT_H_REG` register using the `HAL_I2C_Mem_Read` function. The two bytes of data are then combined into a 16-bit integer using bitwise operations. The temperature value is then calculated using the formula `(temp / 340.0) + 36.53` and stored in the `Temperature` field of the `MPU6050_t` struct.

The `MPU6050_Read_All` function reads all the data from the sensor and stores it in the appropriate fields of the `MPU6050_t` struct. The function first reads 14 bytes of data starting from the `ACCEL_XOUT_H` register using the `HAL_I2C_Mem_Read` function. The 14 bytes of data are then combined into 3 sets of 16-bit integers using bitwise operations. The 3 sets of 16-bit integers represent the accelerometer, gyroscope, and temperature data respectively. The accelerometer and gyroscope data are then converted to floating-point values using the appropriate scaling factors and stored in the corresponding fields of the `MPU6050_t` struct. The temperature data is calculated using the same formula as in the `MPU6050_Read_Temp` function and stored in the `Temperature` field of the `MPU6050_t` struct.

```
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
```

// Kalman angle solve
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

The above code is a function called `Kalman_getAngle` written in C language. It takes in four parameters: a pointer to a struct called `Kalman_t`, a new angle value, a new rate value, and a time interval `dt`. The function uses a Kalman filter algorithm to calculate and return an updated angle value.

The function first calculates the rate by subtracting the bias value stored in the `Kalman_t` struct from the new rate value. It then updates the angle value by multiplying the rate by the time interval `dt`.

Next, the function updates the covariance matrix `P` using the Kalman filter equations. The matrix `Q` represents the process noise covariance, and `R` represents the measurement noise covariance. The function also calculates the Kalman gain `K` using the updated covariance matrix and the measurement noise covariance.

Finally, the function calculates the difference between the new angle value and the updated angle value, and uses the Kalman gain to correct the angle and bias values. It also updates the covariance matrix using the Kalman gain.

Overall, this function is used to filter noisy sensor data and provide a more accurate estimate of the angle value.

## Reading Information Returned by MPU6050 Using I2C

### Configuring I2C Bus in CubeMX

In the CubeMX left-hand functional category bar, select `Communication` - `I2Cx`, change the I2C option from `disable` to `I2C`, and configure the parameters in the pop-up configuration interface (default is fine):

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220403190116.png)

### Configuring I2C to Read Information Returned by MPU6050 in Code

First, call the MPU6050 library in `main.c`:

```c title="main.c"
/* USER CODE BEGIN Includes */

#include "mpu6050.h"

/* USER CODE END Includes */
```

Then, instantiate the object:

```c title="main.c"
/* USER CODE BEGIN PV */

MPU6050_t MPU6050;

/* USER CODE END PV */
```

Initialize in the main function and continue executing the program when finished:

```c title="main.c"
/* USER CODE BEGIN 2 */

while (MPU6050_Init(&hi2c1) == 1);

/* USER CODE END 2 */
```

Read the variables calculated by the library in the while loop and give a certain delay buffer:

```c title="main.c"

/* USER CODE BEGIN 3 */

		MPU6050_Read_All(&hi2c1, &MPU6050);
		HAL_Delay(100);
	}

/* USER CODE END 3 */
```

After executing this statement, variables inside the MPU6050 structure can be read, such as `MPU6050.KalmanAngleX` (filtered angle on the X-axis). The elements and types of the MPU6050 structure are as follows:

```c
typedef struct
{

```
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

After configuring the serial port, the following statement can be used to output variables:

```c
printf("XAngle: %.2f°\t", MPU6050.KalmanAngleX);
```

## References and Acknowledgements

- [leech001/MPU6050](https://github.com/leech001/MPU6050)
- [Communication Protocol - I2C](https://wiki-power.com/en/%E9%80%9A%E4%BF%A1%E5%8D%8F%E8%AE%AE-I2C)

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.