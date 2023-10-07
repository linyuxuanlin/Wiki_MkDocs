# Básicos de la sintaxis de VBT

> Esta publicación solo está disponible en inglés.

## Objetos de datos

### TheHdw y TheExec

Hay dos manejadores globales en la interfaz VBT, para operar el hardware del probador:

- **TheHdw (El Hardware)**: Soporte para acceder y controlar los instrumentos, e incluye funciones más generales del hardware, como alarmas.
- **TheExec (El Ejecutivo)**: Para controlar las funciones generales del programa de prueba, como ejecutar la prueba, manejar los resultados de la prueba y registrar el registro de datos.

A continuación se muestran ejemplos de su uso:

```vbscript
' Establecer el rango actual del pin p0
TheHdw.DCVI.Pins("p0").CurrentRange = 0.002
```

```vbscript
' Obtener la ruta del archivo de salida STDF actual
CurrStdfFile = TheExec.Datalog.Setup.STDFOutputFile
```

### Otros objetos de datos

Se incluyen más manejadores globales en la interfaz VBT, como **PinListData**, **DSPWave**, **RtaDataObj (Objeto de datos de ajuste en tiempo de ejecución)** y así sucesivamente. Continuaremos explorándolos en futuros artículos.

## Acceso por instrumento o por pin

La sintaxis VBT admite el acceso al hardware del probador **por instrumento** o **por pin**, son equivalentes en el resultado. A continuación se muestran ejemplos de su uso:

```vbscript
' Acceso por instrumento, aplica un solo instrumento a diferentes pines
With TheHdw.instrument
    .Pins("Vcc").CurrentLimit = 0.75
    .Pins("Vee").ForceValue = 3.2
End With
```

```vbscript
' Acceso por pin, define una lista de pines y luego usa diferentes instrumentos
With TheHdw.Pins("Vcc,Vdd,Vee")
    .instrument1.Disconnect
    .instrument2.CurrentLimit = 0.75
End With
```

## Estructura del código VBT

Un archivo de código VBT debe tener el nombre `VBT_xxx`, y el nombre debe ser único.

El **valor de retorno** de una función VBT se espera que sea 0 por defecto, o puede causar resultados inesperados.

Para los parámetros de **timing** y **levels**, puedes agregarlos en el Editor de Instancias o en la hoja de Prueba Instantánea, no es necesario incluirlos en la función VBT. Y puedes controlar si habilitarlos en la función VBT siguiendo este uso:

```vbscript
TheHdw.Digital.ApplyLevelsTiming
```

Para los **límites de prueba**, puedes usar el siguiente código:

```vbscript
TheExec.Flow.TestLimit
```

para comparar un valor de resultado con límites bajos/alto, y enviar el resultado de la prueba (`TL_SUCCESS`/`TL_ERROR`) y otra información al registro de datos.

Para ver más claramente **la estructura básica** de una función de prueba VBT, aquí hay un ejemplo:

```vbscript
Public Function VBTLeakTest(Pins As PinList, ForceVoltage As Double, PrePattern As PatternSet) As Long
    On Error GoTo errHandler

    Dim measure_results As New PinListData

    ' Configurar timing y levels para el Patrón de Preacondicionamiento
    TheHdw.Digital.ApplyLevelsTiming ConnectAllPins:=True, loadLevels:=True, loadTiming:=True, relaymode:=tlPowered

    ' Ejecutar el Patrón de Preacondicionamiento y probar para Pasar/Fallar
    TheHdw.Patterns(PrePattern).test pfAlways, 0

    ' Forzar V, Medir I
    With TheHdw.DCVI.Pins(Pins)
        .Mode = tlDCVIModeVoltage
            ... ' Código adicional
        measure_results = .Meter.Read
    End With

    ' Probar usando límites en el flujo y escribir en el registro de datos
    Call TheExec.Flow.TestLimit(resultval:=measure_results, unit:=unitAmp, forceval:=ForceVoltage, forceunit:=unitVolt, ForceResults:=tlForceFlow)

    ' Restablecer la variable
    measure_results = Nothing

    Exit Function
errHandler:
    If AbortTest Then Exit Function Else Resume Next
End Function
```

## Multi-sitio

🚧

## Operación de PinList

🚧

## Consejos en VBA

- Evite guardar código en VBA, ya que esto creará enlaces internos en el libro de trabajo. En su lugar, guarde en la interfaz de DataTool.
- Si encuentra el error "Procedimiento demasiado grande", es posible que esté en contra de la restricción de Excel de 64K de límite por archivo vb. Pero en realidad, es posible que haya olvidado cambiar la versión de 32 bits a 64 bits del sistema Windows.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.