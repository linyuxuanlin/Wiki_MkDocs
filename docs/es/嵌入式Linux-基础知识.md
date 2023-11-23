# Linux Embebido - Conceptos Básicos

## Comandos Comunes

- Ver información de la CPU: `cat /proc/cpuinfo`
- Ver la versión del kernel: `cat /proc/version`
- Ver el uso de la memoria: `cat /proc/meminfo`
  - También se puede utilizar el comando `free` para obtener una visión general del uso de la memoria
- Ver el uso del almacenamiento FLASH: `cat /proc/partitions`
- Ver los procesos en ejecución: `top`
- Ver los sistemas de archivos soportados: `cat /proc/filesystems` (nodev indica que no se necesita montar un dispositivo de bloque)
- Ver la frecuencia principal de la CPU: `cat /sys/devices/system/cpu/cpu0/cpufreq/cpuinfo_cur_freq`

## Controladores en Linux

En Linux, los controladores se utilizan para establecer una relación de mapeo entre los dispositivos de hardware y los archivos de Linux.

Por ejemplo, al controlar un LED o un botón, no es necesario conocer la conexión de hardware específica. Solo se necesita saber qué archivo representa a cada dispositivo, y luego se puede controlar el dispositivo de la misma manera a través del archivo.

## Referencias y Agradecimientos

- [[野火]i.MX Linux 开发实战指南](https://doc.embedfire.com/linux/imx6/base/zh/latest/index.html)

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.