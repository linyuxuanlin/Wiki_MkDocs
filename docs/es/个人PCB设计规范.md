# Normas de Diseño de PCB Personal

## Normas de Diseño de PCB

### Diseño por Módulos

**Por función del módulo**: Los circuitos que realizan la misma función (compuestos por componentes discretos que cumplen una función específica) deben ubicarse lo más cerca posible.

**Según el rendimiento eléctrico**:

- Zona de circuitos digitales: **resistente a interferencias y generadora de interferencias**
- Zona de circuitos analógicos: **sensible a interferencias**
- Zona de accionamiento de potencia: **generadora de interferencias**

### Principios de Diseño

- Colocar primero los componentes más grandes.
- Colocar todos los componentes en la capa superior (facilita la soldadura).
- Generador de reloj (cuarzo, etc.): Colocar lo más cerca posible de los dispositivos que utilizan ese reloj.
- Agregar **condensadores de desacoplo en el extremo de alimentación de cada módulo**: para eliminar señales de interferencia en la fuente de alimentación. Colocarlos lo más cerca posible de la fuente de alimentación.
- Agregar un diodo de protección en las bobinas de relé (por ejemplo, 1N4148).

## Normas de Enrutamiento de PCB

### Principios de Enrutamiento

- Evitar que las líneas sean **paralelas entre sí**.
- Evitar que un extremo de una línea quede flotante (puede causar efectos de antena).
- Mantener las longitudes de las rutas lo más cortas posible.
- Los ángulos de las curvas de enrutamiento deben ser mayores de 90°.
- Regla del **3W**: Cuando la distancia entre el centro de las líneas sea al menos 3 veces el ancho de la línea, se puede mantener un 70% de campo eléctrico sin interferencia mutua.
- Evitar la formación de bucles en las rutas.
- Dejar puntos de prueba en ubicaciones críticas.
- Asegurar que el ancho de las pistas a ambos lados de los pads de los componentes sea uniforme (usar la función "teardrop").
- Usar la función "teardrop" después de completar el enrutamiento (mejora la estética y fortalece la compatibilidad electromagnética).
- No perforar agujeros en los pads de los componentes (puede causar soldaduras defectuosas en SMT).
- Evitar enrutamiento o cobre debajo de microcontroladores.

### Secuencia de Enrutamiento

1. Líneas de alimentación.
2. Líneas generales.
3. Líneas de tierra (cobre).
 
Al diseñar el enrutamiento del PCB, generalmente comenzamos con las líneas de alimentación, ya que en la mayoría de los casos, se requieren líneas de alimentación cortas, anchas y directas. Una vez que se completa el enrutamiento de las líneas generales, procedemos a la capa de tierra, que generalmente se configura como "GND" en placas de doble capa.

### Configuración de Reglas

**Ancho de pista**:

- Líneas de alimentación: **30-50 milésimas de pulgada**
- Líneas de señal: **12 milésimas de pulgada**

**Tamaño de agujero**:

- Diámetro interior: **0.45 mm**
- Diámetro exterior: **0.75 mm**

**Conexión de cobre**:

Usar el método Direct.

- Separación segura del cobre: **10 milésimas de pulgada**
- Atributo: **GND**
- Selección de cobre: Pour Over All Same Net Objects
- Eliminar cobre inactivo: Remove Dead Copper

**Tamaño de letra**:

- Ancho de línea mínimo: **6 milésimas de pulgada**
- Altura mínima de caracteres: **32 milésimas de pulgada**

Si se utiliza un tamaño menor, los caracteres impresos en la placa pueden no ser legibles.

**Relación entre el ancho de la pista de PCB y la corriente**:

```markdown
[Texto sin traducción]
```

(Sin cambio en la sección final)

|  **Ancho del trazo / Espesor del cobre**  | **70µm (2 oz)** | **50µm (1.5 oz)** | **35µm (1 oz)** |
| :------------------------: | :-----------: | :-------------: | :-----------: |
| **2.50mm (98 mil)** |   6.00A   |   5.10A   |   4.50A   |
| **2.00mm (78 mil)** |   5.10A   |   4.30A   |   4.00A   |
| **1.50mm (59 mil)** |   4.20A   |   3.50A   |   3.20A   |
| **1.20mm (47 mil)** |   3.60A   |   3.00A   |   2.70A   |
| **1.00mm (40 mil)** |   3.20A   |   2.60A   |   2.30A   |
| **0.80mm (32 mil)** |   2.80A   |   2.40A   |   2.00A   |
| **0.60mm (24 mil)** |   2.30A   |   1.90A   |   1.60A   |
| **0.50mm (20 mil)** |   2.00A   |   1.70A   |   1.35A   |
| **0.40mm (16 mil)** |   1.70A   |   1.35A   |   1.10A   |
| **0.30mm (12 mil)** |   1.30A   |   1.10A   |   0.80A   |
| **0.20mm (8 mil)**  |   0.90A   |   0.70A   |   0.55A   |
| **0.15mm (6 mil)**  |   0.70A   |   0.50A   |   0.20A   |

En general, se recomienda reservar un 15% de margen.

## Referencias y Agradecimientos

- [Información sobre la capacidad de procesamiento de PCB de JLC PCB](https://www.sz-jlc.com/portal/vtechnology.html)
- [¿Cuál es el ancho de trazo adecuado para el enrutamiento de PCB? ¡Te lo hemos preparado!](https://mp.weixin.qq.com/s?__biz=MzI4NDAwOTgzMw==&mid=2650625562&idx=1&sn=29d145ed112c23464ac74bfeeb212aa1&chksm=f388021cc4ff8b0a2e1701726340afb0b60738f8ae448e8f8d0c3b0dee0758a89fe954433011&scene=126&sessionid=1607139114&key=f9ff6c6605e545f8046d3325f95411b620e846faa9864c6589c1a6b69f1ce0d00f26f595bea2995ab23bf54727f1c9f219239f6d2c840605db0dac7c7f884190fcd2134daa54c87cbf6f249bfa9c29f8ddd39b20d50744335451d3acb3466ebcc44d8918dba7d35a22569e0b7a780088439cf35fe0ff5ea9bddbafef36c64bfd3f&ascene=1&uin=MTk5MDUwOTA0Mg%3D%3D&devicetype=Windows+10+x64&version=6300002f&lang=zh_CN&exportkey=A1GQK2ccX%2BvsjA6n1%2BOfSNU%3D&pass_ticket=kq2QkQn3wCfkzXnTBMjx4zRHCHr2TH9lX0mMASdXW7ugPzIdfcJaNdCq2VwvOmMs&wx_header=0)

> Dirección original del artículo: <https://wiki-power.com/>
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.