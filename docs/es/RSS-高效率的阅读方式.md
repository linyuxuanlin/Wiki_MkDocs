# RSS - Una forma eficiente de leer

El RSS significa "Really Simple Syndication" (Sindicación Realmente Simple) y es una herramienta que te permite suscribirte a varios sitios web que te interesan en un solo lugar.

En pocas palabras, cuando un autor al que sigues escribe un artículo en su plataforma (puede ser un blog, una cuenta pública, Quora, etc.), el RSS lo envía para que lo leas.

> Si un sitio web admite RSS, significa que cada vez que publique un nuevo artículo, agregará una entrada en un archivo ubicado en una dirección web específica, utilizando una sintaxis específica (específicamente lenguaje de marcado XML o JSON), que enumera el título del artículo, el autor, la fecha de publicación y la información del contenido (puede ser el artículo completo o un resumen). De esta manera, los usuarios pueden recopilar las direcciones web de estos archivos que ofrecen todos los sitios web que les interesan y verificar periódicamente las actualizaciones de estos archivos para saber si y cuándo se publicó contenido en estos sitios web. La función principal de un lector de RSS es almacenar las direcciones RSS que el usuario ha suscrito, verificar automáticamente las actualizaciones a intervalos fijos y presentar el contenido en un formato fácil de leer para el usuario.

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20200225145439.png)
![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20200225145502.png)

## ¿Por qué usar RSS?

### 1. Conveniencia

Cuando sigues a muchas personas, no necesitas abrir Quora, Jianshu o incluso blogs para obtener actualizaciones, sino que puedes leer todo en una sola terminal.

### 2. Derecho a la información

El opuesto de RSS es la recomendación de algoritmos, como WeChat Official Accounts, Quora, Weibo, Toutiao, etc. Además de la gran cantidad de publicidad en estas plataformas y el problema de la migración, la característica de la recomendación de algoritmos es que no necesitas elegir conscientemente, el algoritmo te dará contenido según tus preferencias. De esta manera, casi no tienes margen de elección y pierdes gradualmente la capacidad de juzgar mientras te alimentan constantemente. Lo más aterrador es que **define tu perfil por ti y te convierte en lo que cree que eres**. El incidente de "Big Data Kills Friends" no es casualidad, y es común que las empresas de Internet espíen la privacidad de los usuarios a través de algoritmos.

**Sé el dueño de la información, no un esclavo.** RSS es un protocolo público que permite cambiar libremente de plataforma y cliente. Lo importante es que **el poder de obtener información es completamente autónomo**. En comparación con la recomendación de algoritmos, RSS tiene control y seguridad, y la privacidad está completamente en manos del usuario.

### 3. Descentralización

Los artículos publicados en plataformas que requieren registro (cuentas públicas, Weibo, Quora, etc.) a menudo se eliminan debido a problemas de sensibilidad. Para la libre circulación de información, es necesario adoptar un enfoque descentralizado, es decir, plataformas construidas por los propios autores. RSS recopila contenido disperso y lo presenta para su lectura.

## Comenzando a leer RSS

### 1. Obtener fuentes RSS

Tomemos Inoreader como ejemplo. El método más simple es copiar la dirección del blog y pegarla en la barra de búsqueda de Inoreader, generalmente se puede suscribir directamente.

Para determinar si un sitio web tiene RSS, simplemente busca este ícono:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/rss.png)

y haz clic en él para suscribirte al enlace RSS directamente.  
Si no hay un ícono, es posible que haya RSS, pero está oculto.

En este caso, podemos usar una extensión del navegador llamada RSS+:

- Primero, instala la extensión Tampermonkey (necesitas acceso a Internet).
- Luego, instala el script RSS+.
- Si el sitio web tiene RSS, lo encontrarás en el pequeño círculo en la esquina inferior derecha.

Para los sitios web sin RSS, puedes crear tu propio RSS. Aquí hay algunas herramientas recomendadas:

