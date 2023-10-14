# كيفية استخدام LaTeX في Markdown

يدعم Markdown بشكل أساسي كتابة الرموز والمعادلات الرياضية باستخدام LaTeX.

## نمط الخط

- السطر الجديد: `\\`
- المسافة: `\`
- الوسط: استخدم `$$` للتغليف
- نمط الخط: عريض: `\mathbf`، مائل: `\mathit`
- حجم الخط: `\tiny`، `\scriptsize`، `\small`، `\normalsize`، `\large`، `\Large`، `\huge`، `\Huge`
- اللون: `\color{قيمة اللون}{رقم/حرف/رمز}`
- التعليق: `\text{المحتوى}`

## العمليات الحسابية الأربعة

- الضرب: `\cdot`
- الجمع: `\times`

## الأس العلوي / الأس السفلي

- الأس العلوي: `^`
- الأس السفلي: `_`
- إذا كان هناك تضمين، استخدم `{}` للتغليف.

مثال: $$X^{2m}_{3n}$$

## الخط العلوي / الخط السفلي

- الخط العلوي: `\overline`
- الخط السفلي: `\underline`

مثال: $$\overline{x^2+a+b}$$

## الكسور

تمثيل الكسور: `\frac{البسط}{المقام}`

## مجموعة المعادلات

الطريقة الأولى: `\begin{array}{c} المعادلة الأولى\\المعادلة الثانية... \end{array}`
الطريقة الثانية: `\begin{cases}…\end{cases}`

## الجذر التربيعي

التنسيق: `\sqrt[n`]{x}`، حيث `n` يشير إلى عدد جذور التربيع، و `x` يشير إلى العنصر الذي يتم استخراج الجذر التربيعي منه.

## الحروف اليونانية

Greek:

| الحروف اليونانية (أحرف كبيرة) | التعبير | الحروف اليونانية (أحرف صغيرة) | التعبير |
| :---------------------------: | :-----: | :---------------------------: | :------: |
|               A               |    A    |                α                |  \alpha  |
|               B               |    B    |                β                |  \beta   |
|               Γ               |  \Gamma |                γ                |  \gamma  |
|               Δ               |  \Delta |                δ                |  \delta  |
|               E               |    E    |                ϵ                | \epsilon |
|               Z               |    Z    |                ε                | \varepsilon |
|               H               |    H    |                η                |   \eta   |
|               Θ               |  \Theta |                θ                |  \theta  |
|               I               |    I    |                ι                |   \iota  |
|               K               |    K    |                κ                |  \kappa  |
|               Λ               | \Lambda |                λ                | \lambda |
|               M               |    M    |                μ                |   \mu   |
|               N               |    N    |                ν                |   \nu   |
|               Ξ               |   \Xi   |                ξ                |   \xi   |
|               O               |    O    |                ο                | \omicron |
|               Π               |   \Pi   |                π                |   \pi   |
|               P               |    P    |                ρ                |   \rho  |
|               Σ               |  \Sigma |                σ                |  \sigma |
|               T               |    T    |                τ                |   \tau  |
|               Υ               | \Upsilon |                υ                | \upsilon |
|               Φ               |   \Phi  |                ϕ                |   \phi  |
|               −               |    -    |                φ                | \varphi |
|               X               |    X    |                χ                |   \chi  |
|               Ψ               |   \Psi  |                ψ                |   \psi  |
|               Ω               |  \Omega |                ω                |  \omega |

## العمليات الحسابية

| العامل | الصيغة | العامل | الصيغة |
| :----: | :--------: | :----: | :-------: |
|   ±    |    \pm     |   ∅    | \emptyset |
|   ×    |   \times   |   ∈    |    \in    |
|   ÷    |    \div    |   ∉    |  \notin   |
|   ∣    |    \mid    |   ⊂    |  \subset  |
|   ⋅    |   \cdot    |   ⊃    |  \supset  |
|   ∘    |   \circ    |   ⊆    | \subseteq |
|   ∗    |    \ast    |   ⊇    | \supseteq |
|   ⨀    |  \bigodot  |   ⋂    |  \bigcap  |
|   ⨂    | \bigotimes |   ⋃    |  \bigcup  |
|   ⨁    | \bigoplus  |   ⋁    |  \bigvee  |
|   ≤    |    \leq    |   ⋀    | \bigwedge |
|   ≥    |    \geq    |   ≠    |   \neq    |
|   ≈    |  \approx   |   ≡    |  \equiv   |

## رموز الحساب التفاضلي والتكاملي

| العامل | الصيغة | العامل | الصيغة |
| :----: | :----: | :----: | :----: |
|   ∮    | \oint  |   ∞    | \infty |
|   ∇    | \nabla |   ∫    |  \int  |
|   ∑    |  \sum  |  lim   |  \lim  |
|   →    | \vec{} |   -    |   -    |

## رموز المنطق

| العامل |  الصيغة  | العامل |   الصيغة   |
| :----: | :------: | :----: | :--------: |
|   ∵    | \because |   ∴    | \therefore |
|   ∀    | \forall  |   ∃    |  \exists   |

## المراجع والشكر

- [Markdown 数学公式](https://markdown.budshome.com/formula.html)
- [LaTeX-Symbols.pdf](https://def.fe.up.pt/latex/Symbols.pdf)

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.