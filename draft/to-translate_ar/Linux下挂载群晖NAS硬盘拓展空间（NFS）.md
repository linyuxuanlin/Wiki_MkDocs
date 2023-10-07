# Montar un disco duro de NAS Synology en Linux para expandir el espacio de almacenamiento (NFS)

Si su servidor tiene un espacio de almacenamiento limitado, puede intentar montar un disco duro de NAS Synology como espacio de almacenamiento adicional.

## Configuración en NAS Synology

### Habilitar el servicio NFS

Abra "Configuración" - "Servicio de archivos" - "NFS" en Synology, marque la casilla de verificación del servicio NFS y seleccione el protocolo más reciente.

### Configurar los permisos NFS de la carpeta

En "Configuración" - "Carpeta compartida", seleccione la carpeta compartida que desea habilitar NFS, haga clic en "Editar", cambie a la pestaña "Permisos NFS" y haga clic en "Agregar" para agregar una nueva regla NFS.

En "Servidor o dirección IP", escriba la dirección IP del servidor que necesita acceder a Synology (por ejemplo, si mi servidor y Synology están en la misma red local, simplemente escribo la dirección IP interna de mi servidor 192.168.1.2). Marque las casillas "Permitir conexiones desde puertos no privilegiados" y "Permitir a los usuarios acceder a las carpetas montadas", y mantenga las demás configuraciones por defecto.

## Montar en el servidor

Primero, instale el servicio NFS:

```bash
apt update
apt install nfs-common
```

Luego, cree una ruta de montaje en el servidor, por ejemplo:

```bash
sudo mkdir /DATA/nfs/music
```

Finalmente, ejecute el comando de montaje:

```bash
mount -t nfs Dirección IP de NAS:Ruta de carpeta compartida /Ruta de cliente NFS
```

Por ejemplo:

```bash
sudo mount -t nfs 192.168.1.3:/volume1/music /DATA/nfs/music
```

Si no hay errores, puede usar el comando "df" para verificar el estado de montaje.

## Referencias y agradecimientos

- [Montar NAS Synology como disco virtual en Linux (Ubuntu) a través del servicio NFS](https://cloud.tencent.com/developer/article/2104277)

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.