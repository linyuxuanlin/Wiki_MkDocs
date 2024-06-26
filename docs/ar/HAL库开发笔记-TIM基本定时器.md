# ملاحظات تطوير مكتبة HAL - المؤقت الأساسي TIM

في STM32 ، هناك ثلاثة أنواع من المؤقتات: المؤقت الأساسي والمؤقت العام والمؤقت المتقدم ، والتي تستخدم لمعالجة مهام الدورة المتكررة المختلفة. في هذه المقالة ، سأقدم شرحًا مفصلاً للمؤقت الأساسي.

## المبدأ الأساسي

نحن نستخدم عادة المؤقتات الأساسية كمؤقتات ، ونستخدم المؤقتات العامة لإخراج إشارات PWM.

### خصائص المؤقت الأساسي

في STM32F4 ، تتمتع المؤقتات الأساسية TIM6 و TIM7 بالخصائص التالية:

- مرتبطة بشبكة APB1
- عداد تزايدي بتحميل تلقائي بقيمة 16 بت
- مقسم قابل للبرمجة بقيمة 16 بت ، يستخدم لتقسيم تردد ساعة العداد (أي التعديل أثناء التشغيل) ، وتتراوح قيم التقسيم بين 1 و 65536
- دائرة مزامنة لتشغيل DAC
- يولد طلبات انتهاء التجاوز عند حدوث حدوث تجاوز العداد

### مراجع الوظائف الزمنية الشائعة

- **HAL_TIM_Base_Init()**: تهيئة وحدة المؤقت الأساسية
- **HAL_TIM_Base_DeInit()**: تعطيل المؤقت ، عكس العملية التهيئة
- **HAL_TIM_Base_MspInit()**: دالة التهيئة MSP ، يتم استدعاؤها تلقائيًا عند تهيئة المؤقت
- **HAL_TIM_Base_MspDeInit()**: عكس العملية السابقة
- **HAL_TIM_Base_Start()**: تشغيل المؤقت
- **HAL_TIM_Base_Stop()**: إيقاف المؤقت
- **HAL_TIM_Base_Start_IT()**: تشغيل المؤقت بوضع الانقطاع
- **HAL_TIM_Base_Stop_IT()**: إيقاف المؤقت بوضع الانقطاع
- **HAL_TIM_Base_Start_DMA()**: تشغيل المؤقت بوضع DMA
- **HAL_TIM_Base_Stop_DMA()**: إيقاف المؤقت بوضع DMA

## استخدام المؤقت الأساسي لتومض LED بشكل منتظم

هذه التجربة تستخدم المؤقت الأساسي لتنفيذ وظيفة العد ، حيث يتغير حالة LED كل 0.5 ثانية.

### تكوين المؤقت الأساسي في CubeMX

أولاً ، نفتح صفحة تكوين ساعة الشجرة Clock Configuration ، ونجد ونسجل قيمة APB1 Timer clocks الموجودة على الجانب الأيمن الأقصى:

![](https://media.wiki-power.com/img/20210407152250.png)

هذا يرجع إلى أن TIM2-TIM7 و TIM12-TIM14 في سلسلة STM32F4 مرتبطة بشبكة APB1 ذات السرعة المنخفضة ، بينما TIM1 و TIM8-TIM11 مرتبطة بشبكة APB2 ذات السرعة العالية. نحن نستخدم هنا المؤقت الأساسي TIM6 ، لذا يجب أن ننظر إلى سرعة APB1 (هنا بعد تقسيم التضاعف هي 90 ميجا هرتز).

ثم ، نجد المؤقت TIM6 في الشريط الجانبي Timer ، ونقوم بتحديد "Activated" لتنشيط المؤقت ، ونقوم بتكوين المعلمات التالية في الجزء السفلي:

![](https://media.wiki-power.com/img/20210407173136.png)

معاني المعلمات:

- **Prescaler** (عامل التقسيم المسبق): 8999
- **Counter Mode** (وضع العد): Up (يبدأ العد من 0 ويتجاوز بعد العد إلى عامل التقسيم المسبق)
- **Counter Period** (فترة العد / قيمة التحميل): 4999
- **auto-reload preload** (إعادة التحميل التلقائي): Enable (سيتم إعادة التحميل التلقائي للقيمة الأولية عند الفيض)

نظرًا لأنني استخدم مصدر الساعة هنا بتردد 90 ميجا هرتز ، فإنني أضبط عامل التقسيم المسبق على 8999 (أي تقسيم 9000) ، وبعد التقسيم يكون التردد 10 كيلو هرتز (90 ميجا هرتز / 9000). قيمة التحميل محددة على 4999 (عد كل 5000 مرة في الفترة الواحدة) ، لذا يتم الحصول على فترة 500 مللي ثانية.

ثم نقوم بتمكين الانقطاعات في علامة التبويب NVIC:

![](https://media.wiki-power.com/img/20210407155959.png)

### تكوين المؤقت الأساسي في الشيفرة

افتح المؤقت في `main.c`:

```c title="main.c"
/* USER CODE BEGIN 2 */

HAL_TIM_Base_Start_IT(&htim6);

/* USER CODE END 2 */
```

أضف وظيفة الاستدعاء في `stm32f4xx_it.c`:

```c title="stm32f4xx_it.c"
/* USER CODE BEGIN 1 */

void HAL_TIM_PeriodElapsedCallback(TIM_HandleTypeDef *htim)
{
    if(htim->Instance == TIM6)
    {
        HAL_GPIO_TogglePin(LED1_GPIO_Port, LED1_Pin);
    }

}

/* USER CODE END 1 */
```

لمزيد من المعلومات حول تكوين LED، يمكنك الرجوع إلى المقالة السابقة [**HAL 库开发笔记-GPIO**](https://wiki-power.com/HAL%E5%BA%93%E5%BC%80%E5%8F%91%E7%AC%94%E8%AE%B0%EF%BC%88%E4%BA%8C%EF%BC%89-GPIO) .

عند تنزيل البرنامج، سترى أن LED تتبدل بين الحالات المفتوحة والمغلقة بفترة 500 مللي ثانية (أي أنها تتجاوز كل 500 مللي ثانية وتنتج حدثًا للتجاوز، ونقوم بعملية انعكاس للمصباح LED في وظيفة الاستدعاء).

## المراجع والشكر

- [STM32CubeMX 实战教程（四）—— 基本定时器（还是点灯）](https://blog.csdn.net/weixin_43892323/article/details/104534920)
- [进阶篇 VI [Timer & PWM]](https://alchemicronin.github.io/posts/fd31d369/)

> عنوان النص: <https://wiki-power.com/>
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.
