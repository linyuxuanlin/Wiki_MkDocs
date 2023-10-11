# DAC - المعلمات الثابتة

> هذه المقالة متاحة باللغة الإنجليزية فقط.

محول الرقمي إلى تناظري (ADC) هو جهاز يحول تسلسل من البيانات الرقمية المدخلة إلى إشارات تناظرية.

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20221011141644.png)

## المعلمات الثابتة

تحتوي المعلمات الثابتة لـ DAC بشكل رئيسي على:

- الإخراج عند الصفر
- نطاق الإخراج الكامل (FSR)
- حجم LSB
- خطأ الإزاحة
- خطأ الزيادة
- خطأ عدم الخطية التفاضلي (DNE أو DNL)
- خطأ عدم الخطية التكاملي (INE أو INL)

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20221011144045.png)

### الإخراج عند الصفر

**الإخراج عند الصفر** هو قيمة الإخراج المقاسة عند تقديم رمز الإدخال الرقمي لمستوى الصفر/التعويض إلى DUT.

### نطاق الإخراج الكامل (FSR)

يُسمى نطاق الجهد الناتج عن DAC بين الحد الأدنى ($V_{ZS}$) والحد الأقصى ($V_{FS}$) من الإخراجات التناظرية بـ **نطاق الإخراج الكامل (FSR)**:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20221011142249.png)

### حجم LSB

يتم تعريف التغيير المتوسط في الجهد عندما يكون بين رموز الإدخال باسم LSB:

$$
LSB=\frac{FSR_{measured}}{2^{bits}-1}
$$

### خطأ الإزاحة

**خطأ الإزاحة** (خطأ مستوى الصفر) هو الفرق في الجهد بين نقطة الإزاحة (الأولية) المثالية والفعلية.

$$
OffsetError=V_{ZS(Actual)}-V_{ZS(ideal)}
$$

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20221011144415.png)

### خطأ الزيادة

**خطأ الزيادة** هو الفرق في الجهد بين نقطتي الزيادة المثالية والفعلية على دالة النقل.

$$
GainError=FSR_{Ideal}-FSR_{Actual}
$$

حيث

$$
FSR_{Ideal}=V_{FS(ideal)}-V_{ZS(ideal)}
$$

$$
FSR_{Actual}=V_{FS(Actual)}-V_{ZS(Actual)}
$$

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20221011144925.png)

### خطأ عدم الخطية التفاضلي (DNL)

**خطأ عدم الخطية التفاضلي (DNL)** هو الفرق في الجهد الناتج في نقطة محددة، مقارنة بالإخراج في الإدخال السابق، ثم يطرح منها قيمة LSB الخاصة بالجهاز:

$$
DNL=(V_{in2}-V_{in1})-LSB_{average}
$$

حيث يمثل $V_{in2}$ الجهد في الانتقال العلوي، و $V_{in1}$ الانتقال السفلي.

DNL هو مقياس لخطأ الخطية "الإشارة الصغيرة". يتم قياس DNL من خطوة واحدة إلى الأخرى، وليس من كل خطوة إلى القيمة المثالية.

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20221011153556.png)

### خطأ الخطية الغير متكامل (INL)

**خطأ الخطية الغير متكامل (INL)** هو التأثير التراكمي لجميع قيم الخطأ غير الخطية. إنه مقياس لخطأ الخطية "الإشارة الكبيرة". يتم حساب INL في أي نقطة على المنحنى عن طريق الانحراف عن الخط الخطي المثالي.

$$
ExpectedOutput[i]=FSR*InputCode[i]+OffsetError
$$

$$
INL[i]=\frac{ActualOutput[i]-ExpectedOutput[i]}{LSB_{average}}
$$

كما يمكن التعبير عن INL كدالة لـ DNL:

$$
INL[i]=\sum_{n=1}^{n=i}DNL[n]
$$

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20221011184739.png)

## كيفية اختبار المعلمات الثابتة

### إعداد نظام الاختبار

إعداد نظام الاختبار لاختبار المعلمات الثابتة لـ DAC:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20221011185006.png)

مخطط تدفق إعداد الإشارة:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20221011185447.png)

### مفهوم الاختبارات

يتم سرد إجراء اختبار المعلمات الثابتة لـ DAC DUT أدناه.

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20221011185739.png)

#### 1. قياس الجهد الناتج عن تطبيق الإدخالات الرقمية من الصفر إلى الحد الأقصى

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20221011185711.png)

#### 2. حساب DNL لكل رمز إدخال

$$
DNL[i]=\frac{OutputMeasured[i]-OutputMeasured[i-1]-LSB_{average}}{LSB_{average}}
$$

حيث

$$
LSB_{average}=\frac{OutputMeasured[n]-OutputMeasured[0]}{2^{bits}-1}
$$

#### 3. الحصول على أقصى وأدنى DNL

#### 4. حساب INL لكل خطوة

#### 5. الحصول على أقصى وأدنى INL

## المراجع والشكر

- _أساسيات الاختبار باستخدام ATE_
- _The-Fundamentals-of-Mixed-Signal-Testing_Brian-Lowe_

> الأصلي: <https://wiki-power.com/>  
> يتم حماية هذا المنشور باتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) ويجب إعادة إنتاجه مع الإشارة إلى المصدر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.
