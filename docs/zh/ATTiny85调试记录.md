---
id: ATTiny85调试记录
title: ATTiny85 调试记录
---

## Bootloader

```shell
P:\Arduino\hardware\tools\avr/bin/avrdude -C "P:\Arduino\hardware\tools\avr/etc/avrdude.conf" -v -pattiny85 -carduino -PCOM4 -b119200 -Uflash:w:D:\t85_default.hex:i -U lfuse:w:0xE1:m -U hfuse:w:0xDD:m -U efuse:w:0xFE:m
```

## Arduino 作为 ISP 下载器

|    Attiny     | Arduino |
| :-----------: | :-----: |
| Pin 1（PB5）  |   D10   |
| Pin 4 （GND） |   GND   |
| Pin 5 （PB0） |   D11   |
| Pin 6 （PB1） |   D12   |
| Pin 7 （PB2） |   D13   |
| Pin 8 （VCC） |   5V    |

先给 Arduino 烧 ISP 程序：

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20200426144425.png)

打开 IDE 首选项，在附加开发板地址中填写：

```
https://raw.githubusercontent.com/damellis/attiny/ide-1.6.x-boards-manager/package_damellis_attiny_index.json
```

打开开发板管理器：

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20200426144642.png)

搜索并安装（可能需要代理）：
![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20200426144732.png)

烧录时注意选对芯片型号、时钟速率（Internal 16 MHz）、Arduino 所在的端口，注意编程器选择 `Arduino as ISP`：

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20200426144834.png)

## 总结

## 参考与致谢

- [基于 ATTiny85 的 digispark Arduino 最小系统的自制教程（一）](https://blog.csdn.net/Argon_Ghost/article/details/103637870?depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-4&utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-4)
- [基于 ATTiny85 的 digispark Arduino 最小系统的自制教程（二）](https://blog.csdn.net/Argon_Ghost/article/details/103859931)
- [Digispark USB 开发板把玩笔记（一）：认识这块小巧、便宜、多功能的 Arduino 兼容板](https://zhuanlan.zhihu.com/p/73336394)
- [Connecting and Programming Your Digispark](http://digistump.com/wiki/digispark/tutorials/connecting)
- [Attiny85 Micronucleus bootloader 燒錄](http://iremo-tw.blogspot.com/2018/03/attiny85-micronucleus-bootloader.html)
- [ATtiny85 制作迷你小游戏机](https://www.jianshu.com/p/55e86b4e0194)
- [DigiSpark ATtiny85 8 脚 Arduino AVR ISP 编程的那点事儿 BootLoader 熔丝](http://blog.sina.com.cn/s/blog_6566538d0102w6qk.html)
- [Quick Reference Frequently requested info](http://digistump.com/wiki/digispark/quickref)

> 文章作者：**Power Lin**
> 原文地址：<https://wiki-power.com>
> 版权声明：文章采用 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议，转载请注明出处。
