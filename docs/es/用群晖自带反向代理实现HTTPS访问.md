# Cómo implementar el acceso HTTPS con el proxy inverso incorporado de Synology

En primer lugar, necesitarás una dirección IP o un nombre de dominio para acceder a Synology desde el exterior, y ya habrás solicitado un certificado SSL. Puedes encontrar una explicación detallada en el artículo [**Cómo solicitar automáticamente un certificado de dominio con acme.sh (Synology Docker)**](https://wiki-power.com/es/%E5%9F%BA%E4%BA%8Eacme.sh%E8%87%AA%E5%8A%A8%E7%94%B3%E8%AF%B7%E5%9F%9F%E5%90%8D%E8%AF%81%E4%B9%A6%EF%BC%88Synology%20Docker%EF%BC%89).

## Configuración del proxy inverso

Abre `Panel de control` - `Puerta de enlace de inicio de sesión` - `Avanzado` - `Servidor de proxy inverso`.

En el caso de [**Cómo construir un gestor de contraseñas con Bitwarden (Synology Docker)**](https://wiki-power.com/es/%E5%9F%BA%E4%BA%8EBitwarden%E6%90%AD%E5%BB%BA%E5%AF%86%E7%A0%81%E7%AE%A1%E7%90%86%E5%99%A8%EF%BC%88Synology%20Docker%EF%BC%89), agregamos un servicio de proxy inverso con el nombre `bitwarden`. Completa la configuración según la siguiente imagen:

![](https://img.wiki-power.com/d/wiki-media/img/20210503213004.png)

- `Origen`
  - `Protocolo`: selecciona `HTTPS`
  - `Nombre de host`: introduce el nombre de dominio para acceder desde el exterior
  - `Puerto`: introduce el puerto para acceder desde el exterior
  - Marca la casilla `Habilitar HSTS` (redirección forzada a HTTPS)
- `Destino`
  - `Protocolo`: selecciona `HTTP`
  - `Nombre de host`: introduce `localhost`
  - `Puerto`: introduce el puerto de acceso interno (para Bitwarden, es el puerto mapeado `80` del contenedor, como `8003`)

## Configuración del certificado

Abre `Panel de control` - `Seguridad` - `Certificado`, selecciona el certificado en uso, haz clic en `Configuración` y asegúrate de que el certificado correspondiente al servicio de proxy inverso `bitwarden` sea el certificado actual.

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
