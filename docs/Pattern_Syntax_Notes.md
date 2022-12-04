---
id: Pattern_Syntax_Notes
title: Pattern Syntax Notes 🚧
---

## Meanings of Pattern Data Characters

Input Drive:

- `0`: Drive low.
- `1`: Drive high.
- `2`: High voltage (if supported).
- `D`: Drive ADS (Alternate Data Source) (retrieve data from the ADS).
- `I`: Drive inverse ADS, (retrieve data from the ADS and invert).

Output Compare:

- `L`: Expect low.
- `H`: Expect high.
- `M`: Expect midband.
- `V`: Expect valid.
- `X`: Mask.
- `W`: Window strobe continue.
- `E`: Expect ADS (read expect data from the ADS).
- `C`: Expect inverse ADS (read expect data from the ADS and invert).
- `-`: Repeat previous state.
