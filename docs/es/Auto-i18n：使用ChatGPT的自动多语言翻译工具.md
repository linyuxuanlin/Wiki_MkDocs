# Auto-i18n: Utilizando la herramienta de traducción automática multilingüe de ChatGPT

Auto-i18n es una herramienta que utiliza ChatGPT para traducir automáticamente archivos Markdown a varios idiomas de manera masiva.

Logra la completa automatización de la internacionalización (i18n) de artículos de blog. Simplemente debes enviar tus publicaciones a un repositorio de GitHub y, gracias a las acciones de GitHub, se traducirán automáticamente a varios idiomas. Actualmente, se admiten inglés, español y árabe, con la promesa de soportar más idiomas en el futuro.

**Dirección del proyecto**: [**linyuxuanlin/Auto-i18n**](https://github.com/linyuxuanlin/Auto-i18n)

Así es cómo se ve mi blog después de implementar la internacionalización:

![](https://img.wiki-power.com/d/wiki-media/img/202310151317234.png)

## Puesta en marcha rápida

1. En primer lugar, clona el repositorio en tu máquina local.
2. Renombra `env_template.py` a `env.py` y proporciona tu información de API de ChatGPT. Puedes obtener una clave API gratuita en el proyecto [**chatanywhere/GPT_API_free**](https://github.com/chatanywhere/GPT_API_free).
3. Ejecuta `pip install openai` para instalar las dependencias necesarias.
4. Ejecuta el programa `auto-translater`. Automáticamente procesará todos los archivos Markdown en el directorio de prueba `testdir/to-translate`, traduciéndolos en masa a inglés, español y árabe.

## Descripción detallada

El funcionamiento del programa `auto-translater.py` es el siguiente:

1. El programa procesará automáticamente todos los archivos Markdown en el directorio de prueba `testdir/to-translate`. Puedes excluir archivos que no necesitas traducir mediante la variable `exclude_list`.
2. Los nombres de los archivos procesados se registrarán en un archivo llamado `processed_list.txt`, de forma que en ejecuciones posteriores, los archivos ya procesados no se traducirán nuevamente.
3. Para los artículos originalmente escritos en inglés, el programa no los traducirá nuevamente al inglés, ni los devolverá al chino, sino que los traducirá a otros idiomas. Debes agregar la siguiente línea al artículo para que el programa lo identifique: `> This post was originally written in English.` (asegúrate de dejar una línea en blanco arriba y abajo). Consulta [este artículo de prueba en inglés](https://github.com/linyuxuanlin/Auto-i18n/blob/main/testdir/to-translate/测试文章_en.md) como referencia.
4. Si necesitas volver a traducir un artículo específico (por ejemplo, si la traducción no es precisa o el contenido ha cambiado), puedes agregar `[translate]` al artículo (también asegúrate de dejar una línea en blanco arriba y abajo). Esto anulará las reglas de `exclude_list` y `processed_list`. Consulta [este artículo de prueba con marca de fuerza](https://github.com/linyuxuanlin/Auto-i18n/blob/main/testdir/to-translate/测试文章_force-mark.md) como referencia.

## Guía de automatización con GitHub Actions

Puedes crear un archivo `.github/workflows/ci.yml` en tu propio repositorio de proyectos. Esto permitirá que, cuando se detecten actualizaciones en el repositorio de GitHub, GitHub Actions realice automáticamente la traducción y realice un commit automático en el repositorio original.

Puedes utilizar el contenido del archivo `ci.yml` como referencia a partir de esta plantilla: [ci_template.yml](https://github.com/linyuxuanlin/Auto-i18n/blob/main/ci_template.yml).

Deberás agregar dos secrets en la sección `Settings` - `Secrets and variables` - `Repository secrets` de tu repositorio: `CHATGPT_API_BASE` y `CHATGPT_API_KEY`. Además, debes comentar la línea `import env` en el programa `auto-translater.py`.

## Troubleshooting

1. Si necesitas verificar la disponibilidad de la clave de la API de ChatGPT, puedes consultar el programa [verify-api-key.py](https://github.com/linyuxuanlin/Auto-i18n/blob/main/Archive/verify-api-key.py).
2. Cuando te encuentres con problemas al usar GitHub Actions, asegúrate primero de verificar si las rutas están referenciadas correctamente (por ejemplo, `dir_to_translate`, `dir_translated_en`, `dir_translated_es`, `dir_translated_ar`, `processed_list`).

## Issues to Resolve

1. Si el archivo Markdown contiene Front Matter, es posible que se vea afectado por la traducción, lo que puede causar problemas. Mi solución es evitar el uso de Front Matter y utilizar directamente el título de primer nivel como el título del artículo.
2. Si el artículo está incompleto, puede ocurrir que ChatGPT te ayude a traducir y completar automáticamente el contenido (un poco misterioso).
3. En algunas situaciones especiales, la traducción puede no ser precisa o algunos campos pueden quedar sin traducir. Después de la traducción, es necesario verificar y ajustar manualmente.

## Contributions

¡Te invitamos a contribuir a este proyecto! Si deseas aportar código, reportar problemas o hacer sugerencias, consulta nuestra [guía de contribución](https://github.com/linyuxuanlin/Auto-i18n/blob/main/CONTRIBUTING.md).

## Copyright and License

Este proyecto está bajo la [licencia MIT](https://github.com/linyuxuanlin/Auto-i18n/blob/main/LICENSE).

## Issues and Support

Si encuentras cualquier problema al utilizar Auto-i18n o necesitas asistencia técnica, no dudes en [presentar un problema](https://github.com/linyuxuanlin/Auto-i18n/issues).

## References and Acknowledgments

Agradecemos a [**chatanywhere/GPT_API_free**](https://github.com/chatanywhere/GPT_API_free) por proporcionar la clave de la API de ChatGPT de forma gratuita.

> Dirección original del artículo: <https://wiki-power.com/>
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.