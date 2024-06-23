# 使用 SKiDL 画 PCB

## 环境配置

```sh
winget install KiCad.KiCad  # 目前使用8.0.3版本
pip install git+https://github.com/devbisme/skidl@development # 要使用新版，并在程序头加入 set_default_tool(KICAD8)
```

环境变量：

```
set KICAD8_SYMBOL_DIR=C:\Users\power\AppData\Local\Programs\KiCad\8.0\share\kicad\symbols
```

发现上面的代码没效果，要手动配置用户变量

## 参考代码

```py
from skidl import *

#print(lib_search_paths)
set_default_tool(KICAD8)


# 创建网络
vcc = Net('VCC')    # 电源
gnd = Net('GND')    # 地
btn = Net('BTN')    # 按键信号
led = Net('LED')    # LED 控制信号

# 按键电路
button = Part('Switch.kicad_sym', 'SW_Push', footprint='Button_Switch_SMD:Nidec_Copal_SH-7040B')
pullup_resistor = Part('Device.kicad_sym', 'R', value='10k', footprint='Resistor_THT:R_Array_SIP4') #R_0_1
button[1] += gnd
button[2] += btn
pullup_resistor[1] += vcc
pullup_resistor[2] += btn

# LED 电路
#led_resistor = Part('Device.kicad_sym', 'R', value='330', footprint='Resistor_SMD:R_0603')
#led_diode = Part('Device.kicad_sym', 'LED', footprint='LED_SMD:LED_0805')
#led_resistor[1] += vcc
#led_resistor[2] += led
#led_diode[1] += led
#led_diode[2] += gnd

# 生成网表
generate_netlist()
print("Netlist generated successfully.")
```

然后在 PCB 页面导入网表
