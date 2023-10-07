# Solución de problemas de ADC y DAC

> Esta publicación solo está disponible en inglés.

## ¿Por qué la fuente de CA debe tener una resolución de 2-4 bits más que el ADC en prueba?

Como una definición a menudo utilizada de ENOB:

$$
ENOB=\frac{SINAD-1.76}{6.02}
$$

Entonces, si el ENOB del DAC (en la fuente de CA) disminuye, el SINAD también disminuirá, lo que significa que el ruido y las distorsiones aumentarán relativamente, lo que afectará la precisión de la medición.

Otro punto es que la resolución de la fuente de CA menor que 2-4 bits inducirá distorsiones armónicas más altas, la señal digital en la salida del ADC se deteriorará tanto por las distorsiones armónicas del DAC como del ADC, y la amplitud del segundo armónico (por ejemplo) podría ser sumada. Debido a que la fuente de CA con una resolución más alta traerá distorsiones armónicas más bajas, los resultados de salida de prueba serán más precisos.

Consulte este artículo: [ADC Production Test Technique Using Low-Resolution Arbitrary Waveform Generator](https://www.hindawi.com/journals/vlsi/2008/482159/)

## ¿Existen otras formas de mejorar la precisión de la medición con la entrada de CA en la prueba de ADC?

Reducir la pendiente de la onda de rampa de entrada puede mejorar la precisión de la medición.

## ¿Qué hacer con el ruido de base alto en la prueba de ADC?

1. Aumente el número de muestras (N) y el número de períodos de señal de prueba muestreados (M), ambos también resultarán en más tiempo de prueba.
2. Aumente la frecuencia de muestreo (Fs).

No es posible distinguir entre ruido y armónicos si solo se muestrea 1 período de señal.

> ¿Existe esta fórmula? Precisión de ruido = frecuencia de muestreo / M

## ¿Cómo medir el error de ganancia del ADC en la práctica?

El método del histograma se utiliza en la práctica para medir el error de ganancia, porque el borde de transición teórico es difícil de detectar.

## ¿Necesitamos un digitalizador de CA con 2-4 bits más de resolución en la prueba del DAC?

No, no es necesario tener un digitalizador de CA de muy alta resolución. Un digitalizador de CA que cumpla con la resolución de Nyquist cumplirá con el estándar de prueba.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.