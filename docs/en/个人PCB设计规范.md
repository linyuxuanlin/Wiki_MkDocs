# Personal PCB Design Guidelines

## PCB Layout Guidelines

### Modular Layout

**By Functional Module**: Circuits that serve the same function (composed of discrete components to perform a specific task) should be placed close together.

**Based on Electrical Performance**:

- Digital Circuit Area: **Minimize interference and avoid generating interference.**
- Analog Circuit Area: **Minimize interference.**
- Power Drive Area: **May generate interference.**

### Layout Principles

- Prioritize placement of larger components.
- Place all components on the top layer (for easy soldering).
- Clock generators (e.g., crystals): Position them as close as possible to the devices that rely on that clock.
- Add decoupling capacitors at the power input of each module to filter out interference signals from the power source. Ensure they are placed as close as possible to the power supply module.
- Add discharge diodes (e.g., 1N4148) to relay coil connections.

## PCB Routing Guidelines

### Routing Principles

- Avoid running lines parallel to each other.
- Avoid leaving one end of a line floating (which could create antenna effects).
- Keep the total length of traces as short as possible.
- Ensure trace corners have angles greater than 90°.
- Follow the "3W" rule: When the center-to-center distance between traces is at least 3 times the trace width, it can maintain 70% of the electric field without mutual interference.
- Minimize loops in routing; try to avoid creating circular paths.
- Reserve test points at critical signal locations.
- Ensure consistent lead widths on both sides of component pads (use teardrop feature).
- Enable the "teardrop" feature after completing routing (for aesthetics and improved EMC).
- **Do not place vias on component pads** (SMT can lead to solder bridging).
- Avoid running traces or copper pours under microcontroller chips.

### Routing Sequence

1. Power lines
2. General signal traces
3. Ground planes (copper pours)

When routing a PCB, it's common to start with the power lines. In most cases, power lines need to be **short, thick, direct, and have fewer vias**, giving them the highest priority.

After routing the general signal traces, the final step is to establish copper pours. For typical double-layer boards, copper pours are typically set to **ground**.

### Rule Settings

**Trace Width**:

- Power lines: **30-50** mil
- Signal lines: **12** mil

**Via Sizes**:

- Inner diameter: **0.45** mm
- Outer diameter: **0.75** mm

**Copper Pour Connections**:

Use the "Direct" method

(Slightly unclear; further clarification needed when time permits)

- Copper pour safety clearance: **10** mil
- Attribute: **GND**
- Copper pour selection: **Pour Over All Same Net Objects**
- Remove dead copper: **Remove Dead Copper**

**Character Sizes**:

- Minimum line width: **6** mil
- Minimum character height: **32** mil

Characters printed on the board that are smaller than these values may appear unclear.

**Relationship Between PCB Trace Width and Current**:


```markdown
| Trace Width/Copper Thickness | 70µm (2 oz) | 50µm (1.5 oz) | 35µm (1 oz) |
| :--------------------------: | :---------: | :-----------: | :---------: |
| 2.50mm (98mil)              |    6.00A    |    5.10A     |   4.50A    |
| 2.00mm (78mil)              |    5.10A    |    4.30A     |   4.00A    |
| 1.50mm (59mil)              |    4.20A    |    3.50A     |   3.20A    |
| 1.20mm (47mil)              |    3.60A    |    3.00A     |   2.70A    |
| 1.00mm (40mil)              |    3.20A    |    2.60A     |   2.30A    |
| 0.80mm (32mil)              |    2.80A    |    2.40A     |   2.00A    |
| 0.60mm (24mil)              |    2.30A    |    1.90A     |   1.60A    |
| 0.50mm (20mil)              |    2.00A    |    1.70A     |   1.35A    |
| 0.40mm (16mil)              |    1.70A    |    1.35A     |   1.10A    |
| 0.30mm (12mil)              |    1.30A    |    1.10A     |   0.80A    |
| 0.20mm (8mil)               |    0.90A    |    0.70A     |   0.55A    |
| 0.15mm (6mil)               |    0.70A    |    0.50A     |   0.20A    |

A general 15% margin is usually recommended.

## References and Acknowledgments

- [JLCPCB PCB Manufacturing Capability](https://www.sz-jlc.com/portal/vtechnology.html)
- [What's the Appropriate Trace Width for PCB Routing?](https://mp.weixin.qq.com/s?__biz=MzI4NDAwOTgzMw==&mid=2650625562&idx=1&sn=29d145ed112c23464ac74bfeeb212aa1&chksm=f388021cc4ff8b0a2e1701726340afb0b60738f8ae448e8f8d0c3b0dee0758a89fe954433011&scene=126&sessionid=1607139114&key=f9ff6c6605e545f8046d3325f95411b620e846faa9864c6589c1a6b69f1ce0d00f26f595bea2995ab23bf54727f1c9f219239f6d2c840605db0dac7f884190fcd2134daa54c87cbf6f249bfa9c29f8ddd39b20d50744335451d3acb3466ebcc44d8918dba7d35a22569e0b7a780088439cf35fe0ff5ea9bddbafef36c64bfd3f&ascene=1&uin=MTk5MDUwOTA0Mg%3D%3D&devicetype=Windows+10+x64&version=6300002f&lang=zh_CN&exportkey=A1GQK2ccX%2BvsjA6n1%2BOfSNU%3D&pass_ticket=kq2QkQn3wCfkzXnTBMjx4zRHCHr2TH9lX0mMASdXW7ugPzIdfcJaNdCq2VwvOmMs&wx_header=0)

> Original: <https://wiki-power.com/>
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.
```

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.