- [feed43](http://feed43.com/)
- [RSSHub](https://docs.rsshub.app/#%E5%BE%AE%E5%8D%9A)
- [FeedOcean](https://feedocean.com/?lang=zh-CN)

## Cómo usar RSS para obtener información de alta calidad

### 1. Encuentra fuentes interesantes

Hay muchas herramientas para encontrar fuentes interesantes, como [Feedly](https://feedly.com/), [Inoreader](https://www.inoreader.com/) y [RSSHub](https://docs.rsshub.app/). Estas herramientas no solo pueden suscribirse a blogs sin RSS, sino que también pueden suscribirse directamente a columnas de Zhihu, cuentas públicas de WeChat, Weibo, Tieba, etc. Consulte la documentación para obtener información detallada.

### 2. Elija un lector de RSS

**Inoreader** tiene una versión gratuita con funciones básicas completas y un tiempo de captura de aproximadamente 15 minutos, lo que cumple con los requisitos. Tiene una versión web, iOS (requiere una cuenta de App Store en EE. UU.) Y una versión de Android.

**Reabble** se basa en la API de Inoreader y está diseñado para la lectura de tinta electrónica. Se recomienda actualizar a la versión de pago (¥ 21 por año, 7 artículos / día en la versión gratuita y no admite notificaciones push). Configuré la entrega programada de nuevos artículos a mi Kindle a las 9 a.m. todos los días, lo que también facilita la anotación y la exportación de extractos de libros. Si desea leer en su computadora, también puede abrir [reabble.com](https://reabble.com), crear un acceso directo en su escritorio, la interfaz es más simple y no tiene publicidad que Inoreader.

## Suscribirse a algunas fuentes interesantes

Nota: RSS no es adecuado para suscribirse a sitios web de noticias, ya que la actualización es demasiado rápida y el contenido es complicado, lo que resulta en una mala experiencia de lectura. Por lo tanto, RSS es más adecuado para suscribirse a sitios web de **blogs de alta calidad**. No es mejor tener demasiadas fuentes de suscripción. Demasiadas fuentes de suscripción pueden causar "sobrecarga de información", y descubrirá que recibe cientos de nuevas noticias todos los días, pero no tiene tiempo para leerlas.

Exporté mi fuente de suscripción, puede consultarla: [**Mi fuente de suscripción**](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/doc/Blogs.opml)  
Puede importar el archivo `.opml` en Inoreader u otro lector de RSS.

Actualización de abril de 2023: Método para construir un agregador de RSS autoalojado: [**Homelab - FreshRSS, un agregador de RSS autoalojado**](https://wiki-power.com/es/Homelab-%E8%87%AA%E6%89%98%E7%AE%A1RSS%E8%81%9A%E5%90%88%E5%99%A8FreshRSS/)。

## Preguntas frecuentes

P: ¿El lector de RSS será obsoleto con el tiempo?  
A: La lectura de libros no ha sido obsoleta. Una tendencia es que todas las plataformas de Internet siempre se desarrollan en la dirección que a la gente le gusta, hasta que el contenido se vuelve acuoso y una nueva plataforma lo reemplaza, como Zhihu y Douban. RSS no se ve afectado por el auge y la caída de la plataforma, a menos que aparezca un protocolo mejor, RSS no será obsoleto.

## Conclusión

Cito las palabras de "[notajerk](https://sspai.com/user/701048/updates)":

> Al obtener información en línea, puede ser un poco cursi imaginarse a uno mismo como un emperador que escucha las opiniones de sus ministros en la antigüedad. Para el emperador, lo más peligroso y lo que no debería hacer es exponer sus gustos, que es la base para que los subordinados sean engañados y, finalmente, para ser destituido. Un emperador sabio mantendrá su mente en calma y objetiva (neutral), insistirá en escuchar las opiniones de todas las partes sin exponer sus propias ideas, y verificará la credibilidad de cada opinión con hechos objetivos. Este es el principio que cada persona debe seguir para obtener información después de miles de años. **La selección de fuentes de información también es el lugar donde vale la pena invertir tiempo**.

## Referencias y agradecimientos

- [Cosas que no sabías que podías hacer con RSS](https://sspai.com/post/34280)
- [¿Cómo encontrar la dirección RSS de un sitio web? Use RSS +!](https://blog.wizos.me/20181022-258.html)
- [Lista de herramientas RSS](https://blog.wizos.me/20180412-134.html)
- [Mi introducción al uso de RSS](https://www.cnblogs.com/buwuliao/p/8379549.html)
- [Recopilación de RSS de texto completo hecha en casa (con herramientas recomendadas)](https://www.douban.com/note/522518464/)
- [Sobre el "renacimiento" de RSS](https://sspai.com/post/43998)

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
