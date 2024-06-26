# مخطط الطاقة (Buck) - XL2009E1

XL2009E1 هو رقاقة Buck من شركة شينلونج ، بإدخال يصل إلى 36 فولت ، وإخراج 3 أمبير ، وتردد ثابت 180 كيلو هرتز ، ويتميز بوظيفة حماية التيار الزائد ، حيث يتم تخفيض التردد إلى 48 كيلو هرتز عند حدوث اختصار.

مستودع المشروع: [**Collection_of_Power_Module_Design/DC-DC(Buck)/XL2009E1**](<https://github.com/linyuxuanlin/Collection_of_Power_Module_Design/tree/main/DC-DC(Buck)/XL2009E1>)

## الميزات الرئيسية

- الهيكل: DC/DC (Buck)
- رقم الجهاز: XL2009E1
- الحزمة: SOP8L
- الجهد الداخلي: 8-36 فولت
- الجهد الخارجي: 1.25-32 فولت
- الفرق الأدنى بين الجهد الداخلي والخارجي: 0.3 فولت
- أقصى نسبة تشغيل: 100%
- التردد العملي: ثابت 180 كيلو هرتز
- أقصى تيار خرج: 3 أمبير
- الكفاءة (الجهد الداخلي 12 فولت ، الجهد الخارجي 5 فولت @ 2.1 أمبير): 89%
- السعر المرجعي: 2.1 يوان صيني
- ميزات أخرى
  - حلقة تيار ثابت للإخراج
  - حماية مدمجة من الاختصار
  - حماية مدمجة من التيار الحد

## دائرة تطبيق نموذجية

وفقًا للدليل الفني ، يتم توفير دائرة تطبيق نموذجية (مدخل 8-36 فولت ، إخراج 5 فولت @ 2.1 أمبير):

![](https://media.wiki-power.com/img/20220407103157.png)

## تعريف الأقطاب

![](https://media.wiki-power.com/img/20220407065806.png)

- FB: دخل ردود الفعل ، يتم تقسيمه بواسطة مقاومة من $V_{OUT}$ للحصول على ردود الفعل ، ولا يمكن توصيله مباشرة إلى الأرض. الجهد المرجعي لردود الفعل هو 1.25 فولت.
- OCSET: دخل ضبط تيار الإخراج الثابت.
- VC: مكثف تجاوز المنظم الداخلي. عادة ما يتم توصيله بين 1 ميكروفاراد إلى VIN.
- VIN: دخل الطاقة. الجهد الداخلي هو 8-36 فولت. يجب أن يكون هناك سعة كبيرة للتوازن.
- SW: إخراج مفتاح Buck.

## وصف الميزات

### مخطط الوظائف الداخلية

![](https://media.wiki-power.com/img/20220407070413.png)

### تعديل الجهد الخارجي

يوفر XL2009E1 جهد مرجع داخلي قدره 1.25 فولت. يتم تقسيم الجهد الخارجي عن طريق مقاومة تقسيم الجهد من $V_{OUT}$ وإدخاله إلى دبوس FB ، ويتم تعديله داخليًا. يُوصى باستخدام مقاومة تقسيم الجهد ذات انحراف 1٪ أو أقل ومعامل حرارة 100 جزء في المليون أو أقل. يُفضل اختيار قيمة مقاومة التقسيم الأعلى لتحسين كفاءة الحمولة الخفيفة ، ولكن إذا كانت كبيرة جدًا ، فإن المنظم سيكون أكثر عرضة للتأثر بضوضاء تيار الإدخال وأخطاء الجهد الناتجة عنه. يُوصى باختيار قيمة مقاومة الجانب السفلي $R_1$ بقيمة 4.7 كيلو أوم ، وحساب قيمة مقاومة الجانب العلوي $R_2$ باستخدام الصيغة التالية:

$$
V_{OUT}=1.25*(1+\frac{R_2}{R_1})
$$

### اختيار ديود شوتكي

من الأفضل أن يكون الجهد الكهربائي الأقصى للثنائي أعلى بنسبة 25٪ من الجهد الكهربائي الأقصى للمدخل. لضمان أقصى قدر من الموثوقية ، يجب أن يكون تيار الثنائي المقدر مساويًا لأقصى تيار خرج للمنظم. في حالة تفوق الجهد الكهربائي للمدخل بكثير على الجهد الكهربائي الخارجي ، سيكون تيار الثنائي المتوسط أقل ، وفي هذه الحالة يمكن استخدام ثنائي بتصنيف تيار متوسط أقل ، ويكون تقريبًا $(1-D) * I_{OUT}$ ، ولكن يجب أن يكون تصنيف التيار الذروي أعلى من أقصى تيار حمل.

يوفر دليل بيانات XL2009E1 جدول اختيار مباشر للثنائي (3 أمبير):

| الجهد الكهربائي | النموذج     |
| --------------- | ----------- |
| 20 فولت         | SK32        |
| 30 فولت         | SK33/30WQ03 |
| 40 فولت         | SK34/30WQ04 |
| 50 فولت         | SK35/30WQ05 |
| 60 فولت         | SK36        |

### منحنيات المعلمات

علاقة الجهد الخارجي بالتيار:

![](https://media.wiki-power.com/img/20220407100229.png)

علاقة الكفاءة بالتيار الخارجي:

![](https://media.wiki-power.com/img/20220407103033.png)

علاقة التيار الخارجي بمقاومة RCS (التحكم بالتيار الثابت):

![](https://media.wiki-power.com/img/20220407102905.png)

## المراجع والشكر

- [XL2009_Datasheet](https://datasheet.lcsc.com/lcsc/1806111754_XLSEMI-XL2009E1_C73335.pdf)

> عنوان النص: <https://wiki-power.com/>
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.
