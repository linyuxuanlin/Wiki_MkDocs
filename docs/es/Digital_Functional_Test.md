# Prueba Funcional Digital 🚧

## Referencias y Agradecimientos

- _Los Fundamentos de la Prueba de Semiconductores Digitales_
- _Fundamentos de la Prueba Utilizando ATE_

> Original: <https://wiki-power.com/>  
> Esta publicación está protegida por un acuerdo [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) y debe ser reproducida con atribución.

## Sincronización de Impulsos de Conducción y Comparación

- D0 o Inicio de Conducción: Comienzo del ciclo para cada canal
- D1 o Datos de Conducción: Inicio del pulso de conducción para cada canal
- D2 o Retorno de Conducción: Fin del pulso de conducción para cada canal
- D3 o Apagado de Conducción: Tiempo del interruptor de E/S
- R0 o Inicio de Comparación (Encendido): Inicio de la ventana de comparación para cada canal (disparo de ventana)
- R1 o Fin de Comparación (Apagado): Fin de la ventana de comparación para cada canal (disparo de ventana) o disparo de borde

## Solución de Problemas en la Depuración Funcional Digital

1. Reduzca la frecuencia de prueba.
2. Visualice la forma de onda real y modifique la posición de la comparación.
3. Repita las líneas de patrón varias veces para prevenir la influencia del tiempo de configuración.
4. Utilice el método Shmoo para el análisis.
5. Cambie el orden de ejecución de las pruebas para prevenir la interacción entre las pruebas.
6. Preste atención al Modo de Conductor Electrónico de Pin.
7. ¿Vt, Hi-Z, Largeswing-VT1K o Smallswing-VT?
   - Hi-Z: se utilizará el puente de equilibrio para la conducción, y VCOM se utilizará para las cargas de corriente.
   - Vt: conexión directa al nivel de Vt a través de una resistencia de 50Ω. Si la salida de DUT se ejecuta a alta velocidad, el uso de VT resulta en menos reflejos observados por el comparador.
8. Compruebe si TDR está calibrado.
9. Defectos en el patrón en sí mismo.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.