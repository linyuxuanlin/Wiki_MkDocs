# Linux embebido - Subsistema GPIO

## Referencias y agradecimientos

- [8. Control de zumbador (Subsistema GPIO)](https://doc.embedfire.com/linux/stm32mp1/linux_base/zh/latest/linux_app/gpio_subsystem/gpio_subsystem.html)

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

## Introducción al subsistema GPIO

GPIO (General Purpose I/O) se refiere a los puertos de entrada/salida generales. Estos pines suelen tener múltiples funciones, siendo la más básica la detección de entrada de nivel alto o bajo y la salida. Algunos pines también se pueden vincular a los periféricos integrados del controlador principal, y se pueden utilizar como pines de comunicación para UART, I2C, red, detección de voltaje, entre otros.

Al igual que con el subsistema LED, Linux proporciona un marco de controlador para el subsistema GPIO. Este marco de controlador exporta los pines GPIO de la CPU al espacio de usuario, y podemos controlarlos accediendo al sistema de archivos `/sys`. El subsistema GPIO admite el uso de pines para funciones básicas de entrada/salida, y la función de entrada admite la detección de interrupciones. (En el directorio `Documentation/gpio` del código fuente del kernel de Linux se puede encontrar una explicación más detallada sobre el subsistema GPIO).

## Directorio de dispositivos GPIO

El directorio exportado por el subsistema GPIO al espacio de usuario es `/sys/class/gpio`, que se puede ver con el siguiente comando:

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.