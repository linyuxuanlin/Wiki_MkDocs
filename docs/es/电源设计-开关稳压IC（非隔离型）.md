# Diseño de Fuentes de Alimentación - Circuitos Integrados Reguladores de Conmutación (sin aislamiento)

## Factores a considerar en el diseño

El diseño de fuentes de alimentación conmutadas debe tener en cuenta al menos los siguientes criterios:

- **Voltaje de Entrada/Salida**: Debe seleccionarse dentro del rango de voltaje de operación recomendado por el dispositivo, teniendo en cuenta las fluctuaciones del voltaje real para garantizar que no exceda las especificaciones del dispositivo.
- **Corriente de Salida**: Debe reservarse un margen de corriente de salida y se deben evaluar las corrientes de pico y la disipación de calor del circuito, cumpliendo con los requisitos de reducción de potencia.
- **Rizado**: El rizado es un parámetro importante para medir la fluctuación del voltaje de salida del circuito y debe ser monitoreado tanto en condiciones de carga ligera como pesada, generalmente evaluado con un ancho de banda de 20 MHz utilizando un osciloscopio.
- **Eficiencia**: La eficiencia debe evaluarse tanto en condiciones de carga ligera como pesada. La carga ligera afecta la potencia en espera, mientras que la carga pesada influye en la elevación de temperatura. Por lo general, bajo una entrada de 12 V y una salida de 5 V con una corriente de 10 mA, se requiere una eficiencia del 80% o superior.
- **Respuesta Transitoria**: La respuesta transitoria evalúa la capacidad del sistema para ajustar rápidamente la salida de voltaje en respuesta a cambios bruscos en la carga. Se requiere que la fluctuación del voltaje de salida sea menor al 10% pico a pico.
- **Frecuencia de Conmutación**: Generalmente se encuentra por encima de los 500 kHz y afecta la selección de inductores y condensadores, además de tener implicaciones en cuestiones como EMC y ruido en condiciones de carga ligera.
- **Voltaje de Referencia y Precisión de Retroalimentación**: El voltaje de retroalimentación debe compararse con la referencia interna, y se utiliza junto con resistencias de divisor de voltaje externas para lograr diferentes salidas. El voltaje de referencia puede variar según el producto y se requiere una precisión del 1% en las resistencias de retroalimentación.
- **Estabilidad Lineal y de Carga**: La estabilidad lineal refleja la estabilidad de la salida de voltaje ante cambios en el voltaje de entrada, mientras que la estabilidad de carga se relaciona con cambios en la carga de salida. Se requiere generalmente un 1% de estabilidad, con un máximo del 3%.
- **Nivel EN**: El nivel alto y bajo de EN debe cumplir con las especificaciones del dispositivo, ya que algunos circuitos integrados no pueden operar fuera de un rango de voltaje específico. Además, debido a las necesidades de control de temporización, este pin puede tener una capacitancia adicional y, para la regulación de nivel y la descarga, también se requiere una resistencia a tierra.
- **Rendimiento de Protección**: Deben estar presentes protecciones contra sobrecorriente (OCP) y sobrecalentamiento (OTP), y estas condiciones deben poder restablecerse automáticamente.
- **Otros Requisitos**: El proyecto debe incluir un arranque suave, consideraciones de resistencia térmica, y asegurarse de que el rango de temperatura de operación sea adecuado para temperaturas extremadamente altas o bajas.

Principios de selección: Universalidad, relación costo-efectividad, facilidad de adquisición, larga vida útil, compatibilidad y capacidad de reemplazo, cumplimiento de reducción de potencia, facilidad de producción y normalización.

## Modos de Modulación

### PFM (Modo de Modulación de Frecuencia de Pulso)

En el modo PFM, el ancho de pulso de conmutación permanece constante, pero la frecuencia de salida se ajusta para lograr una tensión de salida estable. Este modo es adecuado para aplicaciones de larga duración, especialmente con cargas ligeras, y tiene la ventaja de un bajo consumo de energía.

### PWM (Modo de Modulación de Ancho de Pulso)

En el modo PWM, la frecuencia de los pulsos de conmutación no cambia, pero se ajusta el ancho de los pulsos para mantener una tensión de salida estable. Este modo es altamente eficiente y genera poco rizado y ruido.

## Consideraciones sobre la Conexión a Tierra de la Bobina de Potencia

Desde el punto de vista de EMI, se recomienda la conexión a tierra. En cuanto a la inductancia, en el caso de inductores blindados, la conexión a tierra prácticamente no tiene impacto. Sin embargo, para inductores de tipo núcleo de aire, la conexión a tierra puede tener un pequeño impacto, y debe decidirse según la situación.

## Cómo Determinar la Saturación de la Bobina de Potencia

