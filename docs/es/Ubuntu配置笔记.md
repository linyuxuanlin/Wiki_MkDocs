# Notas de Configuración de Ubuntu

## Problema de la Hora en el Sistema Dual

Después de instalar un sistema dual, es común que surja un problema de sincronización de la hora entre Windows y Ubuntu. Puedes resolverlo utilizando el siguiente comando:

```shell
timedatectl set-local-rtc 1 --adjust-system-clock
```

## Instalación de Software

1. Chrome
2. VS Code
3. [**Qv2ray**](https://qv2ray.net/)
4. Git
   - `sudo apt install git`
   - `git config --global user.name "John Doe"`
   - `git config --global user.email johndoe@example.com`

## Consejos

### Ver Archivos Ocultos

Puedes utilizar la combinación de teclas `Ctrl` + `H` para mostrar archivos ocultos.

### Abrir la Terminal

La combinación de teclas `Ctrl` + `Alt` + `T` te permitirá abrir la terminal.

### Comandos

Nota: `<xx>` indica obligatorio, `(xx)` indica opcional.

- cd
  - Cambia el directorio de trabajo
  - `cd <ruta del directorio>`
- pwd
  - Muestra la ruta absoluta actual
  - `pwd`
- mkdir
  - Crea un directorio
  - `mkdir (opciones) <nombre del directorio>`
- ls
  - Lista el contenido de un directorio
  - `ls (opciones) (nombre del directorio)`
- touch
  - Cambia la marca de tiempo de un archivo o directorio
  - `touch (opciones) <nombre del archivo>`
- mv
  - Mueve o renombra archivos/directorios
  - `mv (opciones) (archivo/directorio de origen) <archivo/directorio de destino>`
- cp
  - Copia archivos/directorios
  - `cp (opciones) (nombre del archivo/directorio de origen) <nombre del archivo/directorio de destino>`
- rm
  - Elimina archivos/directorios
  - `rm (opciones) <nombre del archivo/directorio>`

## Referencias y Agradecimientos

- [Tutorial de Instalación de ROS](https://mp.weixin.qq.com/s?__biz=MzU4Mzc1NDA5Mw==&mid=2247486645&idx=1&sn=8ba442af57060b4d608d4c24d4307921&chksm=fda504b7cad28da11a2dd782b60dce466d53ad8e260f161b1e47f24423cc1e9f9aabc486c7f3&mpshare=1&scene=1&srcid=1125YhpxcX5as5se6rsek2IS&sharer_sharetime=1606233866320&sharer_shareid=57baeb2b96d0cff9b17ac2c15b36602b&key=a402d93e91746f46ae3228f3f1014e2c74a235c331168642475573a82dabce23902b3593a2a240439e9e37cd9b2ceaeab2b3b2130d952ee61260b30c6cad24ab3f1907dd57abfae9934d0c9487ddc4364b41261c6fb7277d94de784fa9718f9f60712a15b25f505ab7105346330f16f4b659970a5143e8aa882da96dc76c0100&ascene=1&uin=MTk5MDUwOTA0Mg%3D%3D&devicetype=Windows+10+x64&version=6300002f&lang=zh_CN&exportkey=A0ZOktA1B68GOdT4vmLQPxA%3D&pass_ticket=b2tffRx7FG4vxDxfZxW7b9rGQf%2FK8YGbZtslM9VWUgnItoiwUPJYOD8ciwJbwx%2BC&wx_header=0)

[para_ser_reemplazado[1]]
[para_ser_reemplazado[2]]

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.