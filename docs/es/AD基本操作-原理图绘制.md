# AD 基本操作 - 原理图绘制

—— Tutorial de la serie Altium Designer

## Antecedentes

Después del calentamiento en el capítulo anterior, estamos listos para entrar en el proceso de dibujo de diagramas esquemáticos.

## Dibujo del Diagrama Esquemático

### Ajuste del Tamaño de la Hoja

Siguiendo el proceso básico mencionado anteriormente, hemos creado un nuevo proyecto y hemos agregado el archivo del diagrama esquemático al proyecto. En este punto, se mostrará una hoja en blanco. Puedes comenzar a dibujar el diagrama esquemático directamente en esta hoja. Si el diagrama esquemático se vuelve complicado, también puedes **ajustar el tamaño de la hoja** para que los componentes no se vean demasiado apretados:

1. Haz **doble clic** en cualquier parte en blanco de la hoja.
2. En el panel de Propiedades, ve a la sección **Opciones de Página**.
3. Haz clic en el menú desplegable de **Tamaño de la Hoja** para ajustar el tamaño de la hoja.

### Colocación de Componentes

A continuación, comenzamos a colocar componentes. La instalación de bibliotecas se explicó en el capítulo anterior. Abre el panel **Componentes**, haz clic en el menú desplegable que muestra el nombre de la biblioteca instalada y podrás cambiar a la biblioteca que deseas utilizar. Después de cambiar, utiliza la barra de búsqueda para encontrar los componentes que necesitas (no es necesario presionar Enter después de escribir), luego simplemente arrastra el componente necesario con el botón izquierdo del ratón y colócalo en el diagrama esquemático.

Si olvidas a qué biblioteca pertenece un componente, también puedes utilizar la función de búsqueda global. Haz clic en el icono de las **tres barras horizontales** a la izquierda del nombre de la biblioteca y selecciona **Búsqueda en Bibliotecas Basadas en Archivos**, y podrás buscar en todas las bibliotecas disponibles.

### Propiedades de los Componentes

Los componentes colocados tienen varias propiedades clave:

- **Designator**: El identificador único del componente, no puede tener el mismo nombre. Por lo general, se usan R1, R2... para resistencias y C1, C2... para condensadores (consulta el capítulo anterior para obtener información adicional).
- **Comment**: Parámetros de tamaño del componente, como resistencia, capacidad, número de modelo del chip, etc.
- **Description**: Descripción de la función del componente.
- **Footprint**: Enlace a la biblioteca de encapsulados, que conecta el componente con un encapsulado de PCB específico.
- **Models**: Incluye modelos de simulación y de integridad de señal.

### Operaciones Básicas

- **Clic izquierdo**: Seleccionar comando
- **Clic largo izquierdo**: Arrastrar objeto
- **Doble clic izquierdo**: Configurar propiedades del objeto
- **Clic derecho**: Cancelar o mostrar menú de comandos
- **Clic largo derecho**: Arrastrar la página del diagrama esquemático
- **Ctrl + Rueda del ratón**: Hacer zoom en la página
- **Shift + Clic izquierdo/Selección en cuadro**: Seleccionar varios componentes

Para operaciones más avanzadas, usa el comando **S** (Seleccionar) para abrir el menú de comandos:

| Atajo | Comando Detallado | Función |
| :----- | :---------------- | :------------------------------------------------------------------- |
| E      | Seleccionar con **Lazo**  | Selecciona componentes dentro de un área trazada con el lazo; inicia el trazado con un clic izquierdo y finalízalo con otro clic izquierdo para delimitar el área de selección. |
| I      | **Dentro del Área**   | Selecciona todos los componentes dentro de un área delimitada. |
| O      | **Fuera del Área**  | Invierte la selección, seleccionando todos los componentes fuera del área delimitada. |
| L      | **Toque de Línea** | Selecciona los componentes que son tocados por una línea trazada. |
| C      | **Conexión**    | Selecciona componentes con el mismo nombre de red. |
| A      | **Todos** | Selecciona todos los componentes. |
| T      | **Alternar Selección** | Invierte la selección actual: lo que estaba seleccionado se deseleccionará y viceversa. |

- Rotación de componentes: Seleccione el componente y presione **Barra espaciadora**.
- Copiar, cortar y pegar: **Ctrl + C**, **Ctrl + X**, **Ctrl + V**.
- Copiar y rellenar automáticamente la designación: Seleccione el componente y **arrastre mientras mantiene presionada la tecla Shift**, para pegar componentes con designaciones incrementales. El paso se puede configurar en **TP** (Herramientas-Preferencias-Esquemático-General).
- Dibujar cables: **Ctrl + W**.
- Dibujar etiquetas de red: **PN**.
- Colocar fuente de alimentación/tierra: Seleccione la opción directamente en la barra de herramientas con el **botón izquierdo** y elija el estilo con el **botón derecho**.

### Numeración automática global de componentes

Cuando el proyecto del esquema es grande y contiene muchos componentes, a veces puede haber designaciones duplicadas o faltantes. En este caso, puede utilizar la gestión global de designaciones: **TAA**, en lugar de hacerlo manualmente.

Marque los componentes que desee numerar automáticamente, haga clic en **Actualizar lista de cambios**, luego haga clic en **Aceptar cambios (crear ECO)**, **ejecute el cambio**, y así los componentes se numerarán automáticamente.

## Conclusión

Lo anterior describe las operaciones más básicas para dibujar un esquema, como proporcionar un conjunto de utensilios de cocina. Para crear diseños más atractivos, lo que realmente importa es la **imaginación** y la **práctica constante**.

## Referencias y Agradecimientos

- [Sección de Altium Designer de la empresa Altium](https://seujxh.wordpress.com/2018/09/30/altium%e5%85%ac%e5%8f%b8altium-designer%e4%b8%93%e6%a0%8f/)

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.