# Cómo escribir un currículum utilizando Markdown

![](https://media.wiki-power.com/img/20210318220041.png)

Escribir un currículum utilizando Markdown que se pueda previsualizar en línea y exportar como PDF.

**URL de previsualización**: [**cv-template.wiki-power.com**](https://cv-template.wiki-power.com/)

**Cómo exportar como PDF**: En la página web, utiliza la combinación de teclas `Ctrl` + `P` para abrir la interfaz de impresión. Selecciona `Microsoft Print to PDF` como impresora y podrás exportar una versión en PDF de tu currículum.

## Instrucciones de uso

Abre el proyecto [**linyuxuanlin/Markdown-CV-Site**](https://github.com/linyuxuanlin/Markdown-CV-Site) y haz clic en el botón verde "Use this template" para inicializar tu propio repositorio.

Abre [**Vercel**](https://vercel.com/) y haz clic en "New Project". Importa el repositorio de GitHub que acabas de inicializar y configura los siguientes parámetros:

- `FRAMEWORK PRESET`: Selecciona `Other`
- `BUILD COMMAND`: Ingresa `npm run build`
- `OUTPUT DIRECTORY`: Ingresa `dist`

Haz clic en "Next" y espera unos segundos hasta que se genere el sitio web.

Si deseas modificar el contenido del currículum, edita los archivos `_config.yml` y `markdown/resume-template.md` en el directorio raíz. Después de hacer push al repositorio de GitHub, se activará automáticamente la construcción en Vercel.

## Referencias y agradecimientos

Este proyecto se basa en [**BigLiao/markCV**](https://github.com/BigLiao/markCV) y se han realizado algunas simplificaciones y mejoras en la interfaz de usuario. La plantilla del currículum utiliza el contenido predeterminado de [**冷熊简历**](https://cv.ftqq.com/).

- [聊聊简历怎么写？](https://mp.weixin.qq.com/s/P64bm-SBYXyQymfHAR1rqA)

> Dirección original del artículo: <https://wiki-power.com/>
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
