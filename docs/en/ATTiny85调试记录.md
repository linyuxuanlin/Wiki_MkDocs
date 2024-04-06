# ATTiny85 Debugging Record

## Bootloader

```shell
P:\Arduino\hardware\tools\avr/bin/avrdude -C "P:\Arduino\hardware\tools\avr/etc/avrdude.conf" -v -pattiny85 -carduino -PCOM4 -b119200 -Uflash:w:D:\t85_default.hex:i -U lfuse:w:0xE1:m -U hfuse:w:0xDD:m -U efuse:w:0xFE:m
```

## Using Arduino as ISP Programmer

|   Attiny    | Arduino |
| :---------: | :-----: |
| Pin 1 (PB5) |   D10   |
| Pin 4 (GND) |   GND   |
| Pin 5 (PB0) |   D11   |
| Pin 6 (PB1) |   D12   |
| Pin 7 (PB2) |   D13   |
| Pin 8 (VCC) |   5V    |

First, burn the ISP program to the Arduino:

![ISP Program Burning](https://media.wiki-power.com/img/20200426144425.png)

Open the IDE's preferences and add the following URL to the Additional Boards Manager URLs:

```
https://raw.githubusercontent.com/damellis/attiny/ide-1.6.x-boards-manager/package_damellis_attiny_index.json
```

Open the Boards Manager:

![Boards Manager](https://media.wiki-power.com/img/20200426144642.png)

Search for and install the package (you might need a proxy):

![Installing Package](https://media.wiki-power.com/img/20200426144732.png)

When burning the bootloader, make sure to select the correct chip model, clock speed (Internal 16 MHz), the port where Arduino is connected, and choose "Arduino as ISP" as the programmer:

![Burning Configuration](https://media.wiki-power.com/img/20200426144834.png)

## Conclusion

## References and Acknowledgments

- [Homemade Tutorial for Building a Digispark Arduino Minimal System Based on ATTiny85 (Part 1)](https://blog.csdn.net/Argon_Ghost/article/details/103637870?depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-4&utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-4)
- [Homemade Tutorial for Building a Digispark Arduino Minimal System Based on ATTiny85 (Part 2)](https://blog.csdn.net/Argon_Ghost/article/details/103859931)
- [Exploring the Digispark USB Development Board (Part 1): Getting to Know This Compact, Affordable, and Versatile Arduino Compatible Board](https://zhuanlan.zhihu.com/p/73336394)
- [Connecting and Programming Your Digispark](http://digistump.com/wiki/digispark/tutorials/connecting)
- [Programming the Attiny85 Micronucleus Bootloader](http://iremo-tw.blogspot.com/2018/03/attiny85-micronucleus-bootloader.html)
- [Creating a Mini Game Console with ATtiny85](https://www.jianshu.com/p/55e86b4e0194)
- [Insights into DigiSpark ATtiny85: AVR ISP Programming and Bootloader Details](http://blog.sina.com.cn/s/blog_6566538d0102w6qk.html)
- [Quick Reference: Frequently Requested Information](http://digistump.com/wiki/digispark/quickref)

> Original: <https://wiki-power.com/>
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.
