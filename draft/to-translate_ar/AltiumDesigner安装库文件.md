# Instalación de archivos de biblioteca en Altium Designer

1. Copie todos los archivos de biblioteca en la carpeta correspondiente de **Shared\Library** del software;
2. Abra Altium Designer, haga clic en la página **Components** en el panel derecho, haga clic en el icono de **tres barras** en la esquina superior derecha, seleccione la opción **File-based Library Preferences**, haga clic en la página **Installed**, haga clic en el botón **Install** e instale los archivos de biblioteca correspondientes;
3. Algunas situaciones especiales:
   - La ruta de la biblioteca integrada de JLC se encuentra en la carpeta **JLCSMT_LIB\Project Outputs for Miscellaneous Devices LC**;
   - Si los archivos de biblioteca de terceros no son en formato de **biblioteca integrada (.IntLib)**, sino en forma de **biblioteca esquemática (SchLib)** o **biblioteca de encapsulamiento (PcbLib)**, es necesario **instalar ambos** archivos. En este caso, debe hacer clic en la lista desplegable a la derecha de la ventana de selección de ruta que aparece al instalar los archivos de biblioteca y cambiar el comodín a **All Files\(\*.\*\)**, de lo contrario solo se mostrarán archivos en formato **.Intlib**.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.