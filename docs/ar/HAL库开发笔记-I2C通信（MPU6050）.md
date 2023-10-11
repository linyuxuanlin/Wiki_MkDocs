# ملاحظات تطوير مكتبة HAL - الاتصال عبر I2C (MPU6050)

يستند هذا المقال إلى مجموعة تطوير RobotCtrl الخاصة بنا ، ويتم تشغيل نواة الميكروكنترولر باستخدام STM32F407ZET6 ، ويتم شرح طريقة الاتصال عبر I2C باستخدام وحدة MPU6050. يرجى الرجوع إلى مخطط الدائرة والمزيد من التفاصيل حول مجموعة تطوير RobotCtrl في [**RobotCtrl - STM32 通用开发套件**](https://wiki-power.com/ar/RobotCtrl-STM32%E9%80%9A%E7%94%A8%E5%BC%80%E5%8F%91%E5%A5%97%E4%BB%B6).

## المبادئ الأساسية

### الاتصال عبر I2C

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20211026174634.png)

يمكن الرجوع إلى المقال [**通信协议 - I2C**](https://wiki-power.com/ar/%E9%80%9A%E4%BF%A1%E5%8D%8F%E8%AE%AE-I2C) للحصول على المبادئ الأساسية للاتصال عبر I2C.

### وحدة MPU6050

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220404145145.png)

تعريف دبابيس الوحدة:

- VCC: 3.3V~5V
- GND: الأرض
- SCL: ساعة I2C / ساعة SPI
- SDA: بيانات I2C / بيانات الإدخال SPI
- XDA: توفير ساعة رئيسية لجهاز I2C
- AD0: بت اختيار عنوان الجهاز I2C / مخرج بيانات SPI
- INT: دبوس المقاطعة

### مكتبة MPU6050 مع تصفية كالمان

هنا ، نستخدم مكتبة MPU6050 مع تصفية كالمان: [**leech001/MPU6050**](https://github.com/leech001/MPU6050) ، ونقوم بنسخ `mpu6050.c` و `mpu6050.h` التي تم تنزيلها إلى مجلد المشروع ، وإضافتها إلى المشروع في STM32CubeIDE/Keil:

````c title="mpu6050.h"

#ifndef INC_GY521_H_
#define INC_GY521_H_

#endif /* INC_GY521_H_ */

#include <stdint.h>
#include "i2c.h"

// MPU6050 structure
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

// Kalman structure
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

void MPU6050_Read_All(I2C_HandleTypeDef *I2Cx, MPU6050_t *DataStruct);

# ملف mpu6050.c

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

    // التحقق من هوية الجهاز WHO_AM_I

    HAL_I2C_Mem_Read(I2Cx, MPU6050_ADDR, WHO_AM_I_REG, 1, &check, 1, i2c_timeout);

    if (check == 104) // سيتم إرجاع 0x68 من قبل الاستشعار إذا تم كل شيء بنجاح
    {
        // سجل إدارة الطاقة 0X6B يجب أن نكتب كل 0 لإيقاظ الاستشعار
        Data = 0;
        HAL_I2C_Mem_Write(I2Cx, MPU6050_ADDR, PWR_MGMT_1_REG, 1, &Data, 1, i2c_timeout);

        // تعيين معدل البيانات إلى 1 كيلو هرتز عن طريق كتابة سجل SMPLRT_DIV
        Data = 0x07;
        HAL_I2C_Mem_Write(I2Cx, MPU6050_ADDR, SMPLRT_DIV_REG, 1, &Data, 1, i2c_timeout);

        // تعيين تكوين المسرع في سجل ACCEL_CONFIG
        // XA_ST = 0، YA_ST = 0، ZA_ST = 0، FS_SEL = 0 -> 2 جيجا
        Data = 0x00;
        HAL_I2C_Mem_Write(I2Cx, MPU6050_ADDR, ACCEL_CONFIG_REG, 1, &Data, 1, i2c_timeout);

// تعيين التكوين الدوراني في سجل GYRO_CONFIG
// XG_ST = 0، YG_ST = 0، ZG_ST = 0، FS_SEL = 0 -> 250 درجة / ثانية
Data = 0x00;
HAL_I2C_Mem_Write(I2Cx، MPU6050_ADDR، GYRO_CONFIG_REG، 1، &Data، 1، i2c_timeout);
return 0;
}
return 1;
}

