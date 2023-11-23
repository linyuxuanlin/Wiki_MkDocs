# Cómo habilitar el control remoto RDP a través de Internet (frp)

Utilizando frp para habilitar el control remoto de escritorio en cualquier red.

## Por qué utilizar RDP

RDP es un protocolo incorporado en Windows. En comparación con otros software de escritorio remoto en el mercado, como Todesk, Anydesk, y TeamViewer, tiene las siguientes ventajas:

- Mayor compatibilidad, se adapta automáticamente a la resolución del dispositivo y permite el uso del teclado y el mouse.
- Mayor libertad, no hay restricciones en la cantidad de dispositivos ni un sistema de membresía.
- La velocidad de conexión depende de la velocidad de la red y la configuración del servidor.

## Por qué utilizar frp

RDP solo es compatible con el uso de la misma subred IP. Para habilitar el control remoto en Internet, necesitamos utilizar el método frp para atravesar la red interna.

frp es un software de proxy inverso, es ligero pero potente, y permite que los dispositivos detrás de una red interna o un firewall brinden servicios al mundo exterior. Admite numerosos protocolos como HTTP, TCP, UDP, entre otros.  
El principio de habilitar el control remoto RDP a través de Internet utilizando frp es conectar el dispositivo controlado al servidor, y luego conectarnos al dispositivo controlado a través del servidor, logrando así el control remoto.

## Preparación

- Servidor (puede ser un servidor en la nube o una máquina física con una dirección IP pública)
- Dispositivo controlado (Windows debe ser una versión profesional o superior)
- Dispositivo de control remoto (compatible con todas las plataformas)

## Configuración del servidor

Primero, verifiquemos la arquitectura del servidor:

```shell
arch
```

