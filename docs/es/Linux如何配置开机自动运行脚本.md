# Cómo configurar la ejecución automática de scripts al arrancar en Linux

## Para sistemas que utilizan SysV init

Nota: Los siguientes métodos son adecuados para distribuciones de Linux que utilizan el sistema SysV init (como Ubuntu 18.04 o versiones posteriores, o Debian). Para distribuciones que utilizan Systemd (como Ubuntu 18.04 o versiones posteriores), utilice el comando `systemctl` para administrar los servicios de inicio.

Supongamos que el script que deseamos ejecutar automáticamente al arrancar se llama `xxx.sh`. Primero, cree un script de inicio en el directorio `/etc/init.d`, por ejemplo, con el nombre `autorun.sh`:

```shell
sudo nano /etc/init.d/autorun.sh
```

Agregue el script que desea ejecutar automáticamente al arrancar:

```bash title="autorun.sh"
#!/bin/bash
/ruta/al/xxx.sh  # Reemplace con la ruta específica
```

Agregue el script `autorun.sh` a los servicios de inicio del sistema:

```shell
sudo update-rc.d autorun.sh defaults
```

Establezca el script `autorun.sh` para que se inicie automáticamente al arrancar:

```shell
sudo update-rc.d autorun.sh enable
```

De esta manera, el script `autorun.sh` se ejecutará automáticamente al reiniciar el sistema.

## Para sistemas que utilizan Systemd

Si su distribución de Linux utiliza Systemd como administrador de inicio (por ejemplo, Ubuntu 18.04 o versiones posteriores), puede utilizar el comando `systemctl` para configurar la ejecución automática.

Supongamos que el script que desea ejecutar automáticamente al arrancar es `xxx.sh`. Primero, cree un archivo Unit que describa el servicio que desea iniciar automáticamente, por ejemplo, `autorun.service`:

```shell
sudo nano /etc/systemd/system/autorun.service
```

En el archivo Unit, defina la configuración de su servicio. A continuación, se muestra un ejemplo:

```service title="autorun.service"
[Unit]
Description=Mi Servicio
After=network.target
[Service]
ExecStart=/ruta/a/xxx.sh
[Install]
WantedBy=default.target
```

Los parámetros significan lo siguiente:

- `Description`: Descripción de su servicio.
- `After`: Especifica cuándo se debe iniciar su servicio en relación con otros servicios. Por ejemplo, `network.target` significa que su servicio se iniciará después de que se inicie el servicio de red.
- `ExecStart`: Especifica la ruta del script o comando que desea ejecutar.
- `WantedBy`: Especifica el objetivo (target) en el que su servicio debe iniciarse. `default.target` significa que se iniciará en el objetivo predeterminado.

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

Ahora su servicio está configurado para ejecutarse automáticamente al arrancar el sistema. Puede reiniciar el sistema para verificar si el servicio se inicia correctamente.

---

[Reemplace_esto[1]]  
[Reemplace_esto[2]]

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.