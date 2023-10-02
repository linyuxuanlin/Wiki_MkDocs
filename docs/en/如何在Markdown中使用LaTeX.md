# How to Use LaTeX in Markdown

Markdown natively supports writing mathematical formulas and symbols using LaTeX.

## Font Styles

- Line break: `\\`
- Space: `\`
- Centering: wrap with `$$`
- Font styles: bold: `\mathbf`, italic: `\mathit`
- Font size: `\tiny`, `\scriptsize`, `\small`, `\normalsize`, `\large`, `\Large`, `\huge`, `\Huge`
- Color: `\color{color value}{number/letter/symbol}`
- Comment: `\text{content}`

## Arithmetic Operations

- Dot product: `\cdot`
- Cross product: `\times`

## Superscript/Subscript

- Superscript: `^`
- Subscript: `_`
- Use `{}` to nest if necessary.

Example: $$X^{2m}_{3n}$$

## Overline/Underline

- Overline: `\overline`
- Underline: `\underline`

Example: $$\overline{x^2+a+b}$$

## Fractions

Representation of fractions: `\frac{numerator}{denominator}`

## System of Equations

Method 1: `\begin{array}{c} expression 1\\expression 2... \end{array}`
Method 2: `\begin{cases}…\end{cases}`

## Square Root

Format: `\sqrt[n`]{x}`, where `n` represents the root degree and `x` represents the radicand.

## Greek Letters

| Greek Letter (uppercase) | Expression | Greek Letter (lowercase) | Expression |
| :---------------------: | :-------: | :----------------------: | :--------: |
|            A            |     A     |            α             |   \alpha   |
|            B            |     B     |            β             |   \beta    |
|            Γ            |   \Gamma  |            γ             |   \gamma   |
|            Δ            |   \Delta  |            δ             |   \delta   |
|            E            |     E     |            ϵ             |  \epsilon  |
|            Z            |     Z     |            ε             | \varepsilon |
|            H            |     H     |            η             |    \eta    |
|            Θ            |   \Theta  |            θ             |   \theta   |
|            I            |     I     |            ι             |    \iota   |
|            K            |     K     |            κ             |   \kappa   |
|            Λ            |  \Lambda  |            λ             |  \lambda   |
|            M            |     M     |            μ             |    \mu    |
|            N            |     N     |            ν             |    \nu    |
|            Ξ            |    \Xi    |            ξ             |    \xi     |
|            O            |     O     |            ο             |  \omicron  |
|            Π            |    \Pi    |            π             |    \pi     |
|            P            |     P     |            ρ             |    \rho    |
|            Σ            |   \Sigma  |            σ             |   \sigma   |
|            T            |     T     |            τ             |    \tau    |
|            Υ            |  \Upsilon |            υ             |  \upsilon |
|            Φ            |   \Phi   |            ϕ             |    \phi    |
|            −            |     -     |            φ             |  \varphi  |
|            X            |     X     |            χ             |    \chi    |
|            Ψ            |   \Psi   |            ψ             |    \psi    |
|            Ω            |  \Omega   |            ω             |   \omega   |

## Operators

| Operator | Expression | Operator | Expression |
| :------: | :-------: | :------: | :-------: |
|   ±     |    \pm    |    ∅     | \emptyset |
|    ×     |   \times  |    ∈     |    \in    |
|    ÷     |    \div   |    ∉     |  \notin   |
|    ∣     |    \mid   |    ⊂     |  \subset  |
|    ⋅     |   \cdot   |    ⊃     |  \supset  |
|    ∘     |   \circ   |    ⊆     | \subseteq |
|    ∗     |    \ast   |    ⊇     | \supseteq |
|    ⨀     |  \bigodot |    ⋂     |  \bigcap  |
|    ⨂     | \bigotimes|    ⋃     |  \bigcup  |
|    ⨁     | \bigoplus |    ⋁     |  \bigvee  |
|    ≤     |    \leq   |    ⋀     | \bigwedge |
|    ≥     |    \geq   |    ≠     |   \neq   |
|    ≈     |  \approx  |    ≡     |  \equiv  |

## Calculus Symbols

| Operator | Expression | Operator | Expression |
| :------: | :-------: | :------: | :-------: |
|    ∮     | \oint     |    ∞     | \infty   |
|    ∇     | \nabla    |    ∫     |  \int    |
|    ∑     |  \sum     |   lim    |  \lim    |
|    →     | \vec{}    |    -     |    -     |

## Logical Symbols

| Operator |  Expression | Operator |   Expression  |
| :------: | :---------: | :------: | :-----------: |
|    ∵     | \because    |    ∴     | \therefore    |
|    ∀     | \forall     |    ∃     |  \exists      |

## References and Acknowledgments

- [Markdown Mathematical Formula](https://markdown.budshome.com/formula.html)
- [LaTeX-Symbols.pdf](https://def.fe.up.pt/latex/Symbols.pdf)

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.