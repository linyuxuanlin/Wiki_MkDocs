# Guía de Diseño EMC

La Compatibilidad Electromagnética (EMC, por sus siglas en inglés, Electromagnetic Compatibility) se refiere a la capacidad de un dispositivo para funcionar normalmente en su entorno electromagnético sin causar interferencias electromagnéticas inaceptables en otros elementos de ese entorno. En términos simples, significa que tu placa no debe temer las interferencias de otros y, al mismo tiempo, debe evitar interferir con los demás, logrando así un estado de "compatibilidad".

La EMC abarca la **Interferencia Electromagnética (EMI)** y la **Susceptibilidad Electromagnética (EMS)**.

Los elementos clave de EMI incluyen:

- **Emisión Radiada (RE)**: Se refiere a cómo una fuente de interferencia acopla su señal a otro circuito eléctrico a través del espacio.
- **Emisión Conducida (CE)**: Se trata de cómo una señal en un circuito eléctrico se acopla a otro circuito a través de un medio conductor.
- **Armónicos (Harmonic)**: Pruebas de interferencia de corriente armónica.
- **Parpadeo (Flicker)**: Pruebas de cambios en el voltaje y el parpadeo.

Los elementos clave de EMS incluyen:

- **Resistencia a la Interferencia Radiada (RS)**: Pruebas de resistencia a campos electromagnéticos de radiofrecuencia.
- **Resistencia a la Interferencia Conducida (CS)**: Pruebas de resistencia a la interferencia conducción inducida por campos de radiofrecuencia (inserción de corriente).
- **Descarga Electroestática (ESD)**: Pruebas de resistencia a la estática (experimentos de descarga electrostática).
- **Perturbaciones de Impulso Transitorio (EFT)**: Pruebas de resistencia a grupos de pulsos de transición eléctrica rápida.
- **Descenso de Voltaje (DIP)**: Pruebas de resistencia a interrupciones breves y cambios en el voltaje.
- **Sobretensión (SURGE)**: Pruebas de resistencia a sobretensiones (rayos).
- **Resistencia al Campo Magnético de Frecuencia de Potencia (PFMF)**: Pruebas de resistencia al campo magnético de frecuencia de potencia.

## Métodos Básicos de Optimización EMC

Los factores que contribuyen a los problemas de EMC son las fuentes de interferencia electromagnética, las vías de acople y los dispositivos sensibles.

Principios clave:

1. Cuanto mayor sea el área del circuito de corriente de alta frecuencia (S), mayor será la radiación de EMI.
2. Cuanto mayor sea la frecuencia de corriente del circuito (f), mayor será la radiación de EMI, y la intensidad del campo electromagnético radiado aumentará proporcionalmente al cuadrado de la frecuencia de corriente f.

Métodos fundamentales para abordar estos problemas incluyen:

- Supresión en la vía de transmisión: Esto implica técnicas como filtrado, blindaje, puesta a tierra, disposición y enrutamiento adecuados.
- Separación espacial: Aumentar la distancia entre la fuente de interferencia y el circuito sensible es una forma efectiva de reducir las interferencias espaciales y las interferencias de acoplamiento inductivo.
- Separación temporal: Desactivar la señal útil durante la emisión de una señal de interferencia y transmitirla cuando la señal de interferencia está inactiva.
- Procesamiento del espectro: Cambios en el espectro y técnicas de expansión del espectro.
- Aislamiento eléctrico: Aislamiento óptico, relés de aislamiento, transformadores de aislamiento, conversión DC/DC.

### Minimizar el área de los circuitos de alta frecuencia y los circuitos de alimentación

Principios fundamentales:

1. Las señales siempre regresan a la fuente.
2. El flujo de señal regresa por el camino de menor impedancia.

En señales de alta frecuencia, el flujo de señal regresa generalmente por la ruta de menor inductancia, que suele ser también la de menor área del bucle. Para frecuencias bajas (generalmente en KHz y por debajo), el flujo de señal a menudo sigue la ruta de menor resistencia.

### Mantener la integridad de la pantalla de retorno de la señal

