# Cómo construir una biblioteca en línea con Calibre (Docker en Synology)

Cómo construir una biblioteca en línea con calibre-web (Docker) en Synology NAS.

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210429125418.png)

En comparación con el método tradicional de usar carpetas, el método de gestión de bibliotecas representado por Calibre de código abierto puede proporcionar funciones más ricas, como lectura en línea, descarga, conversión de formato, envío por correo electrónico, eliminación de libros duplicados, etc. Calibre-web es una imagen de Docker basada en Calibre que nos permite implementar la biblioteca en servidores como Synology de manera muy conveniente.

## Crear una carpeta inicial

En primer lugar, cree una carpeta de recursos de biblioteca. Aquí, creé una carpeta compartida llamada `book` directamente en la raíz del disco:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210429214028.png)

En consecuencia, cree una carpeta llamada `calibre-web` en la carpeta `docker`, que se utiliza específicamente para almacenar los archivos de configuración de la imagen de Docker.

## Crear contenedor

Abra el paquete Docker de Synology, busque `johngong/calibre-web` en el registro, descárguelo haciendo doble clic y luego inicialice el contenedor y haga clic en la configuración avanzada.

En la página `Volumen`, agregue carpetas de mapeo y cargue las rutas `/library` y `/config` respectivamente:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210429214908.png)

En la página `Configuración de puerto`, agregue el mapeo de puerto y principalmente mapee el puerto `8083` interno del contenedor. Aquí elegí `5004`.

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210429215121.png)

Luego, cree y ejecute el contenedor.

## Ejecutar prueba

Abra la dirección IP interna de Synology: 5004 para abrir la interfaz de administración. La cuenta predeterminada es `admin` y la contraseña es `admin123`.

Tenga en cuenta que la función de carga de libros no está habilitada de forma predeterminada. Debe hacer clic en `Permisos de administración` - `Editar configuración básica` - `Habilitar carga` en orden para habilitar la función de carga de libros.

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210429215628.png)

## Habilitar HTTPS

### Usar el proxy inverso incorporado en Synology (recomendado)

Puede consultar el tutorial específico en el artículo [**Implementar acceso HTTPS con proxy inverso incorporado en Synology**](https://wiki-power.com/es/%E7%94%A8%E7%BE%A4%E6%99%96%E8%87%AA%E5%B8%A6%E5%8F%8D%E5%90%91%E4%BB%A3%E7%90%86%E5%AE%9E%E7%8E%B0HTTPS%E8%AE%BF%E9%97%AE).

### Método de agregar certificado directamente

Copia el certificado y el archivo de clave que ha solicitado en la carpeta `docker/calibre-web/`.

Luego, en calibre-web, haga clic en `Permisos de administración` - `Editar configuración básica` - `Configuración del servidor` en orden para configurar la ruta del archivo de certificado SSL y clave (por ejemplo, `/config/wiki-power.com.cer` y `/config/wiki-power.com.key`), y luego haga clic en Guardar.

De esta manera, puede habilitar el acceso HTTPS.

## Referencias y agradecimientos

- [Instalación del sistema de gestión de libros calibre-web en Synology Docker](https://www.chrno.cn/index.php/docker/15.html)

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.