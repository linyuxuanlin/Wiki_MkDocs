# Solución de problemas de ADC y DAC

## ¿Por qué la fuente de CA debe tener de 2 a 4 bits más de resolución que el ADC bajo prueba?

Como una definición comúnmente utilizada de ENOB:

$$
ENOB=\frac{SINAD-1.76}{6.02}
$$

Por lo tanto, si el ENOB del DAC (en la Fuente de CA) disminuye, el SINAD también disminuirá, lo que significa que el ruido y las distorsiones aumentarán relativamente, lo que afectará la precisión de la medición.

Otro punto importante es que una resolución de la Fuente de CA inferior a 2-4 bits inducirá distorsiones armónicas más altas. La señal digital en la salida del ADC se verá deteriorada por las distorsiones armónicas tanto del DAC como del ADC, y la amplitud del segundo armónico (por ejemplo) podría sumarse. Debido a que una Fuente de CA con una resolución más alta reducirá las distorsiones armónicas, los resultados de la salida de la prueba serán más precisos.

Consulte este artículo: [Técnica de Prueba de Producción de ADC Utilizando un Generador de Formas de Onda Arbitraria de Baja Resolución](https://www.hindawi.com/journals/vlsi/2008/482159/)

## ¿Existen otras formas de mejorar la precisión de la medición con la entrada de CA en la prueba de ADC?

Reducir la pendiente de la onda de rampa de entrada puede mejorar la precisión de la medición.

## ¿Qué hacer con el ruido base alto en la prueba de ADC?

1. Aumentar el número de muestras (N) y el número de períodos de señal de prueba muestreados (M), lo que también resultará en más tiempo de prueba.
2. Aumentar la frecuencia de muestreo (Fs).

No es posible distinguir entre el ruido y las armónicas si solo se muestrea un período de señal.

> ¿Existe esta fórmula? Precisión de ruido = frecuencia de muestreo / M

## ¿Cómo medir el error de ganancia de ADC en la práctica?

En la práctica, se utiliza el método del histograma para medir el error de ganancia, ya que es difícil detectar el borde de transición teórico.

## ¿Necesitamos un Digitalizador de CA con 2-4 bits más de resolución en la prueba del DAC?

No, no es necesario contar con un Digitalizador de CA de alta resolución. Un Digitalizador de CA que cumpla con la resolución de Nyquist será suficiente para cumplir con el estándar de prueba.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.