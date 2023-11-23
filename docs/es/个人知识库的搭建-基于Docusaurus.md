# Creación de una base de conocimientos personal - Basada en Docusaurus

Continuando desde el artículo anterior [**Por qué necesitas una base de conocimientos**](https://wiki-power.com/%E4%B8%BA%E4%BB%80%E4%B9%88%E4%BD%A0%E9%9C%80%E8%A6%81%E4%B8%80%E4%B8%AA%E7%9F%A5%E8%AF%86%E5%BA%93), en este artículo, vamos a realizar una explicación detallada sobre la construcción de una base de conocimientos utilizando el marco Docusaurus.

Antes de comenzar con este artículo, asegúrate de tener lo siguiente preparado:

- Acceso a Internet sin restricciones.
- La capacidad de adaptarse a situaciones cambiantes.
- Un conocimiento básico de inglés.

## Configuración del entorno local

### Instalación de Node.js

Visita el [**sitio web oficial de Node.js**](https://nodejs.org/zh-cn/) y descarga e instala Node.js.

### Instalación y configuración de VS Code

Utilizaremos VS Code como editor local para modificar el marco del sitio y escribir artículos.

En primer lugar, descarga e instala VS Code desde el [**sitio web oficial de VS Code**](https://code.visualstudio.com/).

Una vez que la instalación del software esté completa, puedes optar por instalar los siguientes dos complementos:

- [**Paquete de idioma chino simplificado**](https://marketplace.visualstudio.com/items?itemName=MS-CEINTL.vscode-language-pack-zh-hans): Esto traducirá la interfaz de VS Code al chino simplificado.
- [**Markdown All in One**](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one): Proporciona un mayor soporte para la sintaxis Markdown.

Después de instalar los complementos, es posible que necesites reiniciar VS Code según las indicaciones.

Para obtener instrucciones más detalladas sobre la configuración, puedes consultar el artículo [**Guía de productividad de VS Code - Configuración del entorno**](https://wiki-power.com/VSCode%E7%94%9F%E4%BA%A7%E5%8A%9B%E6%8C%87%E5%8D%97-%E7%8E%AF%E5%A2%83%E9%85%8D%E7%BD%AE).

### Instalación del marco Docusaurus

Dirígete al directorio donde deseas crear el proyecto del sitio web.

Por ejemplo, si quieres crear un proyecto de base de conocimientos en una carpeta llamada "wiki" en la unidad D de tu computadora, abre VS Code, selecciona "Archivo" - "Abrir carpeta", elige la unidad D y selecciona la carpeta "wiki".

Utiliza el comando npx para inicializar el sitio web:

```shell
npx @docusaurus/init@latest init [nombre] [plantilla]
```

Por ejemplo, si el nombre de la carpeta de tu proyecto de sitio web es "wiki", sustituye "[nombre]" por "wiki" y, según la [**documentación oficial**](https://v2.docusaurus.io/docs/installation#scaffold-project-website), "[plantilla]" se refiere al tema de la plantilla del sitio web. En este caso, puedes sustituirlo por "classic". Por lo tanto, el comando que debes ejecutar es el siguiente:

```shell
npx @docusaurus/init@latest init wiki classic
```

Dentro de VS Code, utiliza el atajo de teclado `Ctrl` + <code>`</code> para abrir la terminal, pega la línea de código anterior y pulsa Enter. Espera pacientemente a que se complete la carga.

Cuando la carga se complete, utiliza el siguiente comando en la terminal para cambiar al directorio del proyecto del sitio web:

```shell
cd [nombre]
```

Sustituye "[nombre]" por el nombre de la carpeta de tu proyecto de sitio web, que en nuestro caso es "wiki" según el paso anterior.

Luego, ejecuta el siguiente comando:

```shell
npm run start
```

Esto iniciará la implementación local del sitio web. Después de que se complete la implementación, se abrirá automáticamente la página [**localhost:3000**](localhost:3000) en tu navegador. Si todo sale bien, verás que el sitio web se ha generado con éxito.

## Implementación del sitio web en la nube

En el paso anterior, logramos generar con éxito el sitio web, pero solo se desplegó localmente y no se puede acceder a él desde Internet. Necesitamos desplegar el sitio web en un servidor en la nube para que otros usuarios puedan acceder a él desde Internet.

### Registrar una cuenta en GitHub

Regístrese en [**el sitio web de GitHub**](https://github.com/join).

### Instalar Git

Descargue el software Git desde [**el sitio web oficial de Git**](https://git-scm.com/downloads) y realice la instalación.

Reinicie VS Code, abra la terminal y pegue los siguientes comandos para inicializar Git:

```shell
git config --global user.name "nombre_de_usuario"
git config --global user.email "correo@example.com"
```

En este punto, reemplace `"nombre_de_usuario"` con su nombre de usuario de Git, se recomienda que coincida con el nombre de usuario que acaba de registrar en GitHub, por ejemplo, yo lo reemplacé con `linyuxuanlin`. De manera similar, reemplace `"correo@example.com"` con la dirección de correo electrónico que utilizó para registrarse en GitHub.

Para obtener instrucciones de configuración más detalladas, consulte este artículo [**Notas de aprendizaje de Git**](https://wiki-power.com/Git%E5%AD%A6%E4%B9%A0%E7%AC%94%E8%AE%B0) (en chino).

### Configurar el repositorio del proyecto en VS Code

Para poder enviar los cambios a GitHub en el siguiente paso, necesitamos configurar el repositorio Git del proyecto en VS Code y subirlo a GitHub.

Dentro de VS Code, use la combinación de teclas `Ctrl` + `Shift` + `G` para abrir la interfaz de gestión de código fuente, inicialice el repositorio Git del proyecto y realice el primer commit.

Luego, use la combinación de teclas `Ctrl` + `Alt` + `S` para enviar el repositorio Git local a GitHub (siga las indicaciones para iniciar sesión en su cuenta de GitHub).

### Usar Vercel para desplegar el sitio web en la nube

La funcionalidad de Vercel aquí es equivalente a GitHub Actions + GitHub Pages, es decir, despliegue continuo automático y presentación de sitios web estáticos. Se elige Vercel debido a que la velocidad de acceso a los sitios web estáticos generados por Vercel es mucho más rápida en comparación con GitHub Pages, especialmente en China.

En primer lugar, visite directamente [**la página de inicio de sesión de GitHub de Vercel**](https://github.com/login?client_id=Iv1.9d7d662ea00b8481&return_to=%2Flogin%2Foauth%2Fauthorize%3Fclient_id%3DIv1.9d7d662ea00b8481%26scope%3Dread%253Auser%252Cuser%253Aemail%26state%3DFdx6thivZ89LeAihPfRiiYf9) y registre una cuenta de Vercel utilizando su cuenta de GitHub.

Una vez completado, haga clic en "Nuevo Proyecto" en el sitio web de Vercel e importe el repositorio correspondiente de GitHub (por ejemplo, el repositorio "wiki" que creamos anteriormente). Es posible que deba seguir las indicaciones y volver a iniciar sesión en GitHub. Después de la importación, simplemente haga clic en "Siguiente" y, en poco tiempo, su sitio web estará desplegado con éxito.

## Resumen

En este artículo, logramos desplegar una base de conocimiento basada en Docusaurus tanto localmente como en la nube. Si encuentra algún problema durante este proceso, no dude en ponerse en contacto conmigo en [**WeChat**](https://wiki-power.com/WeChat). En el próximo artículo (pendiente de actualización), explicaré en detalle la configuración personalizada.

## Referencias y Agradecimientos

- [Documentación de Docusaurus](https://v2.docusaurus.io/docs/)

> Dirección original del artículo: <https://wiki-power.com/>
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.