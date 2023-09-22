IG-XL digital pattern language

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

**Header Statement** is combimed with these statements: digital instrument, pin map, compiler control, import tset or label. Here is an example:

```
digital_inst = HSDMQ;               // Digital instrument statement
opcode_mode = single;               // Compile statement
import tset tset1;              // Time sets import statement
import subr PLL_Loop;               // Subroutines import statement
```

## Setup Statement

**Setup Statement** is combimed with pin setup, instruments, scan pin.

## Pattern Module

A **pattern module** is combimed with pin list and a set of vectors. There are 2 types of it: vector memory (VM) and memory (SRM):

```
vm_vector [module-name] (pin-list)
{ vectors }

srm_vector [module-name] (pin-list)
{ vectors }
```

At least 1 pattern module is required in a pattern file. If more than 1, their colummns and pin lists need to be the same.
