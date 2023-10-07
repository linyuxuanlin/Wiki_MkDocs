# Cómo configurar la ejecución automática de scripts al iniciar Linux

## Para sistemas que utilizan SysV init

Nota: Los siguientes métodos son aplicables a distribuciones de Linux que utilizan el sistema SysV init (como Ubuntu 18.04 y versiones posteriores, o Debian). Para distribuciones que utilizan Systemd (como Ubuntu 18.04 y versiones posteriores), utilice el método `systemctl` para administrar los servicios de inicio.

Supongamos que el script que deseamos ejecutar automáticamente al iniciar es `xxx.sh`. Primero, cree un script de inicio en el directorio `/etc/init.d`, por ejemplo, llamado `autorun.sh`:

```shell
sudo nano /etc/init.d/autorun.sh
```

Agregue el script que desea ejecutar automáticamente al inicio:

```bash title="autorun.sh"
#!/bin/bash
/path/to/xxx.sh  # cambiar por la ruta específica
```

Agregue el script `autorun.sh` al servicio de inicio del sistema:

```shell
sudo update-rc.d autorun.sh defaults
```

Configure el script `autorun.sh` para que se inicie automáticamente al iniciar el sistema:

```shell
sudo update-rc.d autorun.sh enable
```

De esta manera, el script `autorun.sh` se ejecutará automáticamente después de reiniciar.

## Para sistemas que utilizan Systemd

Si su distribución de Linux utiliza Systemd como administrador de inicio (como Ubuntu 18.04 y versiones posteriores), puede utilizar el comando `systemctl` para configurar la ejecución automática.

Supongamos que el script que desea ejecutar automáticamente al iniciar es `xxx.sh`. Primero, cree un archivo Unit que describa el servicio que desea iniciar automáticamente, como `autorun.service`:

```shell
sudo nano /etc/systemd/system/autorun.service
```

En el archivo Unit, defina la configuración de su servicio. Aquí hay un ejemplo:

```service title="autorun.service"
[Unit]
Description=Mi servicio
After=network.target
[Service]
ExecStart=/path/to/xxx.sh
[Install]
WantedBy=default.target
```

Los parámetros son:

- `Description`: descripción de su servicio.
- `After`: especifica qué otros servicios deben iniciarse antes de su servicio. Por ejemplo, `network.target` significa que su servicio se iniciará después de que se inicien los servicios de red.
- `ExecStart`: especifica la ruta del script o comando que desea ejecutar.
- `WantedBy`: especifica el objetivo (target) en el que su servicio debe iniciarse. `default.target` significa que su servicio se iniciará cuando se inicie el objetivo predeterminado.

Guarde y cierre el archivo, luego ejecute el siguiente comando para recargar la configuración de Systemd:

```shell
sudo systemctl daemon-reload
```

Habilite su servicio con el siguiente comando:

```shell
sudo systemctl enable autorun.service
```

Finalmente, inicie el servicio con el siguiente comando:

```shell
sudo systemctl start autorun.service
```

Ahora, su servicio está configurado para ejecutarse automáticamente al iniciar el sistema. Puede reiniciar el sistema para verificar si el servicio se inicia correctamente.

---

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.