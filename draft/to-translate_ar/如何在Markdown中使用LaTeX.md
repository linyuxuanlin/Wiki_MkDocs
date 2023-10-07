# Cómo usar LaTeX en Markdown

Markdown admite nativamente el uso de LaTeX para escribir fórmulas y símbolos matemáticos.

## Estilos de fuente

- Salto de línea: `\\`
- Espacio: `\`
- Centrado: usar `$$` para envolver
- Estilos de fuente: negrita: `\mathbf`, cursiva: `\mathit`
- Tamaño de fuente: `\tiny`, `\scriptsize`, `\small`, `\normalsize`, `\large`, `\Large`, `\huge`, `\Huge`
- Color: `\color{valor de color}{número / letra / símbolo}`
- Comentario: `\text{contenido}`

## Operaciones aritméticas

- Producto punto: `\cdot`
- Producto cruzado: `\times`

## Subíndices / Superíndices

- Superíndice: `^`
- Subíndice: `_`
- Si hay anidamiento, use `{}` para contener.

Ejemplo: $$X^{2m}_{3n}$$

## Subrayado / Sobrescrito

- Sobrescrito: `\overline`
- Subrayado: `\underline`

Ejemplo: $$\overline{x^2+a+b}$$

## Fracciones

Representación de fracciones: `\frac{numerador}{denominador}`

## Sistemas de ecuaciones

Método 1: `\begin{array}{c} expresión 1\\expresión 2... \end{array}`
Método 2: `\begin{cases}…\end{cases}`

## Raíz cuadrada

Formato: `\sqrt[n`]{x}`, donde `n` representa la raíz cuadrada y `x` representa el término que se está sacando raíz.

## Letras griegas

| Letra griega (mayúscula) | Expresión | Letra griega (minúscula) | Expresión |
| :---------------------: | :------: | :---------------------: | :-------: |
|            A            |    A     |            α            |  \alpha   |
|            B            |    B     |            β            |   \beta   |
|            Γ            |  \Gamma  |            γ            |  \gamma   |
|            Δ            |  \Delta  |            δ            |  \delta   |
|            E            |    E     |            ϵ            | \epsilon |
|            Z            |    Z     |            ε            | \varepsilon |
|            H            |    H     |            η            |   \eta    |
|            Θ            |  \Theta  |            θ            |  \theta   |
|            I            |    I     |            ι            |   \iota   |
|            K            |    K     |            κ            |  \kappa   |
|            Λ            | \Lambda  |            λ            |  \lambda  |
|            M            |    M     |            μ            |    \mu    |
|            N            |    N     |            ν            |    \nu    |
|            Ξ            |   \Xi    |            ξ            |    \xi    |
|            O            |    O     |            ο            | \omicron |
|            Π            |   \Pi    |            π            |   \pi    |
|            P            |    P     |            ρ            |   \rho   |
|            Σ            |  \Sigma  |            σ            |  \sigma  |
|            T            |    T     |            τ            |   \tau   |
|            Υ            | \Upsilon |            υ            | \upsilon |
|            Φ            |   \Phi   |            ϕ            |   \phi   |
|            −            |    -     |            φ            | \varphi |
|            X            |    X     |            χ            |   \chi   |
|            Ψ            |   \Psi   |            ψ            |   \psi   |
|            Ω            |  \Omega  |            ω            |  \omega  |

## Operadores

# Símbolos matemáticos en Markdown

Aquí hay una lista de símbolos matemáticos comunes que se pueden usar en Markdown. 

## Operadores

| Operador | Expresión | Operador | Expresión |
| :-----: | :------: | :-----: | :------: |
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

## Símbolos de cálculo

| Operador | Expresión | Operador | Expresión |
| :-----: | :------: | :-----: | :------: |
|   ∮    | \oint  |   ∞    | \infty |
|   ∇    | \nabla |   ∫    |  \int  |
|   ∑    |  \sum  |  lim   |  \lim  |
|   →    | \vec{} |   -    |   -    |

## Símbolos lógicos

| Operador |  Expresión  | Operador |   Expresión   |
| :-----: | :------: | :-----: | :--------: |
|   ∵    | \because |   ∴    | \therefore |
|   ∀    | \forall  |   ∃    |  \exists   |

## Referencias y agradecimientos

- [Markdown 数学公式](https://markdown.budshome.com/formula.html)
- [LaTeX-Symbols.pdf](https://def.fe.up.pt/latex/Symbols.pdf)

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.