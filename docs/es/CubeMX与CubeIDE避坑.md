# CubeMX y CubeIDE: evita problemas

## El nombre y la ruta del proyecto no pueden estar en chino

Como se indica, el nombre y la ruta del proyecto deben estar en inglés, de lo contrario pueden aparecer errores extraños.

## El puerto de depuración está desactivado por defecto

Descripción del problema:

- Se detecta ST-Link, pero no se detecta la placa, aparece el mensaje `No target connected`.
- La descarga funciona la primera vez, pero no la segunda ni las siguientes.

Causa:

- CubeMX desactiva el puerto de depuración.

Solución (temporal):

- Utiliza la herramienta **STM32 ST-LINK Utility** para restaurar el firmware de fábrica.
- O utiliza el método proporcionado en [**este artículo**](https://www.jianshu.com/p/cea16b641c3d) (a través de Keil).

Solución (a largo plazo):

- En la configuración SYS de CubeMX, cambia la opción de depuración a Serial Wire (SW).

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20200531162352.jpg)

## Los comentarios en chino aparecen como caracteres extraños en STM32CubeIDE

Si el código se importa desde Keil, asegúrate de que la codificación original sea GB2312.

Haz clic en la barra de menú - `Window` - `Preferences` - `General` - `Apperance` - `Colors and Fonts` - `C/C++` - `Editor` - `C/C++ Editor Text Font`, haz clic en `Edit` a la derecha, asegúrate de que la fuente admita caracteres chinos (como Microsoft YaHei), y confirma que el script es `中文 GB2312`.

Si aún no se soluciona, haz clic con el botón derecho en el nombre del proyecto en el árbol de archivos de la izquierda, haz clic en `Properties`, cambia la codificación de fuente en el panel `Resource` a `GBK` (si no aparece, escríbelo directamente), y guarda los cambios.

## Cómo cambiar el idioma de STM32CubeIDE a chino

Abre el enlace **<http://mirrors.ustc.edu.cn/eclipse/technology/babel/update-site/>**, selecciona el directorio de datos más reciente (por ejemplo, `mirrors.ustc.edu.cn/eclipse/technology/babel/update-site/`), y copia el enlace.

En la barra de menú de STM32CubeIDE, selecciona `Help` - `Install New Software`, haz clic en `Add`, escribe `language` en el campo `Name`, pega el enlace que acabas de copiar en el campo `Location`, y haz clic en `Add`. En la ventana emergente, selecciona el paquete de idioma chino simplificado, instálalo y reinicia el software según las instrucciones.

## Referencias y agradecimientos

- [STM32 调试器配置异常导致的问题与解决方法（一）](https://www.jianshu.com/p/cea16b641c3d)
- [STM32cubeIDE 环境配置安装-汉化-主题设置](https://blog.csdn.net/wct3344142/article/details/104142863)

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