Consulte la página de [**Releases**](https://github.com/fatedier/frp/releases) de frp y descargue la versión que coincida con su arquitectura (por ejemplo, si tengo una arquitectura `X86_64`, seleccionaré `amd64`):

```shell
wget https://github.com/fatedier/frp/releases/download/v0.36.2/frp_0.36.2_linux_amd64.tar.gz
```

Una vez descargado, descomprima y cambie el nombre:

```shell
tar -zxvf frp_0.36.2_linux_amd64.tar.gz && mv frp_0.36.2_linux_amd64 frp
```

Veamos los archivos dentro de la carpeta frp:

```shell
cd frp && ls
```

- frps
- frps.ini
- frpc
- frpc.ini

Entre ellos, `frps` y `frps.ini` son el programa y el archivo de configuración del servidor (la "s" al final significa servidor), mientras que `frpc` y `frpc.ini` están relacionados con el cliente (la "c" al final significa cliente). Por ahora, no los necesitamos, así que podemos eliminarlos:

```shell
rm -f frpc frpc.ini
```

A continuación, modifiquemos el archivo `frps.ini`:

```shell
vim frps.ini
```

```ini title="frps.ini"
[common]
bind_port = 7000
dashboard_port = 7500
token = 12345678
dashboard_user = admin
dashboard_pwd = admin
```

- **bind_port**: el puerto al que se conectan los clientes y el servidor, se utilizará más adelante al configurar el cliente, generalmente se puede dejar en su valor predeterminado.
- **dashboard_port**: el puerto del panel de control del servidor, generalmente se puede dejar en su valor predeterminado. Si se establece en el valor predeterminado de `7500`, se puede acceder al panel de control a través del puerto `7500` (por ejemplo, `IP del servidor:7500`) para verificar el estado de frp.
- **token**: la contraseña para la conexión entre el cliente y el servidor, establezca una contraseña por su cuenta.
- **dashboard_user** / **dashboard_pwd**: el nombre de usuario y la contraseña del panel de control, establezca un nombre de usuario y una contraseña por su cuenta.

Después de editar, presione `Esc` y luego ingrese `:wq` para guardar y salir.

Para ejecutar el servicio frp en segundo plano, podemos usar el comando nohup:

```shell
nohup ./frps -c frps.ini &
```

Si ve la siguiente salida:

```shell
nohup: ignoring input and appending output to 'nohup.out'
```

Significa que el servicio se está ejecutando correctamente. También podemos usar el comando `jobs` para verificar los servicios en ejecución.

Para probar si la configuración del servidor se ha realizado correctamente, podemos acceder a `x.x.x.x:7500` utilizando el nombre de usuario y la contraseña configurados anteriormente, para ver si podemos acceder al panel de control sin problemas. Si no se puede acceder al panel de control, es posible que se haya bloqueado el puerto correspondiente en el firewall del servidor.

## Configuración del cliente

Consulte la página de [**Releases**](https://github.com/fatedier/frp/releases) de frp para seleccionar y descargar la versión que corresponda a su arquitectura. Después de descargarlo, descomprímalo y cambie el nombre. Puede eliminar los archivos `frps` y `frps.ini`. Abra el archivo `frpc.ini`:

```ini title="frpc.ini"
[common]
server_addr = x.x.x.x
server_port = 7000
token = 12345678
[rdp]
type = tcp
local_ip = 127.0.0.1
local_port = 3389
remote_port = 7001
[smb]
type = tcp
local_ip = 127.0.0.1
local_port = 445
remote_port = 7002
```

- **server_addr**: Dirección IP del servidor, modifíquela según corresponda.
- **server_port**: Mantenga el mismo valor que el `bind_port` del servidor, que por defecto es `7000`.
- **token**: Contraseña de conexión, manténgala igual que la configurada en el servidor.

A continuación, configuraremos las reglas personalizadas:

- **[rdp]**: [xxx] representa el nombre de la regla, puede personalizarlo.
- **type**: Tipo de protocolo de reenvío, puede ser TCP/UDP.
- **local_port**: Número de puerto local, aquí se debe ingresar el puerto del protocolo RDP (3389).
- **remote_port**: Número de puerto abierto en el servidor, puede personalizarlo.

> El protocolo RDP (Remote Desktop Protocol) tiene el número de puerto predeterminado 3389 y utiliza el protocolo TCP.
> El protocolo SMB (Server Message Block) para compartir archivos en Windows tiene el número de puerto predeterminado 445 y utiliza el protocolo TCP.

Para ejecutar frpc en segundo plano, crearemos el script `frpc.vbs` y pegaremos el siguiente contenido:

```vbscript title="frpc.vbs"
set ws=WScript.CreateObject("WScript.Shell")
ws.Run "c:\frp\frpc.exe -c c:\frp\frpc.ini",0
```

Tenga en cuenta que es posible que deba modificar la ruta.

Coloque `frpc.vbs` en la carpeta `C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp` para que se inicie automáticamente al iniciar el sistema.

Si desea probarlo, puede ejecutar el script directamente o reiniciar para que se ejecute automáticamente.

## Configuración del cliente remoto

### El cliente de control es un dispositivo móvil

Si desea controlar una computadora de forma remota desde un teléfono móvil o un iPad, primero debe instalar la aplicación "Microsoft Remote Desktop" y luego seguir estos pasos:

1. En la aplicación, haga clic en el símbolo "+" en la esquina superior derecha y seleccione "Agregar PC".
2. En "Nombre de PC", ingrese "IP:remote_port", por ejemplo, `x.x.x.x:7001`, y luego haga clic en "Volver".
3. En "Nombre de cuenta", ingrese el nombre de usuario y la contraseña de la computadora controlada y luego haga clic en "Volver".

Si todo está configurado correctamente, debería poder controlar la computadora de forma remota sin problemas.

### El cliente de control es Windows

Simplemente busque y abra "Conexión de Escritorio Remoto" en el menú de inicio, ingrese "IP:remote_port", por ejemplo, `x.x.x.x:7001`, y siga las instrucciones para ingresar el nombre de usuario y la contraseña, para poder controlar la computadora de forma remota.

## Referencias y agradecimientos

- [Cómo hacer un túnel a través de la red local con frp](https://sspai.com/post/52523)
- [Uso del comando nohup en Linux](https://ehlxr.me/2017/01/18/Linux-%E7%9A%84-nohup-%E5%91%BD%E4%BB%A4%E7%9A%84%E7%94%A8%E6%B3%95/)
- [【Tutorial】Acceso remoto a través de frp](https://pa.ci/77.html)

> Dirección original del artículo: <https://wiki-power.com/>
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.