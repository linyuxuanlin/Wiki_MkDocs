## TIC 是什么

**TIC（Test Interface Controller）** 是一种测试协议，

**TIC** 是由 **AMBA（Advanced Microcontroller Bus Architecture，高级微控制器总线架构）** 规范定义的。这是嵌入式微控制器的片上通信标准，它包含了三类总线：

- **AHB**: the Advanced High-performance Bus，高性能总线
- **ASB**: the Advanced System Bus，系统总线
- **APB**: the Advanced Peripheral Bus，外设总线

AMBA 的理念是，允许对系统中的单个模块进行隔离测试，每个模块的测试只依赖于总线接口。因此需要由一种测试方法，以实现对没有连接到总线的外设上的输入输出进行测试。
