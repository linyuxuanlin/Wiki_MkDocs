# Guía de diseño EMC

La compatibilidad electromagnética (EMC, por sus siglas en inglés) se refiere a la capacidad de un dispositivo para funcionar correctamente en su entorno electromagnético sin causar interferencias electromagnéticas inaceptables en otros dispositivos del entorno. En términos simples, significa que su placa no debe ser susceptible a interferencias y debe evitar interferir con otros dispositivos para lograr un estado de "compatibilidad".

La EMC incluye la interferencia electromagnética (EMI) y la susceptibilidad electromagnética (EMS).

Los elementos de EMI son:

- Emisión radiada (RE): se refiere a la interferencia de una fuente que acopla su señal a otra red eléctrica a través del espacio.
- Emisión conducida (CE): se refiere a la interferencia de una señal en una red eléctrica que se acopla a otra red eléctrica a través de un medio conductor.
- Armónicos: prueba de interferencia de corriente armónica.
- Parpadeo: prueba de cambio y parpadeo de voltaje.

Los elementos de EMS son:

- Resistencia a la radiación (RS): prueba de resistencia a la radiación de campo electromagnético de radiofrecuencia.
- Resistencia a la conducción (CS): prueba de resistencia a la interferencia de conducción inducida por campo de radiofrecuencia (inyección de corriente alta).
- Protección contra descargas electrostáticas (ESD): prueba de resistencia a la descarga electrostática (prueba de descarga electrostática).
- Interferencia de pulso transitorio (EFT): prueba de resistencia a grupos de pulsos de transición rápida.
- Caída de voltaje (DIP): prueba de resistencia a interrupciones y cambios de voltaje a corto plazo.
- Sobretensión, rayo (SURGE): prueba de resistencia a sobretensión (rayo).
- Resistencia al campo magnético de frecuencia de potencia (PFMF): prueba de resistencia al campo magnético de frecuencia de potencia.

## Métodos básicos de optimización de EMC

Los elementos que causan problemas de EMC son: fuentes de interferencia electromagnética, vías de acoplamiento y dispositivos sensibles.

Reglas:

1. Cuanto mayor sea el área del circuito de corriente de alta frecuencia S, mayor será la emisión radiada de EMI.
2. Cuanto mayor sea la frecuencia de la corriente del circuito f, mayor será la emisión radiada de EMI, y la intensidad del campo electromagnético radiado aumentará proporcionalmente al cuadrado de la frecuencia de la corriente f.

Métodos básicos de respuesta:

- Supresión del canal de transmisión: los métodos específicos incluyen filtrado, blindaje, conexión a tierra, superposición y enrutamiento razonable.
- Separación espacial: es un método efectivo para suprimir la interferencia de radiación espacial y la interferencia de acoplamiento de inducción al aumentar la distancia entre la fuente de interferencia y el circuito sensible.
- Separación temporal: la señal útil se cierra temporalmente cuando se emite una señal de interferencia y se transmite durante el tiempo en que la señal de interferencia se detiene.
- Procesamiento de espectro: cambio de espectro, tecnología de expansión de espectro.
- Aislamiento eléctrico: aislamiento fotoeléctrico, aislamiento de relé, aislamiento de transformador, conversión DC/DC.

### Minimizar el área del circuito de alta frecuencia y del circuito de alimentación

Principios básicos:

1. La señal siempre regresa al extremo fuente.
2. El flujo de retorno de la señal siempre sigue el camino de menor impedancia.

En señales de alta frecuencia, el camino de retorno de la señal suele ser el camino de menor inductancia, que suele ser el camino de menor área de circuito. En frecuencias bajas (generalmente por debajo de la frecuencia de kHz), el flujo de retorno de la señal suele seguir el camino de menor resistencia.

### Mantener la integridad de la pantalla de retorno de la señal tanto como sea posible

