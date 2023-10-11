# Flip - Placa de desarrollo Linux basada en F1C200s de Allwinner

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220527234815.jpeg)

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220527234855.jpeg)

Repositorio del proyecto: [**linyuxuanlin/Flip**](https://github.com/linyuxuanlin/Flip)

Vista previa en línea del proyecto:

<div class="altium-iframe-viewer">
  <div
    class="altium-ecad-viewer"
    data-project-src="https://github.com/linyuxuanlin/Flip/raw/main/Hardware/Flip_V0.1.zip"
  ></div>
</div>

F1C100s/F1C200s se basan en la arquitectura de CPU ARM9, tienen el mismo encapsulado y la única diferencia es que F1C100S tiene 32 MB de memoria DDR1 incorporada, mientras que F1C200S tiene 64 MB.

Además, este chip integra dispositivos periféricos universales como USB OTG, UART, SPI, TWI, TP, SD/MMC, CSI, entre otros.

## Parámetros básicos

Los parámetros básicos de F1C200s son los siguientes:

- Arquitectura de CPU ARM9 a 400M
- SIP de memoria DDR1 de 64 MB
- SD2.0, eMMC 4.41
- Decodificación de video H.264/MPEG1 a 1920x1080@30fps, codificación MJPEG a 1280x720@30fps
- Audio, 2xDAC y 1xADC, DAC hasta 192kHz, ADC hasta 48kHz
- 1 x interfaz I2S/PCM
- Interfaz RGB de pantalla de hasta 1280x720@60fps
- Salida de TV CVBS, compatible con NTSC/PAL
- USB OTG
- SDIO
- IR
- 3 x TWI
- 2 x SPI
- 3 x UART
- Sistema operativo Melis o Linux SDK
- Paquete QFN88, 10mm x 10mm

Diagrama de arquitectura del sistema F1C200s:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220422152227.png)

Diagrama de aplicación típica:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220513232027.png)

Definición de pines:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220422153239.png)

## Referencias y agradecimientos

- [【目录】全志 F1C100S/F1C200S 学习笔记](https://blog.csdn.net/p1279030826/article/details/113370239)
- [peng-zhihui/Planck-Pi](https://github.com/peng-zhihui/Planck-Pi)
- [小白自制 Linux 开发板 一. 瞎抄原理图与乱画 PCB](https://www.cnblogs.com/twzy/p/14714651.html)
- [MangoPi](https://mangopi.cc/f1c200s)

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

## Diseño de cada módulo

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
