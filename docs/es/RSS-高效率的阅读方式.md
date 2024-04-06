# RSS - Una Forma Eficiente de Leer

El acrónimo RSS significa "Sindicación Realmente Simple" (Really Simple Syndication), y es una herramienta que te permite suscribirte a diversos sitios web de tu interés en un solo lugar.

En pocas palabras, cuando un autor que sigues publica un artículo en su plataforma (ya sea un blog, un canal público, o una plataforma como Zhihu), RSS te lo envía para que puedas leerlo.

> Si un sitio web admite RSS, significa que cada vez que publica un nuevo artículo, agrega una entrada a un archivo en una ubicación específica, en un formato específico (generalmente lenguaje de marcado XML o JSON). Esta entrada incluye el título del artículo, el autor, la fecha de publicación y el contenido (que puede ser el artículo completo o un resumen). De esta manera, los usuarios solo necesitan recopilar las direcciones de estos archivos proporcionadas por los sitios que les interesan y verificar periódicamente si hay actualizaciones en el contenido de estos archivos para saber si los sitios han publicado algo nuevo. La función principal de un lector de RSS es almacenar las direcciones de RSS a las que el usuario se ha suscrito, verificar automáticamente las actualizaciones a intervalos regulares y presentar el contenido de manera legible para el usuario.

