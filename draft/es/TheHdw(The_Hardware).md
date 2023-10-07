# TheHdw (El Hardware) 🚧

**TheHdw** es un objeto para acceder a propiedades y métodos relacionados con el hardware del sistema de prueba.

## DCVI

```vbscript
TheHdw.DCVI
```

### Pines

```vbscript
TheHdw.DCVI.Pins(PinList)
```

---

## TheHdw.PPMU

🚧

## TheHdw.Digital

### ApplyLevelsTiming

Para cargar los datos de nivel y tiempo.

#### Uso

```vbscript
TheHdw.Digital.ApplyLevelsTiming(ConnectAllPins, LoadLevels, LoadTiming, RelayMode, InitPinsHi, InitPinsLo, InitPinsHiZ, PinLevelsSheet, DCCategory, DCSelector, TimeSetSheet, ACCategory, ACSelector, EdgeSetSheet)
```

#### Parámetros

- **ConnectAllPins**: Booleano opcional, valor predeterminado como `False`.
  - `True`: Conectar todos los pines del dispositivo.
  - `False`: No conectar.
- **LoadLevels**: Booleano opcional, valor predeterminado como `False`.
  - `True`: Cargar valores de nivel.
  - `False`: No cargar.
- **LoadTiming**: Booleano opcional, valor predeterminado como `False`.
  - `True`: Cargar valores de tiempo.
  - `False`: No cargar.
- **RelayMode**: `tlRelayMode` opcional, valor predeterminado como `tlUnpowered`. Controla el cambio en caliente de los relés.
  - `tlPowered`: Cambio en caliente. No apaga el DUT antes de establecer los niveles y conectar.
  - `tlUnpowered`: Evita el cambio en caliente. Apaga el DUT antes de establecer los niveles y conectar.
- **InitPinsHi**: Cadena opcional. Establece los pines con estado de conductor alto.
- **InitPinsLo**: Cadena opcional. Establece los pines con estado de conductor bajo.
- **InitPinsHiZ**: Cadena opcional. Establece los pines con estado de conductor de impedancia.
- **PinLevelsSheet**: Cadena opcional. Una hoja de niveles de pin.
- **DCCategory**: Cadena opcional.
- **DCSelector**: Cadena opcional.
- **TimeSetSheet**: Cadena opcional.
- **ACCategory**: Cadena opcional.
- **ACSelector**: Cadena opcional.
- **EdgeSetSheet**: Cadena opcional.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.