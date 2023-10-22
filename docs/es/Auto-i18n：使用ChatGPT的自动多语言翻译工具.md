# Auto-i18n: Utilizando la herramienta de traducción automática multilingüe de ChatGPT

Auto-i18n es una herramienta que utiliza ChatGPT para traducir automáticamente archivos Markdown a varios idiomas de forma masiva. Logra la completa automatización de la internacionalización (i18n) de artículos de blog. Simplemente sube tus entradas de blog a un repositorio de GitHub y utiliza GitHub Actions para traducirlas automáticamente a varios idiomas (actualmente se admiten inglés, español y árabe, con planes de agregar más idiomas en el futuro).

Las principales características de Auto-i18n son las siguientes:

- **Traducción masiva multilingüe**: Auto-i18n ofrece una funcionalidad de traducción masiva que te permite traducir múltiples documentos Markdown en una sola vez, aumentando significativamente la eficiencia de los proyectos de internacionalización.
- **Compatibilidad con Front Matter**: Auto-i18n es compatible con la sintaxis de Front Matter en Markdown, lo que te permite personalizar las reglas de traducción o sustitución para diferentes campos.
- **Sustitución de contenido fijo**: Auto-i18n también admite la sustitución de contenido fijo. Si deseas que las traducciones de ciertos campos repetitivos en el documento se mantengan iguales, esta función te ayudará a mantener la coherencia del documento.
- **Flujo de trabajo automatizado**: Puedes automatizar el proceso de traducción con GitHub Actions. Sin intervención manual, el trabajo de traducción se realiza automáticamente y se actualizan los documentos, lo que te permite centrarte más en el contenido.

## Puesta en marcha rápida

1. Clona el repositorio en tu máquina local, cambia el nombre de `env_template.py` a `env.py` y proporciona tu API de ChatGPT. Si no tienes una API propia, puedes obtener una gratuita en [GPT_API_free](https://github.com/chatanywhere/GPT_API_free) o utilizar [go-chatgpt-api](https://github.com/linweiyuan/go-chatgpt-api) para convertir la versión web de ChatGPT en una API.
2. Instala los módulos necesarios con el comando `pip install -r requirements.txt`.
3. Ejecuta el comando `python auto-translater.py` para ejecutar el programa. Automáticamente procesará todos los archivos Markdown en el directorio de prueba `testdir/to-translate` y los traducirá a inglés, español y árabe (con planes de agregar más idiomas en el futuro).

## Descripción detallada

El flujo de trabajo del programa `auto-translater.py` es el siguiente:

1. El programa procesará automáticamente todos los archivos Markdown en el directorio de prueba `testdir/to-translate`. Puedes excluir archivos que no desees traducir especificándolos en la variable `exclude_list`.
2. Los nombres de los archivos procesados se registrarán en el archivo generado automáticamente `processed_list.txt`. Cuando ejecutes el programa nuevamente, los archivos previamente procesados no se traducirán de nuevo.
3. Para los artículos escritos originalmente en inglés, el programa no los traducirá nuevamente al inglés ni los revertirá al chino; en su lugar, los traducirá a otros idiomas. Debes agregar el campo `> Este post fue escrito originalmente en inglés.` (asegurándote de dejar una línea en blanco antes y después) para que el programa lo identifique. Consulta [este ejemplo](testdir/to-translate/测试文章_en.md).
4. Si necesitas volver a traducir un artículo específico (por ejemplo, si la traducción no es precisa o si el contenido del artículo ha cambiado), puedes agregar el campo `[translate]` en el artículo (también con una línea en blanco antes y después). Esto anulará las reglas de `exclude_list` y `processed_list` y forzará la traducción. Consulta [este ejemplo](testdir/to-translate/测试文章_force-mark.md).
5. Si el archivo Markdown contiene Front Matter, se seguirán las reglas definidas en el programa en `front_matter_translation_rules`:
   1. Traducción automática: realizada por ChatGPT. Esto es aplicable a campos como el título y la descripción del artículo.
   2. Sustitución de campos fijos: útil para campos como categorías o etiquetas. Por ejemplo, si tienes un nombre de etiqueta en chino que no deseas que se traduzca a diferentes etiquetas en inglés, para evitar confusiones en los índices.
   3. Sin procesamiento alguno: si el campo no se encuentra en ninguna de las dos reglas anteriores, se mantendrá el texto original, lo que es adecuado para campos como la fecha o la URL.

## Guía de Automatización de GitHub Actions

Puedes crear un archivo `.github/workflows/ci.yml` en tu propio repositorio de proyectos. Este archivo permitirá que GitHub Actions realice automáticamente tareas de traducción y haga commits automáticos en tu repositorio cuando detecte actualizaciones en el repositorio de GitHub.

El contenido de `ci.yml` se puede basar en la plantilla que se encuentra en [ci_template.yml](ci_template.yml).

Para que funcione, debes agregar dos secretos en la sección `Settings` de tu repositorio: `CHATGPT_API_BASE` y `CHATGPT_API_KEY`. Además, asegúrate de comentar la línea `import env` en el programa `auto-translater.py`.

## Solución de Problemas

1. Si necesitas verificar la disponibilidad de la clave de la API de ChatGPT, puedes utilizar el programa [verify-api-key.py](Archive/verify-api-key.py) para realizar pruebas. Si estás utilizando la API oficial en China, necesitarás un proxy local.

2. Si el Front Matter en el Markdown no se reconoce correctamente, puedes utilizar el programa [detect_front_matter.py](Archive/detect_front_matter.py) para hacer pruebas.

3. Si encuentras problemas al utilizar GitHub Actions, asegúrate de verificar primero que las referencias de los directorios sean correctas (por ejemplo, `dir_to_translate`, `dir_translated_en`, `dir_translated_es`, `dir_translated_ar`, `processed_list`).

## Problemas Pendientes

1. En algunas situaciones especiales, la traducción puede no ser precisa, o es posible que ciertos campos no se traduzcan correctamente. Se recomienda verificar manualmente la traducción antes de publicar el artículo.

2. (Ya resuelto) ~~Si el Markdown contiene Front Matter, se conservará el contenido original del Front Matter. La funcionalidad de traducir los parámetros del Front Matter está en desarrollo.~~

## Contribuciones

¡Te invitamos a contribuir a este proyecto! Si deseas aportar código, informar de problemas o hacer sugerencias, consulta la [Guía de Contribución](CONTRIBUTING.md).

## Derechos de Autor y Licencia

Este proyecto se encuentra bajo la licencia [MIT](LICENSE).

## Problemas y Soporte

Si tienes algún problema al utilizar Auto-i18n o necesitas soporte técnico, no dudes en [informarlo](https://github.com/linyuxuanlin/Auto-i18n/issues).

Mi blog utiliza Auto-i18n para admitir múltiples idiomas. Puedes ver una demostración en [Power's Wiki](https://wiki-power.com).

[![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/202310222223670.png)](https://wiki-power.com)

## Agradecimientos

- Agradecemos a [chatanywhere/GPT_API_free](https://github.com/chatanywhere/GPT_API_free) por proporcionar una clave gratuita de la API de ChatGPT.
- Agradecemos a [linweiyuan/go-chatgpt-api](https://github.com/linweiyuan/go-chatgpt-api) por proporcionar un método para convertir ChatGPT en versión web a una API.

[![Gráfico de Historial de Estrellas](https://api.star-history.com/svg?repos=linyuxuanlin/Auto-i18n&type=Date)](https://star-history.com/#linyuxuanlin/Auto-i18n&Date)

> Dirección original del artículo: <https://wiki-power.com/>
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.