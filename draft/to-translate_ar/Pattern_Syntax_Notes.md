# Notas de sintaxis de patrones 🚧

> Esta publicación solo está disponible en inglés.

Un archivo de patrón digital contiene principalmente 3 partes:
**Declaración de encabezado**, **Declaración de configuración** y **Módulo de patrón**. (**Las declaraciones de preprocesamiento** y **comentarios** son opcionales).

A continuación se muestra un archivo de patrón de ejemplo en formato `.atp` que se utiliza principalmente:

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

## Declaración de encabezado

La **Declaración de encabezado** contiene estas declaraciones: instrumento digital, asignación de pines, control de compilador, importación de tset o etiqueta. Aquí hay un ejemplo:

```
digital_inst = HSDMQ;           // Declaración de instrumento digital
opcode_mode = single;           // Declaración de compilación
import tset tset1, tset1;       // importar conjuntos de tiempo
import subr xxx;                // importar subrutinas
```

Parámetros frecuentemente utilizados:

- Declaraciones de instrumentos digitales
  - **digital_inst**: `hsdm`(HSD1000, UltraPin800), `hsdmq`(UltraPin1600), `hsdp`(UltraPin2200) ...
- Especificaciones del mapa de pines:
  - **pinmap_workbook**: nombre del libro de trabajo IG‑XL, como `"xxx.igxl"`
  - **sheetname**: nombre de la hoja del mapa de pines, como `"pinmap"`
- Declaraciones de control de compilador
  - **compressed**: `sí` o `no`
  - **opcode_mode**: `single` o `dual` o `quad`(UltraPin1600), cada 1/2/4 vectores pueden incluir un opcode.
  - **save_comments**: `sí` o `no`
  - **version**: como `V1.0`
- Tset y etiqueta
  - **Tset**: `import tset tset1, tset2, ... ;`
  - **Etiqueta**: `import label label1, label2, ... ;`

## Declaración de configuración

La **Declaración de configuración** contiene la configuración de pines, instrumentos y pines de escaneo.

```
pin_setup = {
    gpio_1    2x;                                           //Configuración de pines: gpio_1 configurado en modo 2X
}
instruments = {
vcc:DCVS 1;                                                 // Instrumento DCVS
    tdo:DigCap 32:format=twos_complement:auto_trig_enable;  // Instrumento DigCap
}
scan_pins = {
    tdi, tdo;                                               // tdi - escaneo de entrada, tdo - escaneo de salida
}
```

Parámetros frecuentemente utilizados:

- Caracteres de Estado de Pin y Microcódigos
  - **Caracteres de Estado de Pin**: `0`(Conducir Bajo), `1`(Conducir Alto), `2`(Conducir Voltaje Alto solo para UP800), `L`(Esperar Bajo), `H`(Esperar Alto), `M`(Esperar Banda Media), `V`(Esperar Válido), `X`(Máscara), `W`(Strobe de Ventana), `D`(Conducir ADS (DigSrc/MTO)), `I`(Conducir ADS inverso (DigSrc/MTO)), `E`(Esperar ADS (DigSrc/MTO)), `C`(Esperar ADS inverso (DigSrc/MTO)), `-`(Repetir estado anterior).
  - **Microcódigos de DigCap**: `Trig`(Iniciar una captura), `Store`(Almacenar una muestra de datos), `Trig, Store`(Combinación de Trig y Store), `Store, Inst_Cond_Strobe`(Almacenar y activar la señal interna de `condición` para actuar sobre ella).

## Módulo de Patrón

Un **módulo de patrón** contiene una lista de pines y un conjunto de vectores. Hay 2 tipos de módulos: memoria de vector (VM) y memoria (SRM):

```
vm_vector [nombre-de-módulo] (lista-de-pines)
{ vectores }

srm_vector [nombre-de-módulo] (lista-de-pines)
{ vectores }
```

Se requiere al menos 1 módulo de patrón en un archivo de patrón. Si hay más de 1, sus columnas y listas de pines deben ser iguales.

Parámetros frecuentemente utilizados:

- lista-de-pines
  - **Elementos de Pin**: `pin-o-grupo[.modificador][:radix]`, el radix podría ser `:S`(Simbólico, por defecto), `:B`(Bin), `:D`(Dec), `:O`(Oct), `:H`(Hex)
- Etiqueta: por determinar

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.