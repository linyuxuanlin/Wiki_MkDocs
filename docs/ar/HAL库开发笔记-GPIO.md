# ملاحظات تطوير مكتبة HAL - GPIO

## المبدأ الأساسي

GPIO هو مخرج / مدخل عام (General Purpose Input Output).

![](https://media.wiki-power.com/img/20200615205256.jpg)

لنأخذ مثالًا على رقاقة F103C8T6 (الصورة أعلاه) ، بالإضافة إلى الأرجل الملونة (مصدر الطاقة وبعض الوظائف الأخرى) ، يُطلق على جميع الأرجل باسم GPIO. يمكننا أن نرى مدى تعميمها.

وظيفة GPIO هي إدخال / إخراج إشارة كهربائية. دعنا نلقي نظرة على الهيكل الداخلي لها:

![](https://media.wiki-power.com/img/20200615211744.jpg)

- الدبابيس I/O على اليمين هي دبابيس الرقاقة الفعلية. يمنع المقاومتان الثنائيتان المحمية إلى حد ما تدمير الرقاقة بسبب الجهد الغير طبيعي الخارجي.
- الإطار المحاط بالخط الأحمر هو وظيفة الإدخال (قراءة الرقاقة للإشارة الخارجية). المقاومتان الموصلتان بالتبديل ، هما لتحقيق وظيفة الإدخال السحب العلوي / السحب السفلي. إذا لم يتم إغلاق البابين ، فإننا نسميه إدخالًا عائمًا (لا يوجد مستوى مرجعي). جميع طرق الإدخال الثلاثة تعطي قيم رقمية (مستوى عالي / منخفض). بالإضافة إلى ذلك ، هناك وظيفة الإدخال التناظرية ، كما يوحي الاسم ، وهي قراءة الكمية التناظرية على الدبوس. (سنتطرق إلى وظيفة الإدخال المشتركة لاحقًا).
- الإطار المحاط بالخط الأزرق هو وظيفة الإخراج. هناك 4 أنماط للإخراج: الدفع والسحب والدفع المشترك والسحب المشترك.

### أنماط الإدخال والإخراج

أنماط الإدخال:

- **إدخال عائم**: لا سحب علوي ولا سحب سفلي ، هذا هو الوضع الافتراضي بعد إعادة تعيين STM32.
- **إدخال سحب علوي**: قم بإغلاق التبديل الذي يحتوي على مقاومة السحب العلوي للحفاظ على مستوى المرجع عاليًا ، وعندما يكون إشارة الإدخال منخفضة ، يتم تنشيطها.
- **إدخال سحب سفلي**: قم بإغلاق التبديل الذي يحتوي على مقاومة السحب السفلي للحفاظ على مستوى المرجع منخفضًا ، وعندما يكون إشارة الإدخال عالية ، يتم تنشيطها.
- **إدخال تناظري**: في هذا الوضع ، لا يوجد سحب علوي ولا سحب سفلي ، ولا يمر عبر المقاومة المنطقية TTL ، يقرأ STM32 مباشرة الإشارة التناظرية على الدبوس.

أنماط الإخراج:

- **إخراج سحب**: يشير سحب إلى تصريف المصدر (الدبوس العلوي للمفتاح العلوي) ، يتم استخدام هذا الوضع فقط للمفتاح السفلي. نعلم أن المفتاح MOS هو عنصر قابل للتحكم بالجهد. فهمه كصنبور ماء ، عند إدخال إشارة جهد منخفض على بوابة MOS العلوية (الدبوس الأيسر) ، يتم توصيل MOS السفلي.
- **إخراج الدفع**: هناك نوعان من أنماط الدفع ، النوع الأول هو إدخال إشارة جهد منخفض على بوابتي MOS في نفس الوقت ، في هذه الحالة يتم قطع MOS العلوي وتوجيه التيار من VDD إلى الدبوس الخارجي ، ويكون المستوى العالي على الدبوس. النوع الثاني هو العكس ، إدخال إشارة جهد عالي على بوابتي MOS في نفس الوقت ، في هذه الحالة يتم قطع MOS العلوي وتوجيه التيار من الدبوس الخارجي إلى GND الداخلي ، ويكون المستوى المنخفض على الدبوس.
- **الدفع المشترك**
- **السحب المشترك**

### مراجع الدوال GPIO الشائعة

قراءة حالة GPIO ، وإرجاع مستوى عالي / منخفض:

```c
GPIO_PinState HAL_GPIO_ReadPin(GPIOx ، GPIO_Pin);
```

كتابة حالة GPIO ، وكتابة مستوى عالي / منخفض:

```c
HAL_GPIO_WritePin(GPIOx ، GPIO_Pin ، PinState);
```

عكس مستوى GPIO:

```c
HAL_GPIO_TogglePin(GPIOx ، GPIO_Pin);
```

## تشغيل LED

قبل المتابعة إلى التجربة التالية ، يجب تكوين معلمات مختلفة مثل تنزيل المنفذ التسلسلي والساعة في CubeMX.
لن نتطرق إلى ذلك هنا ، يرجى الرجوع إلى المقالة [**HAL 库开发笔记 - 环境配置**](https://wiki-power.com/HAL%E5%BA%93%E5%BC%80%E5%8F%91%E7%AC%94%E8%AE%B0-%E7%8E%AF%E5%A2%83%E9%85%8D%E7%BD%AE) لمعرفة كيفية التكوين.

### تكوين GPIO في CubeMX

قم بتعيين المنفذ المناسب للمصباح LED كمخرج وقم بتعيين المستوى الابتدائي.

![](https://media.wiki-power.com/img/20210205150422.png)

على اللوحة الخاصة بي ، يجب تعيين دبوس `PD4` و `PI3` هذين GPIO كمخرج (`GPIO_Output`).
إذا كنت ترغب في تشغيل المصباح عند تشغيل الطاقة ، فقم بتعيين المستوى الابتدائي على منخفض (`Low`).

### تكوين GPIO في الكود

إذا تم التكوين بشكل صحيح ، يمكن تشغيل مصابيح LED المستخدم عند تشغيل الطاقة.  
إذا كنت ترغب في إضافة تأثير وميض للمصابيح ، فما عليك سوى إضافة بضعة أسطر من الكود في منطقة الكود الخاصة بالمستخدم في الحلقة الرئيسية:

```c title="main.c"
/* USER CODE BEGIN 3 */

HAL_Delay(500);
HAL_GPIO_TogglePin(GPIOD ، GPIO_PIN_4);
HAL_GPIO_TogglePin(GPIOI ، GPIO_PIN_3);

}
/* USER CODE END 3 */
```

![](https://media.wiki-power.com/img/20210205151322.png)

يمكن تحقيق تأثير وميض المصابيح.

## تحكم الأضواء باستخدام الأزرار

بعد تعلم إخراج GPIO ، سنتعلم الآن وضع الإدخال لـ GPIO باستخدام الأزرار.

### تكوين GPIO في CubeMX

بعد تكوين منفذ GPIO الذي ينتمي إليه المصابيح وفقًا للطريقة المذكورة أعلاه ، استنادًا إلى مخطط الأزرار المدمج:

![](https://media.wiki-power.com/img/20210205150422.png)

قم بتعيين GPIO المرتبط بالزر (PI8) كإدخال (GPIO_Input). استنادًا إلى المخطط الأساسي ، حدد السحب العلوي الداخلي (Pull-up). قم بتوليد الكود.

### تكوين GPIO في الكود

أضف الكود التالي في منطقة الكود الخاصة بالمستخدم في الحلقة الرئيسية:

```c title="main.c"
/* USER CODE BEGIN 3 */

if(HAL_GPIO_ReadPin(KEY1_GPIO_Port,KEY1_Pin)==0)
{
	HAL_Delay(100);
	if(HAL_GPIO_ReadPin(KEY1_GPIO_Port,KEY1_Pin)==0)
	{
		HAL_GPIO_WritePin(LED1_GPIO_Port,LED1_Pin,GPIO_PIN_RESET);
	}
}else{
	HAL_GPIO_WritePin(LED1_GPIO_Port,LED1_Pin,GPIO_PIN_SET);
}

}
/* USER CODE END 3 */
```

بهذه الطريقة يمكن تحقيق تأثير تشغيل الأضواء عند الضغط على الزر وإيقاف تشغيلها عند رفع الضغط عنه.

هناك العديد من الأشخاص الذين لا يفهمون ماذا يعني `GPIO_PIN_SET` و `GPIO_PIN_RESET`. في الواقع ، تقوم هاتين المتغيرتين بتعيين مستوى الجهد العالي / المنخفض للمنفذ GPIO فقط. يعتمد ما إذا كانت المصابيح مشتعلة أو مطفأة على مخطط الدائرة.

بالإضافة إلى ذلك ، يقوم `HAL_Delay(100)` بإزالة اهتزاز الزر في الكود. ومع ذلك ، يستخدم الدالة `HAL_Delay()` الاستطلاع ، مما يستهلك الموارد ويتسبب في تعليق النظام. في المقالة التالية ، سنستخدم المقاطعات الأجهزة لحل هذا العيب.

## المراجع والشكر

- [【STM32】STM32CubeMX 教程二 -- 基本使用 (新建工程点亮 LED 灯)](https://blog.csdn.net/as480133937/article/details/98947162)
- [STM32CubeMX 实战教程（二）—— 按键点个灯](https://blog.csdn.net/weixin_43892323/article/details/104343933)

> عنوان النص: <https://wiki-power.com/>  
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.
