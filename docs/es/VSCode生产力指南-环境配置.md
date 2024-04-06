# Guía de Productividad de VS Code - Configuración del Entorno

—— Cómo convertir VS Code en una herramienta altamente eficiente para la productividad.

![Imagen](https://media.wiki-power.com/img/20200319135609.png)

## Antecedentes

> Si quieres hacer bien tu trabajo, primero debes tener buenas herramientas. La creación es un hermoso proceso, y tener herramientas adecuadas lo hace aún más cómodo.

### ¿Por qué elegir VS Code?

- Es de código abierto y gratuito, además de ser estéticamente atractivo.
- Ofrece funciones de edición completas, como autocompletado y resaltado de sintaxis.
- Permite la depuración de código directamente en el editor.
- Integra Git de manera nativa.
- Ofrece un amplio soporte para complementos y personalización.

## Instalación del Software

Puedes descargar la última versión de VS Code en el sitio web oficial: <https://code.visualstudio.com/>

Generalmente, recomendamos descargar la versión **Stable**. Si no te asustan los errores y deseas probar las últimas características, también puedes optar por la versión **Insiders**.

Una vez completada la descarga e instalación, al abrir el software, verás la página de inicio:

![Página de Inicio](https://media.wiki-power.com/img/20200318224855.png)

## Instalación de Complementos

Para mantener un tamaño de instalación reducido, VS Code incluye solo las funciones más básicas. Sin embargo, si deseas aumentar tu eficiencia, estas funciones por sí solas no son suficientes. Afortunadamente, VS Code ofrece una amplia gama de complementos de terceros para satisfacer tus necesidades específicas.

A continuación, te presentamos algunos complementos útiles (puedes hacer clic en los enlaces para instalarlos):

### Básicos

- [**Paquete de Idioma Chino (Simplificado)**](https://marketplace.visualstudio.com/items?itemName=MS-CEINTL.vscode-language-pack-zh-hans): Permite la localización en chino simplificado de VS Code.
- [**Sincronización de Configuraciones**](https://marketplace.visualstudio.com/items?itemName=Shan.code-settings-sync): Facilita la copia de seguridad de configuraciones y complementos, así como la sincronización en múltiples dispositivos.
  - **Configuración**: Configura tu `GitHub Gist ID` y `GitHub Access Token` correspondientes.
  - **Uso**: Usa `Shift + Alt + U` para cargar y `Shift + Alt + D` para descargar.
  - (La versión más reciente de VS Code ya incluye una función de sincronización, pero este complemento sigue siendo útil para la gestión de versiones).

### Markdown

- [**Markdown Todo en Uno**](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one): Ofrece un soporte avanzado de sintaxis Markdown.
- [**Pegar Imagen en Markdown**](https://marketplace.visualstudio.com/items?itemName=onesdev.vscode-paste-image-plus): Permite pegar imágenes en documentos Markdown y las copia al directorio /res.
- [**Pangu-Markdown**](https://marketplace.visualstudio.com/items?itemName=xlthu.Pangu-Markdown): Normaliza el formato de Markdown (agrega espacios entre caracteres chinos e ingleses, reemplaza la puntuación con normas, etc.).
  - **Configuración**: Habilita la formateo automático al guardar.
- [**vscode-pandoc**](https://marketplace.visualstudio.com/items?itemName=DougFinke.vscode-pandoc): Agrega soporte para Pandoc, lo que permite exportar documentos Markdown a formatos como PDF, Word, HTML, entre otros.
  - **Configuración**: Asegúrate de tener [Pandoc](https://pandoc.org/installing.html) instalado.

### Embellecimiento

- [**Indenticator**](https://marketplace.visualstudio.com/items?itemName=SirTori.indenticator): Resalta la profundidad de la sangría del código.
- [**vscode-icons**](https://marketplace.visualstudio.com/items?itemName=vscode-icons-team.vscode-icons): Agrega iconos atractivos para diferentes formatos de archivo.

### Lenguajes de programación

- [**C/C++**](https://marketplace.visualstudio.com/items?itemName=ms-vscode.cpptools)
- [**Python**](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

### Desarrollo Front-end

- [**Prettier - Code formatter**](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode): Herramienta de formateo automático para lenguajes front-end como HTML, CSS y JavaScript.
  - **Uso**: `Ctrl + Shift + P`
- [**Color Manager**](https://marketplace.visualstudio.com/items?itemName=RoyAction.color-manager): Muestra vistas previas directas de los colores correspondientes a los valores.
- [**Live Server**](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer): Ejecuta páginas web locales dentro de VS Code.

### Otras utilidades

- [**Google Translate**](https://marketplace.visualstudio.com/items?itemName=hancel.google-translate): Proporciona traducción dentro de VS Code.
  - **Uso**: `Ctrl + Alt + T`
- [**Start git-bash**](https://marketplace.visualstudio.com/items?itemName=McCarter.start-git-bash): Agrega la terminal `bash` a VS Code.
- [**TinyPNG**](https://marketplace.visualstudio.com/items?itemName=andi1984.tinypng): Comprime imágenes.
  - **Configuración**: Establece una clave API de `TinyPNG` correcta.
  - **Uso**: Haz clic derecho en las imágenes en el árbol de archivos - `TinyPNG: Comprimir`
- [**Zhihu Daily**](https://marketplace.visualstudio.com/items?itemName=YRM.zhihu): Ideal para procrastinar, navega por las noticias diarias de Zhihu dentro de VS Code.
- [**坤坤鼓励师**](https://marketplace.visualstudio.com/items?itemName=sakura1357.cxk): Si programas durante una hora seguida, recibirás un recordatorio exclusivo de baile de baloncesto de Cai Xukun para tomar un descanso.

## Temas

Puedes elegir tu tema favorito en `Archivo - Preferencias - Tema de color`. Por ejemplo, yo he seleccionado el tema `Monokai Dimmed`:

![Tema de Monokai Dimmed](https://media.wiki-power.com/img/20200319132727.png)

Si sientes que los temas predeterminados no son suficientes, también puedes buscar y descargar temas de tu elección en la tienda de complementos usando la palabra clave "theme".

## Configuraciones Comunes

Para una experiencia más fluida al usar VS Code por primera vez, puedes personalizar algunas configuraciones comunes. Abre la página de configuración a través de `Archivo - Preferencias - Configuración`.

### Guardado Automático

````markdown
Puede configurar `Files: Auto Save` en cualquiera de los tres valores distintos a `off`. En el uso diario, la función de autoguardado resulta bastante conveniente.

### Tipografía

Una fuente de ancho fijo es imprescindible para escribir código. Personalmente, recomiendo [**Microsoft YaHei Mono**](https://github.com/linyuxuanlin/File-host/blob/main/software-development/Microsoft-YaHei-Mono.ttf) como fuente.

Después de descargar el archivo de fuente .ttf, instálelo, reinicie VS Code y, en la sección `Configuración - Editor de texto - Fuente - Font Family`, agregue `'Microsoft YaHei Mono'` al principio de la lista de fuentes para habilitarla.

## Atajos de Teclado Comunes

|          Acción          |           Atajo           |
| :----------------------: | :-----------------------: |
|    Panel de Comandos     | `F1` o `Ctrl + Shift + P` |
|         Terminal         | <code>Ctrl + &#96;</code> |
|  Explorador de Recursos  |    `Ctrl + Shift + E`     |
|     Búsqueda Global      |    `Ctrl + Shift + F`     |
| Gestión de Código Fuente |    `Ctrl + Shift + G`     |
|         Ejecutar         |    `Ctrl + Shift + D`     |
|  Gestión de Extensiones  |    `Ctrl + Shift + X`     |
| Cambio Rápido de Archivo |        `Ctrl + D`         |

## Control de Código Fuente

¿Cansado de tener que ingresar tu nombre de usuario y contraseña cada vez que haces una confirmación en GitHub? Simplemente ejecuta el siguiente comando:

```shell
git config --global credential.helper store
```
````

Luego reinicia VS Code y eso es todo.

## Conclusión

Estos son los ajustes básicos para configurar tu entorno en VS Code. En el próximo artículo, discutiremos en detalle cómo utilizar Git, Jupyter Notebook y fragmentos de código personalizados. ¡Estén atentos!

### Enlaces de Referencia

- [Documentación · Visual Studio Code](https://code.visualstudio.com/docs)
- [¿Por qué elegí usar VS Code para el desarrollo front-end?](https://zhuanlan.zhihu.com/p/28631442)
- [¿Siempre te pide el nombre de usuario y la contraseña al hacer una confirmación en VS Code?](https://www.jianshu.com/p/8854713433c5)
- [Cómo editar bloques de código markdown (snippets) en VS Code](https://www.jianshu.com/p/a87e9ca2d208)
- [Cómo agregar fragmentos de código personalizados en Visual Studio Code](https://blog.walterlv.com/post/add-custom-code-snippet-for-vscode.html##%E5%85%B3%E4%BA%8E%E6%96%87%E4%BB%B6%E5%90%8D%E7%A7%B0)

> Dirección original del artículo: <https://wiki-power.com/>
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

```

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
```
