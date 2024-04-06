# BookJourney - Aplicación Mini de Libros de Segunda Mano

![Imagen](https://media.wiki-power.com/img/书程小驿.jpg)

Repositorio del Proyecto: [**linyuxuanlin/BookJourney**](https://github.com/linyuxuanlin/BookJourney)

Demo (Experimenta escaneando con WeChat):

![Imagen](https://media.wiki-power.com/img/1.jpg)

## Antecedentes

Un amigo tenía la idea de incursionar en un negocio secundario, vendiendo libros de segunda mano a través de WeChat Moments, y me pidió que desarrollara una aplicación mini de WeChat para ello. Dado que tenía tiempo libre durante las vacaciones de verano, decidí aceptar el desafío y poner en práctica mis habilidades. La necesidad era crear una aplicación mini de tipo tienda en línea que permitiera publicar información sobre nuevos libros de forma periódica y que permitiera a los compradores seleccionar los libros por sí mismos.

## Desarrollo

En lugar de reinventar la rueda, encontré un proyecto de código abierto de una aplicación mini de tipo tienda en línea llamado [wechat-app-mall](https://github.com/EastWorld/wechat-app-mall). Utilicé este proyecto como base y realicé modificaciones para adaptarlo a mis preferencias y estilos. (La función de búsqueda global fue de gran utilidad en este proceso). Las características visuales predeterminadas de esta aplicación mini de código abierto no se ajustaban a mi sentido estético. Lo que buscaba era lograr que las páginas fueran lo más limpias posible, de modo que los usuarios se centraran en el contenido que deseaba mostrar. Después de muchas iteraciones, logré que el diseño visual cumpliera con mis requisitos.

En cuanto a las funciones, eliminé una serie de características relacionadas con la negociación de precios y recompensas por compartir, y mantuve solo las funciones esenciales.

Dado que yo no era el responsable de agregar nuevos productos al catálogo en el futuro, era importante que la edición de productos en el backend fuera intuitiva y basada en una interfaz gráfica. Para ello, BookJourney utilizó el backend de [api 工厂](https://www.it120.cc/), lo que eliminó la necesidad de configurar mi propio servidor y facilitó la tarea de otros miembros del equipo al agregar nuevos productos. Sin embargo, esto impuso restricciones de almacenamiento para los usuarios gratuitos.

## Desafíos

Durante el desarrollo de BookJourney, me encontré con varios desafíos. Uno de los desafíos notables fue el problema de los pagos. En un principio, pensé en integrar el pago a través de WeChat para que los usuarios pudieran realizar pedidos de manera sencilla, pero descubrí que WeChat había eliminado la opción de pago para las aplicaciones mini registradas por personas físicas. La única alternativa era registrar una cuenta de empresa, lo que a su vez requería tener una empresa registrada. Investigando más a fondo, descubrí que registrar una empresa no era una tarea sencilla. Se requería contratar a una firma contable, tener una dirección comercial, un contrato legal, pasar por la revisión del gerente bancario, y todo el proceso podía llevar dos o tres meses y costar cerca de mil dólares, sin incluir las tarifas adicionales. La solución fue cambiar el botón de compra por un botón de contacto directo con el servicio al cliente. De esta manera, los usuarios solo tenían que tomar una captura de pantalla de la página del "carrito de compras" y enviarla a un miembro del equipo de servicio al cliente para realizar el pedido.

## Preguntas Frecuentes

P: ¿Por qué se llama BookJourney?

R: Originalmente teníamos un nombre en chino muy bonito, "书程小驿", pero al registrar la aplicación mini, descubrimos que ese nombre ya estaba siendo utilizado, por lo que tuvimos que optar por una alternativa.

P: ¿Generó ganancias el proyecto?

R: Ingresos totales: ¥16.66...

## Conclusión

Con el paso del tiempo, queda claro que este proyecto fue un fracaso.

En la etapa inicial, no investigamos adecuadamente el mercado ni comprendimos las necesidades de los usuarios. En lugar de eso, simplemente creamos un producto que nos parecía genial. En el futuro, al emprender proyectos, es importante no solo enfocarse en la tecnología, sino también prestar atención al mercado y comprender qué tipo de productos necesita.

## Referencias y Agradecimientos

- [EastWorld / wechat-app-mall](https://github.com/EastWorld/wechat-app-mall)

[Para_ser_reemplazado[1]]  
[Para_ser_reemplazado[2]]

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