Además de la imagen proporcionada, la saturación de la bobina de potencia también se puede determinar observando la elevación anormal de temperatura y zumbidos, entre otros síntomas.

## Requisitos para la Selección de Componentes Periféricos

- **Condensadores de Entrada/Salida**: Deben cumplir con los requisitos de resistencia de voltaje (al menos 1.5-2 veces el voltaje de entrada) y rizado de entrada.
- **Condensador BST (Bootstrap)**: Utilizado para elevar el voltaje en la apertura del interruptor interno del chip. Se debe seleccionar según las recomendaciones del manual de datos (generalmente 0.1-1uF) y la resistencia de voltaje debe ser mayor que el voltaje de entrada.
- **Bobina de Potencia**: Los requisitos de inductancia varían según la tensión de salida. Se debe prestar atención a la elevación de temperatura y la corriente de saturación, generalmente se requiere un 1.3 veces la corriente máxima (o la corriente de saturación de la bobina debe ser mayor que la corriente máxima de salida + 0.5 veces la corriente de rizado de la bobina).
- **Condensador de Retroalimentación**: Seleccionado según las recomendaciones del manual de datos, con valores diferentes para chips de diferentes fabricantes y tensiones de salida.
- **Resistencia de Retroalimentación y Resistencia de Divisor de Voltaje EN**: Deben seleccionarse de acuerdo con las especificaciones y requerimientos del manual, y se requiere una precisión del 1%.

##

```markdown
- Inductores: Es preferible optar por inductores moldeados integralmente, ya que tienen una menor emisión electromagnética (EMI).
- Red de retroalimentación: Las líneas de retroalimentación deben mantenerse lo más alejadas posible de los inductores y las fuentes de ruido de alimentación. Cuando se cumple el primer requisito, se pueden utilizar líneas cortas y gruesas en la medida de lo posible. Lo ideal es que las líneas de retroalimentación estén en el lado opuesto de la PCB con respecto a los inductores y separadas por un plano de tierra en el medio. Por lo general, las resistencias de división de voltaje se conectan a tierra de señal (AGND) y la línea de retroalimentación se conecta a tierra.
- Condensadores de desacople: Los condensadores cerámicos de desacople de entrada deben ubicarse lo más cerca posible de las terminales $V_{IN}$ y GND del chip para reducir la inductancia parásita; el polo negativo del condensador puede tener agujeros adicionales para reducir la impedancia. Normalmente, es necesario utilizar condensadores electrolíticos de gran capacidad antes de la entrada de la fuente de alimentación, seguidos de condensadores más pequeños.
- El circuito de potencia debe ser corto y grueso siempre que sea posible, manteniendo un área de bucle pequeña para reducir la radiación de ruido. Los inductores deben estar cerca del pin SW y alejados de las líneas de retroalimentación. Los condensadores de salida deben estar cerca de los inductores, y el terminal de tierra debe contar con agujeros adicionales para conexión a tierra.
- Las líneas de los condensadores de BST deben ser cortas y no demasiado delgadas.
- La disipación de calor del chip debe seguir las especificaciones de diseño, y se deben agregar agujeros de disipación de calor en la parte inferior tanto como sea posible.

## Referencias y Agradecimientos

- [Explicación detallada de las tres topologías básicas de fuentes de alimentación conmutadas](http://www.elecfans.com/article/83/116/2016/20160307404422_a.html)
- [Dominar estas habilidades facilitará la operación de circuitos DC-DC](https://mp.weixin.qq.com/s/fqTPyfAKdTlbRxy0-ho9gA)
- [MPS, ¿es ilegal colocar un plano de tierra en la parte inferior de un inductor?](https://mp.weixin.qq.com/s/CgR2jUgujLy3nqwU52rW2Q)
- [Mini lecciones de fuentes de alimentación MPS, episodio tres: Consejos para detectar la saturación de un inductor](https://mp.weixin.qq.com/s?__biz=MzIwMTE4MzQwMw==&mid=2884003106&idx=1&sn=41c7eef3377037a1a1d21179447d0df1&scene=19#wechat_redirect)
- [Cómo elegir un inductor para una fuente de alimentación buck](https://mp.weixin.qq.com/s/tTSoUaeaVQI4TM6ruKpeKw)
- [AN-1149 Pautas de diseño para fuentes de alimentación conmutadas](https://www.ti.com/lit/an/snva021c/snva021c.pdf?ts=1641814411004)
- [Análisis de rizado en fuentes de alimentación conmutadas 🚧](http://www.oliverkung.top/%e5%bc%80%e5%85%b3%e7%94%b5%e6%ba%90%e7%ba%b9%e6%b3%a2%e5%88%86%e6%9e%90/)

> Dirección original del artículo: <https://wiki-power.com/>
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.
```

Por favor, avísame si necesitas alguna aclaración o modificación adicional.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.