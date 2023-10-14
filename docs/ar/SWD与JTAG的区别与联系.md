# الفرق والتشابه بين SWD و JTAG

كما هو معروف ، فإن SWD و JTAG هما واجهتان شائعتان لتنزيل البرامج وتصحيح الأخطاء في الميكروكنترولر. ومن بين ما يشتركان فيه:

- **نطاق الجهد المتوفر**: 1.2 فولت - 5.5 فولت
- **معدل الساعة**: يمكن تكوينه حتى 10 ميجاهرتز
- **تتبع SWO**: معدل بيانات يصل إلى 50 ميجابت / ثانية (وضع UART / NRZ)
- **الجهد العازل**: 1 كيلوفولت
- **التوصيل الساخن**: مدعوم

## JTAG

JTAG هو اختصار لـ Joint Test Action Group (مجموعة عمليات الاختبار المشتركة). ويتوافق مع أحدث المعايير IEEE Standard 1149.1-1990.

إن توبولوجيا JTAG (سلسلة الزهور) هي كما يلي:

![](https://img.wiki-power.com/d/wiki-media/img/20210209191921.png)

يستخدم JTAG عادة 5 دبابيس:

- **TDI** (Test Data In): دبوس الإدخال التسلسلي
- **TDO** (Test Data Out): دبوس الإخراج التسلسلي
- **TCK** (Test Clock): دبوس الساعة ، ويتم تضمين مقاومة سحب 100 كيلو أوم عادةً
- **TMS** (Test Mode Select): دبوس اختيار الوضع (إشارة التحكم)
- **TRST** (Test Reset): دبوس الإعادة

مزايا JTAG:

- لا يقتصر على مجموعة ARM من الشرائح
- لديها المزيد من الاستخدامات للبرمجة والتصحيح واختبار الإنتاج

## SWD

يعني Serial Wire Debug (تصحيح الأسلاك التسلسلية) ، وهو بروتوكول تم تصميمه خصيصًا لـ ARM ويدعم فقط ARM (لذلك يتم تمثيل أدائه بشكل أفضل في ميكروكنترولر سلسلة ARM).

يستخدم SWD عادة 2 دبوس:

- **SWDIO** (Serial Wire Data Input Output): دبوس إدخال / إخراج البيانات التسلسلية
- **SWCLK** (Serial Wire Clock): دبوس ساعة الأسلاك التسلسلية

مزايا SWD:

- يستخدم أقل عدد من الدبابيس ، مع الحاجة فقط إلى دبوسي SWDIO و SWCLK
- يحتوي SWD على وظائف خاصة مثل طباعة معلومات التصحيح
- بالمقارنة مع JTAG ، يتمتع SWD بأداء أفضل في السرعة

## التوافق بين JTAG و SWD

عمومًا ، يحتوي لوحة الميكروكنترولر على مقابس الحرق التالية ، والتي يمكن أن تدعم JTAG و SWD في نفس الوقت:

![](https://img.wiki-power.com/d/wiki-media/img/20210210122923.jpg)

![](https://img.wiki-power.com/d/wiki-media/img/20210210123714.png)

- TCK متوافق مع SWCLK
- TMS متوافق مع SWDIO
- (TDO متوافق مع SWO)

أسباب استخدام SWD بدلاً من JTAG:

- يجب أن يكون تصميم مخطط الدائرة بسيطًا بما فيه الكفاية ويمكن اختباره بدون وظيفة JTAG
- يوجد قيود في حجم اللوحة الدائرية ، ويمكن لـ SWD توفير المساحة
- لم يعد لدى MCU دبابيس إضافية للاستخدام في JTAG

## المراجع والشكر

- [下载调试接口 SWD 和 JTAG 的区别](https://mp.weixin.qq.com/s/MW57t266yvv6TOweeFEUVA)
- [Cortex JTAG，SWD Debug Port Sharing](https://southlife.tistory.com/107)
- [JTAG/SWD Interface](https://www.keil.com/support/man/docs/ulinkplus/ulinkplus_jtagswd_interface.htm)
- [JTAG](https://en.wikipedia.org/wiki/JTAG)

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.