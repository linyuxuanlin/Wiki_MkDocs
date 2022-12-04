---
id: T-Clock桌上小钟（旧）
title: T-Clock 桌上小钟（旧）
---

## 背景

我从柜子里翻出了以前做的一个玩具，拨一下开关，发现还能用，遂将资料整理一下。

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/Tclock1.jpg)

## 硬件部分

元件：

- Arduino 主控
- OLED 屏幕（SSD1306 SPI）
- RTC 时钟模块（DS1307）
- 锂电池 & 充电模块

外壳：因暂时没有好的设计，所以没有制作外壳。

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/3D%20tclock.png)

## 代码

```cpp
#include <U8glib.h>
#include <SPI.h>
#include <Wire.h>
#include <RTClib.h>
U8GLIB_SSD1306_128X64 u8g(10, 9, 12, 11, 13);
//这里适用的 OLED 屏的引脚是：D0,D1,RST,DC
/*接线：
  OLED-Arduino
  D0-D10
  D1-D9
  RST-D13
  DC-D11
*/
RTC_DS1307 RTC;//RTC 按照 IIC 接线
char monthString[37] =
{
  "JanFebMarAprMayJunJulAugSepOctNovDec"
}
;
int  monthIndex[122] =
{
  0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33
}
;
String thisMonth = "";
String thisTime = "";
String thisDay = "";
//用于定义表盘的中心
int clockCentreX = 64;
int clockCentreY = 32;
void draw(void)
{
  u8g.setFont(u8g_font_profont15);
  DateTime now = RTC.now();
  //在底部显示日期
  thisDay = String(now.day(), DEC) + "/";
  thisMonth = "";
  for (int i = 0; i <= 2; i++)
  {
    thisMonth += monthString[monthIndex[now.month() - 1] + i];
  }
  thisDay = thisDay + thisMonth + "/";
  thisDay = thisDay + String(now.year() , DEC);
  const char* newDay = (const char*) thisDay.c_str();
  u8g.drawStr(32, 63, newDay);
  thisTime = "";
  thisTime = String(now.hour()) + ":";
  if (now.minute() < 10)
  {
    thisTime = thisTime + "0";    // 在单数数字前头加个 0
  }
  //数字时间
  thisTime = thisTime + String(now.minute()) ;
  const char* newTime = (const char*) thisTime.c_str();
  u8g.drawStr(10, 10, newTime);
  //画时钟盘面
  u8g.drawCircle(clockCentreX, clockCentreY, 20); // 外面的大圆
  u8g.drawCircle(clockCentreX, clockCentreY, 2);  // 里面的小圆
  //跳动显示
  for ( int z = 0; z < 360; z = z + 30 )
  {
    //始于 0°, 止于 360°
    float angle = z ;
    angle = (angle / 57.29577951) ;   //化度数为弧度
    int x2 = (clockCentreX + (sin(angle) * 20));
    int y2 = (clockCentreY - (cos(angle) * 20));
    int x3 = (clockCentreX + (sin(angle) * (20 - 5)));
    int y3 = (clockCentreY - (cos(angle) * (20 - 5)));
    u8g.drawLine(x2, y2, x3, y3);
  }
  // 秒针
  float angle = now.second() * 6 ;
  angle = (angle / 57.29577951) ; //化度数为弧度
  int x3 = (clockCentreX + (sin(angle) * (20)));
  int y3 = (clockCentreY - (cos(angle) * (20)));
  u8g.drawLine(clockCentreX, clockCentreY, x3, y3);
  // 分针
  angle = now.minute() * 6 ;
  angle = (angle / 57.29577951) ; //化度数为弧度
  x3 = (clockCentreX + (sin(angle) * (20 - 3)));
  y3 = (clockCentreY - (cos(angle) * (20 - 3)));
  u8g.drawLine(clockCentreX, clockCentreY, x3, y3);
  // 时针
  angle = now.hour() * 30 + int((now.minute() / 12) * 6 )   ;
  angle = (angle / 57.29577951) ; //化度数为弧度
  x3 = (clockCentreX + (sin(angle) * (20 - 11)));
  y3 = (clockCentreY - (cos(angle) * (20 - 11)));
  u8g.drawLine(clockCentreX, clockCentreY, x3, y3);
  //显示自己的定制字符
  u8g.setPrintPos(100, 10);
  u8g.print("Lin");
}
void setup(void)
{
  Serial.begin(9600);
  analogReference(EXTERNAL);
  Wire.begin();
  RTC.begin();
  if (! RTC.isrunning())
  {
    Serial.println("RTC is NOT running!");
    RTC.adjust(DateTime(__DATE__, __TIME__));
  }
}
void loop(void)
{
  u8g.firstPage();
  do
  {
    draw();
  }
  while ( u8g.nextPage() );
  delay(10);
}
```

资料下载：

- 所有文件（包含库文件）：[https://github.com/linyuxuanlin/My-Arduino-projects/tree/master/T-Clock](https://github.com/linyuxuanlin/My-Arduino-projects/tree/master/T-Clock)

## 总结

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/Tclock2.jpg)

这是它的背面，如果有好的设计，我将画个外壳给它装上。

## 参考与致谢

- [屏幕无法显示？先测试一下](http://shimo.im/doc/63ALdXdl3EUInWJO)
- [使用 Arduino UNO 为 Arduino Pro Mini 下载程序](http://blog.sina.com.cn/s/blog_53f8d23d0102wv3m.html)
- [U8glib 用法](https://github.com/olikraus/u8glib/wiki/device#ssd1306-128x64)



> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。

