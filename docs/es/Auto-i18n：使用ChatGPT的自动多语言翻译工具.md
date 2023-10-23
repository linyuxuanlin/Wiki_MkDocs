# Auto-i18n: Using the Automatic Multilingual Translation Tool with ChatGPT

Auto-i18n is a tool that utilizes ChatGPT to automatically translate Markdown files into multiple languages. It accomplishes full automation of internationalizing blog articles (i18n - Internationalization). All you need to do is push your blog posts to a GitHub repository, and with the help of GitHub Actions, it will automatically translate them into various languages. Currently, it supports English, Spanish, and Arabic, with plans to add support for more languages in the future.

Key features of Auto-i18n:

- **Batch Multilingual Translation**: Auto-i18n offers batch translation capabilities, allowing you to translate all Markdown documents within an entire directory at once. This significantly enhances the efficiency of multilingual projects.

- **Front Matter Compatibility**: Auto-i18n is compatible with Markdown Front Matter syntax, enabling you to customize translation or replacement rules for different fields.

- **Fixed Content Replacement**: Auto-i18n also supports fixed content replacement. If you want the translations of certain repetitive fields in your documents to remain consistent, this feature can help maintain document consistency.

- **Automated Workflow**: You can use GitHub Actions to implement an automated translation process. With no manual intervention required, the translation work will automatically proceed and update the documents, allowing you to focus more on the content.

## Getting Started

1. Clone the repository to your local machine, rename `env_template.py` to `env.py`, and provide your ChatGPT API key. If you don't have your own API key, you can obtain a free one from [GPT_API_free](https://github.com/chatanywhere/GPT_API_free), or you can use [go-chatgpt-api](https://github.com/linweiyuan/go-chatgpt-api) to convert the web-based ChatGPT into an API.

2. Install the required modules: `pip install -r requirements.txt`.

3. Execute the command `python auto-translater.py` to run the program. It will automatically process all Markdown files in the test directory `testdir/to-translate` and translate them into English, Spanish, and Arabic (with more language support planned for the future).

## Detailed Description

The operation logic of the `auto-translater.py` program is as follows:

