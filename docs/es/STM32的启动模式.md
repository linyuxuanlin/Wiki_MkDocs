# Modos de arranque de STM32

STM32 proporciona los pines BOOT1 y BOOT0, que se pueden configurar para seleccionar el modo de arranque después del reinicio.

A continuación se presentan tres modos de arranque:

## 1. Arranque desde la memoria flash principal

| BOOT0 | BOOT1 |
| :---: | :---: |
|  Bajo | Cualquier |

Arranque desde la memoria flash en el chip (es decir, flash con parámetros de 64K / 128K / 256K), que generalmente se configura de esta manera en condiciones normales.

## 2. Arranque desde la memoria del sistema

| BOOT0 | BOOT1 |
| :---: | :---: |
| Alto | Bajo |

Se requiere esta configuración para descargar programas a través de serie / ISP.

## 3. Arranque desde la SRAM incorporada

| BOOT0 | BOOT1 |
| :---: | :---: |
| Alto | Alto |

El arranque desde la SRAM incorporada tiene dos usos:

- Para aumentar la eficiencia al descargar y depurar repetidamente (ya que la descarga en flash es relativamente lenta). Tenga en cuenta que el programa se perderá después del apagado.
- Para desbloquear la función de protección de lectura del chip / borrar la flash y restaurar la configuración de fábrica.

## Suplemento

En la tabla anterior, "alto" y "bajo" indican una resistencia de 10K conectada a VCC / GND, no una conexión directa a VCC / GND.

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20200603134417.jpg)

## Referencia y agradecimiento

- [Configuración de STM32 BOOT0, BOOT1](https://blog.csdn.net/Creative_Team/article/details/79315876)
- [Configuración y función del modo de arranque de STM32 BOOT](https://blog.csdn.net/weixin_34349320/article/details/86231081?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase)

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.