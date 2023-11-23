# Operaciones Básicas de AD - Fundamentos

—— Serie de tutoriales de Altium Designer

## Antecedentes

Después de configurar el entorno de ejecución del software, es fundamental familiarizarse con algunos conceptos básicos de Altium Designer y el diseño de circuitos antes de empezar a diseñar placas.

## Instalación de Librerías

Las bibliotecas funcionan como envoltorios para cada componente discreto (como resistencias y condensadores) en forma de esquemas y placas de circuito impreso (PCB), lo que facilita su uso directo. No es necesario crear una biblioteca para cada componente, pero **organizar su propia biblioteca es imprescindible**. Imagina que todos los componentes en tu proyecto provienen de fuentes externas y cada fuente tiene sus propias reglas. Cuanto más dependas de otros, más limitado estarás. Tener tu propia biblioteca no solo simplifica la migración y aumenta la eficiencia, sino que también contribuye a la sistematización del conocimiento. Al adaptar las reglas y sistemas a tus necesidades, el conocimiento crecerá exponencialmente a lo largo del tiempo. Si bien al principio el crecimiento puede ser lento, en la etapa avanzada no habrá tareas repetitivas. En ese momento, solo necesitarás aprender nuevos conceptos y agregarlos a tu sistema.

Consejo útil: Extrae todos los componentes necesarios para tu proyecto de tus propias bibliotecas de esquemas y envoltorios.

### Bibliotecas de referencia

