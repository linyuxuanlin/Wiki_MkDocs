# Solución de problemas de ADC y DAC

## ¿Por qué la fuente de CA debe tener de 2 a 4 bits más de resolución que el ADC bajo prueba?

Como una definición frecuentemente utilizada de ENOB:

$$
ENOB = \frac{SINAD - 1.76}{6.02}
$$

Entonces, si el ENOB del DAC (en la Fuente de CA) disminuye, el SINAD también disminuirá, lo que significa que el ruido y las distorsiones aumentarán relativamente, lo que afectará la precisión de la medición.

Otro punto a considerar es que una resolución de la Fuente de CA inferior a 2-4 bits inducirá distorsiones armónicas más altas. La señal digital en la salida del ADC se deteriorará tanto por las distorsiones armónicas del DAC como por las del ADC, y la amplitud del segundo armónico (por ejemplo) podría sumarse. Una Fuente de CA con una mayor resolución reducirá las distorsiones armónicas, lo que hará que los resultados de la salida de la prueba sean más precisos.

Consulta este artículo: [Técnica de Prueba de Producción de ADC Utilizando un Generador de Formas de Onda Arbitrarias de Baja Resolución](https://www.hindawi.com/journals/vlsi/2008/482159/)

## ¿Existen otras formas de mejorar la precisión de la medición con la entrada de CA en la prueba del ADC?

Reducir la pendiente de la onda de rampa de entrada puede mejorar la precisión de la medición.

## ¿Qué hacer con el ruido de base alto en la prueba del ADC?

1. Aumentar el número de muestras (N) y el número de periodos de señal de prueba muestreados (M), lo que también resultará en un mayor tiempo de prueba.
2. Aumentar la frecuencia de muestreo (Fs).

No es posible distinguir entre el ruido y las armónicas si solo se muestrea un período de señal.

> ¿Existe esta fórmula? Precisión de ruido = frecuencia de muestreo / M

## ¿Cómo medir el error de ganancia del ADC en la práctica?

El método del histograma se utiliza en la práctica para medir el error de ganancia, porque el borde de transición teórico es difícil de detectar.

## ¿Necesitamos un digitalizador de CA con 2-4 bits más de resolución en la prueba del DAC?

No, no es necesario un Digitalizador de CA de muy alta resolución. Un Digitalizador de CA que cumpla con la resolución de Nyquist satisfará el estándar de prueba.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.