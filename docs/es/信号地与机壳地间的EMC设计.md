# Diseño EMC entre tierra de señal y tierra de carcasa

Por lo general, entre la tierra de señal y la tierra de la carcasa en una PCB, se utiliza una conexión en paralelo de un condensador de alto voltaje (1~100nF/2kV) y una resistencia grande (1MΩ) con el fin de mejorar el rendimiento EMC, como se muestra a continuación:

![Imagen](https://media.wiki-power.com/img/20220620162528.png)

La función del condensador es permitir el paso de corriente alterna y bloquear la corriente continua. Desde una perspectiva de EMI, esto permite que las interferencias de alta frecuencia generadas internamente en el circuito fluyan hacia la carcasa y se descarguen a través de la tierra, evitando así la radiación de antenas. Desde una perspectiva de EMS, el condensador puede suprimir las diferencias de voltaje transitorias de modo común entre las fuentes de interferencia de alta frecuencia y el circuito, especialmente cuando no es seguro conectar directamente el circuito a tierra (por ejemplo, cuando la tierra de 220VAC después del puente rectificador no se puede conectar directamente a la tierra de la carcasa).

La función de la resistencia es descargar lentamente la carga para prevenir daños al circuito causados por ESD. Si solo se conecta la tierra de señal a la tierra de la carcasa mediante el condensador, la tierra de señal estará flotando. Durante las pruebas de ESD, la tierra de señal acumulará gradualmente una alta carga eléctrica. Si esta carga supera la tensión que las tierras más cercanas entre sí pueden soportar, se producirá una descarga de arco eléctrico que generará una corriente considerable en cuestión de nanosegundos, lo que dañaría el circuito. Al conectar en paralelo esta resistencia, se puede descargar la carga de manera gradual.

## Referencias y Agradecimientos

- [Conexión de resistencia y condensador entre tierra de PCB y carcasa de metal, ¿qué se dice al respecto?](https://mp.weixin.qq.com/s/vAdoDyBed4uIfISrP0Zeyw)

> Dirección original del artículo: <https://wiki-power.com/>
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
