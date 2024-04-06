# Test Interface 与 TIC 基础

在半导体测试中，**TIC（Test Interface Controller，测试接口控制器）** 是一个总线主控器，它遵循的是 **AMBA（Advanced Microcontroller Bus Architecture，高级微控制器总线架构）** 规范中的 **Test Interface** 协议。AMBA 是嵌入式微控制器的片上通信标准，囊括三类总线协议：

- **AHB**（the Advanced High-performance Bus，高性能总线）
- **ASB**（the Advanced System Bus，系统总线）
- **APB**（the Advanced Peripheral Bus，外设总线）

因 AMBA 的理念在于对系统中的单个模块进行隔离测试，每个模块的测试仅依赖于总线接口，需要一种测试方法来对未连接到总线的外设的输入输出进行测试。

![](https://media.wiki-power.com/img/202308262214877.png)

这种测试方法可通过 Test Interface 实现。它采用简单的三线握手机制，以控制 Vector 的读写；同时，它使用 **EBI（External Bus Interface，外部总线接口）** 作为数据路径，以将外部的 Vector 导入内部总线。

## Test Interface 的引脚

![](https://media.wiki-power.com/img/202308262225257.png)

由上图可见，Test Interface 的引脚由三个部分组成：

- 一个时钟引脚 **TCLK**
- 三个控制引脚 **TREQA**，**TREQB** 和 **TACK**
- 一个 32 位的测试总线 **TBUS[31:0]**

在最小配置下，Test Interface 只需要 TREQA 和 TACK 作为 **专用引脚**，用于控制测试模式的进入与退出。其他引脚可以通过复用设备上的引脚来实现。

**TREQA/TREQB（Test Bus Request，测试总线请求）** 是 **输入** 信号。在系统正常运行其间，TREQA 用于请求进入测试模式，从而允许 Vector 被加载进来。在测试过程中，TREQA 与 TREQB 一同使用，以指示下一个 Cycle 将使用的 Vector 类型。

**TACK（Test Bus Acknowledge，测试总线确认）** 是一个 **输出** 信号，用于表示总线的状态，也指示一个测试项何时完成。当 TACK 输出低电平时，表示当前 Vector 需要更多时间，直到 TACK 变为高电平。只有当 TACK 为高电平时，TREQA/TREQB 才会对外部控制信号进行读取。

**TCLK（Test Clock）** 是一个时钟信号输入。Test Interface 的测试时钟是由外部提供的。在普通模式与测试模式之间切换时，要求 TCLK 时钟无毛刺。

**TBUS[31:0]（Test Bus）** 是一个 32 位双向测试接口总线。在输入状态下，它用来传入 Vector Address、Control 信息和执行 Write 操作；在输出状态下，可以用来执行 Read 操作。当需要改变 TBUS 输入输出状态时，测试总线协议确保提供一个用于换向的 Cycle。

当系统正常运行时， Test Interface 受三线控制的真值表如下：

| TREQA | TREQB | TACK | 状态                     |
| ----- | ----- | ---- | ------------------------ |
| 0     | 0     | 0    | 正常运行，未进入测试模式 |
| 1     | 0     | 0    | 请求进入测试模式         |
| 0     | 1     | 0    | 预留，用于外部主机请求   |
| -     | -     | 1    | 已进入测试模式           |

最初，TREQA 为低电平，表示尚未进入测试模式。当 TREQA 被设置为高电平时，将请求进入测试模式。接着，当 TACK 输出高电平时，表示 TIC 允许进入测试模式。此时，TCLK 成为内部时钟源。一旦进入测试模式，三线上的值与对应的系统状态如下：

| TREQA | TREQB | TACK | 状态                              |
| ----- | ----- | ---- | --------------------------------- |
| -     | -     | 0    | 当前操作尚未完成                  |
| 1     | 1     | 1    | Address/Control/TurnAround Vector |
| 1     | 0     | 1    | Write Test Vector                 |
| 0     | 1     | 1    | Read Test Vector                  |
| 0     | 0     | 1    | 退出测试模式                      |

接下来可将 TREQB 设置为高电平，以加载 Address Vector。随后可进行读写操作。当需要退出测试模式时，应先传入一个 Address Vector，确保所有内部传输都已经完成。随后将 TREQA 与 TREQB 都设置为低电平，表示退出测试模式。最终，TACK 会输出低电平，表示已经退出测试模式。

## Vector 的类型

Test Interface 中，Vector 有 5 种类型：

- **Address Vector**：声明地址的 Vector
- **Write Test Vector**：写入的 Vector（0/1）
- **Read Test Vector**：读取的 Vector（L/H）
- **Control Vector**：控制的 Vector
- **TurnAround Vector**：换向 Vector

其中，Address/Control/TurnAround Vector 的触发，均由相同的 TREQA/TREQB 共同值决定。判断 Vector 的类型，可以参考以下的规则：

- 只出现单条 Address/Control/TurnAround Vector：它就是 Address Vector。
- 出现连续一串 Address/Control/TurnAround Vector：除了最后一条是 Control Vector，其他全是 Address Vector。
- 一条 / 多条 Read Vector 之后：总会跟一个 TurnAround Vector。（在 ASB 中是单个，AHB 中需要两个）

除此之外，**Burst Vector** 是将多个 Write/Read Test Vector 串在一起（注意是同一种类型串，不是混着串）。这样只需要应用一次 Address，可以提高测试速度。这个 Address 可以是一直保持静态的（所有 Vector 使用最初传入的同一个 Address），也可以是递增的 Address（取决于 TIC 是否有已启用的 Address 递增器）。在没有递增器的情况下，将默认采用静态 Address。

### Address Vector

在任何 Read/Write 操作之前，必须先传入 Address Vector。它遵循以下规则：

- 必须将 TREQA/TREQB 都置 1，以指示下一个 Cycle 为 Address Vector。
- 在下一个 Cycle 时，Address 被加载到 TBUS[31:0] 上。此时 TREQA/TREQB 上的值将共同决定下一个 Cycle 的状态。

在某些高速信号系统中，可能需要连续加载多个 Address Vector（增加足够的时间让 Address 从外部传输到内部 Address 总线）。在这种情况下 TIC 会在第一个 Address Vector 的 TACK 输出 0，以强制加载第二个 Address Vector Cycle。

### Control Vector

Control Vector 总会跟在一条或一串 Address Vector 之后，它用于更新 TIC 内部的 Control 信息。它遵循以下的规则：

- 必须将 TREQA/TREQB 都置 1，以指示下一个 Cycle 为 Address Vector。
- 在下一个 Cycle 时，Address 被加载到 TBUS[31:0] 上。此时 TREQA/TREQB 都仍然保持为 1，Control Vector 将在下一个 Cycle 中出现。
- 在接下来一个 Cycle 时，Control 信息将被加载到 TBUS[31:0] 上。此时 TREQA/TREQB 上的值将决定下一个 Cycle 的状态。

如果需要设置一个无效的 Control Vector，可以将其第 0 位设置为 0，这样就可以保留但不应用 Control Vector 的信息。

### Write Test Vector

在成功进入测试模式并指定 Address 后，就可以进行读写操作了。Write 操作使用的 Address 由前面的 Address Vector 定义。Write Test Vector 可以跟随在以下 Vector 之后：

- 单一条 Address Vector。
- Address/Control Vector 组成的序列。
- 另一条 Write Test Vector。组成一串 Write Burst。
- 单次/多次 Read 操作后的 TurnAround Vector。

当传输状态需要延迟时，TACK 会变为低电平。在等待的这段时间内，TREQA/TREQB 需要变化以指定下一个 Vector 的类型，但在 TBUS[31:0] 执行的 Write 操作仍然需要持续，在此时不应进行 Read 操作。

### Read Test Vector

与 Write Test Vector 相似，Read 操作使用的 Address 取决于前面的 Vector，可以跟随在以下 Vector 之后：

- 单一条 Address Vector。
- Address/Control Vector 组成的序列。
- 另一条 Read Test Vector。组成一串 Read Burst。
- 单次/多次 Write 操作。

在单次或多次 Read 操作后，必须始终要有一个 TurnAround Vector，以防止外部 TBUS 信号发生总线冲突。

### TurnAround Vector

TurnAround Vector 可用于在 Write/Read 操作间切换时，改变 TBUS 传输的方向。在 Read 操作变为 Write 时，有必要插入 TurnAround Vector。这个操作不会写入新的 Address。

---

以上是 Test Interface 与 TIC 的一些基础知识。关于 TIC 在 AHB 上的具体运行情况，请参考下一篇文章 [**AHB 上的 TIC**](https://wiki-power.com/AHB%E4%B8%8A%E7%9A%84TIC) (撰写中……)。

## 参考与致谢

- _IHI0011 - ARM advanced microcontroller bus architecture (AMBA) specification.Rev 2.0_

> 原文地址：<https://wiki-power.com/>  
> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。
