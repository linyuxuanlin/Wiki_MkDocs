---
id: STM32麦轮小车
title: STM32 麦轮小车
---

## 背景

野狼队在寒假准备来一场校内赛，把大一新生分了几个队，分别做自己的小车，最终会有类似踢足球的比赛。为了能有良好的操控性和灵活度，我打算给小车直接上麦轮。

## STM32 基础

模块知识：

- 外部中断
- 串口
- SysTick 定时器
- TIM 高级定时器
- 驱动舵机
- 驱动电机，实现调速
- 编码器
- 遥控（PS2）

## 运动学原理

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/麦轮。png)

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/麦轮角度。png)

这是我自己推导出来的麦轮算法，翻译成代码是这样的：

```c
void M_process(s16 x,s16 y) { //传入左摇杆 L(x,y) 坐标
    const double Pi = 3.14159265359;
    u16 Vm=7200,r=127; //定义最大速度和坐标圆的半径
    s16 V1,V2,V3,V4,angle; //定义四电机速度，直线 OL 与 x 轴所成角度
    s16 new_x,new_y; //定义中间变量

    //纠正算法，如果 L 坐标超出了坐标圆，那么取在坐标圆上的点。联立圆和正比例函数的方程
    if(pow(x,2)+pow(y,2)>pow(r,2)) {
        new_x=sqrt((pow(x,2)*pow(r,2))/(pow(x,2)+pow(y,2)));
        new_y=sqrt((pow(y,2)*pow(r,2))/(pow(x,2)+pow(y,2)));
        if(x>0) x=new_x ; else x=-new_x;
        if(y>0) y=new_y ; else y=-new_y;
    }

    Vm=(sqrt(pow(x,2)+pow(y,2))/r)*Vm; //按 OL 长度比例取速度
    angle=atan(abs(y)/abs(x))*(180/Pi); //计算直线 OL 与 x 轴所成角度
    if(x==0&&y==0) { //原点
        V1=0; V2=0; V3=0; V4=0;
    }
    if(y==0) { //x 轴上
        if(x>0){
            V1=Vm; V2=-Vm; V3=-Vm; V4=Vm;
        }else{
            V1=-Vm; V2=Vm; V3=Vm; V4=-Vm;
        }
    }
    if(x==0) { //y 轴上
        if(y>0) {
            V1=Vm; V2=Vm; V3=Vm; V4=Vm;
        }else{
            V1=-Vm; V2=-Vm; V3=-Vm; V4=-Vm;
        }
    }
    if(x>0&&y>0) { //第一象限
        V1=Vm;
        V2=(Vm/45)*angle-Vm;
        V3=(Vm/45)*angle-Vm;
        V4=Vm;
    }
    if(x<0&&y>0) { //第二象限
        V1=(Vm/45)*angle-Vm;
        V2=Vm;
        V3=Vm;
        V4=(Vm/45)*angle-Vm;
    }
    if(x<0&&y<0) { //第三象限
        V1=-Vm;
        V2=-(Vm/45)*angle+Vm;
        V3=-(Vm/45)*angle+Vm;
        V4=-Vm;
    }
    if(x>0&&y<0) { //第四象限
        V1=-(Vm/45)*angle+Vm;
        V2=-Vm;
        V3=-Vm;
        V4=-(Vm/45)*angle+Vm;
    }

    //驱动电机
    M1_run(V1);
    M2_run(V2);
    M3_run(V3);
    M4_run(V4);
}
```

代码不算精简。因 PS2 手柄还没送到，所以暂时只有左摇杆的算法（任意方向移动），待测试后再加上右摇杆（自转）。就先这样吧。

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/小车预览%20.jpg)

## FAQ

待补充。

## 总结

待补充。

## 参考与致谢

- [Mecanum Wheel Robot - Bluetooth Controlled](https://www.instructables.com/id/Mecanum-wheel-robot-bluetooth-controlled/)
- [Design of Omnidirectional Mobile Platform Control System Based on STM32 CAN Bus Control](https://image.hanspub.org/Html/11-1540843_22169.htm)



> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。

