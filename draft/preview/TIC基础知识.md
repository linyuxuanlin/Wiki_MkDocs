## TIC 是什么

**TIC（Test Interface Controller）** 是一种测试协议，

**TIC** 是由 **AMBA（Advanced Microcontroller Bus Architecture，高级微控制器总线架构）** 规范定义的。这是嵌入式微控制器的片上通信标准，它包含了三类总线：

- **AHB**: the Advanced High-performance Bus，高性能总线
- **ASB**: the Advanced System Bus，系统总线
- **APB**: the Advanced Peripheral Bus，外设总线

AMBA 的理念是，允许对系统中的单个模块进行隔离测试，每个模块的测试只依赖于总线接口。因此需要有一种测试方法，对没有接到总线的外设上的输入输出进行测试。

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/202308262214877.png)

TIC 总线控制模块就可以实现这样的功能。它可以将外部的 Vector 导入内部总线进行传输。TIC 采用简单的三线握手机制控制 Vector 的读写，外加使用 **EBI（External Bus Interface，外部总线接口）** 作为数据路径，提供双向高速 32 位接口以加载 Vector 数据。

## TIC 的引脚

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/202308262225257.png)

由上图可见，TIC 的引脚由三个部分组成：

- 一个时钟引脚 **TCLK**
- 三个控制引脚 **TREQA**，**TREQB** 和 **TACK**
- 一个 32 位的测试总线 **TBUS[31:0]**

TIC 最小只需要 TREQA 和 TACK 作为 **专用引脚**，来控制测试模式的进入与退出。其他引脚都可以通过复用设备上的引脚来实现。
