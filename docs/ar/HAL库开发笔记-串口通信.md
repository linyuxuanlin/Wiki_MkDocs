# مذكرات تطوير مكتبة HAL - الاتصال بالمنفذ التسلسلي (Serial Port)

تعتمد هذه المقالة على مجموعة تطوير RobotCtrl المصممة ذاتيًا، والنواة المستخدمة في الوحدة المركزية هي STM32F407ZET6. تستخدم الاتصال RS-232 رقاقة SP3232EEN. لمخطط الدائرة وتفاصيل إضافية، يُرجى الرجوع إلى [**RobotCtrl - مجموعة تطوير STM32 العامة**](to_be_replace[3]).

## المبادئ الأساسية

لفهم المبادئ الأساسية للاتصال عبر المنفذ التسلسلي، يُفضل قراءة المقالة [**بروتوكول الاتصال - الاتصال عبر المنفذ التسلسلي**](to_be_replace[3]).

## تجربة الاتصال عبر المنفذ التسلسلي

قبل البدء في التجارب التالية، يجب تكوين المعلمات المختلفة مثل التنزيل عبر المنفذ التسلسلي وتكوين الساعة في CubeMX. للخطوات التفصيلية، يُفضل الرجوع إلى [**مذكرات تطوير مكتبة HAL - إعداد البيئة**](to_be_replace[3]).

### التكوين داخل CubeMX

