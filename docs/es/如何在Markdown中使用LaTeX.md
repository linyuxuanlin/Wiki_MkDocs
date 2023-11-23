# Cómo usar LaTeX en Markdown

Markdown tiene soporte nativo para escribir fórmulas y símbolos matemáticos utilizando LaTeX.

## Estilos de fuente

- Salto de línea: `\\`
- Espacio: `\`
- Centrado: usar `$$` para envolver
- Estilos de fuente: negrita: `\mathbf`, cursiva: `\mathit`
- Tamaño de fuente: `\tiny`, `\scriptsize`, `\small`, `\normalsize`, `\large`, `\Large`, `\huge`, `\Huge`
- Color: `\color{valor_del_color}{número/letra/símbolo}`
- Comentarios: `\text{contenido}`

## Operaciones aritméticas

- Producto punto: `\cdot`
- Producto cruz: `\times`

## Superíndices / Subíndices

- Superíndice: `^`
- Subíndice: `_`
- Si hay anidamiento, usar `{}` para agrupar.

Ejemplo: $$X^{2m}_{3n}$$

## Subrayado / Subrayado inferior

- Subrayado: `\overline`
- Subrayado inferior: `\underline`

Ejemplo: $$\overline{x^2+a+b}$$

## Fracciones

Representación de fracciones: `\frac{numerador}{denominador}`

## Sistemas de ecuaciones

Método 1: `\begin{array}{c} expresión_1\\expresión_2... \end{array}`
Método 2: `\begin{cases}…\end{cases}`

## Raíz cuadrada

Formato: `\sqrt[n]{x}`, donde `n` representa el índice de la raíz y `x` es el radicando.

## Letras griegas

| Greek Letter (Uppercase) | Expression | Greek Letter (Lowercase) | Expression |
| :---------------------: | :--------: | :---------------------: | :--------: |
|           A             |     A      |           α             |   \alpha   |
|           B             |     B      |           β             |    \beta   |
|           Γ             |   \Gamma   |           γ             |   \gamma   |
|           Δ             |   \Delta   |           δ             |   \delta   |
|           E             |     E      |           ϵ             |  \epsilon  |
|           Z             |     Z      |           ε             | \varepsilon |
|           H             |     H      |           η             |    \eta    |
|           Θ             |   \Theta   |           θ             |   \theta   |
|           I             |     I      |           ι             |    \iota   |
|           K             |     K      |           κ             |   \kappa   |
|           Λ             |  \Lambda   |           λ             |  \lambda   |
|           M             |     M      |           μ             |    \mu     |
|           N             |     N      |           ν             |    \nu     |
|           Ξ             |    \Xi     |           ξ             |    \xi     |
|           O             |     O      |           ο             |  \omicron  |
|           Π             |    \Pi     |           π             |    \pi     |
|           P             |     P      |           ρ             |    \rho    |
|           Σ             |  \Sigma    |           σ             |   \sigma   |
|           T             |     T      |           τ             |    \tau    |
|           Υ             | \Upsilon  |           υ             |  \upsilon  |
|           Φ             |   \Phi    |           ϕ             |    \phi    |
|           −             |     -      |           φ             |  \varphi  |
|           X             |     X      |           χ             |    \chi    |
|           Ψ             |   \Psi    |           ψ             |    \psi    |
|           Ω             |  \Omega   |           ω             |   \omega   |

## Operators

| Operador | Expresión  | Operador | Expresión  |
| :------: | :-------: | :------: | :-------: |
|    ±     |    \pm    |    ∅     | \emptyset |
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
|    ≥     |    \geq   |    ≠     |   \neq    |
|    ≈     |  \approx  |    ≡     |  \equiv   |

## Símbolos de cálculo

| Operador | Expresión | Operador | Expresión |
| :------: | :------: | :------: | :------: |
|    ∮     |  \oint   |    ∞     | \infty   |
|    ∇     |  \nabla  |    ∫     |  \int    |
|    ∑     |   \sum   |   lim    |  \lim    |
|    →     |  \vec{}  |    -     |    -     |

## Símbolos lógicos

| Operador |  Expresión  | Operador |   Expresión   |
| :------: | :---------: | :------: | :-----------: |
|    ∵     |  \because   |    ∴     | \therefore    |
|    ∀     |  \forall    |    ∃     |  \exists      |

## Referencias y agradecimientos

- [Markdown Mathematical Formulas](https://markdown.budshome.com/formula.html)
- [LaTeX-Symbols.pdf](https://def.fe.up.pt/latex/Symbols.pdf)

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.