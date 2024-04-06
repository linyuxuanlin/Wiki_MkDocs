# Configuración de una biblioteca en línea con Calibre en Synology (Docker)

Cómo configurar una biblioteca en línea utilizando Calibre-web (Docker) en un NAS Synology.

![Imagen](https://media.wiki-power.com/img/20210429125418.png)

En comparación con el método tradicional de organizar libros en carpetas, la gestión de bibliotecas representada por software de código abierto como Calibre ofrece funciones más avanzadas, como lectura en línea, descargas, conversión de formatos, envío por correo electrónico y eliminación de libros duplicados. Calibre-web es una imagen Docker basada en Calibre que facilita la implementación de una biblioteca en servidores como los de Synology.

## Crear una carpeta inicial

En primer lugar, cree una carpeta de recursos para la biblioteca. En mi caso, he creado una carpeta compartida llamada `book` directamente en la raíz del disco:

![Imagen](https://media.wiki-power.com/img/20210429214028.png)

Además, dentro de la carpeta `docker`, cree una carpeta llamada `calibre-web` dedicada a almacenar los archivos de configuración de Docker.

## Crear el contenedor

Abra el paquete Docker de Synology y busque `johngong/calibre-web` en el registro. Descárguelo haciendo doble clic y luego inicialice el contenedor. Luego, vaya a la configuración avanzada.

En la página de `Volúmenes`, agregue las carpetas mapeadas con las rutas `/library` y `/config`:

![Imagen](https://media.wiki-power.com/img/20210429214908.png)

En la página de `Configuración de puertos`, agregue un mapeo de puerto, principalmente para redirigir el puerto `8083` del contenedor al exterior. En mi caso, he elegido el puerto `5004`.

![Imagen](https://media.wiki-power.com/img/20210429215121.png)

Luego, cree y ejecute el contenedor.

## Realizar pruebas

Abra la dirección IP de su red interna de Synology seguida del puerto `5004` para acceder a la interfaz de administración. Las credenciales por defecto son `admin` y `admin123`.

Tenga en cuenta que la función de carga de libros no está habilitada de forma predeterminada. Debe habilitarla yendo a `Permisos de administración` en la esquina superior derecha, luego a `Editar configuración básica` y finalmente activando la opción `Habilitar carga`.

![Imagen](https://media.wiki-power.com/img/20210429215628.png)

## Habilitar HTTPS

### Usar el proxy inverso incorporado en Synology (recomendado)

Para obtener instrucciones detalladas, consulte el artículo [**Cómo habilitar HTTPS con el proxy inverso incorporado de Synology**](https://wiki-power.com/%E7%94%A8%E7%BE%A4%E6%99%96%E8%87%AA%E5%B8%A6%E5%8F%8D%E5%90%91%E4%BB%A3%E7%90%86%E5%AE%9E%E7%8E%B0HTTPS%E8%AE%BF%E9%97%AE).

### Método para agregar un certificado directamente

Copia una copia de los archivos de certificado y clave que has obtenido en la carpeta `docker/calibre-web`.

Luego, dentro de Calibre-web, vaya a `Permisos de administración`, luego `Editar configuración básica` y finalmente `Configuración del servidor`. Configure la ruta de los archivos de certificado SSL y clave (por ejemplo, `/config/wiki-power.com.cer` y `/config/wiki-power.com.key`) y guarde la configuración.

De esta manera, podrá habilitar el acceso HTTPS.

## Referencias y Agradecimientos

- [Instalación de Calibre-web, un sistema de gestión de libros, en Docker en Synology](https://www.chrno.cn/index.php/docker/15.html)

> Dirección original del artículo: <https://wiki-power.com/>
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