void MPU6050_Read_Accel(I2C_HandleTypeDef * I2Cx، MPU6050_t * DataStruct)
{
uint8_t Rec_Data [6];

// اقرأ 6 بايتات من البيانات بدءًا من سجل ACCEL_XOUT_H
HAL_I2C_Mem_Read(I2Cx، MPU6050_ADDR، ACCEL_XOUT_H_REG، 1، Rec_Data، 6، i2c_timeout);

DataStruct->Accel_X_RAW = (int16_t)(Rec_Data [0] << 8 | Rec_Data [1]);
DataStruct->Accel_Y_RAW = (int16_t)(Rec_Data [2] << 8 | Rec_Data [3]);
DataStruct->Accel_Z_RAW = (int16_t)(Rec_Data [4] << 8 | Rec_Data [5]);

/*** تحويل القيم الخام إلى تسارع بالـ 'g'
يجب علينا القسمة وفقًا لقيمة النطاق الكامل المحددة في FS_SEL
لقد قمت بتكوين FS_SEL = 0. لذلك أقوم بالقسمة على 16384.0
لمزيد من التفاصيل ، تحقق من سجل ACCEL_CONFIG ****/

DataStruct->Ax = DataStruct->Accel_X_RAW / 16384.0;
DataStruct->Ay = DataStruct->Accel_Y_RAW / 16384.0;
DataStruct->Az = DataStruct->Accel_Z_RAW / Accel_Z_corrector;
}

void MPU6050_Read_Gyro(I2C_HandleTypeDef * I2Cx، MPU6050_t * DataStruct)
{
uint8_t Rec_Data [6];

// اقرأ 6 بايتات من البيانات بدءًا من سجل GYRO_XOUT_H
HAL_I2C_Mem_Read(I2Cx، MPU6050_ADDR، GYRO_XOUT_H_REG، 1، Rec_Data، 6، i2c_timeout);

DataStruct->Gyro_X_RAW = (int16_t)(Rec_Data [0] << 8 | Rec_Data [1]);
DataStruct->Gyro_Y_RAW = (int16_t)(Rec_Data [2] << 8 | Rec_Data [3]);
DataStruct->Gyro_Z_RAW = (int16_t)(Rec_Data [4] << 8 | Rec_Data [5]);

/*** تحويل القيم الخام إلى درجات في الثانية (د/ث)
         يجب علينا القسمة وفقًا لقيمة Full scale المحددة في FS_SEL
         لقد قمت بتكوين FS_SEL = 0. لذلك أقوم بالقسمة على 131.0
         لمزيد من التفاصيل ، تحقق من تسجيل GYRO_CONFIG              ****/

    DataStruct->Gx = DataStruct->Gyro_X_RAW / 131.0;
    DataStruct->Gy = DataStruct->Gyro_Y_RAW / 131.0;
    DataStruct->Gz = DataStruct->Gyro_Z_RAW / 131.0;
}

void MPU6050_Read_Temp(I2C_HandleTypeDef *I2Cx, MPU6050_t *DataStruct)
{
    uint8_t Rec_Data[2];
    int16_t temp;

    // قراءة 2 بايت من البيانات بدءًا من تسجيل TEMP_OUT_H_REG

    HAL_I2C_Mem_Read(I2Cx ، MPU6050_ADDR ، TEMP_OUT_H_REG ، 1 ، Rec_Data ، 2 ، i2c_timeout);

    temp = (int16_t)(Rec_Data[0] << 8 | Rec_Data[1]);
    DataStruct->Temperature = (float)((int16_t)temp / (float)340.0 + (float)36.53);
}

