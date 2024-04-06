```markdown
# Consejos para evitar problemas con CubeMX y CubeIDE

## Evita caracteres chinos en nombres y rutas de proyectos

Al crear un nuevo proyecto en CubeMX y CubeIDE, es fundamental que tanto el nombre del proyecto como la ruta estén escritos en inglés. De lo contrario, podrían surgir errores inesperados.

## Desactiva el puerto de depuración por defecto

Descripción del problema:

- Detectas el ST-Link, pero no puedes conectarlo a la placa, y aparece el mensaje `No target connected`.
- La primera vez puedes programar la placa con éxito, pero las siguientes veces no funciona.

Causa:

- CubeMX desactiva el puerto de depuración.

Solución (solución inmediata):

- Usa la herramienta **STM32 ST-LINK Utility** para restablecer el firmware original.
- O sigue los pasos proporcionados en [**este artículo**](https://www.jianshu.com/p/cea16b641c3d) (a través de Keil).

Solución (solución a largo plazo):

- En la configuración SYS de CubeMX, cambia la opción de depuración a Serial Wire (SW).

![Imagen](https://media.wiki-power.com/img/20200531162352.jpg)

## Problemas de caracteres chinos en los comentarios en STM32CubeIDE

Si importas código desde Keil, asegúrate de que el archivo original esté codificado en GB2312.

Sigue estos pasos: Haz clic en la barra de menú - `Window` - `Preferences` - `General` - `Appearance` - `Colors and Fonts` - `C/C++` - `Editor` - `C/C++ Editor Text Font`, haz clic en `Edit` en el lado derecho y asegúrate de que la fuente admita caracteres chinos (como Microsoft YaHei) y que el script esté configurado como `GB2312`.

Si el problema persiste, puedes hacer clic derecho en el nombre del proyecto en el árbol de archivos de la izquierda y seleccionar `Properties`. En el panel `Resource`, cambia la codificación de fuente a `GBK` (si no está en la lista, puedes escribirla directamente). Guarda los cambios para resolver el problema.

## Traducción al chino en STM32CubeIDE

Abre el enlace **<http://mirrors.ustc.edu.cn/eclipse/technology/babel/update-site/>**, navega hasta la última carpeta de datos disponible (por ejemplo, `mirrors.ustc.edu.cn/eclipse/technology/babel/update-site/`) y copia la URL.

En la barra de menú de STM32CubeIDE, selecciona `Help` - `Install New Software`, haz clic en `Add`, ingresa `language` en el campo `Name` y pega la URL copiada en el campo `Location`. Luego, haz clic en "Add". En la ventana emergente, selecciona el paquete de idioma chino simplificado y sigue las instrucciones para instalarlo. Reinicia el software según se indique.

## Referencias y Agradecimientos

- [Problemas y soluciones causados por una configuración inusual del depurador STM32 (Parte 1)](https://www.jianshu.com/p/cea16b641c3d)
- [Configuración, instalación de chino y ajuste de temas en STM32CubeIDE](https://blog.csdn.net/wct3344142/article/details/104142863)

> Dirección original del artículo: <https://wiki-power.com/>
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.
```

**Nota:** Los enlaces a sitios web y las referencias entre corchetes > Dirección original del artículo: <https://wiki-power.com/> y > Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente. no se tradujeron, ya que se mantuvieron tal como están en el texto original.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
