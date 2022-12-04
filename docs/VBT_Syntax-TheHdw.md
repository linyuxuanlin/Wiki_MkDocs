---
id: VBT_Syntax-TheHdw
title: VBT Syntax - TheHdw 🚧
---

**TheHdw** is an object to accesses properties and methods relating to test system hardware.

## TheHdw.DCVI

### Pins

```vb
TheHdw.DCVI.Pins(PinList)
```



## TheHdw.PPMU

🚧

## TheHdw.Digital

### ApplyLevelsTiming

To load the level and timing data.

#### Usage

```VB
TheHdw.Digital.ApplyLevelsTiming(ConnectAllPins, LoadLevels, LoadTiming, RelayMode, InitPinsHi, InitPinsLo, InitPinsHiZ, PinLevelsSheet, DCCategory, DCSelector, TimeSetSheet, ACCategory, ACSelector, EdgeSetSheet)
```

#### Parameters

- **ConnectAllPins**: Optional Boolean, default as `False`.
  - `True`: Connect all device pins.
  - `False`: Do not connect.
- **LoadLevels**: Optional Boolean, default as `False`.
  - `True`: Load level values.
  - `False`: Do not Load.
- **LoadTiming**: Optional Boolean, default as `False`.
  - `True`: Load timing values.
  - `False`: Do not Load.
- **RelayMode**: Optional `tlRelayMode`, default as `tlUnpowered`. Controls the relays' hot switching.
  - `tlPowered`: Hot switching. Not power down the DUT before setting levels and connecting.
  - `tlUnpowered`: Avoid hot switching. Power down the DUT before setting levels and connecting.
- **InitPinsHi**: Optional String. Set the pins start with high driver state.
- **InitPinsLo**: Optional String. Set the pins start with low driver state.
- **InitPinsHiZ**: Optional String. Set the pins start with impedance driver state.
- **PinLevelsSheet**: Optional String. A Pin Levels sheet.
- **DCCategory**: Optional String.
- **DCSelector**: Optional String.
- **TimeSetSheet**: Optional String.
- **ACCategory**: Optional String.
- **ACSelector**: Optional String.
- **EdgeSetSheet**: Optional String.
