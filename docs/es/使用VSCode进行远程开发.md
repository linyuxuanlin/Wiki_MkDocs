# Uso de VS Code para Desarrollo Remoto

—— Utilizando VS Code como herramienta SSH para conectar y desarrollar en servidores remotos.

## Contexto

Después de probar diversas herramientas SSH, finalmente regresé a VS Code por su atractiva interfaz y potentes capacidades. Este artículo es una referencia futura y no profundiza en todos los detalles. Para obtener más tutoriales, consulta los enlaces al final del documento.

Configuración Básica de VS Code: [**Guía de Productividad de VS Code - Configuración del Entorno**](https://wiki-power.com/VSCode生产力指南-环境配置)

## Configuración de Extensiones

Haz clic para instalar la extensión: [**Remote - SSH**](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh)

Simplemente pulsa el botón `Remote` en la esquina inferior izquierda para comenzar a utilizarla.

## Otras Configuraciones

### VS Code no puede supervisar cambios en archivos en espacios de trabajo grandes

Ejecuta este comando para verificar la restricción actual:

```shell
cat /proc/sys/fs/inotify/max_user_watches
```

Edita el archivo `/etc/sysctl.conf`:

```shell
sudo vim /etc/sysctl.conf
```

Agrega el siguiente código para aumentar esta restricción al máximo:

```shell
fs.inotify.max_user_watches=524288
```

Guarda y habilita la configuración:

```shell
sudo sysctl -p
```

### No se puede utilizar un nombre de usuario personalizado para la conexión

En la configuración de VS Code, encuentra `Remote.SSH: Config File` y proporciona la ruta a tu archivo de configuración local, por ejemplo, `C:\Users\tu_usuario\.ssh\config`.

### Fallo en la conexión, pero otros clientes SSH pueden conectarse

Este problema puede deberse a que la versión de sshd en el servidor remoto es inferior a 7.6.0 y carece de la capacidad para mostrar el puerto remoto. Para solucionarlo, debes actualizar la versión de sshd:

- Para Debian o Ubuntu: `sudo apt-get update && sudo apt-get install openssh-server`
- Para Red Hat o CentOS: `sudo yum update openssh-server`

## Referencias y Agradecimientos

- [Experiencia con VSCode Remote | El Desarrollo en un Entorno Linux Remoto es Genial](https://zhuanlan.zhihu.com/p/64849549)
- [Solucionar Problemas de VSCode: VisualStudioCode No Puede Supervisar Cambios en un Espacio de Trabajo Grande](http://www.deadnine.com/somehow/2019/0208/1481.html)

> Dirección original del artículo: <https://wiki-power.com/>
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.