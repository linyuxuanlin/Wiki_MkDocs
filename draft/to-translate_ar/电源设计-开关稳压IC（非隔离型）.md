# Diseño de fuentes de alimentación - IC regulador de conmutación (no aislado)

## Factores a considerar en el diseño

El diseño de fuentes de alimentación conmutadas debe considerar al menos las siguientes condiciones:

- **Voltaje de entrada / salida**: seleccione dentro del rango de voltaje de trabajo recomendado por el dispositivo, considere el rango de fluctuación del voltaje real y asegúrese de no exceder las especificaciones del dispositivo.
- **Corriente de salida**: la corriente de salida debe tener un margen de reserva, también es necesario evaluar la corriente pico instantánea del circuito y la situación de calentamiento, y cumplir con los requisitos de reducción de carga.
- **Ondulación**: la ondulación es un parámetro importante para medir la fluctuación del voltaje de salida del circuito, preste atención a la ondulación en carga ligera y pesada. Por lo general, se utiliza un osciloscopio con una banda de 20 MHz para la prueba.
- **Eficiencia**: debe prestar atención tanto a la carga ligera como a la pesada. La carga ligera afectará la potencia en espera y la carga pesada afectará la temperatura. Por lo general, se observa la eficiencia de 10 mA a 5 V de salida con una entrada de 12 V, y generalmente se requiere un 80% o más.
- **Respuesta transitoria**: la característica de respuesta transitoria refleja si el sistema puede ajustarse rápidamente para garantizar la estabilidad del voltaje de salida cuando la carga cambia drásticamente. Se requiere una fluctuación de voltaje de salida más pequeña, generalmente se requiere menos del 10% del valor pico a pico.
- **Frecuencia de conmutación**: generalmente por encima de 500 kHz, está relacionado con la selección de inductancia y capacitancia, y otros problemas como EMC y ruido en carga ligera también están relacionados con esto.
- **Voltaje de referencia y precisión de retroalimentación**: el voltaje de retroalimentación se compara con el voltaje de referencia interno, y se utiliza en conjunto con la resistencia de retroalimentación externa para producir diferentes voltajes de salida. Los diferentes productos tendrán diferentes voltajes de referencia, como 0.6-0.8 V, y se debe seleccionar una resistencia de retroalimentación con una precisión del 1%.
- **Estabilidad lineal y de carga**: la estabilidad lineal refleja la estabilidad del voltaje de salida cuando el voltaje de entrada cambia; la estabilidad de carga refleja la estabilidad del voltaje de salida cuando la carga cambia. Por lo general, se requiere un 1%, y no se debe exceder el 3% como máximo.
- **Nivel EN**: el nivel alto y bajo de EN debe cumplir con las especificaciones del dispositivo, algunos IC no pueden exceder un rango de voltaje específico. Debido a la necesidad de control de tiempo, este pin agregará capacitancia, por lo que se requiere una resistencia a tierra para la regulación de nivel y la descarga de apagado.
- **Rendimiento de protección**: debe tener protección contra sobrecorriente OCP, protección contra sobrecalentamiento OTP, etc., y las condiciones deben desaparecer después de la protección y recuperarse automáticamente.
- **Otros**: se requiere inicio suave para el proyecto; resistencia térmica y encapsulamiento; el rango de temperatura de uso debe cubrir tanto alta como baja temperatura, etc.

Principios de selección: universalidad, alta relación calidad-precio, fácil adquisición, larga vida útil, compatibilidad y sustituibilidad, reducción de carga, fácil producción y normalización.

## Modulación

### PFM (Modulación de frecuencia de pulso)

El ancho de pulso del interruptor no cambia, y la frecuencia de salida del pulso se cambia para estabilizar el voltaje de salida. Adecuado para uso a largo plazo (especialmente con carga ligera), tiene la ventaja de un bajo consumo de energía.

### PWM (Modulación de ancho de pulso)

La frecuencia de pulso del interruptor no cambia, y el ancho de pulso se cambia para estabilizar el voltaje de salida. Tiene una alta eficiencia y una ondulación y ruido relativamente bajos.

## ¿Se puede colocar cobre en la parte inferior del inductor de potencia?

Desde la perspectiva de EMI, se recomienda colocar cobre; desde la perspectiva de la inductancia, para inductores blindados, la inductancia básicamente no se ve afectada, por lo que también se recomienda colocar cobre; para inductores de tipo E, colocar cobre tiene un ligero efecto en la inductancia, por lo que puede decidirse según la situación.

## Cómo juzgar si el inductor de potencia está saturado

