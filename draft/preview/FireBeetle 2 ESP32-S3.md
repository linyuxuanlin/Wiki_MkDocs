# FireBeetle 2 ESP32-S3

- 基于 ESP32-S3-WROOM-1-N16R8 模组，支持 AI 加速
- 16MB Flash 和 8MB PSRAM
- 拥有强大的神经网络运算能力和信号处理能力，适用于图像识别、语音识别等项目。
- 附带了一个 OV2640 摄像头，拥有 200 万像素和 68° 视场角，最高支持 1600x1200 分辨率
- 板载 GDI 屏幕接口，解决使用屏幕时的接线烦恼，集成电源管理功能，支持锂电池充电和硬件开关机。
- 支持 2.4 GHz Wi-Fi 和 Bluetooth 5 (LE) 双模通讯，支持蓝牙 Mesh 和乐鑫 Wi-Fi Mesh，支持 Matter 协议
- 可以使用 Arduino IDE、ESP-IDF、MicroPython 进行编程

基本参数：

- 工作电压： 3.3V
- Type-C 输入电压： 5V DC
- VCC 输入电压：5V DC
- 最大充电电流： 1A

硬件信息：

- 处理器：Xtensa® 双核 32 位 LX7 微处理器
- 主频：240 MHz
- SRAM：512KB
- ROM：384KB
- Flash：16MB
- PSRAM: 8MB
- RTC SRAM：16KB
- USB: USB 2.0 OTG 全速接口

接口引脚：

- 数字 I/O x26
- LED PWM 控制器 8 个通道
- SPI x4
- UART x3
- I2C x2
- I2S x2
- 红外收发器：发送通道 x5、接收通道 x5
- 2 × 12 位 SAR ADC， 20 个通道
- DMA 控制器，5 个接收通道和 5 个发送通道

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/202308121952628.png)

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20230811172428.png)

ref：

- https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package_esp32_index.json - esp32 - DFRobot FireBeetle 2 ESP32-S3
- CDC: 当您选择 Disabled 时,串口为 RX(44)、TX(43)，如果您需要通过 USB 在 Arduino 监视器上打印，您需要选择 Enable
- GDI 显示屏接口，使用 18pin-FPC
- ESP32-S3 屏幕驱动: https://wiki.dfrobot.com.cn/_SKU_DFR0975_FireBeetle_2_Board_ESP32_S3_Advanced_Tutorial#target_1
- 应用参考：https://wiki.seeedstudio.com/xiao_esp32s3_speech2chatgpt/

想法：

1. +TFT 屏幕，按钮和摄像头采集图像，交给 AI 重绘制，输出到 TFT 屏幕上。（在本地跑 stable diffusion?

- 采集图像
- 通过网络发送到远程主机（或直接使用 mj api）

1. 人脸识别：https://www.hackster.io/mauriciobarroso/face-detection-with-mtcnn-and-tensorflow-lite-for-esp32-s3-30b242
2. 当网卡用![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/202308121947216.png)
3. 延时摄像机： https://www.hackster.io/pradeeplogu0/live-security-camera-with-unihiker-firebeetle-2-esp32s3-5d478e
4. 人脸识别：https://www.hackster.io/mauriciobarroso/face-detection-with-mtcnn-and-tensorflow-lite-for-esp32-s3-30b242
5. Camera Bot telegram: https://www.hackster.io/pradeeplogu0/camera-bot-using-firebeetle-esp32-s3-5147e7
6. TinyML 物品分类识别：https://www.hackster.io/mjrobot/tinyml-made-easy-image-classification-cb42ae

疑难解答：

- 如果烧不进程序：按住 boot 上电后松开
- 局域网内访问失败：检查是否为访客网络，有 AP 隔离
- 没有画面：要点 Start Stream
