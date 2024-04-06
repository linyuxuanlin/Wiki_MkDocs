# Cómo ejecutar VS Code en iPad

Nota: Este tutorial se basa en code-server v3.8.0 y CentOS 8.2.

![](https://media.wiki-power.com/img/20201221140748.jpg)

Se recomienda instalar el servicio code-server utilizando Docker compose.  
Solo se necesita una línea de comando para implementarlo, y no es necesario configurar la ejecución en segundo plano, ya que incluye entornos como Git.  
Para más detalles, consulta: [**Homelab - Editor de código en línea code-server**](https://wiki-power.com/Homelab-%E5%9C%A8%E7%BA%BF%E4%BB%A3%E7%A0%81%E7%BC%96%E8%BE%91%E5%99%A8code-server)

Si no deseas implementar code-server utilizando Docker compose, continúa leyendo.

## Configurar el servidor

En primer lugar, necesitarás un servidor que esté en funcionamiento las 24 horas del día (se recomienda comprar una instancia de Alibaba Cloud / Tencent Cloud para estudiantes, por solo ¥9.9 al mes).  
Para garantizar una buena experiencia de uso, se recomienda la siguiente configuración del servidor:

- 2 núcleos o más
- 1 GB de RAM o más

Instala Linux (en este caso, utilizaré CentOS 8.2) y asegúrate de que SSH se pueda conectar correctamente.

## Instalar code-server

En las versiones más recientes (≥v3.8.0), puedes instalar code-server directamente utilizando el siguiente script:

```shell
curl -fsSL https://code-server.dev/install.sh | sh
```

Si tienes problemas para descargarlo, es probable que se deba a la contaminación del DNS. Consulta [**GitHub - Cambiar el Host**](https://wiki-power.com/GitHub改Host) para solucionarlo.

## Ejecutar code-server

Utiliza el siguiente comando:

```shell
export PASSWORD="Establece una contraseña de acceso" && code-server --port 80 --host 0.0.0.0 --auth password
```

Si no aparece ningún error, abre un navegador e ingresa la dirección IP del servidor para acceder a VS Code en línea.

## Configurar la ejecución en segundo plano

Si ejecutas code-server en primer plano, el proceso se detendrá cuando cierres la conexión SSH.  
Para que se ejecute en segundo plano, puedes utilizar el programa screen (puedes considerarlo como un contenedor).

### Instalar screen

```shell
yum install screen
```

### Crear una tarea en screen

```shell
screen -S VSCode-online # VSCode-online es un nombre que puedes elegir
```

### Iniciar el servicio code-server

```shell
export PASSWORD="Establece una contraseña de acceso" && code-server --port 80 --host 0.0.0.0 --auth password
```

Si todo va bien, podrás acceder a code-server ingresando la dirección IP en el navegador.

## Ampliación

### Agregar un acceso directo en el escritorio

Si estás utilizando un iPad, puedes abrir Safari y hacer clic en el icono de "Compartir" en la esquina superior derecha, luego selecciona "Agregar a la pantalla de inicio".  
De esta manera, puedes utilizarlo como una aplicación y ocultar la barra de estado del navegador.  
Por cierto, también es compatible con teclado y ratón externos.

### Otras operaciones con screen

- Ver el ID de la tarea en ejecución: `screen -ls`
- Volver a ingresar a una tarea en ejecución en screen: `screen -r ID_de_tarea # El ID de la tarea debe incluir el número de identificación con prefijo`
- Finalizar la ejecución de una tarea: `screen -X -S ID_de_tarea quit`
- Salir de la interfaz de screen de la tarea actual: `Ctrl + A + D`

### Parámetros de comando relacionados con code-server

- Acceso a través de Internet: el servicio code-server se ejecuta de forma predeterminada en local (`127.0.0.1`). Para poder acceder a través de una dirección IP, puedes agregar el parámetro `--host 0.0.0.0`.
- Especificar el puerto de ejecución: `--port xxxx`, donde puedes reemplazar `xxxx` por `8888`; también puede ser `80` (usando el protocolo HTTP, accediendo directamente a través de la IP sin necesidad de agregar el número de puerto).
- Establecer una contraseña de acceso: agrega `--auth password`; si no es necesario, no agregues ningún parámetro o agrega `--auth none`.

### Instalación de Git

VS Code se puede utilizar junto con Git para facilitar el desarrollo en la nube.  
Puedes instalar Git utilizando el siguiente comando:

```shell
yum install git
```

### Acceso mediante un nombre de dominio

Acceder a través de la IP del servidor puede resultar un poco extraño, por lo que puedes asociar un nombre de dominio personalizado para acceder al servicio code-server.  
Compra un nombre de dominio y agrega la IP del servidor en la configuración de resolución DNS utilizando el tipo de registro A.

### Errores y soluciones en la versión actual

- No se puede sincronizar la configuración de usuario a través del servicio de sincronización de configuración integrado de VS Code: puedes solucionarlo instalando el complemento [**Settings Sync**](https://marketplace.visualstudio.com/items?itemName=Shan.code-settings-sync) de forma adicional.
- Error al iniciar sesión en GitHub al usar Settings Sync: configúralo utilizando un navegador de computadora.
- No se puede desplazar correctamente la página utilizando la rueda del ratón en un iPad: actualmente solo se puede desplazar directamente tocando la pantalla o utilizando las teclas de dirección del teclado.

## Referencias y agradecimientos

- [Ejecutar VSCode en el navegador (antiguo)](https://wiki-power.com/在浏览器上运行VSCode（旧）)
- [Cambiar el host de GitHub](https://wiki-power.com/GitHub改Host)
- [Instalación y uso de screen](https://www.jianshu.com/p/420569381e74)
- [Guía de configuración · cdr/code-server](https://github.com/cdr/code-server/blob/v3.8.0/doc/guide.md)

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
