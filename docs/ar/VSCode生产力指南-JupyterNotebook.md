# Guía de productividad de VS Code - Jupyter Notebook

Crea herramientas de productividad eficientes con VS Code.

![](https://f004.backblazeb2.com/file/wiki-media/img/20200323155728.png)

Jupyter Notebook es una herramienta muy poderosa que nos permite escribir, ejecutar y visualizar código, datos y resultados en un solo documento. En resumen, nos facilita mucho la tarea de escribir documentos que contienen código.

En el artículo anterior, completamos la configuración básica de VS Code. En este artículo, explicaré cómo usar Jupyter con VS Code.

## Configuración del entorno

Como se sabe, Jupyter Notebooks depende del entorno de Python.  
Para confirmar si tienes un entorno de Python, en el panel de comandos de VS Code (`Ctrl + Shift + P`), escribe **Python: Select Interpreter**. Si ves que hay una versión de Python disponible para seleccionar, entonces no hay problema.

Si no tienes un entorno de Python, puedes instalarlo de la siguiente manera:

1. Descarga el paquete de instalación de la última versión en la [**página web oficial de Python**](https://www.python.org/) (preferiblemente la versión "web-based installer").

Después de configurar el entorno de Python local, también necesitamos instalar el complemento [**Python**](https://marketplace.visualstudio.com/items?itemName=ms-python.python) en VS Code. En una actualización reciente, Jupyter Notebooks ya está incluido en este complemento, así que no es necesario instalarlo por separado.

## Creación de un cuaderno

Después de configurar el entorno, puedes crear un cuaderno Jupyter en blanco (archivo `.ipynb`) en el panel de comandos de VS Code (`Ctrl + Shift + P`) escribiendo **Python: Create Blank New Jupyter**. A continuación, se muestra una prueba simple:

![](https://f004.backblazeb2.com/file/wiki-media/img/20200323153020.png)

Como se puede ver, el código se ejecuta correctamente.

## Operaciones básicas

Jupyter Notebook utiliza **celdas de código (code cells)** para crear, editar y ejecutar código.

![](https://f004.backblazeb2.com/file/wiki-media/img/20200323153717.png)

### Agregar celdas de código

![](https://f004.backblazeb2.com/file/wiki-media/img/20200323153850.png)

### Ejecutar una sola celda de código

![](https://f004.backblazeb2.com/file/wiki-media/img/20200323153939.png)

### Ejecutar varias celdas de código

![](https://f004.backblazeb2.com/file/wiki-media/img/20200323154005.png)

### Mover celdas de código

![](https://f004.backblazeb2.com/file/wiki-media/img/20200323154059.png)

### Eliminar celdas de código

![](https://f004.backblazeb2.com/file/wiki-media/img/20200323154148.png)

### Cambiar entre código y Markdown



### Visor de gráficos

Con el visor de gráficos, puede ver fácilmente los gráficos generados por el código y exportarlos en varios formatos de imagen:

![](https://f004.backblazeb2.com/file/wiki-media/img/20200323154555.png)

### Visor de datos y variables

Puede ver el tipo, la cantidad y el valor de las variables en tiempo real a través del visor de variables:

![](https://f004.backblazeb2.com/file/wiki-media/img/20200323154758.png)

También puede explorar datos más específicos a través del visor de datos:

![](https://f004.backblazeb2.com/file/wiki-media/img/20200323154832.png)

## Referencias y agradecimientos

- [Trabajando con cuadernos Jupyter en Visual Studio Code](https://code.visualstudio.com/docs/python/jupyter-support)
- [¡Nuevo lanzamiento de VS Code Python! ¡Finalmente llegó el soporte nativo para Jupyter Notebook!](https://zhuanlan.zhihu.com/p/85445777)

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.