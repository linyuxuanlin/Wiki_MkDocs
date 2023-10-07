# Cómo solicitar automáticamente un certificado de dominio utilizando acme.sh (Docker en Synology)

Este artículo describe cómo utilizar la imagen Docker acme.sh para implementar la función de solicitud y renovación automática de certificados de dominio.

[**acme.sh**](https://github.com/acmesh-official/acme.sh) puede generar certificados gratuitos de letsencrypt, admite la implementación de Docker, admite dos métodos de verificación de dominio, http y DNS, que incluyen modos manuales, automáticos de DNS y alias de DNS para facilitar diversos entornos y requisitos. Puede solicitar y combinar múltiples certificados de dominio único, certificados de dominio comodín y renovar y implementar automáticamente certificados en proyectos.

## Preparar la API de DNS

Este artículo utiliza Tencent Cloud como ejemplo para solicitar la API de DNS. Para otras plataformas de análisis, consulte la documentación oficial de [**dnsapi**](https://github.com/acmesh-official/acme.sh/wiki/dnsapi).

Primero, abra [**DNSPOD**](https://console.dnspod.cn/), haga clic en el avatar en la esquina superior derecha y seleccione `Administración de claves`.

Luego, cree una nueva clave y copie el **ID** y el **Token**.

## Implementación en Docker de Synology

Este tutorial describe el modo de demonio de Docker, que mantiene el contenedor en ejecución y realiza la función de renovación automática de certificados cuando caducan.

### Crear una carpeta de configuración

Primero, cree la carpeta `/docker/acme.sh` y luego cree manualmente el archivo `account.conf`:

![](https://f004.backblazeb2.com/file/wiki-media/img/20210430212420.png)

Luego, edite este archivo y agregue manualmente estas líneas:

```conf
export DP_Id="ID recién solicitado"
export DP_Key="TOKEN recién solicitado"
AUTO_UPGRADE='1'
```

Luego guarde y cierre el archivo.

### Descargar la imagen y configurar el contenedor

Abra el paquete Docker de Synology, descargue la imagen `neilpang/acme.sh`, haga doble clic para iniciar y seleccione `Configuración avanzada`.

En la página `Volumen`, configure la carpeta montada, haga clic en `Agregar carpeta`, seleccione la ruta local `docker/acme.sh` y complete la ruta de montaje como `/acme.sh` (predeterminado e inmutable):

![](https://f004.backblazeb2.com/file/wiki-media/img/20210430214221.png)

En la página `Red`, seleccione `Usar la misma red que el host de Docker`.

Luego, cambie a la página `Entorno` y escriba el comando `daemon` en el cuadro de comando:

![](https://f004.backblazeb2.com/file/wiki-media/img/20210430215244.png)

Luego, cree y ejecute el contenedor. Haga doble clic en el contenedor en ejecución, cambie a la página `Terminal` y haga clic en `Iniciar mediante comando`, escriba `sh` y haga clic en Aceptar.

Escriba el siguiente comando para actualizar automáticamente:

```shell
acme.sh --upgrade --auto-upgrade
```

Luego, escriba el siguiente comando para solicitar un certificado:

```shell
acme.sh --issue --dns dns_dp -d wiki-power.com -d *.wiki-power.com
```

Donde `dns_dp` representa Tencent Cloud DNSPod, si es Alibaba Cloud, escriba `dns_ali`, Cloudflare escriba `dns_cf`, otros consulte el manual oficial de [**dnsapi**](https://github.com/acmesh-official/acme.sh/wiki/dnsapi). Además, `*.wiki-power.com` representa un certificado de dominio comodín. Si necesita solicitar múltiples dominios al mismo tiempo, puede hacerlo de la siguiente manera:

```shell
acme.sh --issue --dns dns_dp -d aaa.com -d *.aaa.com -d bbb.com -d *.bbb.com -d ccc.com -d *.ccc.com
```

En el modo de demonio, acme.sh actualizará automáticamente los certificados cada 60 días según los registros de solicitud.

### Generación de certificados

Si todo va bien, encontrará los archivos `domain.cer` y `domain.key` en la carpeta `docker/acme.sh/nombre_de_dominio`, que son el certificado y el archivo de clave, y se pueden copiar a donde se necesiten.

## Referencias y agradecimientos

- [Servicios avanzados de Synology NAS - Implementación de acme.sh en Docker para la solicitud automática de certificados de dominio](https://www.ioiox.com/archives/88.html)

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.