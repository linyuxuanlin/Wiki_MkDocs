# Operaciones básicas de AD - Dibujo de esquemas

- Tutorial de la serie Altium Designer

## Antecedentes

Después del calentamiento en el capítulo anterior, comenzamos con la etapa de dibujo de esquemas.

## Dibujo de esquemas

### Ajuste del papel

Siguiendo el proceso básico mencionado anteriormente, creamos un nuevo proyecto y agregamos el archivo de esquema al proyecto. En este punto, aparece una hoja de papel en blanco. Podemos dibujar directamente en ella. Si el esquema se vuelve complicado, también podemos **cambiar el tamaño del papel** para que los componentes no se vean demasiado apretados:

1. **Haga doble clic** en cualquier lugar en blanco de la hoja,
2. En el panel Propiedades, busque la sección **Opciones de página**,
3. Haga clic en el menú desplegable Tamaño de hoja para cambiar el tamaño del papel.

### Colocación de componentes

A continuación, comenzamos a colocar componentes. La instalación de la biblioteca se explicó en el capítulo anterior. Abrimos el panel **Componentes**, hacemos clic en el menú desplegable que muestra el nombre de la biblioteca y podemos cambiar a la biblioteca instalada. Después de buscar el componente necesario en la barra de búsqueda (no es necesario presionar Enter después de escribir), podemos arrastrar el componente directamente al esquema con el botón izquierdo del mouse, lo que colocará el componente con éxito.

Si olvidamos a qué biblioteca pertenece un componente, también podemos utilizar la función de búsqueda global. Haga clic en el icono de **tres barras** a la izquierda del nombre de la biblioteca y seleccione **Búsqueda de bibliotecas basadas en archivos**, lo que nos permitirá buscar todas las bibliotecas disponibles.

### Propiedades del componente

Los componentes colocados tienen varias propiedades clave:

- **Designator**: número de posición del componente. Es una identificación única del componente y no puede tener el mismo nombre. Por lo general, se utilizan R1, R2 ... para resistencias y C1, C2 ... para capacitores (consulte los puntos de conocimiento del capítulo anterior).
- **Comment**: parámetros de tamaño del componente, como valor de resistencia, valor de capacitancia, modelo de chip, etc.
- **Description**: descripción de la función del componente.
- **Footprint**: enlazado a la biblioteca de encapsulados, lo que permite que el componente se corresponda con un encapsulado de PCB.
- **Models**: incluye modelos de simulación, integridad de señal, etc.

### Operaciones básicas

- **Clic izquierdo**: seleccionar comando
- **Clic izquierdo prolongado**: arrastrar objeto
- **Doble clic izquierdo**: establecer propiedades del objeto
- **Clic derecho**: cancelar o mostrar menú de comandos
- **Clic derecho prolongado**: arrastrar página de esquema
- **Ctrl + rueda de desplazamiento**: acercar o alejar la página
- **Mayús + clic izquierdo/selección de cuadro**: seleccionar varios componentes

Para operaciones más avanzadas, use el comando **S** (Seleccionar) para mostrar el menú de comandos:

| Atajo | Comando detallado | Función |
| :----- | :---------------- | :------------------------------------------------------------------- |
| E      | Selección de lazo | Selección de componentes dentro del área del lazo; haga clic con el botón izquierdo para comenzar a dibujar el lazo y haga clic nuevamente para finalizar el dibujo del área |
| I      | Área interior | Seleccione todos los componentes dentro del área seleccionada |
| O      | Área exterior | Seleccione todos los componentes fuera del área seleccionada |
| L      | Línea de contacto | Seleccione los componentes tocados por la línea |
| C      | Conexión | Seleccione los componentes con el mismo nombre de red |
| A      | Todos | Seleccione todos los componentes |
| T      | Alternar selección | Selección inversa, haga clic en los componentes seleccionados para cancelar la selección y haga clic en los componentes no seleccionados para seleccionarlos |

- Rotación de componentes: seleccione el componente y presione la tecla **Espacio**
- Copiar, cortar y pegar: **Ctrl + C**, **Ctrl + X**, **Ctrl + V**
- Copiar y pegar con relleno automático de identificadores: seleccione el componente, mantenga presionada la tecla **Shift** y arrastre para pegar componentes con identificadores incrementales. El incremento se puede configurar en **TP** (**T**ools-**P**reference-Schematic-General).
- Dibujar cables: **Ctrl + W**
- Dibujar etiquetas de red: **PN**
- Colocar alimentación/tierra: seleccione directamente en la barra de herramientas con el botón **izquierdo**, o haga clic con el botón **derecho** para seleccionar diferentes estilos.

### Numeración automática global de componentes

Cuando el proyecto del esquemático es grande y hay muchos componentes, a veces puede haber identificadores duplicados o faltantes. En este caso, se puede utilizar la gestión global de identificadores: **TAA**, en lugar de verificar manualmente.

Seleccione los componentes que necesitan numeración automática, haga clic en **Actualizar lista de cambios**, luego haga clic en **Aceptar cambios (crear ECO)** y **Ejecutar cambios** para completar la numeración automática de los componentes.

## Conclusión

Estas son solo las operaciones básicas para dibujar un esquemático, como proporcionar un conjunto de utensilios de cocina. Para hacer platos más sabrosos, se necesita más **imaginación** y **práctica constante**.

## Referencias y agradecimientos

- [Sección de Altium Designer de la empresa Altium](https://seujxh.wordpress.com/2018/09/30/altium%e5%85%ac%e5%8f%b8altium-designer%e4%b8%93%e6%a0%8f/)

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.