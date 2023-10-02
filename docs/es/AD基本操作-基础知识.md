# Operaciones básicas de AD - Conocimientos básicos

- Tutorial de la serie Altium Designer

## Contexto

Antes de comenzar a diseñar una placa, es importante familiarizarse con algunos conocimientos básicos de Altium Designer y diseño de circuitos después de configurar el entorno de ejecución del software.

## Instalación de archivos de biblioteca

La biblioteca es como una colección de esquemas / PCB encapsulados para cada componente discreto (como resistencias, capacitores, etc.), lo que facilita su uso directo. No es necesario dibujar la biblioteca / encapsulamiento de cada componente. Sin embargo, **es necesario organizar su propia biblioteca**. Supongamos que cada componente utilizado en su proyecto proviene de otras bibliotecas (y cada biblioteca tiene sus propias reglas), cuanto más avance, más estará limitado. Tener su propia biblioteca no solo facilita la migración y mejora la eficiencia, sino que también es beneficioso para la sistematización del conocimiento. Las reglas y el sistema adecuados para usted, desde la perspectiva del eje de tiempo, el conocimiento aumentará exponencialmente. Aunque la curva de crecimiento al principio es lenta, no habrá trabajo repetitivo en el futuro. Lo que necesita hacer es aprender nuevos conocimientos y resumirlos en el sistema.

Consejo: intente extraer todos los componentes necesarios para su proyecto de su propia biblioteca de esquemas / encapsulamientos.

### Bibliotecas de referencia

