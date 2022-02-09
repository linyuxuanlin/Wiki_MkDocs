---
id: 如何在Markdown中使用LaTeX
title: 如何在 Markdown 中使用 LaTeX
---

Markdown 原生支持使用 LaTeX 编写数学公式和符号。

## 字体样式

- 换行：`\\`
- 空格：`\`
- 居中：使用 `$$` 包裹
- 字体样式：加粗：`\mathbf`、斜体：`\mathit`
- 字体大小：`\tiny`、`\scriptsize`、`\small`、`\normalsize`、`\large`、`\Large`、`\huge`、`\Huge`
- 颜色：`\color{颜色值}{数/字/符}`
- 注释：`\text{内容}`

## 四则运算

- 点乘：`\cdot`
- 叉乘：`\times`

## 上 / 下标

- 上标：`^`
- 下标：`_`
- 如有嵌套，使用 `{}` 包含。

例： $$X^{2m}_{3n}$$

## 上 / 下划线

- 上划线：`\overline`
- 下划线：`\underline`

例：$$\overline{x^2+a+b}$$

## 分数

分数的表示：`\frac{分子}{分母}`

## 方程组

方式一：`\begin{array}{c} 表达式一\\表达式二... \end{array}`
方式二：`\begin{cases}…\end{cases}`

## 开平方根

格式：`\sqrt[n`]{x}`，其中 `n` 表示开根次数，`x` 表示被开方项。

## 希腊字母

| 希腊字母（大写） |  表达式  | 希腊字母 （小写） |   表达式    |
| :--------------: | :------: | :---------------: | :---------: |
|        A         |    A     |         α         |   \alpha    |
|        B         |    B     |         β         |    \beta    |
|        Γ         |  \Gamma  |         γ         |   \gamma    |
|        Δ         |  \Delta  |         δ         |   \delta    |
|        E         |    E     |         ϵ         |  \epsilon   |
|        Z         |    Z     |         ε         | \varepsilon |
|        H         |    H     |         η         |    \eta     |
|        Θ         |  \Theta  |         θ         |   \theta    |
|        I         |    I     |         ι         |    \iota    |
|        K         |    K     |         κ         |   \kappa    |
|        Λ         | \Lambda  |         λ         |   \lambda   |
|        M         |    M     |         μ         |     \mu     |
|        N         |    N     |         ν         |     \nu     |
|        Ξ         |   \Xi    |         ξ         |     \xi     |
|        O         |    O     |         ο         |  \omicron   |
|        Π         |   \Pi    |         π         |     \pi     |
|        P         |    P     |         ρ         |    \rho     |
|        Σ         |  \Sigma  |         σ         |   \sigma    |
|        T         |    T     |         τ         |    \tau     |
|        Υ         | \Upsilon |         υ         |  \upsilon   |
|        Φ         |   \Phi   |         ϕ         |    \phi     |
|        −         |    -     |         φ         |   \varphi   |
|        X         |    X     |         χ         |    \chi     |
|        Ψ         |   \Psi   |         ψ         |    \psi     |
|        Ω         |  \Omega  |         ω         |   \omega    |

## 运算符

| 运算符 |   表达式   | 运算符 |  表达式   |
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

## 微积分符号

| 运算符 | 表达式 | 运算符 | 表达式 |
| :----: | :----: | :----: | :----: |
|   ∮    | \oint  |   ∞    | \infty |
|   ∇    | \nabla |   ∫    |  \int  |
|   ∑    |  \sum  |  lim   |  \lim  |
|   →    | \vec{} |   -    |   -    |

## 逻辑符号

| 运算符 |  表达式  | 运算符 |   表达式   |
| :----: | :------: | :----: | :--------: |
|   ∵    | \because |   ∴    | \therefore |
|   ∀    | \forall  |   ∃    |  \exists   |

## 参考与致谢

- [Markdown 数学公式](https://markdown.budshome.com/formula.html)
- [LaTeX-Symbols.pdf](https://def.fe.up.pt/latex/Symbols.pdf)
