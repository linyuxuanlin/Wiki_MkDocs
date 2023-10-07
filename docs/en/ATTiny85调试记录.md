# Debugging Record of ATTiny85

## Bootloader

```shell
P:\Arduino\hardware\tools\avr/bin/avrdude -C "P:\Arduino\hardware\tools\avr/etc/avrdude.conf" -v -pattiny85 -carduino -PCOM4 -b119200 -Uflash:w:D:\t85_default.hex:i -U lfuse:w:0xE1:m -U hfuse:w:0xDD:m -U efuse:w:0xFE:m
```

## Arduino as ISP Downloader

|    Attiny     | Arduino |
| :-----------: | :-----: |
| Pin 1（PB5）  |   D10   |
| Pin 4 （GND） |   GND   |
| Pin 5 （PB0） |   D11   |
| Pin 6 （PB1） |   D12   |
| Pin 7 （PB2） |   D13   |
| Pin 8 （VCC） |   5V    |

First, burn the ISP program to Arduino:

![](https://f004.backblazeb2.com/file/wiki-media/img/20200426144425.png)

Open IDE preferences and fill in the additional board manager URLs:

```
https://raw.githubusercontent.com/damellis/attiny/ide-1.6.x-boards-manager/package_damellis_attiny_index.json
```

Open the board manager:

![](https://f004.backblazeb2.com/file/wiki-media/img/20200426144642.png)

Search and install (may require a proxy):
![](https://f004.backblazeb2.com/file/wiki-media/img/20200426144732.png)

Pay attention to selecting the correct chip model, clock speed (Internal 16 MHz), and the port where Arduino is located when burning. Also, select "Arduino as ISP" as the programmer:

![](https://f004.backblazeb2.com/file/wiki-media/img/20200426144834.png)

## Conclusion

## References and Acknowledgements

- [DIY Tutorial for the Digispark Arduino Minimal System Based on ATTiny85 (Part 1)](https://blog.csdn.net/Argon_Ghost/article/details/103637870?depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-4&utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-4)
- [DIY Tutorial for the Digispark Arduino Minimal System Based on ATTiny85 (Part 2)](https://blog.csdn.net/Argon_Ghost/article/details/103859931)
- [Playing with the Digispark USB Development Board (Part 1): Getting to Know This Small, Cheap, and Multifunctional Arduino-Compatible Board](https://zhuanlan.zhihu.com/p/73336394)
- [Connecting and Programming Your Digispark](http://digistump.com/wiki/digispark/tutorials/connecting)
- [Attiny85 Micronucleus Bootloader Burning](http://iremo-tw.blogspot.com/2018/03/attiny85-micronucleus-bootloader.html)
- [Making a Mini Game Console with ATtiny85](https://www.jianshu.com/p/55e86b4e0194)
- [DigiSpark ATtiny85 8-Pin Arduino AVR ISP Programming and Bootloader Fuse Information](http://blog.sina.com.cn/s/blog_6566538d0102w6qk.html)
- [Quick Reference: Frequently Requested Information](http://digistump.com/wiki/digispark/quickref)

Article Author: **Power Lin**
Original Article Link: <https://wiki-power.com>
Copyright Statement: This article is licensed under the [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) protocol. Please indicate the source when reprinting.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.