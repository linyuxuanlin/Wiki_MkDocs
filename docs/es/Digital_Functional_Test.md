# Prueba Funcional Digital 🚧

## Referencias y Agradecimientos

- _Los Fundamentos de la Prueba de Semiconductores Digitales_
- _Fundamentos de la Prueba Utilizando ATE_

> Original: <https://wiki-power.com/>  
> Esta publicación está protegida por el acuerdo [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) y debe ser reproducida con atribución.

## Temporización de Conducción y Comparación

- D0 o Conducción Encendida: Inicio del ciclo para cada canal.
- D1 o Datos de Conducción: Inicio del pulso de conducción para cada canal.
- D2 o Retorno de Conducción: Fin del pulso de conducción para cada canal.
- D3 o Conducción Apagada: Tiempo de cambio de E/S.
- R0 o Inicio de Comparación (Encendido): Inicio de la ventana de comparación para cada canal (ventana de sincronización).
- R1 o Fin de Comparación (Apagado): Fin de la ventana de comparación para cada canal (ventana de sincronización) o sincronización de flanco.

## Resolución de Problemas en la Depuración Funcional Digital

1. Reduzca la frecuencia de prueba.
2. Vea la forma de onda real y modifique la posición de comparación.
3. Repita las líneas de patrón varias veces para prevenir la influencia del tiempo de configuración.
4. Utilice el método Shmoo para el análisis.
5. Cambie el orden de ejecución de la prueba para evitar la interacción entre las pruebas.
6. Preste atención al Modo del Controlador Electrónico de Pin.
7. Vt, Hi-Z, Largeswing-VT1K o Smallswing-VT?
   - Hi-Z: se utilizará el puente de equilibrio para la conducción, y VCOM se utilizará para las cargas de corriente.
   - Vt: conectado directamente al nivel de Vt a través de una resistencia de 50Ω. Si la salida del DUT funciona a alta velocidad, el uso de VT reduce las reflexiones vistas por el comparador.
8. Verifique si el TDR está calibrado.
9. Defectos en el patrón en sí mismo.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.