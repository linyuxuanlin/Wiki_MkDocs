# Acceso a un NAS Synology mediante frp

Utilizando frp para acceder a un NAS Synology desde cualquier red.

## Por qué utilizar frp para acceder a un NAS Synology

- Falta de una dirección IP pública.
- Servicio QuickConnect demasiado lento.
- Necesidad de adquirir servicios como Hamachi, que requieren la compra de ancho de banda.

## Configuración del servidor

Siga el artículo [**Cómo configurar el servidor de control remoto por RDP en Internet (frp)**](https://wiki-power.com/%E5%A6%82%E4%BD%95%E5%AE%9E%E7%8E%B0%E5%A4%96%E7%BD%91RDP%E8%BF%9C%E6%8E%A7%EF%BC%88frp%EF%BC%89#%E6%9C%8D%E5%8A%A1%E7%AB%AF%E9%85%8D%E7%BD%AE). Es importante tener en cuenta que los parámetros `vhost_http_port` y `vhost_https_port` en el archivo de configuración `frpc.ini` deben mantenerse.

### Asociar un dominio

- Agregue un registro A con la dirección IP del servidor en su servicio de resolución de nombres de dominio.
- Configure la asociación de dominio en su servidor en la nube.

## Configuración del NAS Synology

### Edición del archivo de configuración

Cree un archivo `frpc.ini` en cualquier ubicación y agregue el siguiente contenido:

```ini title="frpc.ini"
[common]
server_addr = IP del servidor
server_port = Puerto frp del servidor, por defecto es 7000
token = Clave, debe ser la misma que la configuración del servidor

[dsm-http]
type = tcp
local_ip = localhost
local_port = Puerto http del DSM de Synology, por defecto es 5000
custom_domains = Dominio asociado
remote_port = Puerto remoto personalizado

[dsm-https]
type = tcp
local_ip = localhost
local_port = Puerto https del DSM de Synology, por defecto es 5001
custom_domains = Dominio asociado
remote_port = Puerto remoto personalizado

[ssh]
type = tcp
local_ip = localhost
local_port = Por defecto es 22
custom_domains = Dominio asociado
remote_port = Puerto remoto personalizado
```

### Método utilizando Docker

Instale la imagen `stilleshan/frpc` en Docker en su NAS Synology y configure el contenedor con los siguientes parámetros:

- Seleccione "Usar ejecución con alta autorización".
- Seleccione "Habilitar reinicio automático".
- En la pestaña "Volúmenes", agregue el archivo `frpc.ini` local y asígnele la ruta de montaje `/frp/frpc.ini`.
- Seleccione "Utilizar la misma red que el host de Docker".

Inicie el contenedor y, en breve, podrá acceder al DSM de Synology utilizando el dominio y el número de puerto HTTP.

## Referencias y Agradecimientos

- [Tutorial sobre cómo instalar y configurar frpc para el reenvío de puertos en una red local en un NAS Synology](https://www.ioiox.com/archives/26.html)

> Dirección original del artículo: <https://wiki-power.com/>
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.