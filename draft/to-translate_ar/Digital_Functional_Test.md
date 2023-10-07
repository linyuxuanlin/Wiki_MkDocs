# Prueba Funcional Digital 🚧

> Esta publicación solo está disponible en inglés.

## Referencias y Agradecimientos

- _Los Fundamentos de la Prueba de Semiconductores Digitales_
- _Fundamentos de la Prueba Utilizando ATE_

> Original: <https://wiki-power.com/>  
> Esta publicación está protegida por el acuerdo [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en), debe ser reproducida con atribución.

## Tiempo de Conducción y Comparación

- D0 o Conducción Encendida: Inicio del ciclo para cada canal.
- D1 o Conducción de Datos: Inicio del pulso de conducción para cada canal.
- D2 o Retorno de Conducción: Fin del pulso de conducción para cada canal.
- D3 o Conducción Apagada: Tiempo del interruptor de E/S.
- R0 o Inicio de Comparación (Encendido): Inicio de la ventana de comparación para cada canal (disparo de ventana).
- R1 o Fin de Comparación (Apagado): Fin de la ventana de comparación para cada canal (disparo de ventana) o borde de disparo.

## Solución de Problemas de Depuración Funcional Digital

1. Reducir la frecuencia de prueba.
2. Ver la forma de onda real, modificar la posición de comparación.
3. Repetir las líneas de patrón varias veces para evitar la influencia del tiempo de configuración.
4. Utilizar el método Shmoo para analizar.
5. Cambiar el orden de ejecución de la prueba, para evitar la interacción entre pruebas.
6. Prestar atención al Modo de Conductor Electrónico de Pin.
7. ¿Vt, Hi-Z, Largeswing-VT1K o Smallswing-VT?
   - Hi-Z: se utilizará el puente de equilibrio para la conducción, y VCOM se utilizará para las cargas de corriente.
   - Vt: conectarse directamente al nivel Vt a través de una resistencia de 50Ω. Si la salida del DUT está funcionando a alta velocidad, el uso de VT resulta en menos reflexiones vistas por el comparador.
8. Verificar si TDR está calibrado.
9. Defectos con el patrón en sí mismo.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.