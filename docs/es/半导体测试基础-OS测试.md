# Fundamentos de Pruebas de Semiconductores - Pruebas OS

Las pruebas de circuito abierto y cortocircuito (OS, Prueba de Circuito Abierto y Cortocircuito, también conocida como prueba de continuidad o contacto) se utilizan para verificar la conectividad eléctrica de todos los pines del sistema de prueba y el dispositivo bajo prueba (DUT), sin generar cortocircuitos con otros pines o con las fuentes de alimentación (tierra). Las pruebas OS permiten detectar rápidamente defectos físicos eléctricos en el DUT, como cortocircuitos en los pines, ausencia de hilos de conexión, daños electrostáticos en los pines y defectos de fabricación, entre otros. También pueden identificar problemas relacionados con componentes de prueba, como problemas en el ProbeCard o el zócalo del dispositivo.

El proceso de prueba OS implica la utilización de diodos de protección entre VDD y tierra. Por lo general, existen dos métodos de prueba: uno que utiliza una fuente de medida programable (PMU) para inyectar corriente y medir el voltaje, y otro que utiliza un enfoque de prueba funcional para proporcionar una referencia de voltaje (VREF) y luego medir el voltaje en respuesta a una carga dinámica.

### Prueba OS - Método Estático

La prueba OS en modo estático, ya sea en serie o en paralelo, implica esencialmente inyectar corriente y medir el voltaje, ya que esta corriente hace que un diodo de protección se polarice positivamente, lo que permite detectar anomalías de circuito abierto o cortocircuito mediante la medición de la caída de voltaje positiva. La figura siguiente muestra un diagrama de prueba que aplica corriente positiva para polarizar el diodo de protección de la fuente de alimentación:

![Diagrama de Prueba](https://media.wiki-power.com/img/20220805165031.png)

El proceso de prueba se lleva a cabo de la siguiente manera:

1. Conectar todos los pines del DUT a tierra, incluyendo los pines de la fuente de alimentación y tierra.
2. La PMU aplica una corriente a los pines (aproximadamente 100 µA).
3. Se mide el voltaje en los pines.
   - Si el voltaje es superior a VOH (+1.5V): Error (Circuito Abierto).
   - Si el voltaje es inferior a VOL (+0.2V): Error (Cortocircuito).
   - En otros intervalos (voltaje positivo, por ejemplo, 0.65V): Aprobado

El diagrama de prueba que aplica corriente negativa para polarizar el diodo de protección de tierra se muestra a continuación:

![Diagrama de Prueba](https://media.wiki-power.com/img/20220728142155.png)

El proceso de prueba es el siguiente:

1. Conectar todos los pines del DUT a tierra, incluyendo los pines de la fuente de alimentación y tierra.
2. La PMU aplica una corriente a los pines (aproximadamente -100 µA).
3. Se mide el voltaje en los pines.
   - Si el voltaje es superior a VOH (-0.2V): Error (Cortocircuito).
   - Si el voltaje es inferior a VOL (-1.5V): Error (Circuito Abierto).
   - En otros intervalos (caída de voltaje negativa después de la polarización, aproximadamente -0.65V): Aprobado

Debido a que la PMU proporciona una corriente constante, se requiere una limitación de voltaje para evitar que el voltaje generado durante la prueba de circuito abierto se vuelva infinito. Si se configura la limitación de voltaje en 3V, el resultado de la prueba para un pin en modo circuito abierto sería de 3V.

Este método solo es adecuado para la prueba de pines de señal IO; no se puede utilizar para probar pines de alimentación. Aunque es posible probar pines de alimentación en condiciones de circuito abierto, se requieren límites de prueba diferentes debido a sus estructuras internas distintas.

En resumen, las características de la prueba OS en modo estático son las siguientes:

- El método en serie prueba un solo pin a la vez, lo que lo hace sencillo pero poco eficiente, adecuado para DUT con pocos pines.
- El método en paralelo requiere un sistema de prueba con PPMU; sin embargo, no puede detectar cortocircuitos entre pines adyacentes. Una solución es realizar dos pruebas separadas (por ejemplo, primero probar los pines 1357 y luego los pines 2468).
- Aplicación de corriente y medición de voltaje.

## Referencias y Agradecimientos

- "The Fundamentals Of Digital Semiconductor Testing"
- "DC Test Theory"

> Dirección original del artículo: <https://wiki-power.com/>
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
