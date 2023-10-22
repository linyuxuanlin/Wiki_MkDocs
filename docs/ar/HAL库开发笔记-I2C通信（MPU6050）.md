# مذكرات تطوير مكتبة HAL - اتصال I2C (MPU6050)

في هذا المقال، سنشرح كيفية استخدام مكتبة HAL للاتصال عبر I2C باستخدام وحدة MPU6050. سيتم تنفيذ هذا الشرح باستخدام مجموعة تطوير RobotCtrl الخاصة بنا، والتي تستند إلى نواة الميكروكنترولر STM32F407ZET6. لمزيد من المعلومات حول مخطط الوحدة وشرح مفصل، يُرجى زيارة [**RobotCtrl - STM32 通用开发套件**](to_be_replace[3]).

## المبادئ الأساسية

### اتصال I2C

![](https://img.wiki-power.com/d/wiki-media/img/20211026174634.png)

يمكنك الانتقال إلى مقالنا حول المبادئ الأساسية لاتصال I2C [**هنا**](to_be_replace[3]).

### وحدة MPU6050

![](https://img.wiki-power.com/d/wiki-media/img/20220404145145.png)

تعريف أطراف الوحدة:

- VCC: 3.3 فولت إلى 5 فولت
- GND: الأرضي
- SCL: ساعة I2C / ساعة SPI
- SDA: بيانات I2C / مدخلات بيانات SPI
- XDA: توفير ساعة رئيسية لجهاز I2C
- AD0: بت اختيار عنوان الجهاز I2C / مخرجات بيانات SPI
- INT: دبوس التقاط الانقطاع

### مكتبة MPU6050 مع تصفية كالمان

في هذا المكان، سنستخدم مكتبة MPU6050 مع تصفية كالمان. يمكنك العثور على هذه المكتبة هنا: [**leech001/MPU6050**](https://github.com/leech001/MPU6050). يجب نسخ ملفات `mpu6050.c` و `mpu6050.h` التي تم تنزيلها إلى مجلد المشروع وإضافتها إلى مشروعك داخل بيئة التطوير STM32CubeIDE أو Keil.

```c title="mpu6050.h"

#ifndef INC_GY521_H_
#define INC_GY521_H_

#endif /* INC_GY521_H_ */

#include <stdint.h>
#include "i2c.h"

// هيكل MPU6050
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

// هيكل كالمان
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


```c
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

// إعداد MPU6050
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

    // التحقق من هوية الجهاز WHO_AM_I

    HAL_I2C_Mem_Read(I2Cx, MPU6050_ADDR, WHO_AM_I_REG, 1, &check, 1, i2c_timeout);

    if (check == 104) // سيتم إرجاع 0x68 من قبل الجهاز إذا تم كل شيء بنجاح
    {
        // تسجيل إدارة الطاقة 0X6B يجب أن نكتب الصفراء جميعها لإيقاظ الجهاز
        Data = 0;
        HAL_I2C_Mem_Write(I2Cx, MPU6050_ADDR, PWR_MGMT_1_REG, 1, &Data, 1, i2c_timeout);

        // تعيين معدل البيانات ليكون 1 كيلو هرتز عن طريق كتابة سجل SMPLRT_DIV
        Data = 0x07;
        HAL_I2C_Mem_Write(I2Cx, MPU6050_ADDR, SMPLRT_DIV_REG, 1, &Data, 1, i2c_timeout);

        // تعيين تكوين المعايرة للتسارع في سجل ACCEL_CONFIG
        // XA_ST=0,YA_ST=0,ZA_ST=0, FS_SEL=0 -> 2g
        Data = 0x00;
        HAL_I2C_Mem_Write(I2Cx, MPU6050_ADDR, ACCEL_CONFIG_REG, 1, &Data, 1, i2c_timeout);
```

```c
        // ... المزيد من الإعدادات والتكوينات هنا
    }
    return 0;
}

void MPU6050_Read_All(I2C_HandleTypeDef *I2Cx, MPU6050_t *DataStruct)
{
    // قراءة بيانات MPU6050 وملء هيكل البيانات DataStruct هنا
}

double Kalman_getAngle(Kalman_t *Kalman, double newAngle, double newRate, double dt)
{
    // حساب الزاوية باستخدام معادلة كالمان هنا وإرجاعها
}
```

```markdown
// قم بتعيين تكوين جهاز الجيروسكوب في سجل GYRO_CONFIG
// XG_ST=0، YG_ST=0، ZG_ST=0، FS_SEL=0 -> 250 درجة/ثانية
البيانات = 0x00;
HAL_I2C_Mem_Write(I2Cx، MPU6050_ADDR، GYRO_CONFIG_REG، 1، &Data، 1، i2c_timeout);
ارجاع 0;
}

ارجاع 1;
}