![](https://f004.backblazeb2.com/file/wiki-media/img/20211215190631.png)

Como se muestra en la figura, si se corta el plano de retorno de la señal, la corriente de la señal no podrá volver al origen a través de la ruta óptima (más corta), lo que aumentará el área del circuito de la señal al buscar una ruta alternativa de retorno de la señal, lo que aumentará el área del circuito de la señal.

En casos especiales, la tierra digital y la tierra analógica deben estar aisladas para evitar interferencias cruzadas.

### Alejar las señales de alta velocidad de los conectores

Los cables conectados a la PCB a través de conectores son antenas eficientes, y las señales de alta velocidad son propensas a generar diferencias de potencial que impulsan la corriente hacia los cables conectados, lo que provoca una radiación excesiva.

### Suprimir el tiempo de subida y bajada de la señal de alta velocidad

Al ralentizar el tiempo de subida y bajada de la señal digital, se puede controlar eficazmente la frecuencia armónica de alta orden. Un tiempo de transición demasiado largo puede provocar problemas de integridad de la señal y sobrecalentamiento.

## Componentes EMC

Los componentes comunes de EMC incluyen inductores comunes, perlas magnéticas y capacitores de filtrado.

Modelos comunes de filtros:

![](https://f004.backblazeb2.com/file/wiki-media/img/20211219173751.png)

### Inductor común

Modelo equivalente del inductor común:

![](https://f004.backblazeb2.com/file/wiki-media/img/20211219173856.png)

![](https://f004.backblazeb2.com/file/wiki-media/img/20211219174546.png)

### Perlas magnéticas

Para obtener información sobre la introducción y selección de perlas magnéticas, consulte la sección [**Componentes básicos - Inductores y perlas magnéticas · Perlas magnéticas**](https://wiki-power.com/es/%E5%9F%BA%E6%9C%AC%E5%85%83%E5%99%A8%E4%BB%B6-%E7%94%B5%E6%84%9F%E4%B8%8E%E7%A3%81%E7%8F%A0#%E7%A3%81%E7%8F%A0).

### Capacitores de filtro

Para obtener información sobre la introducción y selección de capacitores, consulte la sección [**Componentes básicos - Capacitores**](https://wiki-power.com/es/%E5%9F%BA%E6%9C%AC%E5%85%83%E5%99%A8%E4%BB%B6-%E7%94%B5%E5%AE%B9).

## Diseño de EMC en PCB 🚧

### Principios 3W y 20H

El principio 3W establece que si la distancia entre los centros de las líneas es al menos 3 veces el ancho de la línea, se puede mantener un 70% de campo eléctrico entre las líneas sin interferencias mutuas. Para lograr un 98% de campo eléctrico sin interferencias mutuas, se utiliza la regla de 10W.

El principio 20H establece que el borde del plano de alimentación debe estar al menos a una distancia de 20 veces la separación entre los planos de tierra para suprimir los efectos de radiación en el borde. Esto puede limitar el 70% del campo eléctrico dentro del borde de tierra; si se reduce en 100H, se puede limitar el 98% del campo eléctrico dentro.

## Referencias y agradecimientos

- [Introducción a la compatibilidad electromagnética](https://blog.infonet.io/2021/04/04/%E7%94%B5%E7%A3%81%E5%85%BC%E5%AE%B9%E4%BB%8B%E7%BB%8D/)
- [Compatibilidad electromagnética (EMC): Guía de diseño de EMC simple y efectiva](https://zhuanlan.zhihu.com/p/142866381)
- [Secretos de diseño EMI/EMC - Manual esencial para ingenieros de diseño de productos electrónicos](https://www.mr-wu.cn/emc-emi-she-ji-mi-ji/)
- [Supresión de interferencias electromagnéticas conducidas mediante inductores comunes híbridos](https://www.richtek.com/Design%20Support/Technical%20Document/AN008?sc_lang=zh-CN)
- [[Circuito] Conceptos básicos de EMC\_Interferencia común y diferencial](https://zhenhuizhang.tk/post/dian-lu-emc-ji-chu-gai-nian-_-gong-mo-chai-mo-gan-rao/)

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.