# Operaciones básicas de AD - Configuración del entorno

- Tutorial de la serie Altium Designer

## Antecedentes

Este tutorial se basa en Altium Designer 19 (también compatible con la versión 20) y seguiré actualizando para las versiones posteriores.

## Descarga del software

Consulte directamente el [**Tutorial de instalación de Altium Designer 2020**](https://mp.weixin.qq.com/s?__biz=MzIwMjE1MjMyMw==&mid=502718968&idx=1&sn=4c37dc403171ffad01fca95b5a537b2e&chksm=0ee141143996c8021799bb5bf5407b7b56c2d7fa5dc484bda61893efd74a06a1f6be63a7a35e&scene=20&xtrack=1&key=088e5814bbd70a9bf7fb42111d02cbb81bb55981baea77169d867e2871add46f26dccde79326a96e819591677be92412fc05ff2af437922652dfe7ae1b94dc8172f36186ba0b2b460004027131ceae2c&ascene=1&uin=MTk5MDUwOTA0Mg%3D%3D&devicetype=Windows+10+x64&version=62090523&lang=zh_CN&exportkey=AyOYwgP948kprM0EiAGMcyk%3D&pass_ticket=6jBDTE0Qqg%2BrAl1wrTIo2UeJLmUrtbfUKPpgRGdeqhwXUk8QVkc%2Fyekd3BvlvVsB) para descargar el software, no se explicará aquí.

## Ajuste de la configuración

Para hacer bien el trabajo, primero debemos preparar las herramientas. Al abrir Altium Designer por primera vez, podemos ajustar algunas configuraciones para que la herramienta sea más fácil de usar. Encuentre el icono de **engranaje** en la esquina superior derecha, **abrir la página de configuración** y continuar con las siguientes operaciones.

### Configuración en chino

1. Haga clic en la pestaña **System - General** en la lista de la izquierda, marque la opción **Use localized resources** en la sección **Localizatioin**
2. Haga clic en **Aplicar** para guardar la configuración y reiniciar Altium Designer

### Editor de PCB

1. Haga clic en la pestaña **PCB Editor** en la lista de la izquierda
2. En la sección **General** de **PCB Editor**, marque **Rebuild copper pour after modification** en la sección **Copper Pour**; marque **Disable opening old version reports** y **Disable opening new version reports** en la sección **Document Format Modification Report**; en la sección **Other**, cambie el **tipo de cursor** a **Large 90**
3. Haga clic en la pestaña **Display**, marque **Apply highlight during interactive editing** en la sección **Highlight Options**
4. Haga clic en la pestaña **Board Insight Color Overrides**, seleccione **Solid (Overlay Color)** en la sección **Basic Style**
5. Haga clic en la pestaña **DRC Violations Display**, seleccione **Solid (Overlay Color)** en la sección **Conflict Overlay Style**
6. Haga clic en **Aplicar** para guardar la configuración y reiniciar Altium Designer

### Panel

1. Cierre la página de configuración, seleccione **View - Panel** en la barra de menú principal y haga clic en **Components, Messages** en orden.
2. Haga clic en el icono de **clip** en la esquina superior derecha del panel emergente y fije el panel en el lado derecho.

### Configuración de fondo como cuadrícula

1. Abra cualquier archivo de PCB (si no hay uno, cree uno nuevo)
2. Presione **Ctrl + G** para abrir la ventana de configuración de la cuadrícula
3. En la sección **Display**, configure ambas pestañas **Fine** y **Coarse** en **Dots**

## Compatibilidad con el método de entrada

Si no puede usar los atajos de teclado, verifique si ha cambiado al estado en inglés (el estado del método de entrada se muestra como **ENG** en la barra de estado), si no hay esta opción, siga los siguientes pasos:

1. Abre el **Panel de Control** y selecciona la página de **Reloj, idioma y región - Idioma**
2. Haz clic en el botón de **Agregar idioma**, agrega **Inglés** y selecciona **Inglés (Estados Unidos)**
3. Puedes cambiar el método de entrada en la barra de tareas del escritorio

## Resumen

En este capítulo, hemos configurado el entorno básico de Altium Designer y podemos comenzar a diseñar placas de circuito con alegría :\) 

## Referencias y Agradecimientos

- [Altium Designer Columna de Altium Corporation](https://seujxh.wordpress.com/2018/09/30/altium%e5%85%ac%e5%8f%b8altium-designer%e4%b8%93%e6%a0%8f/) 

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.