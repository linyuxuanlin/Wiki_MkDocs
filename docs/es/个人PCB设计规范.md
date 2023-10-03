# Normas de diseño de PCB personalizado

## Normas de diseño de la disposición de PCB

### Disposición modular

**Por módulos de función**: Los circuitos que realizan la misma función (compuestos por componentes discretos que implementan un módulo específico) deben colocarse lo más cerca posible.

**Por rendimiento eléctrico**:

- Área de circuitos digitales: **sensible a interferencias y generador de interferencias**
- Área de circuitos analógicos: **sensible a interferencias**
- Área de conducción de potencia: **generador de interferencias**

### Principios de diseño

- Colocar primero los componentes más grandes
- Todos los componentes deben colocarse en la capa superior (para facilitar la soldadura)
- Generador de reloj (cristal, etc.): colocar lo más cerca posible de los componentes que lo utilizan
- Agregar capacitores de desacoplamiento en la entrada de alimentación de cada módulo: para filtrar las señales de interferencia de la fuente de alimentación. Asegurarse de colocarlos lo más cerca posible del módulo de alimentación.
- Agregar un diodo de descarga en la bobina del relé (como 1N4148)

## Normas de enrutamiento de PCB

### Principios de enrutamiento

- Evitar que las líneas sean paralelas
- No dejar un extremo flotando (puede generar un efecto de antena)
- Mantener la longitud total de las líneas lo más corta posible
- Los ángulos de las líneas deben ser mayores a 90°
- Regla de los 3W: cuando la distancia entre los centros de las líneas es al menos 3 veces el ancho de la línea, se puede mantener un 70% de campo eléctrico sin interferencia mutua
- Regla de lazo mínimo: evitar que las líneas formen un bucle
- Se pueden reservar puntos de prueba en lugares críticos de la señal
- La anchura de los pines de los componentes debe ser uniforme en ambos lados (usar la función de "tear drop")
- Después de completar el enrutamiento, activar la función de "tear drop" (para mejorar la estética y la compatibilidad electromagnética)
- No hacer agujeros en los pines de los componentes (los componentes SMT pueden causar soldaduras frías)
- Evitar en la medida de lo posible el enrutamiento / cobre debajo del chip del microcontrolador

### Orden de enrutamiento

1. Línea de alimentación
2. Línea general
3. Línea de tierra (cobre)

Cuando se realiza el enrutamiento de PCB, generalmente se coloca primero la línea de alimentación. En la mayoría de los casos, la línea de alimentación debe ser **corta, gruesa, recta y con pocos agujeros**, por lo que tiene la prioridad más alta.

Después de completar el enrutamiento de las líneas de señal general, finalmente debemos colocar el cobre. Para una placa de doble capa común, la propiedad del cobre generalmente se establece como **tierra**.

### Configuración de reglas

**Ancho de línea**:

- Línea de alimentación: **30-50** mil
- Línea de señal: **12** mil

**Tamaño del agujero**:

- Diámetro interno: **0,45** mm
- Diámetro externo: **0,75** mm

**Conexión de cobre**:

Usar el método Direct

(Algunas explicaciones no están claras, se agregarán más adelante)

- Distancia de seguridad de cobre: **10** mil
- Propiedad: **GND**
- Selección de cobre: Pour Over All Same Net Objectc,
- Eliminar el cobre muerto: Remove Dead Copper

**Tamaño de caracteres**:

- Ancho de línea mínimo: **6** mil
- Altura mínima de caracteres: **32** mil

Si es menor que los valores anteriores, los caracteres impresos en la placa pueden no ser claros. 

**Relación entre el ancho de línea de PCB y la corriente**:


|  Ancho de línea / Espesor de cobre  | 70µm (2 oz) | 50µm (1.5 oz) | 35µm (1 oz) |
| :-------------: | :----------: | :------------: | :----------: |
| 2.50mm (98mil) | 6.00A | 5.10A | 4.50A |
| 2.00mm (78mil) | 5.10A | 4.30A | 4.00A |
| 1.50mm (59mil) | 4.20A | 3.50A | 3.20A |
| 1.20mm (47mil) | 3.60A | 3.00A | 2.70A |
| 1.00mm (40mil) | 3.20A | 2.60A | 2.30A |
| 0.80mm (32mil) | 2.80A | 2.40A | 2.00A |
| 0.60mm (24mil) | 2.30A | 1.90A | 1.60A |
| 0.50mm (20mil) | 2.00A | 1.70A | 1.35A |
| 0.40mm (16mil) | 1.70A | 1.35A | 1.10A |
| 0.30mm (12mil) | 1.30A | 1.10A | 0.80A |
| 0.20mm (8mil) | 0.90A | 0.70A | 0.55A |
| 0.15mm (6mil) | 0.70A | 0.50A | 0.20A |

Generalmente se requiere una reserva del 15% de margen.

## Referencias y agradecimientos

- [JLC PCB Rango de capacidad de procesamiento de tecnología](https://www.sz-jlc.com/portal/vtechnology.html)
- [¿Qué ancho de línea es adecuado para el cableado de PCB? ¡Ya lo hemos preparado para ti!](https://mp.weixin.qq.com/s?__biz=MzI4NDAwOTgzMw==&mid=2650625562&idx=1&sn=29d145ed112c23464ac74bfeeb212aa1&chksm=f388021cc4ff8b0a2e1701726340afb0b60738f8ae448e8f8d0c3b0dee0758a89fe954433011&scene=126&sessionid=1607139114&key=f9ff6c6605e545f8046d3325f95411b620e846faa9864c6589c1a6b69f1ce0d00f26f595bea2995ab23bf54727f1c9f219239f6d2c840605db0dac7f884190fcd2134daa54c87cbf6f249bfa9c29f8ddd39b20d50744335451d3acb3466ebcc44d8918dba7d35a22569e0b7a780088439cf35fe0ff5ea9bddbafef36c64bfd3f&ascene=1&uin=MTk5MDUwOTA0Mg%3D%3D&devicetype=Windows+10+x64&version=6300002f&lang=zh_CN&exportkey=A1GQK2ccX%2BvsjA6n1%2BOfSNU%3D&pass_ticket=kq2QkQn3wCfkzXnTBMjx4zRHCHr2TH9lX0mMASdXW7ugPzIdfcJaNdCq2VwvOmMs&wx_header=0)

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.