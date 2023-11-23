# Método para habilitar la virtualización en placas base MSI

## Reiniciar y acceder a la BIOS

```cmd
shutdown.exe /r /o
```

Después de reiniciar, haga clic en `Solucionar problemas (Troubleshoot)` - `Opciones avanzadas (Advanced options)` - `Ajustes de firmware UEFI (UEFI Firmware Settings)` para ingresar a la BIOS de la placa base.

## Localizar la configuración relevante

1. Presione `F7` para acceder a las opciones avanzadas.
2. Navegue hasta `OC` - `Características de CPU (CPU Features)`.
3. Encuentre `Modo SVM / Virtualización Intel (según la CPU)`.

## Modificar la configuración

Cambie de `Deshabilitado (Disabled)` a `Habilitado (Enabled)`.

## Guardar y salir

Presione `F10` para guardar y salir.

## Referencias y agradecimientos

- [Cómo acceder a la BIOS](https://zhuanlan.zhihu.com/p/34223088)
- [Cómo habilitar la tecnología de virtualización en computadoras y placas base MSI](http://mumu.163.com/20181108/25905_784199.html)

> Dirección original del artículo: <https://wiki-power.com/>
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.