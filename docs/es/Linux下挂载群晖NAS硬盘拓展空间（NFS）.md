# Montar un disco NAS de Synology en Linux para ampliar el espacio (NFS)

Si tu servidor tiene un espacio de almacenamiento limitado, puedes intentar montar un disco NAS de Synology como una extensión de tu espacio de almacenamiento.

## Configuración en el NAS de Synology

### Habilitar el servicio NFS

Abre la configuración de Synology, selecciona "Servicios de archivos" y activa el servicio NFS. Puedes elegir el protocolo más reciente.

### Configurar los permisos NFS de la carpeta

En la sección "Carpetas compartidas" dentro de la configuración, elige la carpeta compartida que deseas habilitar para NFS. Haz clic en "Editar" y ve a la pestaña de "Permisos NFS". Luego, haz clic en "Agregar" para crear una nueva regla NFS.

En "Servidor o dirección IP", introduce la dirección IP del servidor desde el cual deseas acceder al NAS de Synology (por ejemplo, si tu servidor y el NAS de Synology están en la misma red local, puedes ingresar la dirección IP interna de tu servidor, como 192.168.1.2). Marca las opciones "Permitir conexiones desde puertos no privilegiados" y "Permitir a los usuarios acceder a carpetas montadas". Puedes dejar los demás ajustes en su configuración predeterminada.

## Montar en el servidor

En primer lugar, instala el servicio NFS:

```bash
apt update
apt install nfs-common
```

Luego, en el servidor, crea la ruta de montaje, por ejemplo:

```bash
sudo mkdir /DATOS/nfs/musica
```

Finalmente, ejecuta el comando de montaje:

```bash
mount -t nfs IP_del_NAS:ruta_de_carpeta_compartida /ruta_del_cliente_NFS
```

Por ejemplo:

```bash
sudo mount -t nfs 192.168.1.3:/volume1/musica /DATOS/nfs/musica
```

Si no se producen errores, puedes usar el comando `df` para verificar el estado del montaje.

## Referencias y Agradecimientos

- [Cómo montar un disco NAS de Synology en Linux (Ubuntu) a través del servicio NFS](https://cloud.tencent.com/developer/article/2104277)

> Dirección original del artículo: <https://wiki-power.com/>
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.