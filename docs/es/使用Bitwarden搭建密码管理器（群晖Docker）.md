# Configuración de Bitwarden como administrador de contraseñas en Synology Docker

Nota: Debido a que la imagen de bitwarden_rs ha cambiado de nombre y la extensión de navegador oficial de Bitwarden no es compatible con versiones antiguas, lo que impide el inicio de sesión, asegúrese de reemplazar `bitwardenrs/server` por `vaultwardenrs/server` en el texto a continuación y asegúrese de que la versión sea igual o superior a 1.27.0.

Este artículo describe cómo implementar de forma privada el servidor de administración de contraseñas Bitwarden en su propio Synology utilizando Docker.

![Imagen](https://media.wiki-power.com/img/20210503221838.png)

Actualmente existen diversas soluciones de administración de contraseñas como 1Password, Lastpass, KeePass, Bitwarden, entre otras. Cada una tiene sus ventajas y desventajas. En este caso, la necesidad es poder sincronizar en múltiples dispositivos, que sea de código abierto y se pueda implementar de manera privada, además de contar con la función de rellenar automáticamente las contraseñas. Por eso, se eligió implementar Bitwarden en el Synology personal, ya que cumple con estos requisitos y además ofrece una interfaz atractiva.

## Implementación en Synology Docker

### Creación de una carpeta para almacenar datos

En el directorio "docker", cree una carpeta para almacenar los datos de Bitwarden, por ejemplo, "docker/bitwarden".

### Descarga de la imagen y configuración del contenedor

Abra la suite Docker de Synology, descargue la imagen "bitwardenrs/server", iníciela con un doble clic y marque la opción "Habilitar reinicio automático". Luego, acceda a la configuración avanzada.

En la página de "Volúmenes", configure la carpeta de montaje seleccionando "Agregar carpeta" y elija la ruta local "docker/bitwarden". El directorio de montaje debe ser "/data" (por defecto).

![Imagen](https://media.wiki-power.com/img/20210503211711.png)

En la página de "Configuración de puertos", configure manualmente el puerto del contenedor correspondiente al puerto local 80 (por ejemplo, se puede configurar como "8003").

![Imagen](https://media.wiki-power.com/img/20210503211759.png)

Una vez finalizada la configuración, inicie el contenedor. Luego, abra su navegador e ingrese la dirección IP local de Synology seguida del puerto (por ejemplo, "IP-de-Synology:8003") para acceder a la página de inicio de sesión de Bitwarden. Sin embargo, cuando intente crear una cuenta e iniciar sesión, es posible que vea un mensaje de error.

![Imagen](https://media.wiki-power.com/img/20210503212146.png)

Esto se debe a que el contenedor Docker en sí no proporciona configuración de puerto seguro (HTTPS), y Bitwarden requiere HTTPS para iniciar sesión (con cifrado SSL para evitar ataques de intermediarios). Por lo tanto, es necesario utilizar el servicio de proxy inverso incorporado en Synology para acceder a través de HTTPS al puerto HTTP interno. Puede encontrar un tutorial detallado en [**Cómo implementar el acceso HTTPS con el proxy inverso incorporado de Synology**](https://wiki-power.com/%E7%94%A8%E7%BE%A4%E6%99%96%E8%87%AA%E5%B8%A6%E5%8F%8D%E5%90%91%E4%BB%A3%E7%90%86%E5%AE%9E%E7%8E%B0HTTPS%E8%AE%BF%E9%97%AE).

## Uso en varios dispositivos

Puede descargar clientes de Bitwarden desde la [**página de descargas oficial**](https://bitwarden.com/download/).

### Cliente de escritorio

Se recomienda utilizar la extensión del navegador [**Bitwarden - Administrador de contraseñas gratuito**](https://chrome.google.com/webstore/detail/bitwarden-free-password-m/nngceckbapebfimnlniiiahkandclblb) para iniciar sesión. Cuando inicie sesión, haga clic en el pequeño engranaje en la esquina superior izquierda y vaya a la configuración.

![Imagen](https://media.wiki-power.com/img/20210503215149.png)

En "Entorno de autohospedaje", ingrese la "URL del servidor" como la IP de su Synology seguida del puerto externo. Luego podrá iniciar sesión normalmente.

Si lo prefiere, también puede descargar la aplicación de escritorio.

### Cliente móvil

Aquí tienes la traducción al español:

```markdown
Descarga la aplicación Bitwarden directamente desde la AppStore o cualquier tienda de aplicaciones. Al iniciar sesión en la aplicación, también será necesario configurar un entorno de autohospedaje, un proceso que es idéntico al de la versión de escritorio.

## Respaldo de la Base de Datos de Contraseñas

Existen dos métodos para respaldar la base de datos de Bitwarden:

1. Desde la aplicación web o el cliente, selecciona la opción `Exportar base de datos de contraseñas`.
2. Realiza una copia de seguridad directa de la carpeta `data`.

## Referencias y Agradecimientos

- [Servicios avanzados en NAS Synology - Implementación de Bitwarden, el administrador de contraseñas multiplataforma](https://www.ioiox.com/archives/70.html)
- [Configuración de un servidor de contraseñas Bitwarden de terceros en un NAS Synology](https://ppgg.in/blog/10271.html#comment-8463)

> Dirección original del artículo: <https://wiki-power.com/>
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.
```

Por favor, avísame si necesitas alguna otra traducción o si tienes alguna otra pregunta.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
