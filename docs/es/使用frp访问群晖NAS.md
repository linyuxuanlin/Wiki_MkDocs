# Accediendo a Synology NAS con frp

Acceda a Synology NAS en cualquier red utilizando frp.

## ¿Por qué acceder a Synology a través de frp?

- Sin IP pública
- El servicio QuickConnect es demasiado lento
- Servicios como Peanut Shell requieren la compra de tráfico por separado

## Configuración del servidor

Ir al artículo [**Cómo implementar el control remoto RDP externo (frp) · Configuración del servidor**](https://wiki-power.com/es/%E5%A6%82%E4%BD%95%E5%AE%9E%E7%8E%B0%E5%A4%96%E7%BD%91RDP%E8%BF%9C%E6%8E%A7%EF%BC%88frp%EF%BC%89#%E6%9C%8D%E5%8A%A1%E7%AB%AF%E9%85%8D%E7%BD%AE). Tenga en cuenta que los parámetros `vhost_http_port` / `vhost_https_port` en el archivo de configuración `frpc.ini` deben mantenerse.

### Asociar un nombre de dominio

- Agregue un registro A en la resolución de nombres de dominio con la dirección IP del servidor.
- Configure la asociación de nombres de dominio en el servidor en la nube.

## Configuración de Synology NAS

### Edite el archivo de configuración

Cree un archivo `frpc.ini` en cualquier ubicación y agregue el siguiente contenido:

```ini title="frpc.ini"
[common]
server_addr = Dirección IP del servidor
server_port = Puerto frp del servidor, predeterminado 7000
token = Clave, debe ser la misma que la configurada en el servidor

[dsm-http]
type = tcp
local_ip = localhost
local_port = Puerto http DSM de Synology, predeterminado 5000
custom_domains = Nombre de dominio asociado
remote_port = Puerto remoto personalizado

[dsm-https]
type = tcp
local_ip = localhost
local_port = Puerto https DSM de Synology, predeterminado 5001
custom_domains = Nombre de dominio asociado
remote_port = Puerto remoto personalizado

[ssh]
type = tcp
local_ip = localhost
local_port = predeterminado 22
custom_domains = Nombre de dominio asociado
remote_port = Puerto remoto personalizado
```

### Método de uso de Docker

Instale la imagen `stilleshan/frpc` en Docker de Synology y use los siguientes parámetros para inicializar el contenedor:

- Seleccione "Ejecutar el contenedor con privilegios elevados".
- Seleccione "Habilitar reinicio automático".
- Agregue el archivo seleccionando "Volumen" y seleccione el archivo `frpc.ini` local. La ruta de montaje correspondiente es `/frp/frpc.ini`.
- Seleccione "Usar la misma red que el host de Docker".

Inicie el contenedor y espere un momento para acceder a Synology DSM a través del nombre de dominio y el número de puerto http.

## Referencias y agradecimientos

- [Tutorial de penetración de red interna de Synology NAS con Docker frpc](https://www.ioiox.com/archives/26.html)

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.