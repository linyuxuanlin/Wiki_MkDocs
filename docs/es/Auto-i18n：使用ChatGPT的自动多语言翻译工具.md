# Auto-i18n: herramienta de traducción automática multilingüe utilizando ChatGPT

Auto-i18n es una herramienta que utiliza ChatGPT para traducir automáticamente archivos Markdown a varios idiomas.

Implementa la internacionalización (i18n) de artículos de blogs de manera completamente automatizada. Solo necesita enviar su publicación al repositorio de GitHub y, con la ayuda de GitHub Actions, se traducirá automáticamente a varios idiomas. (Actualmente admite inglés, español y árabe, y se agregarán más idiomas en el futuro).

**Dirección del proyecto**: [**linyuxuanlin/Auto-i18n**](https://github.com/linyuxuanlin/Auto-i18n)

El resultado de mi blog después de implementar i18n:

![](https://img.wiki-power.com/d/wiki-media/img/202310151317234.png)

## Guía rápida

1. Primero, clone el repositorio en su computadora.
2. Renombre `env_template.py` a `env.py` y complete su información de API de ChatGPT. Puede solicitar una clave API gratuita en el proyecto [**chatanywhere/GPT_API_free**](https://github.com/chatanywhere/GPT_API_free).
3. Ejecute `pip install openai` para instalar las dependencias necesarias.
4. Ejecute el programa `auto-translater`, que procesará automáticamente todos los archivos Markdown en el directorio de prueba `testdir/to-translate` y los traducirá a inglés, español y árabe.

## Descripción detallada

La lógica de ejecución del programa `auto-translater.py` es la siguiente:

1. El programa procesará automáticamente todos los archivos Markdown en el directorio de prueba `testdir/to-translate`. Puede excluir archivos que no necesite traducir en la variable `exclude_list`.
2. Los nombres de archivo procesados se registrarán en `processed_list.txt`, que se generará automáticamente. La próxima vez que ejecute el programa, los archivos procesados no se volverán a traducir.
3. Para los artículos escritos originalmente en inglés, el programa no los volverá a traducir al inglés ni los traducirá de regreso al chino, sino que los traducirá a otros idiomas. Debe agregar el campo `> This post was originally written in English.` (asegúrese de dejar una línea en blanco arriba y abajo) en el artículo para que el programa lo reconozca. Consulte [测试文章\_en.md](https://github.com/linyuxuanlin/Auto-i18n/blob/main/testdir/to-translate/测试文章_en.md) para obtener más información.
4. Si necesita volver a traducir un artículo específico (por ejemplo, si los resultados de la traducción no son precisos o si el contenido del artículo ha cambiado), puede agregar el campo `[translate]` en el artículo (también debe dejar una línea en blanco arriba y abajo). Esto ignorará las reglas de `exclude_list` y `processed_list` y forzará el procesamiento de la traducción. Consulte [测试文章\_force-mark.md](https://github.com/linyuxuanlin/Auto-i18n/blob/main/testdir/to-translate/测试文章_force-mark.md) para obtener más información.

## Guía de automatización de GitHub Actions

Puede crear `.github/workflows/ci.yml` en su propio repositorio de proyectos para que, cuando se detecte una actualización en el repositorio de GitHub, se realice automáticamente el procesamiento de traducción y se confirme automáticamente en el repositorio original.

El contenido de `ci.yml` se puede consultar en la plantilla: [ci_template.yml](https://github.com/linyuxuanlin/Auto-i18n/blob/main/ci_template.yml)

Debe agregar dos secrets en `Settings` - `Secrets and variables` - `Repository secrets`: `CHATGPT_API_BASE` y `CHATGPT_API_KEY`, y comentar la declaración `import env` en el programa `auto-translater.py`.

## Solución de problemas

1. Si necesita verificar la disponibilidad de la clave de API de ChatGPT, puede consultar el programa [verify-api-key.py](https://github.com/linyuxuanlin/Auto-i18n/blob/main/Archive/verify-api-key.py).
2. Cuando tenga problemas con GitHub Actions, verifique primero si las rutas se están referenciando correctamente (por ejemplo, `dir_to_translate`, `dir_translated_en`, `dir_translated_es`, `dir_translated_ar`, `processed_list`).

## Problemas pendientes

1. Si el archivo Markdown contiene Front Matter, también puede causar problemas al ser traducido. Mi solución es no utilizar Front Matter y utilizar el título de primer nivel como título del artículo.
2. Si el artículo no está completo, puede ocurrir que ChatGPT lo traduzca y complete automáticamente (¡misterioso!).
3. En algunas situaciones especiales, puede haber traducciones inexactas o campos que no se traducen, por lo que es necesario verificar y ajustar manualmente después de la traducción.

## Contribuciones

¡Bienvenido a contribuir a este proyecto! Si desea contribuir con código, informar problemas o hacer sugerencias, consulte nuestra [guía de contribución](https://github.com/linyuxuanlin/Auto-i18n/blob/main/CONTRIBUTING.md).

## Derechos de autor y licencia

Este proyecto está bajo la [licencia MIT](https://github.com/linyuxuanlin/Auto-i18n/blob/main/LICENSE).

## Problemas y soporte

Si tiene algún problema al utilizar Auto-i18n o necesita soporte técnico, no dude en [enviar un problema](https://github.com/linyuxuanlin/Auto-i18n/issues).

## Referencias y agradecimientos

Gracias a [**chatanywhere/GPT_API_free**](https://github.com/chatanywhere/GPT_API_free) por proporcionar una clave de API gratuita de ChatGPT.

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.