- [**Power_Lib_Altium**](https://github.com/linyuxuanlin/Power_Lib_Altium): Mi propia biblioteca organizada. Incluye envoltorios completos y solo esquemas de componentes necesarios para mis proyectos. Actualización constante.
- [**AltiumDesigner_PcbLibrary**](https://github.com/KitSprout/AltiumDesigner_PcbLibrary): Una biblioteca bastante completa.
- [**My_PCB_Library_Github**](https://github.com/Samwuzhitao/My_PCB_Library_Github): Una biblioteca muy completa que incluye algunas placas de soluciones para microcontroladores.
- [**JLCSMT_LIB**](https://gitee.com/JLC_SMT/JLCSMT_LIB): Una biblioteca estándar proporcionada por JLC PCB que contiene todos los componentes aptos para soldadura SMT de JLC PCB. Usar esta biblioteca integrada proporciona una buena compatibilidad al diseñar placas o soldar componentes.
- [**Hare_Library**](https://github.com/linyuxuanlin/Power_Lib_Altium/tree/master/Other_Libs/Hare_Library): Una biblioteca de esquemas y envoltorios organizada por Bin, que incluye la mayoría de los componentes necesarios para hardware dentro del equipo.

Cómo instalar bibliotecas: Consulta [**Cómo instalar bibliotecas en Altium Designer**](https://wiki-power.com/AltiumDesigner安装库文件)

### Componentes Inusuales

Las bibliotecas mencionadas anteriormente cubren más del 95% de los tipos de componentes disponibles en el mercado. Si no puedes encontrar un componente específico, puedes probar los siguientes métodos:

Complementos de AD:

- [**Altium Library Loader**](https://www.samacsys.com/altium-designer-library-instructions/): Realmente fácil de usar.

Motor de búsqueda: [**Descarga de Esquemas y Envoltorios · NAV de Power**](https://nav.wiki-power.com/#87696a153c91c609c4c595e421e880ae)

## Atajos

En el contexto de Altium Designer, dominar los atajos comunes puede mejorar significativamente la eficiencia. Los atajos del sistema de Altium Designer se basan en combinaciones de letras subrayadas en los comandos de menú, por ejemplo, el atajo para **Place-Line** es **P-L** (presionar primero P y luego L).

### Esquemático

- Display Library Panel: **PP**
- Draw Wires: **Ctrl + W**
- Draw Network Labels: **PN**
- Copy Components and Automatically Update Reference Designators: **Hold Shift + Drag**
- Number the Drawing: **TAT**
- Automatically Number Components: **TAA**
  - Reset All: Reset all component reference designators to "letter + ?" format
  - Update Change List: Update the component list with reference designator changes
  - Accept Changes (Create ECO): Accept reference designator changes to implement schematic changes
- Generate BOM Table: **RI**
- Update PCB: **DU**
- Align Left (Right): **AL** (**AR**)

### PCB

- Import Schematic Changes to PCB: **DI**
- Overlay PCB Changes Back to Schematic: **DU**
- Switch Units (Inches/Millimeters): **Q**
- Rotate Components (Any Angle): **EMO**
- Place Components on the Bottom Layer: **Drag while pressing L**
- Automatic Layout: **Select + TOL**
- Set the Origin Coordinates: **EOS**
- Set the Grid: **G**
- Auto Route: **UAA**
- Clear Routing: **UUA**
- Highlight Connections: **Hold Shift + Move Cursor over Wire**
- Highlight Connected Net: **Hold Ctrl + Left-click**
- Horizontal Flip: **Ctrl + F**
- Measure: **Ctrl + M**
- Switch View (2D / 3D): **2 / 3**
- Rotate in 3D View: **Hold Shift + Drag**
- Clear Filters: **Shift + C**
- Toggle Single/Multi-Layer Display: **Shift + S**
- Cover Vias with Solder Mask (Optional, can be selected when PCB is being fabricated)
  1. Click on a via
  2. Right-click - Find Similar Objects
  3. Select Size property as Same to activate selecting all vias
  4. In the Solder Mask Expansion property, check both top and bottom layers
- Set Routing Rules
  1. **UAA**
  2. Create a strategy and edit the rules
  3. Modify rules under Routing in general (create new rules)
     - Width: Set line thickness
     - Routing Via Style: Set via rules
     - Copper Pour: ?

### Schematic Library

To be completed...

### Footprint Library

- Measure Distance: **Ctrl + N**
- Switch Units (Inches/Millimeters): **Q**

## Processes and Standards

The basic process for designing a circuit board from scratch is as follows:

```markdown
1. Iniciar
   1. Crear un nuevo proyecto
   2. Crear esquemáticos y archivos PCB dentro del proyecto
2. Dibujar el esquemático
   1. Asegurarse de que la compilación sea exitosa
3. Diseñar el PCB
   1. Importar cambios desde el esquemático
   2. Ocultar las designaciones de componentes
      1. Abrir el panel **Propiedades** en el lado derecho
      2. Hacer clic en el ícono del **ojo** junto a **Designator** para desactivarlo
   3. Dibujar la forma de la placa
      - Cambiar a rutas de 90°/45° (**Shift+Space**)
      - Definir la placa según la forma dibujada (**DSD**)
      - **Configurar las propiedades del marco de la placa como Capa Mecánica 1**
      - Agujeros de montaje
        - Tornillos M3: interior **3.1** mm, exterior **4** mm
   4. Colocar componentes
      - Consultar el artículo [**Normas de disposición de componentes en PCB**](https://wiki-power.com/PCB%E5%85%83%E4%BB%B6%E5%B8%83%E5%B1%80%E8%A7%84%E8%8C%83)
   5. Enrutamiento
      - Configurar reglas de enrutamiento
        - Consultar las [**Normas de enrutamiento en PCB**](https://wiki-power.com/PCB%E5%B8%83%E7%BA%BF%E8%A7%84%E8%8C%83)
      - **No activar el enrutamiento automático.**
      - Habilitar la función de "teardrops" (teardrop)
   6. Etiquetado de texto (pines, derechos de autor, texto informativo)
      - Colocar en la capa de serigrafía (superior/inferior)
      - Si se coloca en la capa inferior, reflejar primero
   7. Rellenar con cobre (**PG**)
      - Consultar las [**Normas de enrutamiento en PCB**](https://wiki-power.com/PCB%E5%B8%83%E7%BA%BF%E8%A7%84%E8%8C%83)
4. Fabricación de la placa
   1. Guardar el proyecto
   2. Comprimir el archivo **.pcb** (esto no es ideal; si es posible, exportar a Gerber)
   3. Cargar en la asistencia para realizar pedidos de JLCPCB
   4. (Opcional: montaje superficial SMT)

## Otro conocimiento

### Atributos de componentes

- **Designator**: Número de identificación único del componente que se utiliza para diferenciar los componentes en el esquemático.
  - **R**: Resistencia
  - **RN**: Red de resistencias
  - **C**: Condensador
  - **J**: Conector/Cable
  - **X**: Oscilador
  - **D**: Diodo
  - **Q** o **T**: Transistor
  - **FB**: Ferrita
  - **U**: Circuito integrado
  - **TP**: Punto de prueba
- **Comment**: Parámetros del componente, como valor de resistencia, capacidad de condensador, número de modelo de circuito integrado, etc.
- **Description**: Utilizado para describir la función del componente.

### Agregar un logotipo

Consultar el artículo [**Agregando un logotipo**](https://seujxh.wordpress.com/2018/10/03/logo%E6%B7%BB%E5%8A%A0/).

### Gestión de proyectos con Git

Ver [**Consideraciones al usar Git en Altium Designer**](https://wiki-power.com/AD%E4%BD%BF%E7%94%A8Git%E7%9A%84%E6%B3%A8%E6%84%8F%E4%BA%8B%E9%A1%B9) para más detalles.

## Resumen

Esto abarca los conceptos básicos de Altium Designer y diseño de circuitos. En el próximo capítulo, comenzaremos el diseño del esquemático.

## Referencias y Agradecimientos
```


- [Columna de Altium Designer de la compañía Altium](https://seujxh.wordpress.com/2018/09/30/altium%e5%85%ac%e5%8f%b8altium-designer%e4%b8%93%e6%a0%8f/)
- [Lista oficial de montaje superficial SMT de Jialichuang en la biblioteca integrada de PADS](http://club.szlcsc.com/article/details_2757_1.html)
- [Concepto de uso de Git en Altium Designer](https://blog.csdn.net/weifengdq/article/details/78406438)
- [Uso de control de versión](https://www.altium.com/documentation/altium-designer/using-version-control-ad)

> Dirección original del artículo: <https://wiki-power.com/>
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.