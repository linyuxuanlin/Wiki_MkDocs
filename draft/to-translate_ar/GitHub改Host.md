# GitHub Cambio de Host

## Problema

Error: `curl: (7) Failed to connect to raw.githubusercontent.com port 443: Connection refused`

## Causa

DNS contaminado en el país.

## Solución

Agregar lo siguiente al archivo host de la máquina local:

```
199.232.68.133 raw.githubusercontent.com
199.232.68.133 user-images.githubusercontent.com
199.232.68.133 avatars2.githubusercontent.com
199.232.68.133 avatars1.githubusercontent.com
```

Ruta del host:

- Windows: `C:\Windows\System32\drivers\etc`
- Linux: `/etc/hosts`

A continuación, se presenta un método de operación en Linux:

1. Abra la terminal
2. Ingrese el comando: `vi /etc/hosts`
3. Presione `A` para cambiar al modo de edición
4. Agregue las líneas de host mencionadas anteriormente al final
5. Presione `Esc` para salir de la edición y `:wq` para guardar y salir

## Ampliación

### Consulta de IP de dominio

Utilice [**IPAddress**](https://www.ipaddress.com/)

## Referencias y agradecimientos

- [Agregar Host para acelerar el acceso a github](https://yangshun.win/blogs/2b7abf4f/#%E4%BF%AE%E6%94%B9-host)

> Autor del artículo: **Power Lin**
> Dirección original: <https://wiki-power.com>
> Declaración de derechos de autor: Este artículo utiliza la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Por favor, indique la fuente al volver a publicar.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.