# أساسيات التحويلات فورييه

هناك عدة خوارزميات لتحويل البيانات من مجال الزمن إلى مجال التردد كما يلي.

## سلسلة فورييه

**سلسلة فورييه** هي عبارة عن إنشاء موجة معقدة عن طريق جمع موجات جيبية نقية بأمبليتودات وترددات مختلفة، وتفكيك إشارة معقدة إلى مجموعة من الجيبيات ذات الأمبليتودات والترددات المختلفة.

### شروط ديريشليه

تحدد شروط ديريشليه مجموعة من الشروط التي يجب توفرها قبل أن يمكن تفكيك إشارة إلى سلسلة فورييه:

- الإشارة هي وظيفة رياضية، أي أن هناك نقطة واحدة وفقط تتوافق مع كل نقطة على محور الإكس.
- الإشارة دورية.
- المساحة المحصورة بواسطة الإشارة على مدى فترة واحدة هي محددة.

### تفكيك إلى سلسلة فورييه

يمكن تمثيل إشارة معقدة تفي بشروط ديريشليه على أنها مجموع لجيبيات:

$$
f(t)=a_0+A\{\sum_{n=1}^\infty[a_n cos(n \omega_1 t+\phi_n)+b_n sin(n \omega_1 t+\phi_n)]\}
$$

حيث:

- $a_0$ هو المكون التيار المستمر (DC).
- $A$ هو عامل تكبير عام لجميع المكونات الهارمونية.
- $\omega_1$ هو تردد الجيب الأساسي.
- $n$ هو مضاعف صحيح لتردد الجيب الأساسي لكل مصطلح هارموني.

يثبت ذلك أنه ليس فقط بإمكاننا جمع سلسلة من الموجات السينية والكوسينية لإنشاء أي موجة أخرى، ولكن أيضًا أن ترددات الجيبيات هي مضاعفات صحيحة (هارمونيات) لتردد واحد أساسي.

## تحويل فورييه متقطع (DFT)

**تحويل فورييه متقطع (DFT)**: يأخذ البيانات بالنسبة للأمبليتود مقابل الزمن، ومن ثم يترجمها إلى الأمبليتود مقابل التردد.

رياضياً، الخوارزمية هي مجموعة متتابعة لضرب كل نموذج في وقت معقد في عدد مركب:

$$
X(b)=\sum_{n=0}^{N-1}x[n](cos(2\pi nb/N)-jsin(2\pi nb/N))
$$

حيث:

- $n$ هو أحد $N$ عينات.
- $N$ هو إجمالي عدد العينات.
- $b$ هو أحد $B$ أوعية التردد (حيث تمثل كل وعاء نطاق تردد $F_s/N$).
- $j$ هو عامل الخيالي.

خوارزمية DFT تستخدم كل نقطة عينة في المجموعة من 0 إلى N-1 لكل تردد محلل. جميع نقاط العينة N تحتوي على معلومات حول جميع الترددات B، وبالتالي يتطلب كل من الترددات B التي تُرغب في الحصول على معلومات حاجة إلى مجموعة من منتجات العينات الزمنية N. بسبب الأسباب المذكورة أعلاه، يكون معالجة DFT بطيئًا، لأنه يتعين أجراء معاملات بحجم $N^2$. على سبيل المثال، تتطلب DFT بحجم 2000 نقطة مليون حساب، وغالباً ما تكون حسابات العدد العشري أبطأ من حسابات العدد الصحيح.

## تحويل فورييه سريع (FFT)

**تحويل فورييه سريع (FFT)** يحل مشكلة بطء DFT عن طريق تجاوز أجزاء من المجاميع التي تنتج معلومات متكررة. قواعد استخدام FFT:

- يجب أن يكون عدد نقاط العينة قوة للعدد 2 ($2^n$).
- عدد الجمعيات والضرب هو: $\frac{N}{2}\log_2 N$.

## المراجع والاعترافات

- _أسس الاختبار باستخدام ATE_
- _أسس اختبار الإشارة المختلطة بواسطة Brian Lowe_

> النص الأصلي: <https://wiki-power.com/>
> يتم حماية هذا المنشور باتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en)، ويجب إعادة الإنتاج مع الإشارة إلى المصدر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.