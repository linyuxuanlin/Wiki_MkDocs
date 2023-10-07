# BookJourney - Tienda de libros de segunda mano en miniatura

![](https://f004.backblazeb2.com/file/wiki-media/img/书程小驿.jpg)

Repositorio del proyecto: [**linyuxuanlin/BookJourney**](https://github.com/linyuxuanlin/BookJourney)

Demo (escanea con WeChat para probar):

![](https://f004.backblazeb2.com/file/wiki-media/img/1.jpg)

## Antecedentes

Un amigo quería hacer un trabajo secundario vendiendo libros de segunda mano en su círculo de amigos de WeChat, así que me pidió que hiciera una miniatura de WeChat. Como estaba libre durante las vacaciones de verano, decidí practicar. La demanda era crear una miniatura de una tienda en línea, con información de libros nuevos que se publican regularmente, para que los compradores puedan elegir por sí mismos.

## Desarrollo

No quería reinventar la rueda, así que encontré un proyecto de código abierto bastante bueno para una miniatura de tienda en línea: [wechat-app-mall](https://github.com/EastWorld/wechat-app-mall), y lo modifiqué y agregué mi propio estilo. (La búsqueda global es muy útil). El estilo predeterminado de esta miniatura de código abierto no se ajustaba a mi estética. Lo que necesitaba era un diseño que pudiera enfocar la atención del usuario en el contenido que se muestra en una página simple. Después de muchas iteraciones, el estilo básico se ajustó a mis necesidades.

En cuanto a la funcionalidad, eliminé una serie de cosas relacionadas con la negociación y el intercambio de recompensas, y solo dejé las funciones principales.

Como no soy responsable de agregar nuevos productos, la edición de productos en el backend debe ser una interfaz gráfica. BookJourney utiliza el backend de [api factory](https://www.it120.cc/), lo que elimina la necesidad de construir su propio servidor y facilita la adición de nuevos productos por parte de los miembros del equipo. Sin embargo, los usuarios gratuitos tienen limitaciones de almacenamiento.

## Evitar problemas

En el proceso de desarrollo de BookJourney, encontré muchos problemas. Por ejemplo, el problema del pago. El sentido común me dice que debería integrar WeChat Pay para que los usuarios puedan hacer pedidos fácilmente, pero WeChat ha eliminado la ventana de pago de WeChat Pay para los usuarios que se registran en una miniatura personal. (Aunque también considera la seguridad financiera del usuario). La única forma es registrarse en una cuenta empresarial, pero primero necesito una empresa. Después de investigar más, descubrí que no es fácil registrar una empresa. Necesitas encontrar una firma de contabilidad para representarte, tener una dirección de oficina, un contrato de libro rojo, ser revisado por un gerente de banco, el proceso de solicitud dura casi dos o tres meses, el costo es de casi mil yuanes, sin incluir varios cargos adicionales ... La solución es cambiar el botón de pedido directamente a "contactar al servicio al cliente". En este punto, los usuarios solo necesitan tomar una captura de pantalla en la página del "carrito de compras" y enviarla directamente a los miembros del equipo responsables del servicio al cliente para hacer un pedido.

## Preguntas frecuentes

P: ¿Por qué se llama BookJourney?
R: Originalmente tenía un nombre chino bonito llamado "书程小驿", pero descubrí que ya estaba ocupado cuando registré la miniatura, así que tuve que comprometerme.

P: ¿Ganaste dinero?
R: Ingresos totales de ganancias: ¥16.66 ...

## Conclusión

Después del tiempo, este fue un proyecto fallido.

Al principio, no investigué cuidadosamente el mercado ni aclaré las necesidades de los usuarios, solo hice un producto que pensé que era genial. En el futuro, al hacer proyectos, debe prestar atención no solo a la tecnología, sino también al mercado y saber qué tipo de productos necesita el mercado.

## Referencias y agradecimientos

- [EastWorld / wechat-app-mall](https://github.com/EastWorld/wechat-app-mall)

> Dirección original del artículo: <https://wiki-power.com/>
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.