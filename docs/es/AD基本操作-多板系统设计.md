# AD 基本操作 - Diseño de sistemas de placas múltiples 🚧

La razón detrás del diseño de sistemas de placas múltiples es que un proyecto de hardware puede incluir múltiples PCB y diversos elementos de ensamblaje, como carcasas. Si se aborda el diseño desde la perspectiva de cada placa de forma individual, es posible que el producto final presente errores de ensamblaje o interferencias. Al diseñar proyectos de hardware con múltiples elementos, lo mejor es emplear una aproximación mecánica y eléctrica conjunta. Para los ingenieros de hardware, esto se puede lograr directamente en Altium Designer, sin necesidad de utilizar software adicional como SolidWorks.

## Creación de un proyecto de placas múltiples

En primer lugar, se debe crear un archivo de tipo proyecto de placas múltiples (`.PrjMbd`). Luego, se deben generar archivos de diseño lógico basados en el esquema (`.MbsDoc`) y archivos basados en PCB (`.MbaDoc`) dentro del proyecto. Asegúrate de guardarlos. Desde una perspectiva del sistema de archivos, copia las carpetas de proyectos de PCB individuales en el mismo directorio que el archivo `.PrjMbd`, como se muestra a continuación:

![Vista de directorio del proyecto](https://media.wiki-power.com/img/20220106152537.png)

## Entrada de diseño lógico

La entrada de diseño lógico se realiza en función de los conectores físicos en la PCB. Antes de continuar, asegúrate de agregar parámetros a los conectores en el esquema del proyecto (abre las propiedades del conector y agrega "Parámetros" con el nombre "Sistema" y el valor "Conector").

![Agregar parámetros al conector](https://media.wiki-power.com/img/20220106163315.png)

### Creación de módulos y vinculación del proyecto

En el archivo de diseño lógico (`.MbsDoc`), coloca los módulos y, al hacer doble clic en uno, selecciona el proyecto de PCB fuente correspondiente.

### Importación de datos de interfaz de subproyectos

Haz clic con el botón derecho en el ratón y selecciona "Diseño" - "Importar desde subproyecto" para importar automáticamente los puertos con parámetros de conector.

### Adición de conexiones lógicas entre módulos

Utiliza la combinación de teclas rápas "P" - "W" para dibujar líneas de conexión. Haz clic en la línea de conexión para modificar los detalles de conexión de los dos módulos correspondientes en el panel de propiedades.

Si un conector debe conectarse a varias placas, es posible dividir un puerto en las propiedades.

## Ensamblaje físico de placas múltiples

### Importación de PCB desde el archivo de diseño lógico

Utiliza la combinación de teclas "D" - "I" para importar los PCB correspondientes desde el archivo de diseño lógico.

### Simulación de ensamblaje

Arrastra los ejes de coordenadas de cada PCB para simular el ensamblaje.

## Generación de datos de producción

🚧

## Referencias y agradecimientos

- [¿Cómo es la experiencia de diseñar sistemas de placas múltiples en PCB?](https://www.altium.com.cn/blog/pcb%E4%B8%AD%E8%BF%9B%E8%A1%8C%E5%A4%9A%E6%9D%BF%E8%AE%BE%E8%AE%A1%E4%BC%9A%E6%98%AF%E6%80%8E%E6%A0%B7%E7%9A%84%E4%BD%93%E9%AA%8C%EF%BC%9F)
- [Captura del diseño lógico del sistema](https://www.altium.com/cn/documentation/altium-designer/capturing-the-logical-system-design-ad)
- [Creación del ensamblaje físico de placas múltiples](https://www.altium.com/cn/documentation/altium-designer/creating-the-physical-multi-board-assembly-ad)
- [Generación de datos de producción para el diseño de placas múltiples](https://www.altium.com/cn/documentation/altium-designer/generating-multi-board-production-data-ad)

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
