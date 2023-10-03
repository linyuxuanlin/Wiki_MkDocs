# Construyendo una base de conocimientos personal - Basado en Docusaurus

Continuando con el artículo anterior [**Por qué necesitas una base de conocimientos**](https://wiki-power.com/%E4%B8%BA%E4%BB%80%E4%B9%88%E4%BD%A0%E9%9C%80%E8%A6%81%E4%B8%80%E4%B8%AA%E7%9F%A5%E8%AF%86%E5%BA%93), este artículo detallará la construcción de una base de conocimientos basada en el marco de trabajo Docusaurus.

Antes de comenzar, asegúrese de tener lo siguiente:

- Acceso a internet sin restricciones
- Capacidad para adaptarse a situaciones imprevistas
- Un poco de conocimiento de inglés

## Configuración del entorno local

### Instalación de Node.js

Visite el [**sitio web oficial de Node.js**](https://nodejs.org/zh-cn/) para descargar e instalar Node.js.

### Instalación y configuración de VS Code

Usaremos VS Code como editor local para modificar el marco del sitio web y escribir artículos.

Primero, descargue e instale VS Code desde el [**sitio web oficial de VS Code**](https://code.visualstudio.com/).

Después de instalar el software, puede instalar los siguientes dos complementos:

- [**Chinese (Simplified) Language Pack**](https://marketplace.visualstudio.com/items?itemName=MS-CEINTL.vscode-language-pack-zh-hans): para traducir la interfaz de usuario de VS Code al chino
- [**Markdown All in One**](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one): para proporcionar soporte para más sintaxis de Markdown

Es posible que deba reiniciar VS Code después de instalar los complementos.

Para obtener instrucciones de configuración más detalladas, consulte [**Guía de productividad de VS Code - Configuración del entorno**](https://wiki-power.com/VSCode%E7%94%9F%E4%BA%A7%E5%8A%9B%E6%8C%87%E5%8D%97-%E7%8E%AF%E5%A2%83%E9%85%8D%E7%BD%AE) (en chino).

### Instalación del marco de trabajo Docusaurus

Cambie al directorio donde desea crear el proyecto del sitio web.

Por ejemplo, si desea crear una carpeta llamada `wiki` en la unidad D de su computadora como proyecto de base de conocimientos, seleccione `Archivo` - `Abrir carpeta` en VS Code, haga clic en la unidad D y seleccione la carpeta `wiki`.

Inicialice el sitio web usando npx:

```shell
npx @docusaurus/init@latest init [name] [template]
```

Por ejemplo, si el nombre de la carpeta del proyecto del sitio web es `wiki`, reemplace `[name]` con `wiki`. Según la [**documentación oficial**](https://v2.docusaurus.io/docs/installation#scaffold-project-website), `[template]` se refiere al tema de la plantilla del sitio web. Aquí, reemplazaremos `[template]` con `classic`. Por lo tanto, el comando que ejecutaremos es:

```shell
npx @docusaurus/init@latest init wiki classic
```

En VS Code, use el atajo `Ctrl` + <code>`</code> para abrir la terminal, pegue el comando anterior y presione Enter. Espere a que se complete la carga.

Una vez que se complete la carga, use el siguiente comando en la terminal para cambiar al directorio del proyecto del sitio web:

```shell
cd [name]
```

Reemplace `[name]` con el nombre de la carpeta del proyecto del sitio web. Por ejemplo, si usó `wiki` en el paso anterior, use `wiki` aquí.

Luego, ejecute el siguiente comando:

```shell
npm run start
```

Esto iniciará la implementación local del sitio web. Espere a que se complete la implementación y se abrirá automáticamente la página [**localhost:3000**](localhost:3000) en su navegador. Si todo va bien, verá que el sitio web se ha generado correctamente.

## Implementación del sitio web en la nube

En el paso anterior, hemos generado con éxito un sitio web, pero solo se ha implementado localmente y no se puede acceder a él desde Internet. Necesitamos implementar el sitio web en un servidor en la nube para que otros usuarios puedan acceder a él desde Internet.

### Registrarse en GitHub

Regístrese en GitHub en la [**página web oficial de GitHub**](https://github.com/join).

### Instalar Git

Descargue el software Git desde el [**sitio web oficial de Git**](https://git-scm.com/downloads) y complete la instalación.

Reinicie VS Code, abra la terminal y pegue el siguiente comando para inicializar Git:

```shell
git config --global user.name "username"
git config --global user.email "email@example.com"
```

Aquí, debe reemplazar `"username"` con su nombre de usuario de Git para enviar confirmaciones, se recomienda que sea el mismo que el nombre de usuario de la cuenta que acaba de registrar en GitHub. Por ejemplo, lo reemplacé con `linyuxuanlin`. `"email@example.com"` también debe reemplazarse con el correo electrónico registrado en GitHub.

Para obtener más información sobre la configuración, consulte este artículo [**Git学习笔记**](https://wiki-power.com/Git%E5%AD%A6%E4%B9%A0%E7%AC%94%E8%AE%B0).

### Configurar el repositorio del proyecto en VS Code

Para poder enviar el proyecto al servidor de GitHub, debemos configurar el repositorio Git del proyecto en VS Code y cargarlo en GitHub.

En VS Code, use el atajo `Ctrl` + `Shift` + `G` para cambiar a la interfaz de gestión de código fuente, inicialice el repositorio Git del proyecto y realice la primera confirmación.

Luego, use el atajo `Ctrl` + `Alt` + `S` para enviar el repositorio Git local a GitHub (inicie sesión en su cuenta de GitHub según las instrucciones).

### Implementar el sitio web en la nube con Vercel

La función de Vercel es similar a GitHub Action + GitHub Pages, es decir, implementación continua automática + presentación de sitios web estáticos. Elegí Vercel porque los sitios web estáticos que genera son mucho más rápidos que los de GitHub Pages cuando se accede desde China.

Primero, vaya directamente a la [**página de inicio de sesión de GitHub de Vercel**](https://github.com/login?client_id=Iv1.9d7d662ea00b8481&return_to=%2Flogin%2Foauth%2Fauthorize%3Fclient_id%3DIv1.9d7d662ea00b8481%26scope%3Dread%253Auser%252Cuser%253Aemail%26state%3DFdx6thivZ89LeAihPfRiiYf9) y regístrese en Vercel con su cuenta de GitHub.

Después de completar el registro, haga clic en `New Project` en la página web e importe el repositorio correspondiente de GitHub (por ejemplo, el repositorio `wiki` que creamos anteriormente). Es posible que deba iniciar sesión en GitHub nuevamente según las instrucciones. Después de la importación, haga clic en `Next` para continuar y el sitio web se implementará rápidamente.

## Conclusión

En este artículo, hemos implementado la implementación local y en la nube de una base de conocimientos basada en Docusaurus. Si tiene algún problema durante el proceso, puede ponerse en contacto conmigo a través de [**WeChat**](https://wiki-power.com/WeChat). En el próximo artículo (por actualizar), explicaré en detalle la configuración personalizada.

## Referencias y agradecimientos

- [Docs·Docusaurus](https://v2.docusaurus.io/docs/)

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.