# TheExec (El Ejecutivo) 🚧

**TheExec (El Ejecutivo)** es uno de los objetos de más alto nivel que proporciona acceso a propiedades relacionadas con la ejecución de pruebas.

## Flujo

```vbscript
TheExec.Flow
```

### Límite de Prueba

```vbscript
TheExec.Flow.TestLimit(resultVal, lowVal, hiVal, lowCompareSign,
highCompareSign, scaletype, unit, formatStr, TName, compareMode, pinName,
forceVal, forceunit, customUnit, customForceunit, ForceResults, TNum)
```

Parámetros más utilizados:

- **resultVal** (obligatorio): El valor del resultado que se escribirá.
- **lowVal**, **hiVal**: Los límites inferior y superior. El valor predeterminado es lowVal <= resultVal <= hiVal.
- **unit**: La unidad de medida.
  - `unitAmp` `unitVolt` `unitDb` `unitHz` `unitTime` .
- **TName**: Un nombre de prueba para registrar los datos. Si se deja en blanco, se utilizará el nombre de la instancia de la prueba.
- **pinName**: El nombre del pin a registrar.
- **forceVal**, **forceunit**: El valor y la unidad de la condición de prueba.
- **ForceResults**: Si se debe forzar un resultado de aprobación o rechazo, o si se deben usar los límites especificados en una tabla de flujo.

Por ejemplo:

```vbscript
TheExec.Flow.TestLimit resultVal:=Vout_Measure, _
                        unit:=unitVolt, _
                        Tname:="Voltaje de Salida", _
                        pinName:=vout_pin, _
                        forceval:=vin_pin_voltage, _
                        forceunit:=unitVolt, _
                        forceresults:=tlForceFlow, _
                        lowval:=VOT_LowLimit, _
                        hival:=VOT_HiLimit
```

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.