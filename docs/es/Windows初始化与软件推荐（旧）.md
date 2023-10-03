# Inicialización de Windows y recomendaciones de software (antiguo)

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210117142759.jpg)

> Para la versión actualizada, consulte [**Personal Onboarding Workflow (Windows)**](https://wiki-power.com/es/Personal_Onboarding_Workflow_%28Windows%29/)

¿Cuáles son las opciones de configuración y software necesarios después de instalar un sistema Windows?

## Algunas configuraciones personales

- No usar una cuenta de Microsoft para la inicialización
- Activar la opción de diagnóstico (necesario para la versión de vista previa del sistema)
- Renombrar el nombre del equipo
- Configuración - Actualización y seguridad - Opciones de desarrollador - Activar el modo de desarrollador
- Modo de vista previa
- [**Excelente rendimiento**](https://bobi.site/archives/875)
- Instalar el cliente de Synology Drive
- Instalar [**Huorong Security**](https://www.huorong.cn/) (para evitar que Windows Defender elimine archivos por error)
- Iniciar sesión en la cuenta de Microsoft
- Activar Windows: [**HEU_KMS_Activator**](https://github.com/zbezj/HEU_KMS_Activator)
- Actualizar el sistema y los controladores
- Configurar el navegador (Edge Canary)
  - Extensiones
  - [**Activar la descarga en múltiples hilos de Chrome (Edge)**](https://wiki-power.com/es/%E5%BC%80%E5%90%AFChrome%EF%BC%88Edge%EF%BC%89%E5%A4%9A%E7%BA%BF%E7%A8%8B%E4%B8%8B%E8%BD%BD)
- Configuración de control de cuentas de usuario: establecer en "Nunca notificar"
- Personalizar la barra de tareas
- Configurar la configuración personalizada
- Configurar la configuración de visualización
- Configurar el historial y la sincronización del portapapeles
- Configurar el mouse, el touchpad, el teclado, etc.
- Configuración de inicio oculto: [GodMode](https://github.com/linyuxuanlin/File-host/tree/main/software/GodMode.lnk)
- Desactivar la hibernación: `powercfg /hibernate off`
- [**Solucionar el problema de visualización de caracteres chinos en un entorno en inglés**](https://blog.csdn.net/amoscn/article/details/106224359)

## Instalar software

- Software de trabajo
- [**VS Code insiders**](https://code.visualstudio.com/docs/?dv=win64&build=insiders)
  - Sincronización de configuración
- [**Logitech Options**](https://www.logitech.com.cn/zh-cn/product/options): exclusivo para ratones Logitech (descarga e instalación automática)
- [**Python**](https://www.microsoft.com/zh-cn/p/python-39/9p7qfqmjrfp7?rtc=1&activetab=pivot:overviewtab)
- [**WeChat (versión de prueba)**](https://dldir1.qq.com/weixin/Windows/Beta/WeChatBeta.exe)
- [**Git**](https://git-scm.com/downloads)
- [winget](https://www.microsoft.com/zh-cn/p/app-installer/9nblggh4nns1?ocid=9nblggh4nns1_ORSEARCH_Bing&rtc=2&activetab=pivot:overviewtab)
  - Powertoys: `WinGet install powertoys`
- [**QQ versión modificada**](https://github.com/linyuxuanlin/File-host/blob/main/software/QQ%209.4.2.27666%20Lite-20210118%20by%20flighty-Q.exe)

- [**DiskDenius**](https://www.diskgenius.cn/download.php): herramienta de disco
  - Reservar 10 GB de espacio libre (SSD)
  - NTFS, 4096 sectores (alineación de 4k)
- [**KMS**](https://github.com/linyuxuanlin/File-host/tree/main/software/KMS.exe):

  - Activar Windows (ya no funciona)
  - Desactivar Windows Defender

- [**GitHub Desktop**](https://desktop.github.com)

- [**Win10Apps**](https://github.com/linyuxuanlin/File-host/tree/main/software/Win10Apps.exe)
- [**Geek Uninstaller**](https://github.com/linyuxuanlin/File-host/tree/main/software/geekuninstaller.exe)
- [**Bandizip**](https://github.com/linyuxuanlin/File-host/tree/main/software/Bandizip.exe): versión sin publicidad
- [**Dism++**](https://www.chuyu.me/zh-Hans/): herramienta del sistema
- [**JPEGView**](https://github.com/linyuxuanlin/File-host/tree/main/software/JPEGView64.zip)
- [**Kit de herramientas de tarjeta dura**](http://www.kbtool.cn/down.php)
- [**Mem Reduct**](https://github.com/henrypp/memreduct/releases)
- [**OInstall**](https://github.com/linyuxuanlin/File-host/tree/main/software/OInstall.exe): herramienta de Office
- [**PowerToys**](https://github.com/microsoft/PowerToys/releases/)
- [**Snipaste**](https://zh.snipaste.com/download.html)
- [**SpaceSniffer**](https://github.com/linyuxuanlin/File-host/tree/main/software/SpaceSniffer.exe)
- [**Sumatra PDF**](https://www.sumatrapdfreader.org/download-free-pdf-viewer.html)
- [**PotPlayer**](https://daumpotplayer.com/download/)
- [**PicGo**](https://github.com/Molunerfinn/PicGo/releases/tag/v2.3.0-beta.4)
- [**Bamboo**](https://christopherwk210.github.io/bamboo/): software de compresión de imágenes basado en TinyPNG
- [**DeskGo**](https://pm.myapp.com/invc/xfspeed/qqpcmgr/data/DeskGo_2_9_1051_127_lite.exe): organizador de escritorio
- [**Wise Driver Care**](https://github.com/linyuxuanlin/File-host/blob/main/software/Wise%20Driver%20Care.zip): herramienta de gestión e instalación de controladores
- [**NDM**](https://www.neatdownloadmanager.com/index.php/en/): descargador
- [**AltDrag**](https://github.com/linyuxuanlin/File-host/tree/main/software/AltDrag.exe): herramienta pequeña para arrastrar, cambiar el tamaño y ajustar la opacidad de las ventanas
- [**Raidrive**](https://github.com/linyuxuanlin/File-host/blob/main/software/raidrive-2020-6-80.exe): herramienta para montar discos remotos (versión sin publicidad). Yo monto mi NAS como disco local a través de WebDAV. 

## Software opcional

- [**7-Zip**](https://github.com/linyuxuanlin/File-host/tree/main/software/7z.exe): Alta tasa de compresión
- [**WPS Edición Especial**](http://wpspro.support.wps.cn/gov/guangdong/chaozhou/installation/WPS%20Office%202019%20%E4%B8%93%E4%B8%9A%E7%89%88%EF%BC%88%E6%BD%AE%E5%B7%9E%E5%B8%82%E5%85%9A%E6%94%BF%E6%9C%BA%E5%85%B3%E5%8D%95%E4%BD%8D%EF%BC%89.exe): Sin publicidad, limpio y fresco
  - Enlace de respaldo: https://pan.baidu.com/s/1d_DVwbLScESe1Zh7um6YTA
  - Código de extracción: `y1xe`
- [**SoftDownloader**](https://github.com/linyuxuanlin/File-host/tree/main/software/SoftDownloader.zip): Encuentra la mayoría de los programas y los instala con un solo clic
- [**Maestro de Oficina Multicolor**](https://github.com/linyuxuanlin/File-host/tree/main/software/OfficeBox.zip): Herramientas de oficina útiles y poderosas
- [**IObit Unlocker**](https://github.com/linyuxuanlin/File-host/tree/main/software/IObit_Unlocker.exe): Herramienta para desbloquear archivos en uso
- [**EmptyFolderNuker**](https://github.com/linyuxuanlin/File-host/tree/main/software/EmptyFolderNuker.exe): Herramienta para detectar y eliminar carpetas vacías

## Referencias y agradecimientos

> Dirección original del artículo: <https://wiki-power.com/>
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.