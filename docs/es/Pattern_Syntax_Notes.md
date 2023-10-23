# Notas sobre la Sintaxis de Patrones 🚧

Un archivo de patrones digitales consta principalmente de 3 partes:
**Declaración de Encabezado**, **Declaración de Configuración** y **Módulo de Patrón**. (**Declaraciones de Preprocesamiento** y **Comentarios** son opcionales).

A continuación, se muestra un ejemplo de archivo de patrón ampliamente utilizado en formato `.atp`:

```atp
// ejemplo.atp
digital_inst = HSDMQ;
opcode_mode = single;
pinmap_workbook = "..\xx.igxl";
importar tset tset1 ;
instrumentos = {
        (TIC_DATABUS):DigCap 32:format=twos_complement:auto_trig_enable;
}
vm_vector cpr_test($tset TIC_CLK, TIC_ACK, TIC_REQ_A, TIC_DATABUS)
{
cpr_test:
 > tset1 0 X 0 0 .d000000 ;
repetir 100
 > tset1 0 X 1 1 .rFFFFFF ;
 > tset1 0 X 0 0    .X    ;
 ((TIC_DATABUS):DigCap = Almacenar)
 > tset1 0 X 0 0    .V 	  ; // captura
DETENER
 > tset1 0 X 0 0  d000000 ; // fin
}
```

## Declaración de Encabezado

La **Declaración de Encabezado** contiene estas declaraciones: instrumento digital, mapa de pines, control de compilador, importación de conjuntos de tiempos o etiquetas. Aquí tienes un ejemplo:

```
digital_inst = HSDMQ;           // Declaración de instrumento digital
opcode_mode = single;           // Declaración de compilación
importar tset tset1, tset1;       // Importar conjuntos de tiempos
importar subr xxx;                // Importar Subrutinas
```

Parámetros comúnmente utilizados:

- Declaraciones de Instrumentos Digitales
  - **digital_inst**: `hsdm`(HSD1000, UltraPin800), `hsdmq`(UltraPin1600), `hsdp`(UltraPin2200) ...
- Especificaciones del Mapa de Pines:
  - **pinmap_workbook**: Nombre del libro IG‑XL, como `"xxx.igxl"`
  - **sheetname**: Nombre de la hoja del Mapa de Pines, como `"pinmap"`
- Declaraciones de Control del Compilador
  - **compressed**: `sí` o `no`
  - **opcode_mode**: `simple` o `doble` o `cuádruple`(UltraPin1600), cada 1/2/4 vectores pueden incluir un opcode.
  - **save_comments**: `sí` o `no`
  - **versión**: como `V1.0`
- Configuración de Prueba y Etiqueta
  - **Tset**: `importar tset tset1, tset2, ... ;`
  - **Etiqueta**: `importar etiqueta etiqueta1, etiqueta2, ... ;`

## Declaración de Configuración

La **Declaración de Configuración** contiene la configuración de pines, instrumentos y pines de escaneo.

```
pin_setup = {
    gpio_1    2x;                                           // Configuración del pin: gpio_1 configurado en modo 2X
}
instruments = {
vcc:DCVS 1;                                                 // Instrumento DCVS
    tdo:DigCap 32:format=twos_complement:auto_trig_enable;  // Instrumento DigCap
}
scan_pins = {
    tdi, tdo;                                               // tdi - escaneo de entrada, tdo - escaneo de salida
}
```

Parámetros de uso frecuente:

- Caracteres de Estado de Pines y Microcódigos
  - **Caracteres de Estado de Pines**: `0` (Bajo), `1` (Alto), `2` (Alto Voltaje solo para UP800), `L` (Esperar Bajo), `H` (Esperar Alto), `M` (Esperar Medio-banda), `V` (Esperar Válido), `X` (Máscara), `W` (Strobe de Ventana), `D` (Conducir ADS (DigSrc/MTO)), `I` (Conducir ADS inverso (DigSrc/MTO)), `E` (Esperar ADS (DigSrc/MTO)), `C` (Esperar ADS inverso (DigSrc/MTO)), `-` (Repetir estado anterior).
  - **Microcódigos de DigCap**: `Trig` (Iniciar una captura), `Almacenar` (Almacenar una muestra de datos), `Trig, Almacenar` (Combinación de Iniciar y Almacenar), `Almacenar, Inst_Cond_Strobe` (Almacenar y sincronizar la señal interna generada `condición` para actuar sobre ella).

## Módulo de Patrón

Un **módulo de patrón** contiene una lista de pines y un conjunto de vectores. Hay 2 tipos de ellos: memoria de vectores (VM) y memoria (SRM):

```plaintext
vm_vector [nombre-del-módulo] (lista-de-pines)
{ vectores }

srm_vector [nombre-del-módulo] (lista-de-pines)
{ vectores }
```

Se requiere al menos 1 módulo de patrón en un archivo de patrón. Si hay más de 1, sus columnas y listas de pines deben ser iguales.

Parámetros frecuentemente utilizados:

- lista-de-pines
  - **Elementos de Pines**: `pin-o-grupo[.modificador][:radix]`, el radix podría ser `:S` (Simbólico, por defecto), `:B` (Bin), `:D` (Dec), `:O` (Oct), `:H` (Hex)
- Etiqueta: pendiente de definir

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.