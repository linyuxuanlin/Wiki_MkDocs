```markdown
# Fundamentos de la Sintaxis de VBT

## Objetos de Datos

### TheHdw y TheExec

Existen dos manejadores globales en la interfaz de VBT para operar el hardware del probador:

- **TheHdw (El Hardware)**: Proporciona acceso y control a los instrumentos, e incluye funciones generales del hardware, como las alarmas.
- **TheExec (El Ejecutivo)**: Para controlar las funciones relacionadas con el programa de pruebas en general, como ejecutar la prueba, manejar los resultados de la prueba y grabar el registro de datos.

A continuación, se muestran ejemplos de su uso:

```vbscript
' Establecer el rango actual actual del pin p0
TheHdw.DCVI.Pins("p0").CurrentRange = 0.002
```

```vbscript
' Obtener la ruta del archivo STDF de salida actual
CurrStdfFile = TheExec.Datalog.Setup.STDFOutputFile
```

### Otros Objetos de Datos

En la interfaz de VBT se incluyen otros manejadores globales, como **PinListData** (Datos de la Lista de Pines), **DSPWave** (Onda DSP), **RtaDataObj (Objeto de Datos de Ajuste en Tiempo de Ejecución)**, y otros más. Continuaremos explorándolos en futuros artículos.

## Acceso Por Instrumento o Por Pin

La sintaxis de VBT admite el acceso al hardware del probador **por instrumento** o **por pin**, y son equivalentes en el resultado. A continuación, se muestran ejemplos de su uso:

```vbscript
' Acceso por Instrumento, aplica un solo instrumento a diferentes pines
With TheHdw.instrument
    .Pins("Vcc").CurrentLimit = 0.75
    .Pins("Vee").ForceValue = 3.2
End With
```

```vbscript
' Acceso por Pin, define una lista de pines y luego utiliza diferentes instrumentos
With TheHdw.Pins("Vcc,Vdd,Vee")
    .instrument1.Disconnect
    .instrument2.CurrentLimit = 0.75
End With
```

## Estructura del Código de VBT

Un archivo de código VBT debe tener el nombre `VBT_xxx`, y el nombre debe ser único.

El **valor de retorno** de una función de VBT se espera que sea 0 de forma predeterminada, o puede causar resultados inesperados.
```

Para los parámetros relacionados con **timing** (tiempo) y **levels** (niveles), puedes añadirlos en el Editor de Instancias o en la hoja de Prueba Instantánea, sin necesidad de incluirlos en la función VBT. Y puedes controlar si habilitarlos en la función VBT siguiendo este uso:

```vbscript
TheHdw.Digital.ApplyLevelsTiming
```

Para los **límites de prueba**, puedes utilizar el siguiente código:

```vbscript
TheExec.Flow.TestLimit
```

para comparar un valor de resultado con límites bajos/alto, y enviar el resultado de la prueba (`TL_SUCCESS`/`TL_ERROR`) y otra información al registro de datos.

Para comprender más claramente **la estructura básica** de una función de prueba VBT, aquí tienes un ejemplo:

```vbscript
Public Function VBTLeakTest(Pins As PinList, ForceVoltage As Double, PrePattern As PatternSet) As Long
    On Error GoTo errHandler

    Dim measure_results As New PinListData

    ' Configurar timing y niveles para el Patrón de Preacondicionamiento
    TheHdw.Digital.ApplyLevelsTiming ConnectAllPins:=True, loadLevels:=True, loadTiming:=True, relaymode:=tlPowered

    ' Ejecutar el Patrón de Preacondicionamiento y probar si pasa o falla
    TheHdw.Patterns(PrePattern).test pfAlways, 0

    ' Aplicar voltaje y medir corriente
    With TheHdw.DCVI.Pins(Pins)
        .Mode = tlDCVIModeVoltage
            ... ' Código adicional
        measure_results = .Meter.Read
    End With

    ' Prueba utilizando límites en el flujo y escribir en el registro de datos
    Call TheExec.Flow.TestLimit(resultval:=measure_results, unit:=unitAmp, forceval:=ForceVoltage, forceunit:=unitVolt, ForceResults:=tlForceFlow)

    ' Restablecer la variable
    measure_results = Nothing

    Exit Function
errHandler:
    If AbortTest Then Exit Function Else Resume Next
End Function
```

## Multi-Sitio

🚧

## Operación de la Lista de Pines

🚧

## Consejos en VBA

- Evita guardar código en VBA, ya que esto creará enlaces internos en el libro de trabajo. En su lugar, guarda en la interfaz de DataTool.
- Si te encuentras con el error "Procedimiento Demasiado Grande", es posible que estés chocando con la restricción de Excel de 64K límite por archivo vb. Pero en realidad, es posible que hayas olvidado cambiar la versión de 32 bits a 64 bits del sistema Windows.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.