void MPU6050_Read_All(I2C_HandleTypeDef *I2Cx, MPU6050_t *DataStruct)
{
    uint8_t Rec_Data[14];
    int16_t temp;

    // قراءة 14 بايتًا من البيانات بدءًا من تسجيل ACCEL_XOUT_H

    HAL_I2C_Mem_Read(I2Cx ، MPU6050_ADDR ، ACCEL_XOUT_H_REG ، 1 ، Rec_Data ، 14 ، i2c_timeout);

    DataStruct->Accel_X_RAW = (int16_t)(Rec_Data[0] << 8 | Rec_Data[1]);
    DataStruct->Accel_Y_RAW = (int16_t)(Rec_Data[2] << 8 | Rec_Data[3]);
    DataStruct->Accel_Z_RAW = (int16_t)(Rec_Data[4] << 8 | Rec_Data[5]);
    temp = (int16_t)(Rec_Data[6] << 8 | Rec_Data[7]);
    DataStruct->Gyro_X_RAW = (int16_t)(Rec_Data[8] << 8 | Rec_Data[9]);
    DataStruct->Gyro_Y_RAW = (int16_t)(Rec_Data[10] << 8 | Rec_Data[11]);
    DataStruct->Gyro_Z_RAW = (int16_t)(Rec_Data[12] << 8 | Rec_Data[13]);

لا يوجد ترجمة لهذه المقالة حيث أنها تحتوي على رموز برمجية وليست نصاً عادياً.

# قراءة معلومات MPU6050 باستخدام I2C

في هذا الدرس، سنتعلم كيفية استخدام I2C لقراءة معلومات MPU6050. سنستخدم مكتبة MPU6050 المتاحة على GitHub.

## تهيئة الدوائر الكهربائية

يجب توصيل MPU6050 بالميكروكونترولر باستخدام I2C. يجب توصيل SDA و SCL بالميكروكونترولر. يمكن توصيل VCC و GND بأي مصدر طاقة يوفر الجهد المناسب.

## تهيئة MPU6050

يجب تهيئة MPU6050 للعمل بشكل صحيح. يمكن استخدام مكتبة MPU6050 لتهيئة MPU6050. يجب تضمين المكتبة في الملف الرئيسي `main.c` وتهيئة MPU6050 في دالة `MPU6050_Init()`.

```c
uint8_t MPU6050_Init(I2C_HandleTypeDef *I2Cx)
{
    ...
}
````

يجب تمرير مؤشرًا إلى هيكل `I2C_HandleTypeDef` إلى دالة `MPU6050_Init()`.

## استخدام مرشح كالمان

يمكن استخدام مرشح كالمان لتصفية القراءات من MPU6050. يمكن استخدام مكتبة MPU6050 لتطبيق مرشح كالمان. يجب استخدام دالة `MPU6050_KalmanFilter()` لتطبيق المرشح.

```c
double MPU6050_KalmanFilter(MPU6050_t *MPU6050, double newAngle, double newRate, double dt)
{
    ...
}
```

يجب تمرير قيمة زاوية جديدة ومعدل جديد والوقت المنقضي منذ القراءة السابقة إلى دالة `MPU6050_KalmanFilter()`.

## استخدام I2C لقراءة معلومات MPU6050

يجب تهيئة I2C داخل CubeMX. يمكن القيام بذلك من خلال تحديد `I2Cx` في القائمة الجانبية وتغيير الخيار من `disable` إلى `I2C`. يجب تكوين المعلمات في النافذة المنبثقة (يمكن استخدام الإعدادات الافتراضية).

يجب استدعاء مكتبة MPU6050 في `main.c` وإنشاء كائن MPU6050.

```c
MPU6050_t MPU6050;
```

يجب تهيئة MPU6050 في دالة `main()` وقراءة المتغيرات في حلقة while.

```c
while (MPU6050_Init(&hi2c1) == 1)
{
    ...
}

while (1)
{
    MPU6050_Read_All(&hi2c1, &MPU6050);
    HAL_Delay(100);
}
```

بعد تنفيذ هذا الأمر، يمكن قراءة المتغيرات داخل هيكل MPU6050، مثل `MPU6050.KalmanAngleX` (زاوية المحور X بعد التصفية). يتم تعريف عناصر هيكل MPU6050 وأنواعها كما يلي:

```c
typedef struct
{

    int16_t Accel_X_RAW;
    int16_t Accel_Y_RAW;
    int16_t Accel_Z_RAW;
    double Ax;
    double Ay;
    double Az;
```

```c
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

يمكنك بعد تهيئة المنفذ التسلسلي، استخدام العبارة التالية لإخراج المتغير:

```c
printf("XAngle: %.2f°\t", MPU6050.KalmanAngleX);
```

## المراجع والشكر

- [leech001/MPU6050](https://github.com/leech001/MPU6050)
- [通信协议 - I2C](https://wiki-power.com/ar/%E9%80%9A%E4%BF%A1%E5%8D%8F%E8%AE%AE-I2C)

> عنوان النص: <https://wiki-power.com/>  
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.
