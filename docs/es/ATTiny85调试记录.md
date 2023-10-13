# Registro de depuración de ATTiny85

## Bootloader

```shell
P:\Arduino\hardware\tools\avr/bin/avrdude -C "P:\Arduino\hardware\tools\avr/etc/avrdude.conf" -v -pattiny85 -carduino -PCOM4 -b119200 -Uflash:w:D:\t85_default.hex:i -U lfuse:w:0xE1:m -U hfuse:w:0xDD:m -U efuse:w:0xFE:m
```

## Arduino como programador ISP

|    Attiny     | Arduino |
| :-----------: | :-----: |
| Pin 1（PB5）  |   D10   |
| Pin 4 （GND） |   GND   |
| Pin 5 （PB0） |   D11   |
| Pin 6 （PB1） |   D12   |
| Pin 7 （PB2） |   D13   |
| Pin 8 （VCC） |   5V    |

Primero, cargue el programa ISP en Arduino:

![](https://img.wiki-power.com/d/wiki-media/img/20200426144425.png)

Abra las preferencias del IDE y escriba la siguiente dirección en la sección de URLs adicionales de tarjetas:

```
https://raw.githubusercontent.com/damellis/attiny/ide-1.6.x-boards-manager/package_damellis_attiny_index.json
```

Abra el administrador de tarjetas:

![](https://img.wiki-power.com/d/wiki-media/img/20200426144642.png)

Busque y descargue (puede necesitar un proxy):
![](https://img.wiki-power.com/d/wiki-media/img/20200426144732.png)

Al programar, asegúrese de seleccionar el modelo de chip correcto, la velocidad de reloj (Internal 16 MHz), el puerto donde está conectado el Arduino y seleccione `Arduino as ISP` como programador:

![](https://img.wiki-power.com/d/wiki-media/img/20200426144834.png)

## Conclusión

## Referencias y agradecimientos

- [Tutorial de fabricación de sistemas mínimos de Arduino Digispark basados en ATTiny85 (Parte 1)](https://blog.csdn.net/Argon_Ghost/article/details/103637870?depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-4&utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-4)
- [Tutorial de fabricación de sistemas mínimos de Arduino Digispark basados en ATTiny85 (Parte 2)](https://blog.csdn.net/Argon_Ghost/article/details/103859931)
- [Notas sobre el desarrollo de la placa Digispark USB (Parte 1): Conoce esta pequeña, económica y multifuncional placa compatible con Arduino](https://zhuanlan.zhihu.com/p/73336394)
- [Conexión y programación de tu Digispark](http://digistump.com/wiki/digispark/tutorials/connecting)
- [Quemado del bootloader Micronucleus de Attiny85](http://iremo-tw.blogspot.com/2018/03/attiny85-micronucleus-bootloader.html)
- [Creación de una mini consola de juegos con ATtiny85](https://www.jianshu.com/p/55e86b4e0194)
- [Algunas cosas sobre la programación del ISP de Arduino AVR de 8 pines DigiSpark ATtiny85 y la configuración de los fusibles del bootloader](http://blog.sina.com.cn/s/blog_6566538d0102w6qk.html)
- [Referencia rápida: información solicitada con frecuencia](http://digistump.com/wiki/digispark/quickref)

> Autor del artículo: **Power Lin**
> Dirección original: <https://wiki-power.com>
> Declaración de derechos de autor: Este artículo utiliza la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Por favor, indique la fuente al volver a publicar.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