- [**Power_Lib_Altium**](https://github.com/linyuxuanlin/Power_Lib_Altium): mi propia biblioteca. La biblioteca de encapsulamientos es completa y la biblioteca de esquemas solo incluye los modelos de componentes que necesito para mi proyecto. Actualizado constantemente.
- [**AltiumDesigner_PcbLibrary**](https://github.com/KitSprout/AltiumDesigner_PcbLibrary): una biblioteca bastante completa.
- [**My_PCB_Library_Github**](https://github.com/Samwuzhitao/My_PCB_Library_Github): una biblioteca bastante completa que también incluye algunas placas de soluciones de microcontroladores.
- [**JLCSMT_LIB**](https://gitee.com/JLC_SMT/JLCSMT_LIB): biblioteca de integración estándar proporcionada por Jialichuang, que incluye todos los componentes que Jialichuang puede pegar con SMT. Si usa esta biblioteca de integración, la compatibilidad al imprimir / SMT será mejor.
- [**Hare_Library**](https://github.com/linyuxuanlin/Power_Lib_Altium/tree/master/Other_Libs/Hare_Library): biblioteca de esquemas / encapsulamientos organizada por Bingge, que cubre la mayoría de los componentes necesarios para el hardware del equipo.

Cómo instalar archivos de biblioteca: consulte [**Cómo instalar archivos de biblioteca Altium Designer**](https://wiki-power.com/AltiumDesigner安装库文件)

### Componentes poco comunes

Las bibliotecas proporcionadas anteriormente cubren más del 95% de los modelos de componentes en el mercado. Si realmente no puede encontrar el componente necesario, puede intentar los siguientes métodos:

Complementos de AD:

- [**Altium Library Loader**](https://www.samacsys.com/altium-designer-library-instructions/): realmente fácil de usar

Motor de búsqueda: [**Descarga de esquemas y encapsulamientos · NAV de Power**](https://nav.wiki-power.com/#87696a153c91c609c4c595e421e880ae)

## Atajos de teclado

Para Altium Designer, dominar los atajos de teclado comunes puede mejorar en gran medida la eficiencia. Los atajos de teclado del sistema Altium Designer se componen de letras subrayadas en los comandos del menú, como el atajo de teclado de **Place-Line** es **P-L** (primero presione P y luego presione L).

### Esquema

- Mostrar el panel de la biblioteca: **PP**
- Dibujar cables: **Ctrl + W**
- Dibujar etiquetas de red: **PN**
- Copiar componentes y actualizar automáticamente los números de referencia: **Mantener presionado Shift + arrastrar**
- Numerar los dibujos: **TAT**
- Numeración automática de componentes: **TAA**
  - Reset All: restablece todos los números de referencia de los componentes para que estén en formato "letra + ?"
  - Update Change List: actualiza la lista de componentes con los cambios de numeración
  - Accept Changes (Create ECO): acepta los cambios de numeración y realiza los cambios en el esquema original
- Generar lista de materiales (BOM): **RI**
- Actualizar PCB: **DU**
- Alinear a la izquierda (derecha): **AL** (**AR**)

### PCB

- Importar cambios del esquema a la PCB: **DI**
- Sobrescribir cambios de la PCB en el esquema: **DU**
- Cambiar unidades (pulgadas / milímetros): **Q**
- Girar componentes (cualquier ángulo): **EMO**
- Colocar componentes en la capa inferior: **Arrastrar y mantener presionado L**
- Distribución automática: **Seleccionar y presionar TOL**
- Establecer origen de coordenadas: **EOS**
- Establecer cuadrícula: **G**
- Enrutamiento automático: **UAA**
- Limpiar enrutamiento: **UUA**
- Resaltar conexiones: **Mantener presionado Shift + mover el cursor sobre la línea**
- Resaltar línea correspondiente al nodo: **Mantener presionado Ctrl + hacer clic izquierdo**
- Voltear horizontalmente: **Ctrl + F**
- Medir: **Ctrl + M**
- Cambiar vista (2D / 3D): **2 / 3**
- Rotar en la vista 3D: **Mantener presionado Shift + arrastrar**
- Limpiar filtro: **Shift + C**
- Cambiar entre vista de una capa / múltiples capas: **Shift + S**
- Tapar agujeros pasantes (opcional, se puede seleccionar directamente al hacer la placa)
  1. Hacer clic en un agujero pasante
  2. Hacer clic derecho - Buscar objetos similares
  3. Seleccionar Same en la propiedad de tamaño y confirmar para seleccionar todos los agujeros pasantes
  4. En la propiedad de expansión de la máscara de soldadura, seleccionar tanto la capa superior como la inferior
- Establecer reglas de enrutamiento
  1. **UAA**
  2. Crear una nueva estrategia y editar las reglas
  3. Modificar las reglas en Routing (crear nuevas reglas)
     - Width: establecer el grosor de la línea
     - Routing Via Style: establecer las reglas de los agujeros pasantes
     - Cobertura de cobre: ?

### Biblioteca de esquemas

Por completar...

### Biblioteca de encapsulados

- Medir distancia: **Ctrl + N**
- Cambiar unidades (pulgadas / milímetros): **Q**

## Proceso y normas

El proceso básico para diseñar una placa de circuito impreso desde cero es el siguiente:

1. Inicialización
   1. Crear un nuevo proyecto
   2. Crear esquemático y archivo PCB dentro del proyecto
2. Dibujo del esquemático
   1. Asegurarse de que se compila correctamente después de completarlo
3. Dibujo del PCB
   1. Importar cambios desde el esquemático
   2. Ocultar la identificación del componente Designator
      1. Abrir el panel de propiedades a la derecha
      2. Hacer clic en el icono del ojo al lado de Designator para cerrarlo
   3. Dibujar la forma de la placa
      - Cambiar entre líneas de 90°/45° (Shift+Space)
      - Definir la placa con la forma dibujada (DSD)
      - Establecer la propiedad del marco de la placa en la capa mecánica 1
      - Agujeros fijos
        - Tornillo M3: interno 3,1 mm, externo 4 mm
   4. Disposición de componentes
      - Ver artículo [**Normas de disposición de componentes de PCB**](https://wiki-power.com/PCB%E5%85%83%E4%BB%B6%E5%B8%83%E5%B1%80%E8%A7%84%E8%8C%83)
   5. Enrutamiento
      - Establecer reglas de enrutamiento
        - Consultar [**Normas de enrutamiento de PCB**](https://wiki-power.com/PCB%E5%B8%83%E7%BA%BF%E8%A7%84%E8%8C%83)
      - ¡No activar el enrutamiento automático!
      - Activar la función de gota de lágrima
   6. Identificación de fuentes (identificación de pines / derechos de autor / texto engañoso)
      - Colocar en la capa de serigrafía (superior / inferior)
      - Si se coloca en la capa inferior, hay que invertirlo primero
   7. Cobertura de cobre (PG)
      - Consultar [**Normas de enrutamiento de PCB**](https://wiki-power.com/PCB%E5%B8%83%E7%BA%BF%E8%A7%84%E8%8C%83)
4. Fabricación de la placa
   1. Guardar el proyecto
   2. Comprimir el archivo .pcb (si es posible, exportar Gerber)
   3. Subirlo al asistente de pedido de JiaLiChuang
   4. (Opcional SMT)

## Otros conocimientos

### Propiedades del componente

- **Designator**: número de posición del componente, es la identificación única del componente y se utiliza para identificar diferentes componentes en el esquemático
  - **R**: resistencia
  - **RN**: red de resistencias
  - **C**: capacitancia
  - **J**: interfaz / cable de puente
  - **X**: oscilador de cristal
  - **D**: diodo
  - **Q** o **T**: transistor
  - **FB**: perla magnética
  - **U**: chip
  - **TP**: punto de prueba
- **Comment**: parámetros de tamaño del componente, como el valor de resistencia de una resistencia, el valor de capacitancia de un capacitor, el modelo de chip IC, etc.
- **Description**: se utiliza para escribir una descripción de la función del componente

### Agregar un logotipo

Consultar el artículo [**Agregar un logotipo**](https://seujxh.wordpress.com/2018/10/03/logo%E6%B7%BB%E5%8A%A0/).

### Gestión del proyecto con Git

Consultar [**Consideraciones al utilizar Git en AD**](https://wiki-power.com/AD%E4%BD%BF%E7%94%A8Git%E7%9A%84%E6%B3%A8%E6%84%8F%E4%BA%8B%E9%A1%B9)

## Conclusión

Estos son los conocimientos básicos de Altium Designer y diseño de circuitos.  
En el próximo capítulo, comenzaremos a diseñar el esquemático.

## Referencias y agradecimientos

- [Columna de Altium Designer de la compañía Altium](https://seujxh.wordpress.com/2018/09/30/altium%e5%85%ac%e5%8f%b8altium-designer%e4%b8%93%e6%a0%8f/)
- [Lista de integración de PADS de SMT de Jialichuang para pegado \ (versión oficial)](http://club.szlcsc.com/article/details_2757_1.html)
- [Idea de construcción de Git para Altium Designer](https://blog.csdn.net/weifengdq/article/details/78406438)
- [Usando el control de versiones](https://www.altium.com/documentation/altium-designer/using-version-control-ad)

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.