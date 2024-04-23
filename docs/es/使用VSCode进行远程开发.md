```markdown
# Usando VS Code para desarrollo remoto

—— Utiliza VS Code como una herramienta SSH para conectarte a un servidor remoto y programar.

## Contexto

Después de probar diferentes herramientas SSH, al final volví a utilizar VS Code por su interfaz atractiva y potente.  
Este artículo es solo un registro para futura referencia, algunas secciones no están detalladas. Para más tutoriales, consulta los enlaces al final del texto.

Serie de configuración básica de VS Code: [**Guía de productividad de VS Code - Configuración del entorno**](https://wiki-power.com/VSCode生产力指南-环境配置)

## Configuración de extensiones

Haz clic para instalar la extensión: [**Remoto - SSH**](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh)

Haz clic en el botón `Remote` en la esquina inferior izquierda para comenzar a utilizarlo.

## Otras configuraciones

### VS Code no puede monitorear los cambios de archivos en espacios de trabajo extensos

Ejecuta este comando para ver la restricción actual:

```shell
cat /proc/sys/fs/inotify/max_user_watches
```

Edita el archivo `/etc/sysctl.conf`:

```shell
sudo vim /etc/sysctl.conf
```

Agrega el siguiente código para aumentar la restricción al valor máximo:

```shell
fs.inotify.max_user_watches=524288
```

Guarda, activa la configuración:

```shell
sudo sysctl -p
```

### Imposibilidad de iniciar sesión con un nombre de usuario personalizado

En la configuración de VS Code, busca `Remote.SSH: Config File`, ingresa la ruta `C:\Users\tu_usuario_requerido\.ssh\config` y crea el archivo de configuración correspondiente en tu equipo local.

### Fallo en la conexión, aunque otros clientes SSH pueden conectarse

Posiblemente la versión del servicio sshd en el servidor remoto sea inferior a 7.6.0 y carezca de la característica para mostrar el puerto remoto. Para resolver este problema, necesitas actualizar la versión de sshd:

- Para Debian o Ubuntu: `sudo apt-get update && sudo apt-get install openssh-server`
- Para Red Hat o CentOS: `sudo yum update openssh-server`

También podría ser un problema de configuración de proxy, intenta cambiar o desactivar el proxy.

## Referencias y agradecimientos

- [Experiencia con VSCode Remote | El desarrollo en entornos Linux remotos es genial](https://zhuanlan.zhihu.com/p/64849549)
- [Solución al aviso de VSCode: VisualStudioCode no puede monitorear los cambios en este espacio de trabajo extenso](http://www.deadnine.com/somehow/2019/0208/1481.html)

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.
```  

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.