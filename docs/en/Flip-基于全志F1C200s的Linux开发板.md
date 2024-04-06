# Flip - A Linux Development Board based on Allwinner F1C200s

![Image](https://media.wiki-power.com/img/20220527234815.jpeg)

![Image](https://media.wiki-power.com/img/20220527234855.jpeg)

Project Repository: [**linyuxuanlin/Flip**](https://github.com/linyuxuanlin/Flip)

Online Project Preview:

<div class="altium-iframe-viewer">
  <div
    class="altium-ecad-viewer"
    data-project-src="https://github.com/linyuxuanlin/Flip/raw/main/Hardware/Flip_V0.1.zip"
  ></div>
</div>

The F1C100s/F1C200s are based on the ARM9 CPU architecture and have identical packaging. The only difference is that the F1C100S comes with 32MB DDR1 memory, while the F1C200S has 64MB.

In addition, this chip integrates various common peripherals such as USB OTG, UART, SPI, TWI, TP, SD/MMC, and CSI.

## Basic Specifications

Here are the basic specifications of the F1C200s:

- ARM9 CPU architecture running at 400M
- 64MB DDR1 Memory SIP
- SD2.0 and eMMC 4.41 support
- Video capabilities include H.264/MPEG1 decoding at 1920x1080@30fps, and MJPEG encoding at 1280x720@30fps
- Audio support with 2xDAC and 1xADC, DAC up to 192kHz, and ADC up to 48kHz
- 1 x I2S/PCM interface
- RGB display interface supporting up to 1280x720@60fps
- TV CVBS output with support for NTSC/PAL
- USB OTG
- SDIO
- IR
- 3 x TWI (Two-Wire Interface)
- 2 x SPI
- 3 x UART
- Operating system options include Melis or Linux SDK OS
- Package: QFN88, 10mm x 10mm

System architecture diagram of the F1C200s:

![Image](https://media.wiki-power.com/img/20220422152227.png)

Typical application schematic:

![Image](https://media.wiki-power.com/img/20220513232027.png)

Pin definitions:

![Image](https://media.wiki-power.com/img/20220422153239.png)

## References and Acknowledgments

- [Allwinner F1C100S/F1C200S Learning Notes](https://blog.csdn.net/p1279030826/article/details/113370239)
- [peng-zhihui/Planck-Pi](https://github.com/peng-zhihui/Planck-Pi)
- [Homemade Linux Development Board Part 1: Schematic Chaos and PCB Sketch](https://www.cnblogs.com/twzy/p/14714651.html)
- [MangoPi](https://mangopi.cc/f1c200s)

> Original: <https://wiki-power.com/>
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

## Design of Each Module

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.
