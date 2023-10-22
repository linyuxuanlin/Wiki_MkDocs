# Guía de Inicio de ESXi

VMware ESXi es un administrador de máquinas virtuales que se puede instalar directamente en hardware. Esta guía se basa en ESXi 8 y todavía está en fase de borrador.

Puede comenzar siguiendo esta guía: [**Guía de Resolución de Problemas para Enrutador Virtual - Parte 2: Conocimientos Esenciales y Proceso de Instalación para Máquinas Virtuales ESXi 8.0**](https://post.smzdm.com/p/a8x6o5on/p3/?sort_tab=hot/#comments)

Cuando llegue a la sección "5. Modificar el Espacio Predeterminado de ESXi", siga los siguientes pasos para modificar el tamaño predeterminado de ESXi.

### Reduzca el Espacio Usado por VMFSL

Dentro de los primeros 5 segundos después de iniciar la instalación del sistema, presione `Shift` + `O`, ingrese `cdromBoot runweasel systemMediaSize=min` para configurar la memoria virtual al mínimo. Para obtener más detalles, consulte la documentación oficial [**Resumen de Almacenamiento del Sistema ESXi**](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.esxi.install.doc/GUID-474D003B-C6FB-465D-BC1B-5FD30F8E2209.html?hWord=N4IghgNiBcIM4E84BcCmBbAsqgJgSzAGU8AvVEAXyA#esxi-70-system-storage-links-2).

### Instalación de una Máquina Virtual con Windows 11

Windows 11 tiene requisitos de sistema más exigentes y durante la instalación, es posible que aparezca el mensaje "Este equipo no puede ejecutar Windows 11". Esto generalmente se debe a la verificación de TPM y se puede evitar siguiendo estos pasos:

1. En la página de inicio de la máquina virtual, habilite "Seguridad basada en virtualización de Windows".
2. En la página "Instalar ahora" una vez que esté dentro de la máquina virtual de Windows, presione las teclas de acceso rápido `Shift` + `F10` para abrir una ventana de comandos (si no aparece la ventana de comandos, podría deberse a la disposición del teclado, intente conectar un teclado externo).
3. Ingrese "regedit" para abrir el Editor del Registro. En la ruta "HKEY_LOCAL_MACHINE\SYSTEM\Setup", cree dos valores DWORD de 32 bits:
   - `BypassTPMCheck` con un valor hexadecimal de `1`.
   - `BypassSecureBootCheck` con un valor hexadecimal de `1`.

Si aún no puede realizar la instalación, verifique otros requisitos, como una frecuencia de CPU de al menos 1 GHz, más de 64 GB de espacio en disco y más de 4 GB de RAM. Para obtener información detallada, consulte [**Requisitos del Sistema**](https://www.microsoft.com/en-us/windows/windows-11-specifications?r=1).

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.