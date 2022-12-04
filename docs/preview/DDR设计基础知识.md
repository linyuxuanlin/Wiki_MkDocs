---
id: DDR3硬件设计基础
title: 🚧DDR3硬件设计基础
---

## 连接器的规范与设计

DDR 的连接器俗称金手指（Gold Finger/Edge Connector），它是由镀金工艺（金的抗氧化性与传导性都很强）的导电触片组成，因排列如手指状，所以称为「金手指」。

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20200226143912.png)

金手指的设计要求：

- 金手指上金的厚度一般是 0.25-1.3 um，金的厚度根据金手指的插拔次数而定；
- 金手指间的最小距离 6 mil；
- 金手指板卡的设计厚度是 0.8-2.0 mm；
- 金手指最大高度 ≤ 2 inch；
- 金手指倒角的角度可以是 20°/30°/45°/60°/90°；
- 沉锡、沉银焊盘的距离离金手指顶端最小间距 14 mil；
- 金手指的倒角要求如下图所示，除了插入边要倒角以外，插板两侧板也应该设计（1-1.5）45° 的倒角或者 R1-R1.5 的圆角，方便插拔。

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20200226144135.png)

## 参考与致谢

- [金手指是什么？](https://mp.weixin.qq.com/s?__biz=MjM5NTEwMzgzMQ==&mid=2649269244&idx=2&sn=ca73ef4b3734b41d59ab1e14bcb6623a&chksm=bee196c489961fd25380547dcc36f7ff6c129ffd2382a460d432f6152782ab347f7118cf233e&mpshare=1&scene=1&srcid=&sharer_sharetime=1582689705345&sharer_shareid=57baeb2b96d0cff9b17ac2c15b36602b&key=c7906fbfc53fe5d7bc99093e125472fc5bf7bce47f6e60a292ce9c07c4c99bd1855651114bf5b1f7f41907fbbedf35ee741ee5fbca484d64380c1486cc70f0946f35eadff73993f9cbab7af47b3b6e56&ascene=1&uin=MTk5MDUwOTA0Mg%3D%3D&devicetype=Windows+10&version=62080079&lang=zh_CN&exportkey=A%2BV%2F1nGsX3dWAdVVwb3gU4A%3D&pass_ticket=9Co0R2f8RJ%2BAEY%2FRlXB3p4L%2BjB3NsANRp2QCMNR1ZRpWYbXz9Y2XhUZog5FHSu%2Fm)
- [PCB 的金手指设计与加工制作](https://mp.weixin.qq.com/s?__biz=MzA3NTEzODc2Mg==&mid=2651875943&idx=1&sn=e2d707f5af6371740cc9d6512434ca0e&chksm=8491d9c2b3e650d4b597d19d9956449156b64e69e7270c2370ef4dfc40aaab6ee09ea4e690f9&mpshare=1&scene=1&srcid=&sharer_sharetime=1582831875991&sharer_shareid=57baeb2b96d0cff9b17ac2c15b36602b&key=039e41916f0c5b3112996dc0d3d118480fc4471f799c219533de763261185bac35959a99889118a8c749bcca85a2ab1c07491a572297d5281cb91702606e77b45ab7547c5d031fdef888c6ae1860c17d&ascene=1&uin=MTk5MDUwOTA0Mg%3D%3D&devicetype=Windows+10&version=62080079&lang=zh_CN&exportkey=A3n60iUGoPLNJyA6X6FXphE%3D&pass_ticket=z4ox3f8nl73K2MPu0EBLLe%2FAru4MK%2B7c3EfDVNQbWWoZL0WujjMAwkBNocQsOmu8)

> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。


### DDR 储存阵列

详细的描述：

- A0-A9, A10/AP, A11, A12/BC#, A13：为 ACTIVATE 命令提供行地址，同时为 READ/WRITE 命令提供列地址和自动预充电位（A10），以便从某个 Bank 的内存阵列里选出一个位置。
- BA0-BA2：
- CK, CK#：
- CKE：
- CS#：
- DM：
- ODT：
- RAS#, CAS#, WE#：
- RESET#：
- DQ0-DQ7：
- DQS, DQS#：
- TDQS, TDQS#：
- VDD：
- VDDQ：
- VREFCA：
- VREFDQ：
- VSS：
- VSSQ：
- ZQ：
