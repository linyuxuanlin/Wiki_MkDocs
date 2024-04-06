# Modos de Arranque de STM32

STM32 proporciona los pines BOOT1 y BOOT0 que permiten seleccionar el modo de arranque después de un reinicio al configurar el estado de estos pines.

Aquí se presentan tres modos de arranque:

## 1. Arranque desde la Memoria Flash Principal

| BOOT0 |      BOOT1      |
| :---: | :-------------: |
| Bajo  | Cualquier valor |

En condiciones normales, el dispositivo se inicia desde la memoria Flash en el chip (que puede ser una Flash de 64K / 128K / 256K).

## 2. Arranque desde la Memoria del Sistema

| BOOT0 | BOOT1 |
| :---: | :---: |
| Alto  | Bajo  |

Este modo se utiliza cuando se descargan programas a través de una interfaz serie o ISP.

## 3. Arranque desde la SRAM Incorporada

| BOOT0 | BOOT1 |
| :---: | :---: |
| Alto  | Alto  |

Este modo de arranque desde la SRAM incorporada tiene dos aplicaciones principales:

- Mejora la eficiencia al realizar descargas y depuraciones repetidas, ya que cargar en la Flash es relativamente lento. Es importante tener en cuenta que el programa se perderá si se interrumpe la alimentación.
- Utilizado para desactivar la protección de lectura del chip y restablecer la Flash a su configuración original de fábrica.

## Nota

En la tabla anterior, 'Alto' y 'Bajo' indican la configuración de una resistencia de 10K como pull-up o pull-down, en lugar de una conexión directa a VCC o GND.

![Imagen](https://media.wiki-power.com/img/20200603134417.jpg)

## Referencias y Agradecimientos

- [Configuración de los pines BOOT0 y BOOT1 de STM32](https://blog.csdn.net/Creative_Team/article/details/79315876)
- [Configuración y funciones del modo de arranque de STM32](https://blog.csdn.net/weixin_34349320/article/details/86231081?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase)

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
