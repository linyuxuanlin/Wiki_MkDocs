# Cómo implementar el control remoto RDP en Internet (frp)

Usando frp para controlar el escritorio de forma remota en cualquier red.

## ¿Por qué usar RDP?

RDP es un protocolo incorporado en Windows. En comparación con otros software de escritorio remoto en el mercado, como Todesk, Anydesk, y TeamViewer, tiene las siguientes ventajas:

- Mejor compatibilidad, se adapta automáticamente a la resolución del dispositivo y se puede usar para conectar teclados y ratones.
- Mayor libertad, sin límite de cantidad de dispositivos ni sistema de membresía.
- La velocidad de conexión depende de la velocidad de la red de la computadora y la configuración del servidor.

## ¿Por qué usar frp?

RDP solo admite el uso en la misma red IP, por lo que para controlar de forma remota en Internet, necesitamos usar el método frp para penetrar en la red interna.

frp es un software de proxy inverso, es ligero pero potente y puede hacer que los dispositivos detrás de una red interna o un firewall proporcionen servicios al mundo exterior. Admite muchos protocolos, como HTTP, TCP, UDP, etc. El principio de usar frp para controlar el escritorio de forma remota en Internet es conectar el dispositivo controlado al servidor, y luego conectarnos indirectamente al dispositivo controlado a través del servidor.

## Preparación

- Servidor (puede ser un servidor en la nube o una máquina física con IP pública)
- Dispositivo controlado (Windows debe ser una versión profesional o superior)
- Dispositivo de control remoto (compatible con todas las plataformas)

## Configuración del servidor

Primero, verifique la arquitectura del servidor:

```shell
arch
```

Consulte la página de [**Releases**](https://github.com/fatedier/frp/releases) de frp, seleccione la versión que se adapte a su arquitectura (por ejemplo, si su arquitectura es `X86_64`, seleccione `amd64`):

```shell
wget https://github.com/fatedier/frp/releases/download/v0.36.2/frp_0.36.2_linux_amd64.tar.gz
```

Después de descargarlo, descomprímalo y cámbiele el nombre:

```shell
tar -zxvf frp_0.36.2_linux_amd64.tar.gz && mv frp_0.36.2_linux_amd64 frp
```

Veamos los archivos en la carpeta frp:

```shell
cd frp && ls
```

- frps
- frps.ini
- frpc
- frpc.ini

Entre ellos, `frps` y `frps.ini` son los programas y archivos de configuración del servidor (la "s" al final significa "servidor"), mientras que `frpc` y `frpc.ini` están relacionados con el cliente (la "c" al final significa "cliente"), que no usaremos por ahora y se pueden eliminar:

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

- **bind_port**: el puerto al que se conectan el cliente y el servidor, que se utilizará más adelante al configurar el cliente. Por lo general, se puede dejar en el valor predeterminado.
- **dashboard_port**: el puerto del panel de control del servidor, que se puede dejar en el valor predeterminado. Si se establece en el valor predeterminado de `7500`, se puede acceder al panel de control (por ejemplo, `IP del servidor:7500`) para ver el estado de frp.
- **token**: la contraseña para la conexión entre el cliente y el servidor, que debe establecerse por sí mismo.
- **dashboard_user** / **dashboard_pwd**: el nombre de usuario y la contraseña del panel de control, que deben establecerse por sí mismos.

Después de editar, presione `Esc` y luego ingrese `:wq` para guardar y salir.

Para ejecutar el servicio frp en segundo plano, podemos usar el comando nohup:

```shell
nohup ./frps -c frps.ini &
```

Si ve la siguiente salida:

```shell
nohup: ignoring input and appending output to 'nohup.out'
```

significa que el servicio se está ejecutando correctamente. También podemos usar el comando `jobs` para ver los servicios en ejecución.

Para probar si la configuración del servidor se ha realizado correctamente, podemos acceder a `x.x.x.x:7500` utilizando el nombre de usuario y la contraseña configurados anteriormente, para ver si podemos acceder al panel de control sin problemas. Si no se puede acceder al panel de control, es posible que se deba a que el puerto correspondiente no está abierto en el firewall del servidor.

## Configuración del cliente

De nuevo, consulte la página de [**Releases**](https://github.com/fatedier/frp/releases) de frp y descargue la versión adecuada para su arquitectura. Después de descargarlo, descomprima y cambie el nombre del archivo, y puede eliminar los archivos `frps` y `frps.ini`. Abra el archivo `frpc.ini`:

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

- **server_addr**: la dirección IP del servidor, por favor modifíquela según sea necesario.
- **server_port**: mantenga el mismo valor que el `bind_port` del servidor, que por defecto es `7000`.
- **token**: la contraseña de conexión, manténgala igual que la configurada en el servidor.

A continuación, configuramos las reglas personalizadas:

- **[rdp]**: [xxx] indica el nombre de la regla, que se puede personalizar.
- **type**: el tipo de protocolo de reenvío, que puede ser TCP/UDP.
- **local_port**: el número de puerto local, que aquí es el puerto del protocolo RDP (3389).
- **remote_port**: el número de puerto abierto en el servidor, que se puede personalizar.

> El número de puerto predeterminado para el protocolo RDP (Protocolo de escritorio remoto) en Windows es 3389, y el protocolo es TCP.
> El número de puerto predeterminado para el protocolo SMB (Protocolo de uso compartido de archivos de Windows) es 445, y el protocolo es TCP.

Para ejecutar frpc en segundo plano, creamos el script `frpc.vbs` y pegamos el siguiente contenido:

```vbscript title="frpc.vbs"
set ws=WScript.CreateObject("WScript.Shell")
ws.Run "c:\frp\frpc.exe -c c:\frp\frpc.ini",0
```

Tenga en cuenta que es posible que deba modificar la ruta.

Coloque `frpc.vbs` en el directorio `C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp` para que se inicie automáticamente al arrancar.

Si desea probarlo, puede ejecutar el script directamente o reiniciar para que se ejecute automáticamente.

## Configuración del cliente remoto

### El cliente de control es un dispositivo móvil

Si desea controlar su computadora de forma remota en su teléfono o iPad, primero debe instalar la aplicación `Microsoft Remote Desktop` y luego seguir estos pasos:

1. Haga clic en `+` - `Agregar computadora` en la esquina superior derecha de la aplicación.
2. En `Nombre de la computadora`, ingrese `IP:remote_port`, por ejemplo, `x.x.x.x:7001`, y luego haga clic en Atrás.
3. En `Nombre de usuario`, ingrese el nombre de usuario y la contraseña de la computadora controlada, y luego haga clic en Atrás.

Si todo está configurado correctamente, debería poder controlar su computadora de forma remota.

### El cliente de control es Windows

Simplemente busque y abra `Conexión a Escritorio remoto` en el menú Inicio, ingrese `IP:remote_port`, por ejemplo, `x.x.x.x:7001`, y siga las instrucciones para ingresar su nombre de usuario y contraseña para controlar su computadora de forma remota.

## Referencias y agradecimientos

- [Cómo usar frp para la penetración de red interna](https://sspai.com/post/52523)
- [Cómo utilizar el comando nohup en Linux](https://ehlxr.me/2017/01/18/Linux-%E7%9A%84-nohup-%E5%91%BD%E4%BB%A4%E7%9A%84%E7%94%A8%E6%B3%95/)
- [Cómo crear un escritorio remoto personalizado utilizando frp](https://pa.ci/77.html)

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.