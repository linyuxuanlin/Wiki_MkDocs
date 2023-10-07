# EMC Design between Signal Ground and Chassis Ground

Usually, in the PCB design, a high-voltage capacitor (1~100nF/2kV) and a large resistor (1MΩ) are connected in parallel between the signal ground and the chassis ground to improve EMC performance:

![](https://f004.backblazeb2.com/file/wiki-media/img/20220620162528.png)

The capacitor is used to pass AC and block DC. From the perspective of EMI, it can prevent high-frequency interference generated inside the circuit from radiating as an antenna by flowing into the ground through the chassis; from the perspective of EMS, it can suppress the transient common-mode voltage difference between the high-frequency interference source and the circuit, as sometimes the circuit cannot be directly connected (the GND after 220VAC passes through the rectifier bridge cannot be directly connected to the chassis ground) or direct connection is not safe enough.

The resistor is used to discharge the charge and prevent ESD from damaging the circuit. If only the capacitor is connected between the signal ground and the chassis ground, the signal ground will be floating. During ESD testing, the signal ground will gradually accumulate high-voltage charges. Once it exceeds the voltage that the nearest ground between the two grounds can withstand, arcing will occur, generating a large current within a few nanoseconds, damaging the circuit. By connecting this resistor in parallel, the charge can be slowly discharged.

## Reference and Acknowledgment

- [What is the use of a resistor-capacitor connection between PCB ground and metal chassis?](https://mp.weixin.qq.com/s/vAdoDyBed4uIfISrP0Zeyw)

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.