![Imagen](https://media.wiki-power.com/img/20211215190631.png)

Como se muestra en la imagen, si cortas la pantalla de retorno de la señal, la corriente de la señal no podrá regresar al origen a través de la ruta óptima (más corta). En lugar de eso, buscará rutas alternativas, lo que aumentará el área del bucle de la señal. En casos especiales, la tierra digital y la tierra analógica deben estar aisladas para evitar interferencias.

### Mantener las señales de alta velocidad lejos de los conectores

Los cables que se conectan a la PCB a través de conectores actúan como antenas eficientes, y las señales de alta velocidad son propensas a generar diferencias de potencial que impulsarán corriente a través de los cables conectados, lo que puede provocar radiación excesiva.

### Suprimir los tiempos de subida y bajada de señales de alta velocidad

Reduciendo la velocidad de subida y bajada de las señales digitales, puedes controlar eficazmente las frecuencias armónicas de alto orden. Un tiempo de transición excesivamente largo puede dar lugar a problemas de integridad de la señal y sobrecalentamiento.

## Componentes EMC

Los componentes comunes utilizados en EMC incluyen inductores comunes de modo, perlas de ferrita y condensadores de filtrado.

Modelos de filtros comunes:

![Imagen](https://media.wiki-power.com/img/20211219173751.png)

### Inductores Comunes de Modo

Modelos equivalentes de inductores comunes de modo:

![Imagen](https://media.wiki-power.com/img/20211219173856.png)

![Imagen](https://media.wiki-power.com/img/20211219174546.png)

### Perlas de Ferrita

Aquí tienes la traducción del texto al español:

### Introducción y Selección de Perlas Magnéticas

Para obtener información sobre la introducción y selección de perlas magnéticas, por favor visita la sección [**Componentes Básicos - Inductores y Perlas Magnéticas · Perlas Magnéticas**](https://wiki-power.com/%E5%9F%BA%E6%9C%AC%E5%85%83%E5%99%A8%E4%BB%B6-%E7%94%B5%E6%84%9F%E4%B8%8E%E7%A3%81%E7%8F%A0#%E7%A3%81%E7%8F%A0).

### Capacitores de Filtro

Para obtener información sobre la introducción y selección de capacitores, por favor visita la sección [**Componentes Básicos - Capacitores**](https://wiki-power.com/%E5%9F%BA%E6%9C%AC%E5%85%83%E5%99%A8%E4%BB%B6-%E7%94%B5%E5%AE%B9).

## Diseño de EMC en PCB 🚧

### Principio de 3W y 20H

El principio de 3W establece que cuando la distancia entre el centro de las líneas no sea menor a 3 veces el ancho de las líneas, se puede mantener un 70% de separación entre campos eléctricos sin interferencias mutuas. Para lograr un 98% de separación, se utiliza la regla de 10W.

El principio de 20H implica que el borde del plano de alimentación debe estar al menos 20 veces más alejado del borde del plano de tierra que la distancia entre capas, con el propósito de suprimir los efectos de radiación en los bordes. Esto permite limitar un 70% de los campos eléctricos cerca del borde a tierra; si se aleja en 100H, se puede limitar un 98% de los campos eléctricos en el interior.

## Referencias y Agradecimientos

- [Introducción a la Compatibilidad Electromagnética](https://blog.infonet.io/2021/04/04/%E7%94%B5%E7%A3%81%E5%85%BC%E5%AE%B9%E4%BB%8B%E7%BB%8D/)
- [Compatibilidad Electromagnética (EMC): Una Guía de Diseño Directa](https://zhuanlan.zhihu.com/p/142866381)
- [Guía Esencial de Diseño de EMC/EMI para Ingenieros de Productos Electrónicos](https://www.mr-wu.cn/emc-emi-she-ji-mi-ji/)
- [Supresión de Interferencia Electromagnética Con Inductores de Modo Común Híbridos](https://www.richtek.com/Design%20Support/Technical%20Document/AN008?sc_lang=zh-CN)
- [[Circuitos] Conceptos Básicos de EMC - Interferencia en Modo Común y Diferencial](https://zhenhuizhang.tk/post/dian-lu-emc-ji-chu-gai-nian-_-gong-mo-chai-mo-gan-rao/)

[por_reemplazar[1]]
[por_reemplazar[2]]

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
