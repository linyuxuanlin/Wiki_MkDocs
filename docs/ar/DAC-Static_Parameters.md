# DAC - Static Parameters

محول الرقمي إلى تناظري (ADC) هو جهاز يقوم بتحويل تسلسل من البيانات الرقمية الإدخالية إلى إشارات تناظرية.

![](https://media.wiki-power.com/img/20221011141644.png)

## المعلمات الثابتة

تحتوي المعلمات الثابتة لمحول الرقمي إلى تناظري (DAC) بشكل أساسي على:

- الإخراج عند الصفر (Zero Scale Output)
- نطاق الإشارة بالكامل (FSR)
- حجم أقل الوحدة الثنائية (LSB)
- خطأ الإزاحة (Offset Error)
- خطأ الربح (Gain Error)
- خطأ اللاخطية التفاضلي (DNE أو DNL)
- خطأ اللاخطية التكاملي (INE أو INL)

![](https://media.wiki-power.com/img/20221011144045.png)

### الإخراج عند الصفر

**الإخراج عند الصفر** هو القيمة المقاسة للإخراج عندما يتم تقديم رمز الإدخال الرقمي للمستخدم.

### نطاق الإشارة بالكامل (FSR)

النطاق الجهد لإخراج محول الرقمي إلى تناظري (DAC) بين الحد الأدنى ($V_{ZS}$) والحد الأقصى ($V_{FS}$) للإخراج التناظري يُسمى **نطاق الإشارة بالكامل (FSR)**:

![](https://media.wiki-power.com/img/20221011142249.png)

### حجم أقل الوحدة الثنائية (LSB)

تُعرف تغيير متوسط الجهد عند الرموز الإدخالية المتوسطة بالوحدة الأقل (LSB):

$$
LSB=\frac{FSR_{measured}}{2^{bits}-1}
$$

### خطأ الإزاحة (Offset Error)

**خطأ الإزاحة** (الخطأ عند الصفر) هو الفرق الجهد بين النقط الأفتراضية والفعلية (النقط الابتدائية).

$$
OffsetError=V_{ZS(Actual)}-V_{ZS(ideal)}
$$

![](https://media.wiki-power.com/img/20221011144415.png)

### خطأ الربح (Gain Error)

**خطأ الربح** هو الفرق الجهد بين النقط الأفتراضية والفعلية على الدالة التناقلية.

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

![](https://media.wiki-power.com/img/20221011144925.png)

### خطأ اللاخطية التفاضلي (DNL)

**خطأ اللاخطيء التفاضلي (DNL)** هو الفرق في الجهد الناتج في نقطة محددة مقارنة بالإخراج في الإدخال السابق، ثم نقص وحدة الخطوة الأصغر:

$$
DNL=(V_{in2}-V_{in1})-LSB_{average}
$$

حيث $V_{in2}$ هو جهد الانتقال العلوي و$V_{in1}$ هو السفلي.

DNL هو مقياس لخطأ الخطية "بإشارة صغيرة". يتم قياس DNL من خطوة واحدة إلى الأخرى، وليس من كل خطوة إلى القيمة المثلى.

![صورة](https://media.wiki-power.com/img/20221011153556.png)

### خطأ اللاخطيء التكاملي (INL)

**خطأ اللاخطيء التكاملي (INL)** هو التأثير التراكمي لجميع قيم الخطأ غير الخطيء التفاضلي. إنه مقياس لخطأ الخطية "بإشارة كبيرة". INL في أي نقطة على المنحنى هو انحراف الخط الخطي المثالي.

$$
ExpectedOutput[i]=FSR*InputCode[i]+OffsetError
$$

$$
INL[i]=\frac{ActualOutput[i]-ExpectedOutput[i]}{LSB_{average}}
$$

بالإضافة إلى ذلك، يمكن التعبير عن INL أيضًا كوظيفة لـ DNL:

$$
INL[i]=\sum_{n=1}^{n=i}DNL[n]
$$

![صورة](https://media.wiki-power.com/img/20221011184739.png)

## كيفية اختبار المعلمات الثابتة

### إعداد نظام الاختبار

إعداد نظام الاختبار لاختبار المعلمات الثابتة لجهاز التحكم الرقمي إلى تحليله:

![صورة](https://media.wiki-power.com/img/20221011185006.png)

مخطط كتلة لإعداد الإشارة:

![صورة](https://media.wiki-power.com/img/20221011185447.png)

### مفهوم الاختبارات

يتم سرد إجراء اختبار المعلمات الثابتة لوحدة التحكم الرقمية (DAC) فيما يلي.

![صورة](https://media.wiki-power.com/img/20221011185739.png)

#### 1. قياس الجهد الناتج من خلال تطبيق إدخالات البيانات الرقمية من الصفر إلى القيمة الكاملة

![صورة](https://media.wiki-power.com/img/20221011185711.png)

#### 2. حساب DNL لكل رمز إدخال

Here is the provided text translated into Arabic:

```markdown
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
- _أساسيات اختبار الإشارة المختلطة، براين لو_

> المصدر الأصلي: <https://wiki-power.com/>  
> هذا المنشور محمي باتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en)، يجب إعادة إنتاجه مع الإشارة إلى المصدر.
```

Please note that Arabic text is read from right to left, so the mathematical equations and content will be displayed in the correct direction.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.
