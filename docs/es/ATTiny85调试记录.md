# Registro de Depuración ATTiny85

## Bootloader

```shell
P:\Arduino\hardware\tools\avr/bin/avrdude -C "P:\Arduino\hardware\tools\avr/etc/avrdude.conf" -v -pattiny85 -carduino -PCOM4 -b119200 -Uflash:w:D:\t85_default.hex:i -U lfuse:w:0xE1:m -U hfuse:w:0xDD:m -U efuse:w:0xFE:m
```

## Arduino como Programador ISP

|   Attiny    | Arduino |
| :---------: | :-----: |
| Pin 1 (PB5) |   D10   |
| Pin 4 (GND) |   GND   |
| Pin 5 (PB0) |   D11   |
| Pin 6 (PB1) |   D12   |
| Pin 7 (PB2) |   D13   |
| Pin 8 (VCC) |   5V    |

Primero, carga el programa ISP en Arduino:

![Imagen](https://media.wiki-power.com/img/20200426144425.png)

Abre las preferencias del IDE y añade la siguiente URL en la sección de direcciones adicionales para tableros de desarrollo:

```
https://raw.githubusercontent.com/damellis/attiny/ide-1.6.x-boards-manager/package_damellis_attiny_index.json
```

Luego, abre el Administrador de tableros de desarrollo:

![Imagen](https://media.wiki-power.com/img/20200426144642.png)

Busca y realiza la instalación (puede requerir un proxy):

![Imagen](https://media.wiki-power.com/img/20200426144732.png)

Al grabar, asegúrate de seleccionar el modelo de chip correcto, la velocidad de reloj (16 MHz interno), el puerto donde está conectado Arduino y el programador `Arduino as ISP`:

![Imagen](https://media.wiki-power.com/img/20200426144834.png)

## Resumen

## Referencias y Agradecimientos

- [Tutorial DIY del sistema mínimo de Arduino Digispark basado en ATTiny85 (Parte 1)](https://blog.csdn.net/Argon_Ghost/article/details/103637870?depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-4&utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-4)
- [Tutorial DIY del sistema mínimo de Arduino Digispark basado en ATTiny85 (Parte 2)](https://blog.csdn.net/Argon_Ghost/article/details/103859931)
- [Notas sobre la placa de desarrollo USB Digispark (Parte 1): Conoce esta placa compacta, asequible y versátil compatible con Arduino](https://zhuanlan.zhihu.com/p/73336394)
- [Conexión y programación de tu Digispark](http://digistump.com/wiki/digispark/tutorials/connecting)
- [Programación del bootloader Micronucleus para Attiny85](http://iremo-tw.blogspot.com/2018/03/attiny85-micronucleus-bootloader.html)
- [Creación de una mini consola de juegos ATtiny85](https://www.jianshu.com/p/55e86b4e0194)
- [DigiSpark ATtiny85: Cuestiones relacionadas con la programación AVR ISP de 8 pines y la fusión del bootloader](http://blog.sina.com.cn/s/blog_6566538d0102w6qk.html)
- [Referencia rápida: Información frecuentemente solicitada](http://digistump.com/wiki/digispark/quickref)

> Autor del artículo: **Power Lin**
> Dirección original: <https://wiki-power.com>
> Declaración de derechos de autor: Este artículo está bajo la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Por favor, menciona la fuente si deseas republicarlo.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