![](https://f004.backblazeb2.com/file/wiki-media/img/20210723133831.png)

Además, también se puede juzgar a partir de la temperatura anormal, el zumbido, etc.

## Requisitos de selección de componentes periféricos

- **Capacitancia de entrada / salida**: debe cumplir con los requisitos de voltaje (1.5-2 veces el voltaje de entrada) y ondulación de entrada.
- **Capacitancia BST**: capacitancia de arranque de autoalimentación, se utiliza para elevar el voltaje para encender el tubo superior dentro del chip. Por lo general, se selecciona el valor recomendado en el manual de datos (generalmente 0.1-1uF), y la resistencia a la tensión generalmente debe ser mayor que la tensión de entrada.
- **Inductancia**: se requiere una inductancia diferente para diferentes voltajes de salida; preste atención a la temperatura y asegúrese de que la corriente de saturación cumpla con los requisitos de margen, generalmente más del 1.3 veces la corriente máxima (o la corriente de saturación de la inductancia debe ser mayor que la corriente máxima de salida + 0.5 * corriente de ondulación de la inductancia).
- **Capacitancia de retroalimentación**: seleccione el valor según lo requerido en el manual de datos, diferentes fabricantes de chips tendrán diferentes requisitos de valor, y diferentes voltajes de salida también tendrán diferentes requisitos.
- **Resistencia de retroalimentación y resistencia de división EN**: se requiere que se seleccione el valor según las especificaciones, y se debe seleccionar una precisión del 1%.

## Análisis de ondulación de la fuente de alimentación conmutada

🚧

## Requisitos de diseño de PCB



- Inductores: Se debe priorizar la selección de inductores moldeados en una sola pieza, ya que tienen una EMI más baja.
- Red de retroalimentación: Las líneas de retroalimentación deben estar lo más alejadas posible de las líneas de ruido del inductor y la fuente de alimentación. Si se cumple la primera condición, se pueden hacer las líneas lo más cortas y gruesas posible. Lo mejor es que las líneas estén en el otro lado de la PCB opuesto al inductor y separadas por una tierra intermedia. La resistencia de división de voltaje inferior generalmente se conecta a la tierra de la señal AGND y la línea de retroalimentación se puede conectar a tierra.
- Capacitores de desacoplamiento: Los capacitores cerámicos de desacoplamiento de entrada deben estar lo más cerca posible de las entradas $V_{IN}$ y GND del chip para reducir la inductancia parásita. El polo negativo del capacitor se puede aumentar con un orificio pasante para reducir la impedancia. Por lo general, también se necesita un gran capacitor electrolítico de alimentación hacia adelante, y la entrada de alimentación debe pasar primero por un gran capacitor y luego por un capacitor más pequeño.
- El circuito de potencia debe ser lo más corto y grueso posible, manteniendo un área de bucle pequeña y reduciendo la radiación de ruido. El inductor debe estar cerca del pin SW y lejos de la línea de retroalimentación. El capacitor de salida debe estar cerca del inductor y se debe agregar un orificio de tierra en el terminal de tierra.
- Las líneas de los capacitores BST deben ser lo más cortas posible y no demasiado delgadas.
- La disipación de calor del chip debe cumplir con los requisitos de diseño y se deben agregar orificios de disipación de calor debajo del chip tanto como sea posible.

## Referencias y agradecimientos

- [Explicación detallada de las tres topologías básicas de fuentes de alimentación conmutadas - Texto completo](http://www.elecfans.com/article/83/116/2016/20160307404422_a.html)
- [Dominar estas habilidades te permitirá operar fácilmente circuitos DC-DC](https://mp.weixin.qq.com/s/fqTPyfAKdTlbRxy0-ho9gA)
- [¿Es ilegal colocar una tierra intermedia debajo del inductor en las fuentes de alimentación MPS?](https://mp.weixin.qq.com/s/CgR2jUgujLy3nqwU52rW2Q)
- [【Video corto】Sala de clases de fuentes de alimentación MPS Episodio 3: Algunos consejos para detectar la saturación del inductor](https://mp.weixin.qq.com/s?__biz=MzIwMTE4MzQwMw==&mid=2884003106&idx=1&sn=41c7eef3377037a1a1d21179447d0df1&scene=19#wechat_redirect)
- [¿Cómo elegir el inductor para una fuente de alimentación reductora BUCK?](https://mp.weixin.qq.com/s/tTSoUaeaVQI4TM6ruKpeKw)
- [AN-1149 Pautas de diseño para fuentes de alimentación conmutadas](https://www.ti.com/lit/an/snva021c/snva021c.pdf?ts=1641814411004)
- [Análisis de ondulación en fuentes de alimentación conmutadas 🚧](http://www.oliverkung.top/%e5%bc%80%e5%85%b3%e7%94%b5%e6%ba%90%e7%ba%b9%e6%b3%a2%e5%88%86%e6%9e%90/)

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.