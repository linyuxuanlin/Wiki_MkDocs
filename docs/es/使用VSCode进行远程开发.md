# Desarrollo remoto con VS Code

- Utilizando VS Code como herramienta SSH para conectarse a servidores remotos y desarrollar.

## Contexto

Después de probar varias herramientas SSH, finalmente volví a VS Code por su interfaz atractiva y su gran potencial. Este artículo es solo una guía de referencia para futuras consultas, y algunos detalles no se explican en profundidad. Para obtener más tutoriales, consulte los enlaces al final del artículo.

Guía de configuración básica de VS Code: [**Guía de productividad de VS Code - Configuración del entorno**](https://wiki-power.com/VSCode生产力指南-环境配置)

## Configuración de extensiones

Haga clic en "Instalar extensión": [**Remoto - SSH**](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh)

Haga clic en el botón "Remoto" en la esquina inferior izquierda para usarlo.

## Otras configuraciones

### VS Code no puede monitorear cambios de archivos en espacios de trabajo grandes

Ejecute este comando para ver las restricciones actuales:

```shell
cat /proc/sys/fs/inotify/max_user_watches
```

Edite el archivo `/etc/sysctl.conf`:

```shell
sudo vim /etc/sysctl.conf
```

Agregue el siguiente código para aumentar esta restricción al valor máximo:

```shell
fs.inotify.max_user_watches=524288
```

Guarde y active la configuración:

```shell
sudo sysctl -p
```

### No se puede iniciar sesión con un nombre de usuario personalizado

En la configuración de VS Code, busque "Remote.SSH: Config File" y complete el valor de reemplazo con `C:\Users\your_username\.ssh\config`, y cree el archivo de configuración correspondiente en su computadora local.

### Error de conexión, pero se puede conectar con otros clientes SSH

Es posible que la versión de sshd en el servidor remoto sea inferior a 7.6.0 y carezca de la función para mostrar el puerto remoto. Para solucionar este problema, debe actualizar la versión de sshd:

- Para Debian o Ubuntu: `sudo apt-get update && sudo apt-get install openssh-server`
- Para Red Hat o CentOS: `sudo yum update openssh-server`

## Referencias y agradecimientos

- [Experiencia remota de VSCode | Desarrollo de entornos Linux remotos es genial](https://zhuanlan.zhihu.com/p/64849549)
- [Solución de problemas de VSCode: VisualStudioCode no puede monitorear cambios de archivos en este espacio de trabajo grande](http://www.deadnine.com/somehow/2019/0208/1481.html)

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.