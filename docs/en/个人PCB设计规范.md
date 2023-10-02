# Personal PCB Design Standards

## PCB Layout Standards

### Modular Layout

**By Function Module**: Circuits that perform the same function (modules composed of discrete components that achieve specific functions) should be placed as close together as possible.

**By Electrical Performance**:

- Digital Circuit Area: **Sensitive to interference and generates interference**
- Analog Circuit Area: **Sensitive to interference**
- Power Drive Area: **Generates interference**

### Layout Principles

- Larger components should be prioritized in placement
- All components should be placed on the top layer (for ease of soldering)
- Clock generators (such as crystal oscillators) should be placed as close as possible to the components that use them
- Add decoupling capacitors at the power input of each module: to filter out interference signals from the power supply. Note that they should be placed as close as possible to the power supply module.
- Add discharge diodes (such as 1N4148) at the relay coil.

## PCB Wiring Standards

### Wiring Principles

- Avoid parallel lines
- Avoid leaving one end floating (which may cause antenna effects)
- Keep the total length of the wires as short as possible
- The bending angle of the wires should be greater than 90°
- **3W** Rule: When the center distance between the wires is not less than 3 times the wire width, 70% of the electric field can be kept from interfering with each other.
- The minimum loop rule: try to avoid forming loops in the wiring
- Test points can be reserved at critical signal points
- The width of the leads on both sides of the component solder pads should be the same (use the teardrop function)
- After completing the wiring, turn on the teardrop function (to increase aesthetics and enhance EMC)
- **Do not drill holes on the component solder pads** (SMT is prone to solder bridging and virtual soldering)
- Try not to run wires or copper under the microcontroller chip.

### Wiring Order

1. Power lines
2. General signal lines
3. Ground lines (copper pour)

When wiring the PCB, we generally start with the power lines. In most cases, the power lines require **short, thick, straight, and fewer holes**, so they have the highest priority in wiring.

After completing the wiring of the general signal lines, we need to pour copper. For ordinary double-layer boards, the copper attribute is generally set to **ground**.

### Rule Settings

**Wire Width**:

- Power lines: **30-50** mil
- Signal lines: **12** mil

**Hole Size**:

- Inner diameter: **0.45** mm
- Outer diameter: **0.75** mm

**Copper Pour Connection**:

Use the Direct method

(some explanations are unclear, to be supplemented when there is time)

- Safe spacing for copper pour: **10** mil
- Attribute: **GND**
- Copper pour selection: Pour Over All Same Net Objectc,
- Remove dead copper: Remove Dead Copper

**Character Size**:

- Minimum line width: **6** mil
- Minimum character height: **32** mil

If the values are smaller than the above, the characters printed on the board may not be clear.

**Relationship between PCB line width and current**:

(No information provided)

| Trace Width/Copper Thickness | 70µm (2 oz) | 50µm (1.5 oz) | 35µm (1 oz) |
| :--------------------------: | :---------: | :-----------: | :---------: |
| 2.50mm (98mil)               |    6.00A    |     5.10A     |    4.50A    |
| 2.00mm (78mil)               |    5.10A    |     4.30A     |    4.00A    |
| 1.50mm (59mil)               |    4.20A    |     3.50A     |    3.20A    |
| 1.20mm (47mil)               |    3.60A    |     3.00A     |    2.70A    |
| 1.00mm (40mil)               |    3.20A    |     2.60A     |    2.30A    |
| 0.80mm (32mil)               |    2.80A    |     2.40A     |    2.00A    |
| 0.60mm (24mil)               |    2.30A    |     1.90A     |    1.60A    |
| 0.50mm (20mil)               |    2.00A    |     1.70A     |    1.35A    |
| 0.40mm (16mil)               |    1.70A    |     1.35A     |    1.10A    |
| 0.30mm (12mil)               |    1.30A    |     1.10A     |    0.80A    |
| 0.20mm (8mil)                |    0.90A    |     0.70A     |    0.55A    |
| 0.15mm (6mil)                |    0.70A    |     0.50A     |    0.20A    |

Generally, a margin of 15% should be reserved.

## References and Acknowledgments

- [JLCPCB PCB Process Capability Range Description](https://www.sz-jlc.com/portal/vtechnology.html)
- [What is the Appropriate Trace Width for PCB Routing? We Have Sorted it Out for You!](https://mp.weixin.qq.com/s?__biz=MzI4NDAwOTgzMw==&mid=2650625562&idx=1&sn=29d145ed112c23464ac74bfeeb212aa1&chksm=f388021cc4ff8b0a2e1701726340afb0b60738f8ae448e8f8d0c3b0dee0758a89fe954433011&scene=126&sessionid=1607139114&key=f9ff6c6605e545f8046d3325f95411b620e846faa9864c6589c1a6b69f1ce0d00f26f595bea2995ab23bf54727f1c9f219239f6d2c840605db0dac7f884190fcd2134daa54c87cbf6f249bfa9c29f8ddd39b20d50744335451d3acb3466ebcc44d8918dba7d35a22569e0b7a780088439cf35fe0ff5ea9bddbafef36c64bfd3f&ascene=1&uin=MTk5MDUwOTA0Mg%3D%3D&devicetype=Windows+10+x64&version=6300002f&lang=zh_CN&exportkey=A1GQK2ccX%2BvsjA6n1%2BOfSNU%3D&pass_ticket=kq2QkQn3wCfkzXnTBMjx4zRHCHr2TH9lX0mMASdXW7ugPzIdfcJaNdCq2VwvOmMs&wx_header=0)

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.