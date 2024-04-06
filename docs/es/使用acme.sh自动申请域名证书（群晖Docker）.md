# Uso de acme.sh para la automatización de certificados de dominio (Docker en Synology)

En este artículo, se describe cómo utilizar la imagen de Docker de acme.sh para lograr la automatización de la solicitud y renovación de certificados de dominio.

[**acme.sh**](https://github.com/acmesh-official/acme.sh) es capaz de generar certificados gratuitos desde Let's Encrypt y es compatible con despliegues en Docker. Admite dos métodos de validación de dominio: HTTP y DNS, incluyendo modos manuales, automatizados y alias de DNS, lo que facilita su implementación en diversos entornos y necesidades. También permite la solicitud de certificados individuales, certificados wildcard y la renovación automática de los mismos, además de su despliegue en proyectos.

## Preparación del API de DNS

En este artículo, se utiliza Tencent Cloud como ejemplo para la solicitud de un API de DNS. Para otras plataformas de resolución, consulte la documentación oficial de [**dnsapi**](https://github.com/acmesh-official/acme.sh/wiki/dnsapi).

Primero, abra [**DNSPOD**](https://console.dnspod.cn/), haga clic en la esquina superior derecha en su avatar y seleccione "Gestión de Claves".

Luego, cree una nueva clave y copie tanto el **ID** como el **Token**.

## Implementación en Docker en Synology

Este tutorial se centra en el modo daemon de Docker, que mantiene el contenedor en ejecución continuamente y automatiza la renovación de los certificados cuando están a punto de expirar.

### Creación de una carpeta de configuración

Primero, cree la carpeta `/docker/acme.sh` y luego cree manualmente un archivo `account.conf`:

![account.conf](https://media.wiki-power.com/img/20210430212420.png)

A continuación, edite este archivo y agregue manualmente las siguientes líneas:

```conf
export DP_Id="ID recién solicitado"
export DP_Key="TOKEN recién solicitado"
AUTO_UPGRADE='1'
```

Luego, guarde y cierre el archivo.

### Descarga de la imagen y configuración del contenedor

Abra el paquete Docker de Synology, descargue la imagen `neilpang/acme.sh`, luego haga doble clic para iniciarla y acceda a "Configuración Avanzada".

En la página "Volúmenes", configure la carpeta que desea montar haciendo clic en "Agregar carpeta" y seleccione la ruta local `/docker/acme.sh`, con la ruta de montaje como `/acme.sh` (predeterminada e inmutable):

![Volumes](https://media.wiki-power.com/img/20210430214221.png)

En la página "Red", marque la casilla "Usar la misma red que el anfitrión de Docker".

A continuación, vaya a la página "Entorno" e introduzca el comando `daemon` en el cuadro "Comando":

![Environment](https://media.wiki-power.com/img/20210430215244.png)

Luego, cree y ejecute el contenedor. Haga doble clic en el contenedor en ejecución, vaya a la página "Terminal" y haga clic en "Iniciar por comando", escriba `sh` y confirme.

Ejecute el siguiente comando para la actualización automática:

```shell
acme.sh --upgrade --auto-upgrade
```

Luego, ejecute el siguiente comando para solicitar el certificado:

```shell
acme.sh --issue --dns dns_dp -d wiki-power.com -d *.wiki-power.com
```

Donde `dns_dp` representa Tencent Cloud DNSPod. Si está utilizando Alibaba Cloud, especifique `dns_ali`, o `dns_cf` para Cloudflare, u otro método según lo indicado en la documentación oficial de [**dnsapi**](https://github.com/acmesh-official/acme.sh/wiki/dnsapi). Además, `*.wiki-power.com` denota la solicitud de un certificado wildcard. Si necesita solicitar múltiples dominios al mismo tiempo, puede hacerlo de la siguiente manera:

```shell
acme.sh --issue --dns dns_dp -d aaa.com -d *.aaa.com -d bbb.com -d *.bbb.com -d ccc.com -d *.ccc.com
```

En el modo daemon, acme.sh renovará automáticamente los certificados cada 60 días.

### Generación de certificados

Si todo va según lo planeado, podrás encontrar los archivos `dominio.cer` y `dominio.key` dentro de la carpeta con el nombre del dominio en `docker/acme.sh/`, los cuales corresponden al certificado y la clave, respectivamente. Estos archivos podrán ser copiados a la ubicación donde los necesites.

## Referencias y Agradecimientos

- [Servicio Avanzado de Synology NAS - Implementación de acme.sh en Docker para la Automatización de Certificados de Dominio](https://www.ioiox.com/archives/88.html)

> Dirección original del artículo: <https://wiki-power.com/>
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
