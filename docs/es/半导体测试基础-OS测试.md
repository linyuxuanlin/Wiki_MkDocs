# Fundamentos de pruebas de semiconductores - Pruebas OS

Las pruebas de circuito abierto y cortocircuito (OS, Open-Short Test, también conocidas como pruebas de continuidad o contacto) se utilizan para **verificar la continuidad eléctrica de todos los pines del dispositivo y del sistema de prueba, y para asegurarse de que no haya cortocircuitos con otros pines o con la fuente de alimentación (tierra)**. Las pruebas OS pueden detectar rápidamente defectos físicos eléctricos en el DUT, como cortocircuitos de pines, falta de alambres de conexión, daño electrostático de pines y defectos de fabricación, así como problemas relacionados con los accesorios de prueba, como problemas de contacto en la ProbeCard o el socket del dispositivo.

El proceso de prueba OS utiliza diodos de protección para VDD y tierra. En general, hay dos métodos de prueba: uno utiliza PMU para inyectar corriente y medir voltaje, y el otro utiliza un método de prueba funcional para proporcionar VREF y medir voltaje con carga dinámica.

### Pruebas OS - Método estático

Las pruebas OS estáticas en serie / paralelo son esencialmente la inyección de corriente y la medición de voltaje, ya que esta corriente hace que un diodo de protección superior o inferior se polarice positivamente, lo que permite detectar anomalías de circuito abierto o cortocircuito midiendo la caída de voltaje polarizado positivamente. El diagrama de prueba para polarizar positivamente el diodo de la fuente de alimentación se muestra a continuación:

![](https://f004.backblazeb2.com/file/wiki-media/img/20220805165031.png)

El proceso de prueba es el siguiente:

1. Conecte todos los pines del DUT (incluyendo la fuente de alimentación y la tierra) a tierra.
2. PMU aplica corriente a los pines (aproximadamente 100µA).
3. Mida el voltaje del pin
   - Mayor que VOH (+1,5V): Falla (abierto)
   - Menor que VOL (+0,2V): Falla (cortocircuito)
   - Otro intervalo (voltaje polarizado positivamente, como 0,65V): Aprobado

El diagrama de prueba para polarizar positivamente el diodo a tierra se muestra a continuación:

![](https://f004.backblazeb2.com/file/wiki-media/img/20220728142155.png)

El proceso de prueba es el siguiente:

1. Conecte todos los pines del DUT (incluyendo la fuente de alimentación y la tierra) a tierra.
2. PMU aplica corriente a los pines (aproximadamente -100µA).
3. Mida el voltaje del pin
   - Mayor que VOH (-0,2V): Falla (cortocircuito)
   - Menor que VOL (-1,5V): Falla (abierto)
   - Otro intervalo (caída de voltaje polarizada positivamente de aproximadamente -0,65V): Aprobado

Debido a que PMU proporciona corriente constante, se requiere un clamp de voltaje para limitar el voltaje generado durante la prueba de circuito abierto, de lo contrario, el voltaje será infinito. Si el voltaje de clamp se establece en 3V, entonces cuando un pin está abierto, el resultado de la prueba es 3V.

Este método solo se aplica a la prueba de pines de señal IO y no se puede utilizar para la prueba de pines de alimentación. Aunque los pines de alimentación también se pueden probar en condiciones de circuito abierto, debido a su estructura interna diferente, se requieren límites de prueba diferentes.

En resumen, las características de las pruebas OS estáticas son:

- El método en serie prueba un solo pin a la vez, es simple pero ineficiente, y es adecuado para DUT con pocos pines.
- El método en paralelo requiere que el sistema de prueba tenga PPMU, la desventaja es que no puede detectar cortocircuitos entre pines adyacentes, la solución es realizar dos pruebas separadas (por ejemplo, la primera prueba de los pines 1357, la segunda prueba de los pines 2468).
- Se aplica corriente y se mide el voltaje.

## Referencias y agradecimientos

- "The Fundamentals Of Digital Semiconductor Testing"
- "DC Test Theory"

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.