# JTAG 状态机

JTAG 状态机的全称是 The JTAG Test Access Port (TAP) State Machine。它由两个部分组成：

- **DR(Data Register)**：数据寄存器。
- **IR(Instruction Register)**：指令寄存器

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20230815135556.png)

状态机随着 TCK(Test Clock) 的边沿运行，通过 TMS(Test Mode Select) 引脚的值控制其行为。假设状态机从测试逻辑复位开始，我们首先设置 TMS = 0 以进入运行测试 / 空闲状态，然后设置 TMS = 1 以开始选择路径。

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20230815145417.png)

JTAG 状态机通常包括以下几个状态：

- **Test-Logic-Reset (TLR)**：在这个状态下，所有的 JTAG 逻辑单元被重置，包括寄存器、状态机等。这是一个初始状态，通常在 JTAG 测试会话开始时进入。无论现在哪个状态，只要保持 TMS 至少 5 个周期高电平，就能恢复到这个模式。
- **Run-Test/Idle**：JTAG 状态机的默认状态。在这个状态下，IC 正常运行，而 JTAG 接口可以执行其他操作，如测试和配置。默认加载一个叫做 IDCODE 的指令（对应设备识别寄存器），如果没有识别到设备就默认加载 Bypass 指令。如果没有特定的操作要执行，JTAG 状态机将一直保持在这个状态。
- **Select-DR-Scan**：用于选择数据寄存器（Data Register）。临时状态，不做具体的操作。
- **Capture-DR**：对应的数据寄存器则将 Din 上对的数据并行加载到寄存器中来，为了后续的数据移位操作做准备。
- **Shift-DR**：数据寄存器执行移位的操作。数据位被逐位地推入或从数据寄存器中移出。
- **Exit-1-DR**：从 Shift-DR 状态过渡而来。它用于准备离开数据移位模式，并可能在寄存器链中传播数据。
- **Pause-DR**：IC 暂停了数据寄存器链中的数据传输。这允许外部系统处理传输的数据。
- **Exit-2-DR**：从 Pause-DR 状态过渡而来。它用于准备从数据寄存器链中退出，可能传播最后一组数据。
- **Update-DR**： 数据寄存器完成移位后，对数据进行「锁存更新」，便于输出
- **Select-IR-Scan**：类似于 Select-DR-Scan 状态，但用于选择指令寄存器（Instruction Register）。
- **Capture-IR**：指令寄存器执行捕获操作，也就是将 Din 上的数据并行加载到指令寄存器中来。
- **Shift-IR**：指令寄存器中的数据移位操作。
- **Exit-1-IR**：类似于 Exit-1-DR 状态，但用于从 Shift-IR 状态过渡而来。
- **Pause-IR**：类似于 Pause-DR 状态，但用于指令寄存器链中的数据。
- **Exit-2-IR**：类似于 Exit-2-DR 状态，但用于从 Pause-IR 状态过渡而来。
- **Update-IR**：指令寄存器完成移位后，对数据进行「锁存更新」，便于输出

- [JTAG 基本原理简介](https://file.elecfans.com/web1/M00/55/FF/pIYBAFs2KiqAJBckAAP1FHTbf5Y419.pdf)
