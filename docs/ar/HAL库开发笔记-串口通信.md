# ملاحظات تطوير مكتبة HAL - الاتصال السلكي

يستند هذا المقال إلى مجموعة تطوير RobotCtrl الخاصة بنا ، ويتم تشغيل نواة الميكروكنترولر باستخدام STM32F407ZET6 ، ويتم استخدام رقاقة SP3232EEN للاتصال RS-232 ، يرجى الرجوع إلى المخطط الأساسي والمقدمة التفصيلية في [**RobotCtrl - STM32 通用开发套件**](https://wiki-power.com/ar/RobotCtrl-STM32%E9%80%9A%E7%94%A8%E5%BC%80%E5%8F%91%E5%A5%97%E4%BB%B6) .

## المبادئ الأساسية

يرجى الرجوع إلى مقالة [**通信协议-串口通信**](https://wiki-power.com/ar/%E9%80%9A%E4%BF%A1%E5%8D%8F%E8%AE%AE-%E4%B8%B2%E5%8F%A3%E9%80%9A%E4%BF%A1) للحصول على المبادئ الأساسية للاتصال السلكي.

## تجربة الاتصال السلكي

قبل القيام بالتجربة التالية ، يجب تكوين معلمات الاتصال السلكي والتوقيت وغيرها من المعلمات في CubeMX. يرجى الرجوع إلى الخطوات المحددة في المقالة [**HAL 库开发笔记 - 环境配置**](https://wiki-power.com/ar/HAL%E5%BA%93%E5%BC%80%E5%8F%91%E7%AC%94%E8%AE%B0-%E7%8E%AF%E5%A2%83%E9%85%8D%E7%BD%AE) للحصول على التكوين.

### تكوين الاتصال السلكي داخل CubeMX

![](https://img.wiki-power.com/d/wiki-media/img/20210207100329.png)

وفقًا للمخطط الأساسي ، فإن منفذ الاتصال الذي سنستخدمه للتجربة هو `USART1` ، أيًا كانت دبابيس `PA9` `PA10`. لذلك ، يجب أولاً تكوين هاتين الدبوسين كوظيفة إرسال واستقبال `USART1` داخل CubeMX ، ثم انقر فوق علامة التبويب USART1 على الجانب الأيسر وقم بتعيين الوضع (Mode) إلى غير متزامن (Asynchronous) وتعديل معلمات مثل معدل البود (Baud Rate) في الأسفل:

![](https://img.wiki-power.com/d/wiki-media/img/20210207100941.png)

تفاصيل المعلمات على النحو التالي:

- **إعدادات معدل البود** (Baud Rate): لا يوجد معدل بود أفضل من غيره ، يجب تعديله وفقًا للحالة الفعلية ، ويجب أن يتطابق مع مساعد التصحيح السلكي.
- **عدد البيانات** (Word Length): إذا تم تمكين التحقق من الزوجية ، فسيتم تقليل البيانات الفعلية عند هذا العدد.
- **التحقق من الزوجية** (Parity): يمكن اختيار التحقق من الزوجية أو عدم التحقق.
- **عدد أوقات التوقف** (Stop Bits): يتم استخدام بت إضافي واحد أو اثنين كإشارة إنهاء الإرسال أو الاستقبال.
- **اتجاه البيانات** (Data Direction): يمكن اختيار الإرسال فقط أو الاستقبال فقط أو وضع الإرسال والاستقبال.
- **التخميد** (Over Sampling): يمكن أن يؤدي معدل العينات 8 أو 16 مرة إلى تقليل الأخطاء في البيانات.

أخيرًا ، يجب تمكين انقطاع الاتصال السلكي لـ USART1 في علامة التبويب NVIC ، كما هو موضح في الشكل:

![](https://img.wiki-power.com/d/wiki-media/img/20210207104641.png)

### تكوين الاتصال السلكي داخل الشفرة

أولاً ، يجب إضافة الشفرة التالية إلى نهاية `stm32f4xx_it.c`:

```c title="stm32f4xx_it.c"
/* USER CODE BEGIN 1 */
void HAL_UART_RxCpltCallback(UART_HandleTypeDef *huart)
{
    if(huart->Instance==USART1)
    {
        HAL_UART_Receive_IT(huart, &aRxBuffer, 1); // 接收并写入 aRxBuffer
        HAL_UART_Transmit(huart, &aRxBuffer, 10, 0xFFFF); // 把接收到的 aRxBuffer 发回去
    }
}
/* USER CODE END 1 */
```

حيث `Buffer` هو متغير عالمي من نوع uint8_t محدد في `main.c`. يتم إنشاء انقطاع الاتصال السلكي بعد كل بايت يتم استقباله ، ويتم إرجاع البيانات الخاصة بهذا البايت وإعادة تمكين الانقطاع. يجب تعريفه في كل من `main.c` و `stm32f4xx_it.c`:

```c title="main.c"
/* المتغيرات الخاصة -----------------------------------------------------------*/
/* USER CODE BEGIN PV */

uint8_t aTxBuffer[] = "USART TEST\r\n"; // سلسلة للإرسال
uint8_t aRxBuffer[20]; // سلسلة للإستقبال

/* USER CODE END PV */
```

```c title="stm32f4xx_it.c"
/* المتغيرات الخاصة -----------------------------------------------------------*/
/* USER CODE BEGIN PV */

extern uint8_t aTxBuffer;
extern uint8_t aRxBuffer;

/* USER CODE END PV */

```

بالإضافة إلى ذلك ، في `main.c` ، نحتاج إلى إضافة دالة تفعيل تقاطع الإستقبال بعد تهيئة المنفذ التسلسلي وقبل الحلقة الرئيسية:

```c title="main.c"
/* USER CODE BEGIN 2 */

HAL_UART_Receive_IT(&huart1, (uint8_t *)aRxBuffer, 1); // دالة تفعيل تقاطع الإستقبال

/* USER CODE END 2 */
```

يمكن أيضًا إرسال رسالة تهيئة للإشارة إلى أن المنفذ التسلسلي قد تم تشغيله:

```c title="main.c"
/* USER CODE BEGIN 2 */

HAL_UART_Transmit(&huart1, (uint8_t*) aTxBuffer, sizeof(aTxBuffer) - 1, 0xFFFF); // إرسال aTxBuffer المخصص السابق

/* USER CODE END 2 */
```

إذا كنت بحاجة إلى إعادة توجيه printf (استخدام دالة printf في STM32 كوظيفة إخراج المنفذ التسلسلي) ، يرجى الرجوع إلى [**STM32CubeIDE 串口重定向（printf）及输出浮点型**](https://wiki-power.com/ar/STM32CubeIDE%E4%B8%B2%E5%8F%A3%E9%87%8D%E5%AE%9A%E5%90%91%EF%BC%88printf%EF%BC%89%E5%8F%8A%E8%BE%93%E5%87%BA%E6%B5%AE%E7%82%B9%E5%9E%8B) .

### التحميل والتحقق

بعد نجاح تفريغ البرنامج ، نفتح مساعد المنفذ التسلسلي ونقوم بتكوين المنفذ ومعدل البت المناسبين.

بعد الاتصال بالمنفذ التسلسلي ، سيتم طباعة محتوى `aTxBuffer` أولاً ، ثم سيتم إعادة طباعة `aRxBuffer` الذي تم استقباله. كما هو موضح في الصورة:

![](https://img.wiki-power.com/d/wiki-media/img/20210403232628.png)

## المراجع والشكر

- [STM32CubeMX 实战教程（六）—— 串口通信](https://blog.csdn.net/weixin_43892323/article/details/105339949)
- [进阶篇 III [UART & USART]](https://alchemicronin.github.io/posts/b4c69a89/#1-0-%E4%BB%80%E4%B9%88%E6%98%AFUART%E5%92%8CUSART%EF%BC%9F%E6%9C%89%E4%BB%80%E4%B9%88%E5%8C%BA%E5%88%AB%E5%98%9B%EF%BC%9F)
- [STM32 非阻塞 HAL_UART_Receive_IT 解析与实际应用](https://zhuanlan.zhihu.com/p/147414331)
- [HAL 库教程 6：串口数据接收](https://blog.csdn.net/geek_monkey/article/details/89165040)

> عنوان النص: <https://wiki-power.com/>  
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.
