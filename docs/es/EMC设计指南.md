# Guía de Diseño de EMC

La Compatibilidad Electromagnética (EMC) se refiere a la capacidad de un dispositivo para funcionar correctamente en su entorno electromagnético sin causar interferencias electromagnéticas inaceptables en dicho entorno. En términos sencillos, significa que su placa no debe temer a las interferencias de otros dispositivos y, al mismo tiempo, debe evitar interferir con otros, alcanzando un estado de "compatibilidad".

**La EMC** incluye la **Interferencia Electromagnética (EMI)** y la **Susceptibilidad Electromagnética (EMS)**.

La EMI consta de los siguientes elementos:

- **Emisión Radiada (RE)**: se refiere a cómo una fuente de interferencia acopla (interfiere) su señal en otra red eléctrica a través del espacio.
- **Emisión Conducida (CE)**: implica cómo una señal se acopla (interfiere) en otra red eléctrica a través de un medio conductor.
- **Armónicos (Harmonics)**: pruebas de interferencia de corriente armónica.
- **Parpadeo (Flicker)**: pruebas de variabilidad de voltaje y parpadeo.

La EMS comprende los siguientes elementos:

- **Resistencia a la Radiación (RS)**: pruebas de resistencia a la radiación de campo electromagnético de radiofrecuencia.
- **Resistencia a la Conducción (CS)**: pruebas de resistencia a la interferencia de conducción inducida por campos de radiofrecuencia (inyección de corriente de alta intensidad).
- **Descarga Electroestática (ESD)**: pruebas de resistencia electrostática (experimentos de descarga electrostática).
- **Interferencia de Pulso Transitorio (EFT)**: pruebas de resistencia a grupos de pulsos transitorios de rápida transición eléctrica.
- **Caídas de Voltaje (DIP)**: pruebas de resistencia a interrupciones temporales y variaciones de voltaje.
- **Sobretensión y Rayos (SURGE)**: pruebas de resistencia a sobretensiones (impactos de rayos).
- **Resistencia al Campo Magnético de Frecuencia Industrial (PFMF)**: pruebas de resistencia al campo magnético de frecuencia industrial.

## Métodos Básicos de Optimización de EMC

Los factores que generan problemas de EMC son las fuentes de interferencia electromagnética, las vías de acoplamiento y los dispositivos sensibles.

Reglas generales:

1. Cuanto mayor sea el área del circuito de corriente de alta frecuencia (S), más grave será la radiación EMI.
2. Cuanto mayor sea la frecuencia de corriente del circuito (f), más grave será la radiación EMI; la intensidad del campo electromagnético aumenta proporcionalmente con el cuadrado de la frecuencia de corriente (f).

Métodos básicos de mitigación:

- Supresión en las rutas de transmisión: Esto implica el uso de técnicas como filtrado, apantallamiento, puesta a tierra, acoplamiento y cableado adecuado.
- Separación espacial: Aumentar la distancia entre la fuente de interferencia y los circuitos sensibles es una estrategia efectiva para suprimir la interferencia por radiación y acoplamiento inductivo.
- Separación temporal: Cerrar la señal útil durante la emisión de señales de interferencia y permitir la transmisión en momentos libres de interferencia.
- Procesamiento espectral: Cambios en el espectro y técnicas de expansión de frecuencia.
- Aislamiento eléctrico: Uso de aislamiento óptico, relés, transformadores y convertidores DC/DC.

### Minimizar el Área de los Circuitos de Alta Frecuencia y los lazos de potencia

Principios fundamentales:

1. Las señales siempre vuelven a la fuente.
2. El flujo de señal de retorno sigue el camino de menor inductancia.

En señales de alta frecuencia, la trayectoria de retorno de la señal suele ser la de menor inductancia, que generalmente también es la de menor área de bucle. En frecuencias más bajas (generalmente KHz y menos), la señal de retorno tiende a seguir el camino de menor resistencia.

### Mantener Integrales las Pantallas de Retorno de Señal

![imagen](https://img.wiki-power.com/d/wiki-media/img/20211215190631.png)

Como se muestra en la imagen, cortar la pantalla de retorno de la señal resulta en que la corriente de señal no siga el camino óptimo (más corto) de regreso a la fuente, lo que puede dar lugar a resultados impredecibles y aumentar el área del bucle de señal. En situaciones especiales, es necesario aislar las tierras digitales y analógicas para prevenir interferencias cruzadas.

### Alejar las Señales de Alta Velocidad de los Conectores

Los cables conectados a la PCB a través de conectores actúan como eficientes antenas, y las señales de alta velocidad tienden a generar diferencias de potencial que pueden conducir corriente a través de los cables conectados, lo que resulta en emisiones electromagnéticas fuera de norma.

### Suprimir los Flancos de Subida y Bajada de las Señales de Alta Velocidad

Ralentizar los flancos de subida y bajada de las señales digitales es una forma efectiva de controlar las frecuencias armónicas superiores. Los tiempos de transición excesivamente largos pueden dar lugar a problemas de integridad de la señal y sobrecalentamiento.

## Componentes de EMC

Los componentes comunes de EMC incluyen inductores de modo común, perlas magnéticas y condensadores de filtro.

Modelos comunes de filtros:

![imagen](https://img.wiki-power.com/d/wiki-media/img/20211219173751.png)

### Inductores de Modo Común

Modelo equivalente de inductores de modo común:

![imagen](https://img.wiki-power.com/d/wiki-media/img/20211219173856.png)

![imagen](https://img.wiki-power.com/d/wiki-media/img/20211219174546.png)

### Perlas Magnéticas

A continuación, se presenta la traducción del texto al español:

**Introducción y Selección de Perlas de Ferrita**

Para obtener información sobre la introducción y selección de perlas de ferrita, por favor consulte la sección [**Componentes Básicos - Inductores y Perlas de Ferrita · Perlas de Ferrita**](https://ejemplo.com/ruta#perlas-de-ferrita).

**Capacitores de Filtro**

Para información y selección de capacitores, por favor visite la sección [**Componentes Básicos - Capacitores**](https://ejemplo.com/ruta#capacitores).

## Diseño EMC para PCB 🚧

### Principio de 3W y 20H

El principio de 3W implica que si la distancia entre el centro de las líneas es al menos 3 veces el ancho de la línea, se puede mantener un 70% de separación entre campos eléctricos sin interferencia mutua. Para lograr un 98% de separación de campos, se utiliza la regla de 10W.

El principio de 20H se refiere a asegurar que el borde del plano de energía esté al menos 20 veces la distancia entre capas del plano de tierra para suprimir los efectos de radiación en el borde. Esto permite que el 70% del campo eléctrico se limite al borde de tierra; si se reduce en 100H, el 98% del campo eléctrico se limita internamente.

## Referencias y Agradecimientos

- [Introducción a la Compatibilidad Electromagnética](https://ejemplo.com/enlace1)
- [Compatibilidad Electromagnética (EMC): Guía de Diseño EMC Directo](https://ejemplo.com/enlace2)
- [Secretos de Diseño EMI/EMC: Manual Esencial para Ingenieros de Diseño de Productos Electrónicos](https://ejemplo.com/enlace3)
- [Supresión de Interferencia Electromagnética Conducida Utilizando Inductores de Modo Común Híbridos](https://ejemplo.com/enlace4)
- [[Circuitos] Conceptos Básicos de EMC - Interferencia en Modo Común y en Modo Diferencial](https://ejemplo.com/enlace5)

> Dirección original del artículo: <https://wiki-power.com/>
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.