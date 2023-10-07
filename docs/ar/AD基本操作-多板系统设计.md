# Operaciones básicas de AD - Diseño de sistemas de múltiples placas 🚧

La razón por la que se utiliza el diseño de sistemas de múltiples placas es que un proyecto de hardware puede contener varias placas PCB y varios elementos de ensamblaje, como carcasas. Si se diseña desde la perspectiva de cada placa, el producto final puede tener errores de ajuste o interferencia. Al diseñar proyectos de hardware con múltiples elementos, es mejor utilizar la colaboración mecánica. Para los ingenieros de hardware, esto se puede lograr directamente en Altium Designer sin necesidad de software como SolidWorks.

## Crear un proyecto de múltiples placas

En primer lugar, cree un archivo de tipo de proyecto de múltiples placas (`.PrjMbd`), cree un archivo de diseño lógico basado en el esquemático del proyecto (`.MbsDoc`) y un archivo basado en PCB (`.MbaDoc`), y luego guárdelo. En el nivel del sistema de archivos, copie varias carpetas de proyectos de PCB individuales en el mismo nivel de directorio que `.PrjMbd`, por ejemplo:

![](https://f004.backblazeb2.com/file/wiki-media/img/20220106152537.png)

## Entrada de diseño lógico

La entrada de diseño lógico se realiza en función de los conectores físicos de la PCB. Antes de esto, debemos agregar parámetros a los conectores en el esquemático del proyecto (abrir las propiedades del conector, agregar `Parameters`, el nombre es `System`, el valor es `Connector`).

![](https://f004.backblazeb2.com/file/wiki-media/img/20220106163315.png)

### Crear un módulo y vincular el proyecto

Coloque el módulo en el archivo de diseño lógico (`.MbsDoc`) y haga doble clic en él para abrir las propiedades y seleccione el proyecto de PCB correspondiente.

### Importar datos de interfaz de subproyectos

Haga clic derecho con el mouse y seleccione `Design` - `Import from Subproject` para importar automáticamente los puertos que tienen parámetros como conectores.

### Agregar conexiones lógicas entre módulos

Use el atajo de teclado `P` - `W` para dibujar una línea de conexión.

Haga clic en la línea de conexión para modificar los detalles de conexión de los dos módulos correspondientes en el panel de propiedades.

Si un conector necesita conectarse a varias placas correspondientes, puede dividir un puerto en las propiedades.

## Ensamblaje físico de múltiples placas

### Importar PCB desde el archivo de diseño lógico

Use el atajo de teclado `D` - `I` para importar el PCB correspondiente del archivo de diseño lógico.

### Simulación de ensamblaje

Arrastre los ejes de coordenadas de cada PCB para simular el ensamblaje.

## Generación de datos de producción

🚧

## Referencias y agradecimientos

- [¿Cómo es la experiencia de diseñar múltiples placas en PCB?](https://www.altium.com.cn/blog/pcb%E4%B8%AD%E8%BF%9B%E8%A1%8C%E5%A4%9A%E6%9D%BF%E8%AE%BE%E8%AE%A1%E4%BC%9A%E6%98%AF%E6%80%8E%E6%A0%B7%E7%9A%84%E4%BD%93%E9%AA%8C%EF%BC%9F)
- [Captura del diseño lógico del sistema](https://www.altium.com/cn/documentation/altium-designer/capturing-the-logical-system-design-ad)
- [Creación del ensamblaje físico de múltiples placas](https://www.altium.com/cn/documentation/altium-designer/creating-the-physical-multi-board-assembly-ad)
- [Generación de datos de producción de múltiples placas](https://www.altium.com/cn/documentation/altium-designer/generating-multi-board-production-data-ad)

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.