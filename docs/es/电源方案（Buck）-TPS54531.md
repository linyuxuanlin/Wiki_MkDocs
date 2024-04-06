# Solución de alimentación (Buck) - TPS54531

El TPS54531 es un convertidor Buck de 3.5V a 28V de entrada, 5A y 570kHz con modo Eco de TI.

Repositorio del proyecto: [**Collection_of_Power_Module_Design/DC-DC(Buck)/TPS54531**](<https://github.com/linyuxuanlin/Collection_of_Power_Module_Design/tree/main/DC-DC(Buck)/TPS54531>)

Vista previa en línea del proyecto:

<div class="altium-iframe-viewer">
  <div
    class="altium-ecad-viewer"
    data-project-src="https://github.com/linyuxuanlin/Collection_of_Power_Module_Design/raw/main/DC-DC(Buck)/TPS54531/TPS54531.zip"
  ></div>
</div>

## Características principales

- **Principio**: DC/DC (Buck)
- **Voltaje de entrada**: 3.5-28 V
- **Voltaje de salida**: Mínimo 0.8 V
- **Corriente de salida**: 5 A
- **Frecuencia de operación**: 570 kHz
- **Eficiencia**: Máximo 92%
- **Precio**: ¥ 3.80
- **Características**:
  - Modo Eco con saltos de pulso en carga ligera
  - Arranque suave ajustable para limitar la corriente de entrada
  - Umbral de bloqueo por subvoltaje programable (UVLO)
  - Protección contra sobretensiones transitorias
  - Protección contra corriente limitada, frecuencia de plegado y apagado térmico por ciclo

## Definición de pines

![](https://media.wiki-power.com/img/20210713153815.png)

## Diseño de referencia

![](https://media.wiki-power.com/img/20210713173605.png)

## Ajuste de parámetros

(Para obtener parámetros más detallados, consulte la hoja de datos)

### Ajuste del voltaje de salida

Ajuste el voltaje de salida (voltaje de referencia $V_{REF}=0.8 V$) mediante la modificación de las resistencias de división de retroalimentación $R_5$ y $R_6$:

$$
V_{OUT}=V_{REF}\times[\frac{R5}{R6}+1]
$$

Se recomienda que $R_5$ tenga un valor aproximado de 10 kΩ. En el diseño de referencia, se necesita una salida de 4.96 V, por lo que se toma $R_5$ = 10.2 kΩ y $R_6$ = 1.96 kΩ.

### Pin de habilitación

El pin EN se desactiva cuando el voltaje es inferior a 1.25 V y se deja flotante para habilitar. Aquí se utiliza una configuración de bloqueo por subvoltaje con dos resistencias.

### Modo Eco de ahorro de energía

Cuando la corriente pico del inductor es inferior a 160 mA, el chip entra en modo de ahorro de energía y apaga la salida.

### Apagado térmico

Cuando la temperatura del chip supera los 165℃, el chip se detiene y se reinicia cuando la temperatura desciende por debajo de los 165℃.

## Referencia de diseño de PCB

![](https://media.wiki-power.com/img/20210713161521.png)

![](https://media.wiki-power.com/img/20210713162833.png)

## Resumen de problemas comunes

- La corriente en el diodo de recirculación y en el inductor debe ser mayor que la corriente de salida.
- La parte posterior del chip debe tener cobre desnudo estañado para la disipación de calor.
- El diseño del PCB debe seguir la dirección de flujo de corriente del Buck.
- La placa terminada puede proporcionar una corriente de salida de 5 A, pero se requiere una disipación adicional de calor para corrientes superiores a 3 A. Los dispositivos de potencia como el diodo y el inductor pueden calentarse.

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
