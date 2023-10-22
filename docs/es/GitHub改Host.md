# Cambio de Host en GitHub

## Problema

Error: `curl: (7) Error al conectar a raw.githubusercontent.com en el puerto 443: Conexión rechazada`

## Causa

Filtrado de DNS en el país.

## Solución

Añadir las siguientes líneas al archivo de host en tu máquina local:

```plaintext
199.232.68.133 raw.githubusercontent.com
199.232.68.133 user-images.githubusercontent.com
199.232.68.133 avatars2.githubusercontent.com
199.232.68.133 avatars1.githubusercontent.com
```

Rutas del archivo de host:

- Windows: `C:\Windows\System32\drivers\etc`
- Linux: `/etc/hosts`

Instrucciones para Linux:

1. Abre la terminal.
2. Ingresa el comando: `vi /etc/hosts`.
3. Presiona `A` para cambiar al modo de edición.
4. Agrega las líneas de host mencionadas al final.
5. Presiona `Esc` para salir del modo de edición, y luego escribe `:wq` para guardar y salir.

## Ampliación

### Consulta la IP de un dominio

Utiliza [**IPAddress**](https://www.ipaddress.com/).

## Referencias y Agradecimientos

- [Cómo agregar Host para acelerar el acceso a GitHub](https://yangshun.win/blogs/2b7abf4f/#%E4%BF%AE%E6%94%B9-host)

> Autor del artículo: **Power Lin**
> Dirección original: <https://wiki-power.com>
> Declaración de derechos de autor: Este artículo está bajo la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Por favor, menciona la fuente si lo compartes.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.