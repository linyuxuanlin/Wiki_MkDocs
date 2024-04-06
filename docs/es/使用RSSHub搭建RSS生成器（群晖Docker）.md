# Construir un Generador de RSS con RSSHub en Synology Docker

Configura un servicio de RSSHub en Synology Docker para generar fuentes de suscripción RSS de contenido variado y peculiar.

![](https://media.wiki-power.com/img/20210504105215.png)

## Despliegue en Synology Docker

Abre el paquete Docker en Synology, descarga la imagen de `diygod/rsshub`, inicia el contenedor con un doble clic y habilita la opción de "Reinicio automático". Luego, accede a la configuración avanzada.

En la página de "Configuración de puertos", establece manualmente un puerto local correspondiente al puerto del contenedor 1200 (por ejemplo, puedes configurarlo como `8004`):

![](https://media.wiki-power.com/img/20210504085806.png)

Después de completar la configuración, inicia el contenedor. Si puedes acceder a la página de RSSHub en la dirección IP local de Synology seguida del puerto 8004, habrás tenido éxito en la instalación.

## Pasos de Uso

Para obtener instrucciones detalladas sobre cómo usarlo, consulta la [**documentación oficial de RSSHub**](https://docs.rsshub.app/).

Como ejemplo sencillo, en la documentación oficial encontrarás el método para generar la fuente RSS de las películas "Currently Playing" de Douban de la siguiente manera:

![](https://media.wiki-power.com/img/20210504104630.png)

Entonces, puedes utilizar `tu_dominio/douban/movie/playing` para generar tu propia fuente RSS en tu servidor.

Se recomienda utilizar la función de proxy inverso incorporada en Synology para habilitar el acceso seguro mediante HTTPS. Puedes encontrar un tutorial detallado en el artículo [**Configurar Acceso HTTPS con el Proxy Inverso de Synology**](https://wiki-power.com/%E7%94%A8%E7%BE%A4%E6%99%96%E8%87%AA%E5%B8%A6%E5%8F%8D%E5%90%91%E4%BB%A3%E7%90%86%E5%AE%9E%E7%8E%B0HTTPS%E8%AE%BF%E9%97%AE).

## Utiliza RSSHub Radar para Detectar Rutas de Manera Automática

[**RSSHub Radar**](https://github.com/DIYgod/RSSHub-Radar) es una extensión de navegador que te permite descubrir y suscribirte rápidamente a fuentes RSS de sitios web y RSSHub.

Simplemente introduce tu dirección personalizada en la página de configuración para empezar a usarla.

## Referencias y Agradecimientos

- [Documentación Oficial de RSSHub](https://docs.rsshub.app/)
- [Instalación de RSSHub en Synology con Docker](https://immwind.com/use-docker-install-rsshub-in-synology)

> Dirección original del artículo: <https://wiki-power.com/>
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
