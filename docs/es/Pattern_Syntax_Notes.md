```markdown
# Notas sobre la Sintaxis de Patrones 🚧

Un archivo de patrón digital consta principalmente de 3 partes:
**Declaración de Encabezado**, **Declaración de Configuración** y **Módulo de Patrón**. (Las **Declaraciones de Preprocesamiento** y los **Comentarios** son opcionales).

A continuación se muestra un ejemplo de archivo de patrón ampliamente utilizado en formato `.atp`:

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
 > tset1 0 X 0 0    .V 	  ; // captura
HALT
 > tset1 0 X 0 0  d000000 ; // fin
}
```

## Declaración de Encabezado

La **Declaración de Encabezado** contiene estas declaraciones: instrumento digital, mapa de pines, control del compilador, importación de conjuntos de tiempos o etiquetas. Aquí tienes un ejemplo:

```
digital_inst = HSDMQ;           // Declaración de instrumento digital
opcode_mode = single;           // Declaración de compilación
import tset tset1, tset1;       // Importar conjuntos de tiempo
import subr xxx;                // Importar Subrutinas
```

Parámetros frecuentemente utilizados:

```

- Declaraciones de Instrumento Digital
  - **digital_inst**: `hsdm`(HSD1000, UltraPin800), `hsdmq`(UltraPin1600), `hsdp`(UltraPin2200) ...
- Especificaciones del Mapa de Pines:
  - **pinmap_workbook**: Nombre del libro IG‑XL, como `"xxx.igxl"`
  - **sheetname**: Nombre de la hoja del Mapa de Pines, como `"pinmap"`
- Declaraciones de Control del Compilador
  - **compressed**: `sí` o `no`
  - **opcode_mode**: `simple` o `dual` o `cuádruple`(UltraPin1600), cada 1/2/4 vectores puede incluir un opcode.
  - **save_comments**: `sí` o `no`
  - **versión**: como `V1.0`
- Tset y Etiqueta
  - **Tset**: `importar tset tset1, tset2, ... ;`
  - **Etiqueta**: `importar etiqueta etiqueta1, etiqueta2, ... ;`

## Declaración de Configuración

La **Declaración de Configuración** contiene la configuración de pines, instrumentos y pines de escaneo.

```
configuración_de_pines = {
    gpio_1    2x;                                           // Configuración de pines: gpio_1 configurado en modo 2X
}
instrumentos = {
vcc:DCVS 1;                                                 // Instrumento DCVS
    tdo:DigCap 32:formato=dos_complemento:auto_trig_enable;  // Instrumento DigCap
}
pines_de_escaneo = {
    tdi, tdo;                                               // tdi - escaneo de entrada, tdo - escaneo de salida
}
```

Parámetros de uso frecuente:

- Caracteres de Estado de Pines y Microcódigos
  - **Caracteres de Estado de Pines**: `0` (Bajo), `1` (Alto), `2` (Alto Voltaje solo para UP800), `L` (Esperar Bajo), `H` (Esperar Alto), `M` (Esperar en el Rango Medio), `V` (Esperar Válido), `X` (Máscara), `W` (Destello de Ventana), `D` (Impulsar ADS (DigSrc/MTO)), `I` (Impulsar ADS inverso (DigSrc/MTO)), `E` (Esperar ADS (DigSrc/MTO)), `C` (Esperar ADS inverso (DigSrc/MTO)), `-` (Repetir estado anterior).
  - **Microcódigos DigCap**: `Trig` (Iniciar una captura), `Store` (Almacenar una muestra de datos), `Trig, Store` (Combinación de Trig y Store), `Store, Inst_Cond_Strobe` (Almacenar y enmascarar la señal de `condición` generada internamente para su posterior acción).

## Módulo de Patrones

Un **módulo de patrones** contiene una lista de pines y un conjunto de vectores. Hay 2 tipos de módulos: memoria de vectores (VM) y memoria (SRM):

```
vm_vector [nombre-del-módulo] (lista-de-pines)
{ vectores }

srm_vector [nombre-del-módulo] (lista-de-pines)
{ vectores }
```

Se requiere al menos 1 módulo de patrones en un archivo de patrones. Si hay más de 1, sus columnas y listas de pines deben ser iguales.

Parámetros de uso frecuente:

- lista-de-pines
  - **Elementos de Pines**: `pin-o-grupo[.modificador][:radix]`, el radix puede ser `:S` (Símbolo, predeterminado), `:B` (Bin), `:D` (Dec), `:O` (Oct), `:H` (Hex)
- Etiqueta: pendiente

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.