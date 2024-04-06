# Guía de productividad de VS Code - Jupyter Notebook

¡Crea una herramienta altamente eficiente con VS Code!

![Imagen](https://media.wiki-power.com/img/20200323155728.png)

Jupyter Notebook es una herramienta poderosa que nos permite escribir, ejecutar código, ver resultados, visualizar datos y revisar resultados, todo dentro de un entorno de documento. En resumen, hace que escribir documentos con código sea mucho más sencillo.

En el artículo anterior, configuramos el entorno básico de VS Code. En este artículo, me sumergiré en los detalles de Jupyter con VS Code.

## Configuración del entorno

Como es bien sabido, Jupyter Notebooks depende del entorno de Python.  
Para verificar si tienes Python instalado, ve al panel de comandos de VS Code (Ctrl + Shift + P) y escribe **Python: Select Interpreter**. Si ves que hay versiones de Python disponibles para seleccionar, estás listo.

Si no tienes un entorno de Python, puedes instalarlo de la siguiente manera:

1. Descarga el paquete de instalación más reciente desde el [**sitio web oficial de Python**](https://www.python.org/) (selecciona la versión basada en web, si es posible).

Después de configurar tu entorno de Python local, necesitarás instalar la extensión [**Python**](https://marketplace.visualstudio.com/items?itemName=ms-python.python) en VS Code. En una reciente actualización, Jupyter Notebooks se incluyó en esta extensión, por lo que no es necesario instalarlo por separado.

## Creación de cuadernos

Una vez que la configuración del entorno está completa, puedes crear un cuaderno Jupyter en blanco (.ipynb) desde el panel de comandos de VS Code (Ctrl + Shift + P) ingresando **Python: Create Blank New Jupyter**. A continuación, realiza una sencilla prueba, como se muestra en la siguiente imagen:

![Imagen](https://media.wiki-power.com/img/20200323153020.png)

Puedes ver que el código se ejecuta correctamente.

## Operaciones básicas

Jupyter Notebook utiliza **celdas de código (code cells)** para crear, editar y ejecutar código.

![Imagen](https://media.wiki-power.com/img/20200323153717.png)

### Agregar celdas de código

![Imagen](https://media.wiki-power.com/img/20200323153850.png)

### Ejecutar una única celda de código

![Imagen](https://media.wiki-power.com/img/20200323153939.png)

### Ejecutar varias celdas de código

![Imagen](https://media.wiki-power.com/img/20200323154005.png)

### Mover celdas de código

![Imagen](https://media.wiki-power.com/img/20200323154059.png)

### Eliminar celdas de código

![Imagen](https://media.wiki-power.com/img/20200323154148.png)

### Alternar entre código y Markdown

![Imagen](https://media.wiki-power.com/img/20200323154242.png)

### Visor de gráficos

El visor de gráficos te permite ver fácilmente las gráficas generadas por tu código y exportarlas en varios formatos:

![Imagen](https://media.wiki-power.com/img/20200323154555.png)

### Visor de datos y variables

Puedes ver en tiempo real el tipo, cantidad y valor de las variables mediante el visor de datos y variables.

```markdown
![Imagen](https://media.wiki-power.com/img/20200323154758.png)

También puedes explorar datos más específicos a través del visor de datos:

![Imagen](https://media.wiki-power.com/img/20200323154832.png)

## Referencias y Agradecimientos

- [Trabajar con Jupyter Notebooks en Visual Studio Code](https://code.visualstudio.com/docs/python/jupyter-support)
- [¡Novedad en Python de VS Code! ¡Soporte nativo de Jupyter Notebook finalmente disponible!](https://zhuanlan.zhihu.com/p/85445777)

> Dirección original del artículo: <https://wiki-power.com/>
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.
```

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