![صورة](https://img.wiki-power.com/d/wiki-media/img/20210207100329.png)

بناءً على الدائرة الكهربائية، يتعين علينا تكوين داخل CubeMX المنفذ التسلسلي الذي سنستخدمه في التجربة، وهو "USART1"، أي أنه يجب تعيين دبوسي "PA9" و"PA10" كوظائف الإرسال والاستقبال لـ "USART1". بعد ذلك، ننتقل إلى علامة التبويب USART1 على الجانب الأيسر ونقوم بتعيين الوضع (Mode) على الوضع الغير متزامن (Asynchronous) ونقوم بتعديل معلمات مثل معدل الباود (Baud Rate) كما هو موضح أدناه:

![صورة](https://img.wiki-power.com/d/wiki-media/img/20210207100941.png)

تفاصيل المعلمات هي كالتالي:

- **إعداد معدل الباود** (Baud Rate): يجب تعديله وفقًا للحالة الفعلية ويجب أن يتطابق مع برنامج تصحيح الاتصال عبر المنفذ التسلسلي.
- **عدد البتات للبيانات** (Word Length): إذا تم تفعيل التحقق من الزوجية/الفردية، فإن البيانات الفعلية ستقل ببت واحد.
- **التحقق من الزوجية/الفردية** (Parity): يمكن اختيار التحقق من الزوجية أو الفردية أو عدم التحقق.
- **بتات التوقف** (Stop Bits): بت إضافي واحد أو اثنين يتم استخدامهما كإشارة للإرسال أو الاستقبال الانتهاء.
- **اتجاه البيانات** (Data Direction): يمكن اختيار الإرسال فقط، الاستقبال فقط أو وضع الإرسال والاستقبال.
- **معدل الأخذ الزائد** (Over Sampling): معدل الأخذ الزائد بمعدل 8 مرات أو 16 مرة يمكن أن يحمي بشكل فعال من الأخطاء في البيانات.

أخيرًا، يتعين تمكين انقطاعات المنفذ التسلسلي USART1 على علامة التبويب NVIC كما هو موضح في الصورة أدناه:

![صورة](https://img.wiki-power.com/d/wiki-media/img/20210207104641.png)

### التكوين داخل الشيفرة

أولاً، يجب أن نقوم بإضافة الشيفرة التالية في نهاية الملف "stm32f4xx_it.c":

```c title="stm32f4xx_it.c"
/* USER CODE BEGIN 1 */
void HAL_UART_RxCpltCallback(UART_HandleTypeDef *huart)
{
    if(huart->Instance==USART1)
    {
        HAL_UART_Receive_IT(huart, &aRxBuffer, 1); // استقبال وكتابة البيانات في aRxBuffer
        HAL_UART_Transmit(huart, &aRxBuffer, 10, 0xFFFF); // إعادة إرسال البيانات المُستقبَلة في aRxBuffer
    }
}
/* USER CODE END 1 */
```

حيث تُعرّف المصفوفة "Buffer" كمتغير عالمي من نوع uint8_t في الملف الرئيس

Here is the provided text translated into Arabic while maintaining the original markdown format:

```c title="main.c"
/* المتغيرات الخاصة -----------------------------------------------------------*/
/* USER CODE BEGIN PV */

uint8_t aTxBuffer[] = "اختبار USART\r\n"; // سلسلة للإرسال
uint8_t aRxBuffer[20]; // سلسلة للاستقبال

/* USER CODE END PV */
```

```c title="stm32f4xx_it.c"
/* المتغيرات الخاصة -----------------------------------------------------------*/
/* USER CODE BEGIN PV */

extern uint8_t aTxBuffer;
extern uint8_t aRxBuffer;

/* USER CODE END PV */

```

وبالإضافة إلى ذلك، في `main.c`، نحتاج إلى إضافة دالة تمكين انقطاع الاستقبال بعد تهيئة المنفذ الفعالة وقبل دورة البرنامج الرئيسية:

```c title="main.c"
/* USER CODE BEGIN 2 */

HAL_UART_Receive_IT(&huart1, (uint8_t *)aRxBuffer, 1); // دالة تمكين انقطاع الاستقبال

/* USER CODE END 2 */
```

يمكن أيضًا إرسال رسالة تهيئة للإشارة بأن المنفذ جاهز للاستخدام:

```c title="main.c"
/* USER CODE BEGIN 2 */

HAL_UART_Transmit(&huart1, (uint8_t*) aTxBuffer, sizeof(aTxBuffer) - 1, 0xFFFF); // إرسال محتوى aTxBuffer المخصص السابق

/* USER CODE END 2 */
```

إذا كنت بحاجة إلى إعادة توجيه printf (استخدام وظيفة printf لإخراج البيانات عبر المنفذ السلسلي في STM32)، يُرجى الرجوع إلى [**STM32CubeIDE 串口重定向（printf）及输出浮点型**](https://wiki-power.com/ar/STM32CubeIDE%E4%B8%B2%E5%8F%A3%E9%87%8D%E5%AE%9A%E5%90%91%EF%BC%88printf%EF%BC%89%E5%8F%8A%E8%BE%93%E5%87%BA%E6%B5%AE%E7%82%B9%E5%9E%8B) للمزيد من المعلومات.

### التنزيل والتحقق

بعد نجاح حرق البرنامج، نقوم بفتح مساعد المنفذ السلسلي وضبط المنفذ ومعدل البت.

بمجرد الاتصال بالمنفذ، سيتم طباعة محتوى `aTxBuffer` أولاً، ثم سيتم إعادة طباعة المحتوى الذي تم استقباله في `aRxBuffer`. كما هو موضح في الصورة:

![صورة](https://img.wiki-power.com/d/wiki-media/img/20210403232628.png)

## المراجع والشكر

- [STM32CubeMX 实战教程（六）—— 串口通信](https://blog.csdn.net/weixin_43892323/article/details/105339949)
- [进阶篇 III [UART & USART]](https://alchemicronin.github.io/posts/b4c69a89/#1-0-%E4%BB%80%E4%B9%88%E6%98%AFUART%E5%92%8CUSART%EF%BC%9F%E6%9C%89%E4%BB%80%E4%B9%88%E5%8C%BA%E5%88%AB%E5%98%9B%EF%BC%9F)
- [STM32 非阻塞 HAL_UART_Receive_IT 解析与实际应用](https://zhuanlan.zhihu.com/p/147414331)
- [HAL 库教程 6：串口数据接收](https://blog.csdn.net/geek_monkey/article/details/89165040)

> عنوان النص: <https://wiki-power.com/>  
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.



> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.