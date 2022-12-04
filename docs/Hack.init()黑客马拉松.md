---
id: Hack.init()黑客马拉松
title: Hack.init( ) 黑客马拉松
---

—— Wight · 基于云平台的去线缆化照明系统。

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/wight.jpg)

项目仓库：[**linyuxuanlin / Wight**](https://github.com/linyuxuanlin/Wight)

## 背景

项目制作于 2017 hack.init\(\) 创客马拉松。 20 多个小时的敲代码、建模、调试各种乱七八糟的 bug、等待打印、展示 & 演讲，终于有点成品的样子。

这个项目主要用于乡村偏远地区的路灯照明系统。 模型有点抽象，其实它正扮演的是一杆路灯。

## 项目创新点

- **太阳能供电。** 自给自足（经查阅详细资料，太阳能发电量足以点亮 LED）
- **去线缆化。** 为偏远山区不方便铺线缆提供便利
- **智能算法。** 检测到夜晚，自动开灯；检测到人或车辆经过，提高 LED 亮度
- **云平台统一控制。** 用的是 GSM 主控，可以批量远程调试
- **拓展性。** 对个别有自定义照明需求的特殊用户提供各种自定义的功能

## 原理及实现

**代码：**

```cpp
#define BUTTONS_address   "channel/widget4_0/cmd/control" //开关命令
#define LIGHT_STATUS_address  "channel/widget4_0/data/light"//开关状态
#define ITENSITY_DATA_address "channel/widget4_0/data/lightsensor"
#define LEDPIN1    D1    //定义灯泡控制引脚
#define LEDPIN2    D2
#define LEDPIN3    D3
#define LEDPIN4    D5
#define CHECKIN1   A0
#define CHECKIN2   D4

int autostate = 2;
int light_state = 2;
void buttons_function(uint8_t *payload, uint32_t len)//自动&浇水按钮
{
    uint8_t SwitchKey;
    uint8_t SwitchKey2;
    aJsonClass aJson;
    aJsonObject *root = aJson.parse((char *)payload);
    if(root == NULL)
    {
        aJson.deleteItem(root);
        return;
    }
    aJsonObject *_switch = aJson.getObjectItem(root, "mode");
    if(_switch != NULL)
    {
        SwitchKey = atoi(_switch->valuestring);
        if(SwitchKey)
        {
            SerialUSB.println("auto on");
            autostate=1;
             IntoRobot.publish(LIGHT_STATUS_address,"1");
        }
        else
        {
            SerialUSB.println("auto off");
            autostate=0;
             IntoRobot.publish(LIGHT_STATUS_address,"0");
        }
    }
    aJsonObject *_switch2 = aJson.getObjectItem(root, "manual");
    if(_switch2 != NULL)
    {
        SwitchKey2 = atoi(_switch2->valuestring);
        if(SwitchKey2)
        {
            SerialUSB.println("manual on");
            light_state=1;
             IntoRobot.publish(LIGHT_STATUS_address,"1");
        }
        else
        {
            SerialUSB.println("manual off");
            light_state=0;
             IntoRobot.publish(LIGHT_STATUS_address,"0");
        }
    }
    else
    {
    }
    aJson.deleteItem(root);
}
void lightup()
{
    digitalWrite(LEDPIN1, HIGH);    // 打开灯泡
    digitalWrite(LEDPIN2, HIGH);    // 打开灯泡
    digitalWrite(LEDPIN3, HIGH);    // 打开灯泡
    digitalWrite(LEDPIN4, HIGH);    // 打开灯泡

}
void light_half_up()
{
    analogWrite(LEDPIN1, 80);    // 打开灯泡
    analogWrite(LEDPIN2, 80);    // 打开灯泡
    analogWrite(LEDPIN3, 80);    // 打开灯泡
    analogWrite(LEDPIN4, 80);    // 打开灯泡

}
void lightdown()
{
    digitalWrite(LEDPIN1, LOW);
    digitalWrite(LEDPIN2, LOW);
    digitalWrite(LEDPIN3, LOW);
    digitalWrite(LEDPIN4, LOW);

}
int getlight()
{
    int k  = analogRead(CHECKIN1);

    SerialUSB.println(k);
    return k;
}
int get_IR_data()
{
    int b = digitalRead(CHECKIN2);
    SerialUSB.println(b);
    return b;
}
void automode()
{
    if(getlight()>=400)
    {
        IntoRobot.publish(LIGHT_STATUS_address,"1");
        if (get_IR_data()==0)
        lightup();
        else
        light_half_up();
    }
    else
    {
    IntoRobot.publish(LIGHT_STATUS_address,"0");
    lightdown();
    }
}

void HUMIDITY_print_function(uint8_t *payload, uint32_t len)
{

}

// IntoRobot.publish(LIGHT_STATUS_address,"1");
// IntoRobot.publish(LIGHT_STATUS_address,"0");
void setup()
{
    pinMode(D4,INPUT);
    SerialUSB.begin(115200);
    SerialUSB.println("hello world");
    pinMode(LEDPIN1, OUTPUT);    //初始化
    pinMode(LEDPIN2, OUTPUT);    //初始化
    pinMode(LEDPIN3, OUTPUT);    //初始化
    pinMode(LEDPIN4, OUTPUT);    //初始化
    //设备接收云平台的灯开关命令
    IntoRobot.subscribe(BUTTONS_address,NULL,buttons_function);
    IntoRobot.subscribe(ITENSITY_DATA_address,NULL,HUMIDITY_print_function);
}
void loop()
{
   int a =map(getlight() ,0,1024,100,0);
   IntoRobot.publish(LIGHT,a);
    SerialUSB.println(getlight());
    if(autostate==0)
    {
        if(light_state ==1)
        lightup();
        else
        lightdown();
    }
    else if (autostate==1)
    {
        SerialUSB.println("state=1");
        automode();
    }
    delay(100);
}
```

**模型：**

![屏幕快照 2017-07-17 下午 5.00.16 (2).png](http://upload-images.jianshu.io/upload_2218072-c2cb025a94089a51.png?imageMogr2/auto-orient/strip|imageView2/2/w/1240)

比赛时间所限，只能粗略画出模型，打印出来组装。

## FAQ

Q：项目后期还有跟进吗？  
 A：暂时没有跟进的计划。创新点挺不错，但是否有商业应用价值，还有待验证。

## 总结

我们在这次比赛中并没有获奖。不过，比赛锻炼了赶代码和路演的能力，也让我提前体验了加班上线的感受，也认识了很多人，收获了好多纪念品。

## 参考与致谢

- 团队成员：林沛杰，黄岳峰，张梓宜
- [IntoRobot 云平台](https://www.intorobot.com/)

> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。

