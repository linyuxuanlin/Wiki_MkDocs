# Flip - A Linux Development Board Based on Allwinner F1C200s

![Imagen](https://media.wiki-power.com/img/20220527234815.jpeg)

![Imagen](https://media.wiki-power.com/img/20220527234855.jpeg)

Repository: [**linyuxuanlin/Flip**](https://github.com/linyuxuanlin/Flip)

Vista previa en línea del proyecto:

<div class="altium-iframe-viewer">
  <div
    class="altium-ecad-viewer"
    data-project-src="https://github.com/linyuxuanlin/Flip/raw/main/Hardware/Flip_V0.1.zip"
  ></div>
</div>

Los chips F1C100s/F1C200s están basados en la arquitectura de CPU ARM9, con un encapsulado similar. La diferencia principal radica en que el F1C100S tiene 32MB de memoria DDR1 integrada, mientras que el F1C200S cuenta con 64MB.

Además, este chip incluye periféricos universales como USB OTG, UART, SPI, TWI, TP, SD/MMC, CSI, entre otros.

## Especificaciones Básicas

Las especificaciones básicas del F1C200s son las siguientes:

- Arquitectura de CPU ARM9 a 400M
- Memoria SIP DDR1 de 64MB
- SD2.0, eMMC 4.41
- Decodificación de video H.264/MPEG1 a 1920x1080@30fps, codificación MJPEG a 1280x720@30fps
- Audio, 2xDAC y 1xADC, DAC de hasta 192kHz, ADC de hasta 48kHz
- 1 x interfaz I2S/PCM
- Interfaz RGB para pantalla de hasta 1280x720@60fps
- Salida de TV CVBS, compatible con NTSC/PAL
- USB OTG
- SDIO
- IR
- 3 x TWI
- 2 x SPI
- 3 x UART
- Sistema operativo Melis o Linux SDK
- Encapsulado QFN88, 10mm x 10mm

Diagrama de arquitectura del sistema F1C200s:

![Imagen](https://media.wiki-power.com/img/20220422152227.png)

Diagrama de aplicación típica:

![Imagen](https://media.wiki-power.com/img/20220513232027.png)

Definición de pines:

![Imagen](https://media.wiki-power.com/img/20220422153239.png)

## Referencias y Agradecimientos

- [**Notas de estudio de Allwinner F1C100S/F1C200S**](https://blog.csdn.net/p1279030826/article/details/113370239)
- [**peng-zhihui/Planck-Pi**](https://github.com/peng-zhihui/Planck-Pi)
- [**Linux Development Board hecho por novatos: Parte 1 - Diseño de esquemas y PCB**](https://www.cnblogs.com/twzy/p/14714651.html)
- [**MangoPi**](https://mangopi.cc/f1c200s)

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

## Diseño de los Módulos Correspondientes

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
