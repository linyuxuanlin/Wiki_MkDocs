# Flip - Linux Development Board based on Allwinner F1C200s

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220527234815.jpeg)

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220527234855.jpeg)

Project Repository: [**linyuxuanlin/Flip**](https://github.com/linyuxuanlin/Flip)

Online Preview of the Project:

<div class="altium-iframe-viewer">
  <div
    class="altium-ecad-viewer"
    data-project-src="https://github.com/linyuxuanlin/Flip/raw/main/Hardware/Flip_V0.1.zip"
  ></div>
</div>

F1C100s/F1C200s are based on the ARM9 CPU architecture, with the same package, and the only difference is that F1C100S has built-in 32MB DDR1 memory, while F1C200S has 64MB.

In addition, this chip also integrates USB OTG, UART, SPI, TWI, TP, SD/MMC, CSI and other universal peripherals.

## Basic Parameters

The basic parameters of F1C200s are as follows:

- ARM9 CPU architecture 400M
- Memory SIP 64MB DDR1
- SD2.0, eMMC 4.41
- Video H.264/MPEG1 1920x1080@30fps decoding，MJPEG 1280x720@30fps encoding
- Audio, 2xDAC and 1xADC, DAC up to 192kHz, ADC up to 48kHz
- 1 x I2S/PCM interface
- Display RGB interface up to 1280x720@60fps
- TV CVBS output, support NTSC/PAL
- USB OTG
- SDIO
- IR
- 3 x TWI
- 2 x SPI
- 3 x UART
- Melis or Linux SDK OS
- Package QFN88, 10mm x 10mm

System architecture diagram of F1C200s:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220422152227.png)

Typical application diagram:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220513232027.png)

Pin definition:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220422153239.png)

## References and Acknowledgments

- [Index] Allwinner F1C100S/F1C200S Study Notes (https://blog.csdn.net/p1279030826/article/details/113370239)
- [peng-zhihui/Planck-Pi] (https://github.com/peng-zhihui/Planck-Pi)
- [Novice Homemade Linux Development Board Part 1: Blindly Copying Schematics and Drawing PCBs] (https://www.cnblogs.com/twzy/p/14714651.html)
- [MangoPi] (https://mangopi.cc/f1c200s)

> Original: <https://wiki-power.com/>
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

## Design of Each Module

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.
