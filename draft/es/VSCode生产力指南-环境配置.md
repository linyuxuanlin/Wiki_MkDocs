# Guía de productividad de VS Code - Configuración del entorno

—— Cómo crear una herramienta de productividad eficiente con VS Code.

![](https://f004.backblazeb2.com/file/wiki-media/img/20200319135609.png)

## Antecedentes

> Si quieres hacer bien tu trabajo, debes primero tener las herramientas adecuadas. La creación es algo hermoso, y si tienes herramientas adecuadas, el proceso será más cómodo.

### ¿Por qué usar VS Code?

- Es de código abierto y gratuito, y tiene una excelente apariencia.
- Tiene funciones de edición completas (autocompletado, resaltado de sintaxis, etc.).
- Puedes depurar el código directamente en el editor.
- Tiene integración con Git.
- Tiene un amplio soporte de complementos y opciones de personalización.

## Instalación del software

Puedes descargar la última versión de VS Code en el sitio web oficial: <https://code.visualstudio.com/>

Por lo general, elegimos descargar la versión **Estable**. Si no temes a los errores y quieres experimentar con las últimas características, también puedes probar la versión **Insiders**.

Después de descargar e instalar el software, lo abrimos y lo primero que vemos es la página de inicio:

![](https://f004.backblazeb2.com/file/wiki-media/img/20200318224855.png)

## Instalación de complementos

Para reducir el tamaño, VS Code solo conserva algunas funciones básicas. Pero si quieres aumentar la eficiencia, estas funciones no son suficientes. 

Afortunadamente, VS Code tiene una variedad de complementos de terceros que pueden ser realmente útiles según tus necesidades.

A continuación, se recomiendan algunos complementos útiles (puedes hacer clic en los enlaces para instalarlos directamente):

### Básicos

- [**Paquete de idioma chino (simplificado)**](https://marketplace.visualstudio.com/items?itemName=MS-CEINTL.vscode-language-pack-zh-hans): traduce VS Code al chino.
- [**Settings Sync**](https://marketplace.visualstudio.com/items?itemName=Shan.code-settings-sync): realiza una copia de seguridad de la configuración y los complementos, y sincroniza entre dispositivos.
  - **Configuración**: configura el `GitHub Gist ID` y el `GitHub Access Token` correspondientes.
  - **Uso**: `Shift + Alt + U` para cargar, `Shift + Alt + D` para descargar.
  - (La última versión de VS Code ya tiene una función de sincronización incorporada, pero si necesitas una gestión de versiones, aún puedes usar este complemento).

### Markdown

- [**Markdown All in One**](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one): proporciona un soporte de sintaxis Markdown más potente.
- [**Markdown Paste Image**](https://marketplace.visualstudio.com/items?itemName=onesdev.vscode-paste-image-plus): pega imágenes en Markdown y las copia en la carpeta /res.
- [**Pangu-Markdown**](https://marketplace.visualstudio.com/items?itemName=xlthu.Pangu-Markdown): formatea el Markdown de manera más estándar (agrega espacios entre caracteres chinos e ingleses, reemplaza la puntuación estándar, etc.).
  - **Configuración**: habilita la opción de formatear automáticamente al guardar.
- [**vscode-pandoc**](https://marketplace.visualstudio.com/items?itemName=DougFinke.vscode-pandoc): agrega soporte para Pandoc, que exporta Markdown a PDF/Word/HTML, etc.
  - **Configuración**: asegúrate de que [Pandoc](https://pandoc.org/installing.html) esté instalado.

- [**Indenticator**](https://marketplace.visualstudio.com/items?itemName=SirTori.indenticator): Destaca la profundidad de la indentación del código.
- [**vscode-icons**](https://marketplace.visualstudio.com/items?itemName=vscode-icons-team.vscode-icons): Agrega iconos atractivos para diferentes formatos de archivo.

### Lenguajes de programación

- [**C/C++**](https://marketplace.visualstudio.com/items?itemName=ms-vscode.cpptools)
- [**Python**](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

### Front-end

- [**Prettier - Code formatter**](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode): Herramienta de formateo automático para lenguajes front-end como HTML/CSS/JavaScript.
  - **Uso**: `Ctrl + Shift + P`
- [**Color Manager**](https://marketplace.visualstudio.com/items?itemName=RoyAction.color-manager): Muestra el color correspondiente a un valor de color.
- [**Live Server**](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer): Ejecuta páginas web locales en VS Code.

### Otros

- [**Google Translate**](https://marketplace.visualstudio.com/items?itemName=hancel.google-translate): Proporciona traducción en VS Code.
  - **Uso**: `Ctrl + Alt + T`
- [**Start git-bash**](https://marketplace.visualstudio.com/items?itemName=McCarter.start-git-bash): Agrega `bash` a la terminal de VS Code.
- [**TinyPNG**](https://marketplace.visualstudio.com/items?itemName=andi1984.tinypng): Comprime imágenes.
  - **Configuración**: Configura la clave de API de `TinyPNG` correctamente.
  - **Uso**: Haz clic derecho en la imagen en el árbol de archivos - `TinyPNG:Compress`
- [**Zhihu Daily**](https://marketplace.visualstudio.com/items?itemName=YRM.zhihu): Ideal para procrastinar, lee noticias de Zhihu Daily en VS Code.
- [**Kunkun Encouragement**](https://marketplace.visualstudio.com/items?itemName=sakura1357.cxk): Si escribes código durante una hora, recibirás un recordatorio de descanso con el baile de baloncesto exclusivo de Cai Xukun.

## Temas

Puedes seleccionar el tema que más te guste en `Archivo - Preferencias - Tema de color`. Por ejemplo, yo he seleccionado el tema `Monokai Dimmed`:

![](https://f004.backblazeb2.com/file/wiki-media/img/20200319132727.png)

Si no te gusta ninguno de los temas proporcionados por defecto, puedes buscar y descargar temas que te gusten en la tienda de extensiones con la palabra clave `theme`.

## Configuraciones comunes

Para hacer que VS Code sea más fácil de usar, puedes cambiar algunas configuraciones comunes. Puedes abrir la página de configuración a través de `Archivo - Preferencias - Configuración`.

### Guardado automático

Se puede configurar `Files: Auto Save` en tres opciones diferentes además de `off`. Es muy útil tener la opción de guardar automáticamente en el uso diario.

### Fuente

La fuente de ancho fijo es esencial para escribir código, personalmente recomiendo la fuente [**Microsoft YaHei Mono**](https://github.com/linyuxuanlin/File-host/blob/main/software-development/Microsoft-YaHei-Mono.ttf).

Después de descargar el archivo de fuente .ttf, instálalo, reinicia VS Code y agrega `'Microsoft YaHei Mono'` al principio de la opción `Settings - Text Editor - Font - Font Family` para habilitar la fuente.

## Atajos de teclado comunes

|     Acción     |           Atajo           |
| :------------: | :-----------------------: |
|   Panel de comandos   | `F1` o `Ctrl + Shift + P` |
|     Terminal     | <code>Ctrl + &#96;</code>  |
|  Explorador de archivos  |     `Ctrl + Shift + E`     |
|   Búsqueda global   |     `Ctrl + Shift + F`     |
| Control de código fuente |     `Ctrl + Shift + G`     |
|     Ejecutar     |     `Ctrl + Shift + D`     |
|   Administrador de extensiones   |     `Ctrl + Shift + X`     |
| Cambiar rápidamente entre archivos |         `Ctrl + D`         |

## Control de código fuente

¿Tienes que ingresar tu nombre de usuario y contraseña cada vez que envías algo a Github? Ingresa el siguiente comando:

```shell
git config --global credential.helper store
```

Reinicia VS Code y listo.

## Conclusión

Estas son las configuraciones básicas de VS Code. En el próximo artículo, discutiremos detalladamente cómo usar Git, Jupyter Notebook y fragmentos de código personalizados. ¡Mantente atento!

### Enlaces de referencia

- [Docs · Visual Studio Code](https://code.visualstudio.com/docs)
- [¿Por qué elegí usar VS Code para el desarrollo web?](https://zhuanlan.zhihu.com/p/28631442)
- [vscode git 提交总让输入用户名及密码](https://www.jianshu.com/p/8854713433c5)
- [Vscode 编辑 markdown 代码块（snippets）](https://www.jianshu.com/p/a87e9ca2d208)
- [Agregar fragmentos de código personalizados en Visual Studio Code](https://blog.walterlv.com/post/add-custom-code-snippet-for-vscode.html##%E5%85%B3%E4%BA%8E%E6%96%87%E4%BB%B6%E5%90%8D%E7%A7%B0)

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.