![Imagen](https://media.wiki-power.com/img/20200225145439.png)
![Imagen](https://media.wiki-power.com/img/20200225145502.png)

## Por Qué Usar RSS

### 1. Conveniencia

Cuando sigues a muchas personas, ya no necesitas abrir uno por uno sitios web como Zhihu, Jian Shu o revisar blogs para buscar actualizaciones. En su lugar, puedes leer todo en un solo lugar.

### 2. Derecho a la Información

RSS se opone a las recomendaciones algorítmicas, como las de WeChat, Zhihu, Weibo, y Jinri Toutiao, entre otras. Sin mencionar la proliferación de publicidad en plataformas de recomendación algorítmica y la molestia de migrar entre ellas. La característica de las recomendaciones algorítmicas es que no necesitas tomar decisiones conscientes; el algoritmo te proporcionará contenido basado en tus preferencias. Esto significa que casi no tienes control sobre lo que ves y, gradualmente, pierdes la capacidad de juzgar. Lo más alarmante es que **el algoritmo define quién eres y te moldea sin que te des cuenta**. La revelación de "el gran dato discrimina" no es casualidad; es una práctica común de las compañías de Internet de hoy en día observar la privacidad de los usuarios mediante algoritmos.

**Sé el dueño de tu información, no un esclavo**. RSS es un protocolo público y te permite cambiar de plataforma y cliente libremente. Lo importante es que **tienes un control total sobre tu derecho a la información**. Comparado con las recomendaciones algorítmicas, RSS ofrece control y seguridad, y mantiene tu privacidad en tus manos.

### 3. Descentralización

Los artículos publicados en plataformas que requieren registro a menudo son eliminados debido a contenido sensible. Para garantizar la libre circulación de información, es necesario adoptar un enfoque descentralizado, es decir, plataformas construidas por los propios autores. RSS recopila contenido disperso y lo presenta para su lectura.

## Comenzando a Leer RSS

### 1. Obtener Fuentes de RSS

Tomemos Inoreader como ejemplo. El método más sencillo es copiar la dirección del blog y pegarla en la barra de búsqueda de Inoreader, generalmente se puede suscribir directamente.

Para saber si un sitio web tiene RSS, busca este ícono al abrirlo:

![Imagen](https://media.wiki-power.com/img/rss.png)

Si ves este ícono, simplemente haz clic en él para suscribirte al enlace RSS.

Si no ves el ícono, es posible que el RSS esté presente, pero un poco más escondido.

En este caso, puedes usar una extensión del navegador llamada RSS+:

- Primero, instala la extensión [Tampermonkey](https://chrome.google.com/webstore/detail/tampermonkey/dhdgffkkebhmkfjojejmpbldmpobfkfo), esto requiere acceso a Internet sin restricciones.
- Luego, instala el script [RSS+](https://greasyfork.org/zh-CN/scripts/373252-rss-show-site-all-rss).
- Ahora, si el sitio web tiene RSS, lo encontrarás en el pequeño círculo en la esquina inferior derecha.

Para sitios web que no tengan RSS, puedes crear tu propio RSS. Aquí hay algunas herramientas recomendadas:

- [feed43](http://feed43.com/)
- [RSSHub](https://docs.rsshub.app/#%E5%BE%AE%E5%8D%9A)
- [FeedOcean](https://feedocean.com/?lang=zh-CN)

Estas herramientas no solo permiten suscribirte a blogs que no tienen RSS, sino que también pueden suscribirte directamente a columnas de Zhihu, cuentas públicas, Weibo y foros, entre otros. Consulta la documentación para obtener instrucciones detalladas.

### 2. Elige un lector de RSS

**Inoreader** ofrece una versión gratuita con funciones básicas sólidas, con un tiempo de actualización de aproximadamente 15 minutos, lo que cumple con los requisitos. Está disponible en la versión web, iOS (requiere una cuenta de App Store de EE. UU.) y en la versión para Android.

**Reabble** se basa en la API de Inoreader y está diseñado para la lectura en pantallas de tinta electrónica. Se recomienda actualizar a la versión de pago (¥21 al año, la versión gratuita permite leer 7 artículos al día pero no admite notificaciones push). Personalmente, he configurado la aplicación para enviar automáticamente nuevos artículos al Kindle a las 9 de la mañana, lo que facilita la realización de anotaciones y la exportación de extractos de libros. Si deseas leer en tu computadora, también puedes acceder directamente a [reabble.com](https://reabble.com), crear un acceso directo en tu escritorio y disfrutar de una interfaz más limpia y sin anuncios en comparación con Inoreader.

## Suscribirse a Fuentes de Interés

Nota: RSS no es adecuado para suscribirse a sitios web de noticias, ya que la información se actualiza con demasiada frecuencia y la cantidad de contenido puede dificultar la experiencia de lectura. Por lo tanto, RSS es más adecuado para la suscripción a sitios web de **alta calidad**, como blogs. No se trata de tener la mayor cantidad de fuentes de suscripción, sino de elegirlas con cuidado. Demasiadas fuentes de suscripción pueden llevar a una "sobrecarga de información", lo que significa que recibirás cientos de nuevas noticias todos los días y no podrás leerlas todas.

He exportado mis fuentes de suscripción, puedes echar un vistazo aquí: [**Mis Suscripciones**](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/doc/Blogs.opml)
Puedes importar el archivo `.opml` en Inoreader u otros lectores de RSS.

Actualización de abril de 2023: Cómo configurar tu propio agregador de RSS autohospedado: [**Homelab - Agregador de RSS autohospedado FreshRSS**](https://wiki-power.com/Homelab-%E8%87%AA%E6%89%98%E7%AE%A1RSS%E8%81%9A%E5%90%88%E5%99%A8FreshRSS/).

## Preguntas Frecuentes

P: ¿El lector de RSS quedará obsoleto en la era actual?
R: La lectura de RSS no ha quedado obsoleta, al igual que la lectura de libros no ha quedado obsoleta. Una tendencia es que las plataformas en línea siempre tienden a evolucionar hacia lo que es popular y atractivo para las masas, lo que a menudo lleva a la dilución del contenido. Nuevas plataformas emergen para tomar su lugar, como lo han hecho plataformas como Quora y Douban. Sin embargo, RSS no se ve afectado por el auge y la caída de las plataformas, a menos que surja un protocolo mejor. Por lo tanto, RSS no será obsoleto a menos que haya un reemplazo significativamente mejor.

## Conclusión

Para citar a "[notajerk](https://sspai.com/user/701048/updates)":

> Cuando se trata de obtener información en línea, puedes adoptar un enfoque un tanto sofisticado, imaginándote a ti mismo como un antiguo emperador escuchando los consejos de sus consejeros. Para un emperador sabio, lo más peligroso y desaconsejable sería revelar sus preferencias personales, ya que esto formaría la base para ser influenciado o despojado del poder por sus subordinados. Un emperador sabio mantendría su mente en calma y objetiva, escucharía las opiniones de todas las partes sin revelar sus propios sentimientos y verificaría la credibilidad de esas opiniones en función de hechos objetivos. Este es el principio que todos deberíamos seguir al obtener información, incluso miles de años después. La elección de las fuentes de información es el aspecto en el que más vale la pena invertir tiempo.

## Referencias y Agradecimientos

- [Cosas sorprendentes que puedes hacer con RSS que quizás no habías considerado](https://sspai.com/post/34280)
- [Cómo encontrar la dirección RSS de un sitio web: ¡Usa RSS +!](https://blog.wizos.me/20181022-258.html)
- [Herramientas de RSS: Una guía completa](https://blog.wizos.me/20180412-134.html)
- [Mi guía de uso de RSS](https://www.cnblogs.com/buwuliao/p/8379549.html)
- [Agregación de RSS de texto completo hecha en casa (con herramientas recomendadas)](https://www.douban.com/note/522518464/)
- [El "renacimiento" de RSS](https://sspai.com/post/43998)

> Dirección original del artículo: <https://wiki-power.com/>
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
