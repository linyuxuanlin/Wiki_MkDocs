# Pattern Syntax Notes 🚧

> This post was originally written in English.

A digital pattern file contains mainly 3 parts:
**Header Statement**, **Setup Statement** and **Pattern Module**. (**Preprocessing statements** and **Comments** are optional).

Below is an mostly used example pattern file in `.atp` format:

```atp
// example.atp
digital_inst = HSDMQ;
opcode_mode = single;
pinmap_workbook = "..\xx.igxl";
import tset tset1 ;
instruments = {
        (TIC_DATABUS):DigCap 32:format=twos_complement:auto_trig_enable;
}
vm_vector cpr_test($tset TIC_CLK, TIC_ACK, TIC_REQ_A, TIC_DATABUS)
{
cpr_test:
 > tset1 0 X 0 0 .d000000 ;
repeat 100
 > tset1 0 X 1 1 .rFFFFFF ;
 > tset1 0 X 0 0    .X    ;
 ((TIC_DATABUS):DigCap = Store)
 > tset1 0 X 0 0    .V 	  ; // capture
HALT
 > tset1 0 X 0 0  d000000 ; // end
}
```

## Header Statement

**Header Statement** contains these statements: digital instrument, pin map, compiler control, import tset or label. Here is an example:

```
digital_inst = HSDMQ;           // Digital instrument statement
opcode_mode = single;           // Compile statement
import tset tset1, tset1;       // import Time sets
import subr xxx;                // import Subroutines
```

Frequently used parameters:

- Digital Instrument Statements
  - **digital_inst**: `hsdm`(HSD1000, UltraPin800), `hsdmq`(UltraPin1600), `hsdp`(UltraPin2200) ...
- Pin Map Specifications:
  - **pinmap_workbook**: IG‑XL workbook name, such as `"xxx.igxl"`
  - **sheetname**: Pin Map sheet name, such as `"pinmap"`
- Compiler Control Statements
  - **compressed**: `yes` or `no`
  - **opcode_mode**: `single` or `dual` or `quad`(UltraPin1600), every 1/2/4 vectors can include an opcode.
  - **save_comments**: `yes` or `no`
  - **version**: such as `V1.0`
- Tset and Label
  - **Tset**: `import tset tset1, tset2, ... ;`
  - **Label**: `import label label1, label2, ... ;`

## Setup Statement

**Setup Statement** contains pin setup, instruments, scan pin.

```
pin_setup = {
    gpio_1    2x;                                           //Pin setup: gpio_1 set to 2X mode
}
instruments = {
vcc:DCVS 1;                                                 // DCVS instrument
    tdo:DigCap 32:format=twos_complement:auto_trig_enable;  // DigCap instrument
}
scan_pins = {
    tdi, tdo;                                               // tdi - scan in, tdo - scan out
}
```

Frequently used parameters:

- Pin State Characters and Microcodes
  - **Pin State Characters**: `0`(Drive Low), `1`(Drive High), `2`(Drive High Voltage only for UP800), `L`(Expect Low), `H`(Expect High), `M`(Expect Mid-band), `V`(Expect Valid), `X`(Mask), `W`(Window Strobe), `D`(Drive ADS (DigSrc/MTO)), `I`(Drive inverse ADS (DigSrc/MTO)), `E`(Expect ADS (DigSrc/MTO)), `C`(Expect inverse ADS (DigSrc/MTO)), `-`(Repeat previous state).
  - **DigCap Microcodes**: `Trig`(Start a capture), `Store`(Store a data sample), `Trig, Store`(Combination of Trig and Store), `Store, Inst_Cond_Strobe`(Store and gate the internally generated `condition` signal to be acted on).

## Pattern Module

A **pattern module** contains pin list and a set of vectors. There are 2 types of it: vector memory (VM) and memory (SRM):

```
vm_vector [module-name] (pin-list)
{ vectors }

srm_vector [module-name] (pin-list)
{ vectors }
```

At least 1 pattern module is required in a pattern file. If more than 1, their colummns and pin lists need to be the same.

Frequently used parameters:

- pin-list
  - **Pin Items**: `pin-or-group[.modifier][:radix]`, radix could be `:S`(Symbolic, default), `:B`(Bin), `:D`(Dec), `:O`(Oct), `:H`(Hex)
- Label: tbd
