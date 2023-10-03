# Diseño EMC entre la tierra de señal y la tierra de la carcasa

Por lo general, entre la tierra de señal y la tierra de la carcasa en una PCB, se utiliza un condensador de alta tensión (1 ~ 100nF / 2kV) y una gran resistencia (1MΩ) en paralelo para mejorar el rendimiento EMC:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220620162528.png)

El condensador actúa como un filtro de paso alto. Desde el punto de vista de EMI, puede evitar la radiación de antena al hacer que las interferencias de alta frecuencia generadas internamente en el circuito fluyan a través de la carcasa hacia la tierra; desde el punto de vista de EMS, puede suprimir la diferencia de voltaje común transitoria entre la fuente de interferencia de alta frecuencia y el circuito, ya que a veces no se puede conectar directamente (la tierra después del puente rectificador de 220VAC no se puede conectar directamente a la tierra de la carcasa) o la conexión directa no es lo suficientemente segura.

La resistencia actúa como una descarga de carga para evitar daños en el circuito por ESD. Si solo se conecta la tierra de señal y la tierra de la carcasa con un condensador, la tierra de señal estará flotando. Durante las pruebas de ESD, la tierra de señal acumulará gradualmente cargas de alta tensión. Una vez que supere la tensión que los dos puntos de tierra más cercanos pueden soportar, se producirá una descarga de arco que generará una corriente muy grande en unos pocos nanosegundos, dañando el circuito. Al agregar esta resistencia en paralelo, se puede descargar lentamente la carga.

## Referencias y agradecimientos

- [¿Qué se dice sobre la conexión de resistencia y capacitancia entre la tierra de PCB y la carcasa metálica?](https://mp.weixin.qq.com/s/vAdoDyBed4uIfISrP0Zeyw)

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.