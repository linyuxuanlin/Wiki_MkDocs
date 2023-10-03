# Cómo escribir un currículum vitae en Markdown

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210318220041.png)

Escriba un currículum vitae en Markdown que se pueda previsualizar en línea y exportar en formato PDF.

**URL de previsualización**: [**cv-template.wiki-power.com**](https://cv-template.wiki-power.com/)

**Cómo exportar en PDF**: Use la combinación de teclas `Ctrl` + `P` en la página web para abrir la ventana de impresión, seleccione `Microsoft Print to PDF` como impresora y podrá exportar una versión en PDF de su currículum vitae.

## Instrucciones de uso

Abra el proyecto [**linyuxuanlin/Markdown-CV-Site**](https://github.com/linyuxuanlin/Markdown-CV-Site), haga clic en el botón verde `Use this template` para inicializar su propio repositorio.

Abra [**Vercel**](https://vercel.com/), haga clic en `New Project`, importe el repositorio de GitHub que acaba de inicializar y configure los siguientes parámetros:

- `FRAMEWORK PRESET`: seleccione `Other`
- `BUILD COMMAND`: escriba `npm run build`
- `OUTPUT DIRECTORY`: escriba `dist`

Haga clic en siguiente y espere unos segundos para que se genere el sitio web.

Si desea modificar el contenido de su currículum vitae, edite los archivos `_config.yml` y `markdown/resume-template.md` en el directorio raíz y, después de enviarlos al repositorio de GitHub, se iniciará automáticamente la construcción en Vercel.

## Referencias y agradecimientos

Este proyecto se basa en [**BigLiao/markCV**](https://github.com/BigLiao/markCV) y se han realizado algunas mejoras en la interfaz de usuario. La plantilla del currículum vitae utiliza el contenido predeterminado de [**冷熊简历**](https://cv.ftqq.com/).

- [¿Cómo escribir un currículum vitae?](https://mp.weixin.qq.com/s/P64bm-SBYXyQymfHAR1rqA)

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.