1. El programa procesará automáticamente todos los archivos Markdown en el directorio de prueba `testdir/to-translate`. Puedes excluir archivos que no necesitas traducir en la variable `exclude_list`.
2. Los nombres de los archivos procesados se registrarán en el archivo generado automáticamente `processed_list.txt`. La próxima vez que ejecutes el programa, los archivos procesados no se traducirán nuevamente.
3. Para artículos originalmente escritos en inglés, el programa no los volverá a traducir al inglés ni al chino, sino que los traducirá a otros idiomas. Debes agregar el campo `> This post was originally written in English.` en el artículo (asegurándote de dejar una línea en blanco antes y después) para que el programa lo reconozca. Por favor, consulta [este artículo de prueba en inglés](https://github.com/linyuxuanlin/Auto-i18n/blob/main/testdir/to-translate/测试文章_en.md) como referencia.
4. Si necesitas volver a traducir un artículo específico (por ejemplo, si la traducción no es precisa o si el contenido del artículo ha cambiado), puedes agregar el campo `[translate]` en el artículo (también dejando una línea en blanco antes y después). Esto ignorará las reglas de `exclude_list` y `processed_list` y forzará la traducción. Consulta [este artículo de prueba con marcado forzado](https://github.com/linyuxuanlin/Auto-i18n/blob/main/testdir/to-translate/测试文章_force-mark.md) para más detalles.
5. Si el archivo Markdown contiene Front Matter, se aplicarán las siguientes reglas según lo definido en el programa:
   1. Traducción automática: realizada por ChatGPT. Adecuado para el título del artículo o el campo de descripción del artículo.
   2. Reemplazo de campo fijo: aplicado a campos como categorías o etiquetas. Por ejemplo, si deseas que el mismo nombre de etiqueta en chino no se traduzca a diferentes etiquetas en inglés y cause errores de indexación.
   3. Sin procesamiento: si el campo no se encuentra en ninguna de las dos reglas anteriores, se mantendrá sin cambios. Esto se aplica a campos como fechas y URL.

## Guía de Automatización de GitHub Actions

Puedes crear un archivo `.github/workflows/ci.yml` en tu propio repositorio de proyectos. Cuando se detectan actualizaciones en el repositorio de GitHub, GitHub Actions puede realizar automáticamente el proceso de traducción y realizar un commit automático en el repositorio original.

Puedes consultar el contenido del archivo `ci.yml` en este [modelo de plantilla](https://github.com/linyuxuanlin/Auto-i18n/blob/main/ci_template.yml).

Debes agregar dos secrets en la sección de `Settings` de tu repositorio en `Secrets and variables` - `Repository secrets`: `CHATGPT_API_BASE` y `CHATGPT_API_KEY`. Asegúrate de comentar la línea `import env` en el programa `auto-translater.py`.

## Solución de Problemas

1. Si necesitas verificar la disponibilidad de la clave de API de ChatGPT, puedes utilizar el programa [verify-api-key.py](https://github.com/linyuxuanlin/Auto-i18n/blob/main/Archive/verify-api-key.py) para realizar pruebas. Si estás utilizando la API oficial en China, necesitarás un proxy local.
2. Si el Front Matter en Markdown no se reconoce correctamente, puedes utilizar el programa [detect_front_matter.py](https://github.com/linyuxuanlin/Auto-i18n/blob/main/Archive/detect_front_matter.py) para realizar pruebas.
3. Si encuentras problemas al usar GitHub Actions, primero verifica si las referencias de rutas son correctas (por ejemplo, `dir_to_translate`, `dir_translated_en`, `dir_translated_es`, `dir_translated_ar`, `processed_list`).

```markdown
1. En algunas circunstancias especiales, es posible que se produzcan traducciones inexactas o que algunos campos no se traduzcan. Se recomienda verificar manualmente las traducciones después de realizarlas antes de publicar el artículo.

2. (Resuelto) ~~Si el Markdown contiene Front Matter, se mantendrá el contenido original del Front Matter. La funcionalidad de traducción de parámetros en la sección Front Matter está en desarrollo.~~

## Contribuciones

¡Te invitamos a contribuir a este proyecto! Si deseas aportar código, informar sobre problemas o hacer sugerencias, consulta nuestra [Guía de Contribución](https://github.com/linyuxuanlin/Auto-i18n/blob/main/CONTRIBUTING.md).

## Derechos de Autor y Licencia

Este proyecto está bajo la Licencia MIT. Puedes consultar los detalles en [Licencia MIT](https://github.com/linyuxuanlin/Auto-i18n/blob/main/LICENSE).

## Problemas y Soporte

Si experimentas cualquier problema al utilizar Auto-i18n o necesitas asistencia técnica, no dudes en [reportar un problema](https://github.com/linyuxuanlin/Auto-i18n/issues).

Mi blog utiliza Auto-i18n para brindar soporte en varios idiomas. Puedes ver una demostración en [Power's Wiki](https://wiki-power.com).

[![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/202310222223670.png)](https://wiki-power.com)

## Agradecimientos

- Agradecemos a [chatanywhere/GPT_API_free](https://github.com/chatanywhere/GPT_API_free) por proporcionar la clave gratuita del API de ChatGPT.
- Agradecemos a [linweiyuan/go-chatgpt-api](https://github.com/linweiyuan/go-chatgpt-api) por ofrecer el método para convertir la versión web de ChatGPT en un API.

[![Gráfico de Historial de Estrellas](https://api.star-history.com/svg?repos=linyuxuanlin/Auto-i18n&type=Date)](https://star-history.com/#linyuxuanlin/Auto-i18n&Date)

> Dirección original del artículo: <https://wiki-power.com/>
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.
```

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.