# Evitar la conversión forzada a HTTPS en Chrome (Edge)

Algunos sitios web solo se pueden acceder a través de HTTP, pero a veces el navegador los convierte automáticamente a HTTPS, lo que provoca errores de acceso. A continuación, se mostrará cómo desactivar esta conversión automática en el navegador.

## Pasos a seguir

Ingresa la siguiente dirección en la barra de direcciones y presiona Enter:

- Chrome: `chrome://net-internals/#hsts`
- Edge: `edge://net-internals/#hsts`

En el campo "Eliminar políticas de seguridad de dominio", ingresa los enlaces que no deseas que se conviertan automáticamente. Por ejemplo, si deseas que `wiki-power.com` no se convierta a HTTPS, ingresa `wiki-power.com` y luego haz clic en "Eliminar" para eliminarlo.

Luego, ingresa la siguiente dirección en la barra de direcciones y presiona Enter:

- Chrome: `chrome://flags/#edge-automatic-https`
- Edge: `edge://flags/#edge-automatic-https`

Cambia la opción "HTTPS automático" de "Predeterminado" a "Deshabilitado" y reinicia el navegador.

## Referencias y agradecimientos

- [Edge o Chrome convierten automáticamente las direcciones web HTTP a HTTPS y no se puede modificar manualmente](https://blog.csdn.net/Thinker001/article/details/117717690)

> Dirección original del artículo: <https://wiki-power.com/>
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.