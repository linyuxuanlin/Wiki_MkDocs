# Linux embebido - Subsistema GPIO

## Referencias y agradecimientos

- [8. Control de un zumbador (Subsistema GPIO)](https://doc.embedfire.com/linux/stm32mp1/linux_base/zh/latest/linux_app/gpio_subsystem/gpio_subsystem.html)

> Dirección original del artículo: <https://wiki-power.com/>
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

## Introducción al subsistema GPIO

GPIO (General Purpose I/O) se refiere a los puertos de entrada/salida generales. Estos pines generalmente tienen múltiples funciones, siendo las más básicas la detección de niveles de entrada y la salida de niveles altos o bajos. Algunos pines también pueden estar vinculados a periféricos integrados en el controlador principal, y se pueden utilizar como pines de comunicación para UART, I2C, red, detección de voltaje, entre otros.

Al igual que el subsistema LED, Linux proporciona un marco de controladores para el subsistema GPIO, que exporta los pines GPIO de la CPU al espacio de usuario. Podemos controlarlos accediendo al sistema de archivos `/sys`. El subsistema GPIO permite utilizar los pines para funciones básicas de entrada/salida, incluyendo la detección de interrupciones en las entradas. (Se puede encontrar una explicación más detallada sobre el subsistema GPIO en el directorio `Documentation/gpio` del código fuente del kernel de Linux).

## Directorio de dispositivos GPIO

El directorio exportado al espacio de usuario por el subsistema de controladores GPIO es `/sys/class/gpio`. Puedes utilizar el siguiente comando para verlo:

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.