# Cómo configurar un gestor de contraseñas con Bitwarden (Docker en Synology)

Nota: Debido a que la imagen de Bitwarden_rs ha cambiado de nombre y la extensión de navegador oficial de Bitwarden no es compatible con versiones antiguas, es necesario reemplazar `bitwardenrs/server` por `vaultwardenrs/server` en el siguiente texto y asegurarse de que la versión sea igual o superior a 1.27.0.

En este artículo se explica cómo realizar una implementación privada del servidor de gestión de contraseñas Bitwarden en Synology mediante Docker, para su uso en múltiples plataformas.

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210503221838.png)

Actualmente, existen varias soluciones de gestión de contraseñas, como 1Password, Lastpass, KeePass y Bitwarden, cada una con sus propias ventajas e inconvenientes. En mi caso, necesitaba una solución que permitiera la sincronización en múltiples dispositivos, fuera de código abierto y pudiera ser implementada de forma privada, además de contar con una función de relleno automático y una interfaz atractiva. Por ello, elegí implementar el servicio Bitwarden en mi Synology.

## Implementación en Docker en Synology

### Creación de una carpeta para almacenar los datos

Se debe crear una carpeta para almacenar los datos de Bitwarden en el directorio `docker` (por ejemplo, `docker/bitwarden`).

### Descarga de la imagen y configuración del contenedor

Abrir el paquete Docker de Synology, descargar la imagen `bitwardenrs/server`, iniciarla haciendo doble clic y seleccionar "Habilitar reinicio automático". Luego, acceder a "Configuración avanzada".

En la página "Volúmenes", configurar la carpeta montada haciendo clic en "Agregar carpeta", seleccionar la ruta local `docker/bitwarden` y establecer la ruta de montaje en `/data` (que no se puede cambiar por defecto):

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210503211711.png)

En la página "Configuración de puertos", establecer manualmente el puerto local correspondiente al puerto 80 del contenedor (por ejemplo, establecerlo en `8003`):

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210503211759.png)

Finalmente, iniciar el contenedor. Al acceder a la dirección IP local de Synology seguida del puerto `8003`, se mostrará la página de inicio de sesión de Bitwarden. Sin embargo, al crear una cuenta e intentar iniciar sesión, se mostrará el siguiente mensaje:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210503212146.png)

Esto se debe a que el contenedor Docker no proporciona una configuración de puerto HTTPS y Bitwarden solo permite el inicio de sesión a través de HTTPS (para evitar ataques de intermediarios mediante cifrado SSL). Por lo tanto, es necesario utilizar el servicio de proxy inverso integrado en Synology para acceder al puerto HTTP interno a través de HTTPS. Para obtener más información, consulte el artículo [**Cómo implementar HTTPS mediante proxy inverso en Synology**](https://wiki-power.com/es/%E7%94%A8%E7%BE%A4%E6%99%96%E8%87%AA%E5%B8%A6%E5%8F%8D%E5%90%91%E4%BB%A3%E7%90%86%E5%AE%9E%E7%8E%B0HTTPS%E8%AE%BF%E9%97%AE).

## Uso en múltiples dispositivos

Se pueden descargar las diferentes versiones de clientes de Bitwarden desde la [**página de descarga oficial**](https://bitwarden.com/download/).

### Cliente de escritorio

Se recomienda utilizar la extensión de navegador [**Bitwarden - Free Password Manager**](https://chrome.google.com/webstore/detail/bitwarden-free-password-m/nngceckbapebfimnlniiiahkandclblb).

Al iniciar sesión, hacer clic en el engranaje en la esquina superior izquierda para acceder a la configuración:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210503215149.png)

En el entorno de `autohospedaje`, ingrese la dirección IP:puerto externo del NAS de Synology en la `URL del servidor` para iniciar sesión correctamente.

Si lo desea, también puede descargar el cliente de escritorio.

### Móvil

Simplemente descargue la aplicación Bitwarden en AppStore o en cualquier tienda de aplicaciones, y configure el entorno de autohospedaje en la página de inicio de sesión, siguiendo los mismos pasos que en la versión de escritorio.

## Copia de seguridad de la base de datos de contraseñas

Hay dos formas de hacer una copia de seguridad de la base de datos de Bitwarden:

1. Seleccione `Exportar base de datos de contraseñas` en la versión web o en el cliente.
2. Haga una copia de seguridad directa de la carpeta `data`.

## Referencias y agradecimientos

- [Servicios avanzados de Synology NAS - Implementación de Bitwarden, un administrador de contraseñas multiplataforma](https://www.ioiox.com/archives/70.html)
- [Construyendo un servidor de contraseñas de Bitwarden de terceros con Synology](https://ppgg.in/blog/10271.html#comment-8463)

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.