void MPU6050_Read_Accel(I2C_HandleTypeDef *I2Cx، MPU6050_t *DataStruct)
{
uint8_t Rec_Data[6];

// اقرأ 6 بايت من البيانات ابتداءً من سجل ACCEL_XOUT_H

HAL_I2C_Mem_Read(I2Cx، MPU6050_ADDR، ACCEL_XOUT_H_REG، 1، Rec_Data، 6، i2c_timeout);

DataStruct->Accel_X_RAW = (int16_t)(Rec_Data[0] << 8 | Rec_Data[1]);
DataStruct->Accel_Y_RAW = (int16_t)(Rec_Data[2] << 8 | Rec_Data[3]);
DataStruct->Accel_Z_RAW = (int16_t)(Rec_Data[4] << 8 | Rec_Data[5]);

/*** قم بتحويل القيم الخامة إلى تسارع بوحدة 'g'
يجب أن نقسم وفقًا للقيمة الكاملة المحددة في FS_SEL
لقد قمت بتكوين FS_SEL = 0. لذا أقسم على 16384.0
للمزيد من التفاصيل، تحقق من سجل ACCEL_CONFIG ***/
DataStruct->Ax = DataStruct->Accel_X_RAW / 16384.0;
DataStruct->Ay = DataStruct->Accel_Y_RAW / 16384.0;
DataStruct->Az = DataStruct->Accel_Z_RAW / Accel_Z_corrector;
}

void MPU6050_Read_Gyro(I2C_HandleTypeDef *I2Cx، MPU6050_t *DataStruct)
{
uint8_t Rec_Data[6];

// اقرأ 6 بايت من البيانات ابتداءً من سجل GYRO_XOUT_H

HAL_I2C_Mem_Read(I2Cx، MPU6050_ADDR، GYRO_XOUT_H_REG، 1، Rec_Data، 6، i2c_timeout);

DataStruct->Gyro_X_RAW = (int16_t)(Rec_Data[0] << 8 | Rec_Data[1]);
DataStruct->Gyro_Y_RAW = (int16_t)(Rec_Data[2] << 8 | Rec_Data[3]);
DataStruct->Gyro_Z_RAW = (int16_t)(Rec_Data[4] << 8 | Rec_Data[5]);
```

```markdown
/*** تحويل القيم الخامة إلى درجات في الثانية (دورة في الثانية)
     يجب علينا القسمة وفقًا للقيمة الكاملة المضبوطة في FS_SEL
     لقد قمت بتكوين FS_SEL = 0. لذلك أقوم بالقسمة على 131.0
     لمزيد من التفاصيل، يُرجى التحقق من تسجيل GYRO_CONFIG
     ****/

DataStruct->Gx = DataStruct->Gyro_X_RAW / 131.0;
DataStruct->Gy = DataStruct->Gyro_Y_RAW / 131.0;
DataStruct->Gz = DataStruct->Gyro_Z_RAW / 131.0;
}

void MPU6050_Read_Temp(I2C_HandleTypeDef *I2Cx, MPU6050_t *DataStruct)
{
    uint8_t Rec_Data[2];
    int16_t temp;

    // اقرأ 2 بايت من البيانات ابتداءً من التسجيل TEMP_OUT_H_REG

    HAL_I2C_Mem_Read(I2Cx, MPU6050_ADDR, TEMP_OUT_H_REG, 1, Rec_Data, 2, i2c_timeout);

    temp = (int16_t)(Rec_Data[0] << 8 | Rec_Data[1]);
    DataStruct->Temperature = (float)((int16_t)temp / (float)340.0 + (float)36.53);
}

