# Guía de Inicialización de ESXi

VMware ESXi es un administrador de máquinas virtuales que se puede instalar en una máquina desnuda. Este tutorial se basa en ESXi 8 y todavía está en fase de borrador.

Puede seguir este tutorial para comenzar: [**"Guía de solución de problemas de enrutadores de software" Parte 2: Conocimientos esenciales y proceso de instalación de ESXi 8.0 para máquinas virtuales de niñera**](https://post.smzdm.com/p/a8x6o5on/p3/?sort_tab=hot/#comments)

Cuando llegue al punto "5. Modificar el espacio predeterminado de ESXI", utilice el siguiente método para cambiar el tamaño predeterminado del espacio de ESXI.

### Reducción de la ocupación de VMFSL

Dentro de los 5 segundos posteriores a hacer clic en "Instalar sistema", presione `Shift` + `O` e ingrese `cdromBoot runweasel systemMediaSize=min` para configurar la memoria virtual al valor mínimo. Consulte la documentación oficial [**Descripción general del almacenamiento del sistema ESXi**](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.esxi.install.doc/GUID-474D003B-C6FB-465D-BC1B-5FD30F8E2209.html?hWord=N4IghgNiBcIM4E84BcCmBbAsqgJgSzAGU8AvVEAXyA#esxi-70-system-storage-links-2) para obtener más información.

### Instalación de una máquina virtual de Windows 11

Windows 11 tiene requisitos de sistema bastante estrictos y es posible que aparezca el mensaje "Este equipo no puede ejecutar Windows 11" durante la instalación. El problema suele ser causado por la comprobación de TPM, que se puede evitar de la siguiente manera:

1. En la página de inicialización de la máquina virtual, habilite "Seguridad basada en la virtualización de Windows".
2. En la página "Instalar ahora" después de ingresar a la máquina virtual de Windows, presione las teclas `Shift` + `F10` para abrir la ventana de cmd (si la ventana de cmd no aparece, puede ser un problema con el teclado del portátil, intente conectar un teclado externo).
3. Ingrese "regedit" para abrir el editor del registro. Cree dos valores DWORD de 32 bits en la ruta "HKEY_LOCAL_MACHINE\SYSTEM\Setup":
   - "BypassTPMCheck" con un valor hexadecimal de "1".
   - "BypassSecureBootCheck" con un valor hexadecimal de "1".

Si aún no se puede instalar, intente verificar otros requisitos. Puede ser que algunos requisitos no se cumplan, como una frecuencia de reloj principal de más de 1 GHz, más de 64 GB de espacio en disco y más de 4 GB de memoria. Consulte [**Requisitos del sistema**](https://www.microsoft.com/en-us/windows/windows-11-specifications?r=1) para obtener más información.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.