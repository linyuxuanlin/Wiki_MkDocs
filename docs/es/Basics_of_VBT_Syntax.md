# Fundamentos de la Sintaxis de VBT

## Objetos de Datos

### TheHdw y TheExec

En la interfaz de VBT, existen dos manejadores globales para operar el hardware del probador:

- **TheHdw (El Hardware)**: Permite el acceso y control de los instrumentos, e incluye funciones generales del hardware, como las alarmas.
- **TheExec (El Ejecutivo)**: Para controlar las funciones relacionadas con el programa de prueba en su totalidad, como ejecutar la prueba, gestionar los resultados de la prueba y registrar el registro de datos.

A continuación, se presentan ejemplos de su uso:

```vbscript
' Establecer el rango actual de la clavija p0
TheHdw.DCVI.Pins("p0").CurrentRange = 0.002
```

```vbscript
' Obtener la ruta del archivo STDF de salida actual
CurrStdfFile = TheExec.Datalog.Setup.STDFOutputFile
```

### Otros Objetos de Datos

En la interfaz de VBT se incluyen más manejadores globales, como **PinListData**, **DSPWave**, **RtaDataObj (Objeto de Datos de Ajuste en Tiempo de Ejecución)**, y otros más. Seguiremos explorándolos en futuros artículos.

## Acceso por Instrumento o por Clavija

La sintaxis de VBT permite acceder al hardware del probador **por instrumento** o **por clavija**, siendo equivalentes en el resultado. A continuación, se presentan ejemplos de su uso:

```vbscript
' Acceso por instrumento, aplica un solo instrumento a diferentes clavijas
With TheHdw.instrument
    .Pins("Vcc").CurrentLimit = 0.75
    .Pins("Vee").ForceValue = 3.2
End With
```

```vbscript
' Acceso por clavija, define una lista de clavijas y luego utiliza diferentes instrumentos
With TheHdw.Pins("Vcc,Vdd,Vee")
    .instrument1.Disconnect
    .instrument2.CurrentLimit = 0.75
End With
```

## Estructura del Código VBT

Un archivo de código VBT debe tener el nombre `VBT_xxx`, y el nombre debe ser único.

El **valor de retorno** de una función VBT se espera que sea 0 de forma predeterminada, o puede causar resultados inesperados.

Para los parámetros relacionados con el **tiempo** y los **niveles**, puedes agregarlos en el Editor de Instancias o en la hoja de Prueba Instantánea; no es necesario incluirlos en la función VBT. Y puedes controlar si habilitarlos en la función VBT mediante el siguiente uso:

```vbscript
TheHdw.Digital.ApplyLevelsTiming
```

Para los **límites de prueba**, puedes utilizar el siguiente código:

```vbscript
TheExec.Flow.TestLimit
```

para comparar el valor del resultado con los límites bajos/alto, y enviar el resultado de la prueba (`TL_SUCCESS`/`TL_ERROR`) y otra información al registro de datos.

Para comprender más claramente **la estructura básica** de una función de prueba VBT, aquí tienes un ejemplo:

```vbscript
Public Function VBTLeakTest(Pins As PinList, ForceVoltage As Double, PrePattern As PatternSet) As Long
    On Error GoTo errHandler

    Dim measure_results As New PinListData

    ' Configurar el tiempo y los niveles para el Patrón de Preacondicionamiento
    TheHdw.Digital.ApplyLevelsTiming ConnectAllPins:=True, loadLevels:=True, loadTiming:=True, relaymode:=tlPowered

    ' Ejecutar el Patrón de Preacondicionamiento y realizar la prueba de Pasar/Fallar
    TheHdw.Patterns(PrePattern).test pfAlways, 0

    ' Aplicar V, Medir I
    With TheHdw.DCVI.Pins(Pins)
        .Mode = tlDCVIModeVoltage
            ... ' Código adicional
        measure_results = .Meter.Read
    End With

    ' Realizar la prueba utilizando los límites en el flujo y escribir en el registro de datos
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

- Evita guardar código en VBA, ya que esto generará enlaces internos en el libro de trabajo. En su lugar, guarda en la interfaz DataTool.
- Si te encuentras con el error "Procedure Too Large", es posible que estés chocando con la restricción de Excel de 64K como límite por archivo vb. Sin embargo, en realidad, podría ser que hayas olvidado cambiar la versión de 32 bits a 64 bits del sistema Windows.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.