void MPU6050_Read_All(I2C_HandleTypeDef *I2Cx, MPU6050_t *DataStruct)
{
    uint8_t Rec_Data[14];
    int16_t temp;

    // اقرأ 14 بايت من البيانات ابتداءً من تسجيل ACCEL_XOUT_H

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
ترجمة إلى العربية:

```c
    DataStruct->Ax = DataStruct->Accel_X_RAW / 16384.0;
    DataStruct->Ay = DataStruct->Accel_Y_RAW / 16384.0;
    DataStruct->Az = DataStruct->Accel_Z_RAW / Accel_Z_corrector;
    DataStruct->Temperature = (float)((int16_t)temp / (float)340.0 + (float)36.53);
    DataStruct->Gx = DataStruct->Gyro_X_RAW / 131.0;
    DataStruct->Gy = DataStruct->Gyro_Y_RAW / 131.0;
    DataStruct->Gz = DataStruct->Gyro_Z_RAW / 131.0;

    // حل زاوية كالمان
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
```

```markdown
ترجمة إلى العربية:

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

يمكن ملاحظة أنه بعد تعيين عنوان I2C، تمت مبادلة البيانات وتهيئة الأرقام في دالة `MPU6050_Init` وتمت إجراء العمليات اللازمة لقراءة القيم في باقي الدوال.

## استخدام I2C لقراءة معلومات MPU6050

### تكوين الحافلة I2C داخل CubeMX

في الجدول المصنف على الجانب الأيسر من CubeMX، حدد `التواصل` - `I2Cx`، وقم بتغيير الخيار من `تعطيل` إلى `I2C`، ثم قم بتكوين المعلمات في الشاشة التي تظهر (يمكن استخدام القيم الافتراضية):

![](https://img.wiki-power.com/d/wiki-media/img/20220403190116.png)

### تكوين قراءة I2C لمعلومات MPU6050 في الشيفرة

أولاً، في الملف `main.c`، قم بتضمين مكتبة MPU6050 كالتالي:

```c title="main.c"
/* USER CODE BEGIN Includes */

#include "mpu6050.h"

/* USER CODE END Includes */
```

ثم، قم بإنشاء كائن من الهيكل `MPU6050_t`:

```c title="main.c"
/* USER CODE BEGIN PV */

MPU6050_t MPU6050;

/* USER CODE END PV */
```

قم بتهيئته في دالة `main`، وانتظر حتى تكتمل عملية التهيئة قبل متابعة تنفيذ البرنامج:

```c title="main.c"
/* USER CODE BEGIN 2 */

while (MPU6050_Init(&hi2c1) == 1);

/* USER CODE END 2 */
```

في حلقة `while` الرئيسية، اقرأ البيانات التي حسبتها المكتبة وانتظر لبعض الوقت:

```c title="main.c"

/* USER CODE BEGIN 3 */

    MPU6050_Read_All(&hi2c1, &MPU6050);
    HAL_Delay(100);
}

/* USER CODE END 3 */
```

عند تنفيذ هذا السطر، ستتم قراءة المتغيرات داخل هيكل MPU6050 مثل `MPU6050.KalmanAngleX` (زاوية المحور X بعد التصفية). تمثل العناصر داخل هيكل MPU6050 كالتالي:

```c
typedef struct
{
```

```markdown
يمكنك العثور على العبارات التالية بعد تكوين الواجهة التسلسلية، حيث يمكنك استخدامها لإخراج البيانات:

```c
printf("زاوية X: %.2f درجة\t", MPU6050.KalmanAngleX);
```

## المراجع والشكر

- [leech001/MPU6050](https://github.com/leech001/MPU6050)
- [بروتوكول الاتصال - I2C](to_be_replace[3])

> عنوان النص: <https://wiki-power.com/>
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.
```

يرجى ملاحظة أنني لم أتمكن من ترجمة الروابط والعبارات ذات العلامات `> عنوان النص: <https://wiki-power.com/>` و`> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.` نظرًا لعدم توفر معلومات حولها في النص الأصلي.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.