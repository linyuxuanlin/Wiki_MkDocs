# Cómo construir un generador de RSS utilizando RSSHub (Docker en Synology)

Construye un servicio RSSHub en Docker en Synology para generar fuentes de suscripción RSS para todo tipo de contenido extraño.

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210504105215.png)

## Despliegue en Docker en Synology

Abre el paquete Docker en Synology, descarga la imagen `diygod/rsshub`, haz doble clic para iniciar, marca la opción "Habilitar reinicio automático" y luego entra en "Configuración avanzada".

En la página "Configuración de puertos", configura manualmente el puerto local correspondiente al puerto del contenedor 1200 (por ejemplo, lo he configurado como "8004"):

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210504085806.png)

Luego, completa la configuración y arranca el contenedor. Si puedes ver la página de RSSHub al ingresar la IP local de Synology:8004, significa que la instalación se ha realizado correctamente.

## Pasos para usar

Para obtener información detallada sobre cómo utilizarlo, consulta la [**documentación oficial de RSSHub**](https://docs.rsshub.app/).

Tomemos un ejemplo simple. En la documentación oficial, se puede encontrar el método de generación de "Películas en cartelera" de Douban como sigue:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210504104630.png)

Entonces, puedes utilizar "tu dominio/douban/movie/playing" para generar tu propia fuente RSS utilizando tu propio servidor.

Se recomienda utilizar el proxy inverso integrado en el sistema Synology para lograr el acceso HTTPS cifrado. Puedes consultar el tutorial en el artículo [**Cómo utilizar el proxy inverso integrado en Synology para lograr el acceso HTTPS**](https://wiki-power.com/%E7%94%A8%E7%BE%A4%E6%99%96%E8%87%AA%E5%B8%A6%E5%8F%8D%E5%90%91%E4%BB%A3%E7%90%86%E5%AE%9E%E7%8E%B0HTTPS%E8%AE%BF%E9%97%AE).

## Utiliza RSSHub Radar para detectar automáticamente la ruta

[**RSSHub Radar**](https://github.com/DIYgod/RSSHub-Radar) es una extensión del navegador que te ayuda a descubrir y suscribirte rápidamente a RSS y RSSHub en el sitio web actual.

Simplemente ingresa la dirección personalizada en su página de configuración para utilizarla.

## Referencias y agradecimientos

- [Documentación oficial de RSSHub](https://docs.rsshub.app/)
- [Cómo instalar RSSHub en Synology utilizando Docker](https://immwind.com/use-docker-install-rsshub-in-synology)

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.