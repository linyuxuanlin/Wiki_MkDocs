# TheHdw (El Hardware) 🚧

**TheHdw** es un objeto para acceder a las propiedades y métodos relacionados con el hardware del sistema de prueba.

## DCVI

```vbscript
TheHdw.DCVI
```

### Pines

```vbscript
TheHdw.DCVI.Pins(ListaDePines)
```

---

## TheHdw.PPMU

🚧

## TheHdw.Digital

### AplicarNivelesyTemporización

Para cargar los datos de nivel y temporización.

#### Uso

```vbscript
TheHdw.Digital.AplicarNivelesyTemporización(ConectarTodosLosPines, CargarNiveles, CargarTemporización, ModoRelé, IniciarPinesAltos, IniciarPinesBajos, IniciarPinesAltaImpedancia, HojaDeNivelesDePines, CategoríaDC, SelectorDC, HojaDeConjuntoDeTiempos, CategoríaAC, SelectorAC, HojaDeConjuntoDeBordes)
```

#### Parámetros

- **ConectarTodosLosPines**: Booleano opcional, con un valor predeterminado de `False`.
  - `True`: Conectar todos los pines del dispositivo.
  - `False`: No conectar.
- **CargarNiveles**: Booleano opcional, con un valor predeterminado de `False`.
  - `True`: Cargar los valores de nivel.
  - `False`: No cargar.
- **CargarTemporización**: Booleano opcional, con un valor predeterminado de `False`.
  - `True`: Cargar los valores de temporización.
  - `False`: No cargar.
- **ModoRelé**: `ModoRelé` opcional, con un valor predeterminado de `tlDesconectado`. Controla el cambio de relés.
  - `tlConectado`: Cambio activo. No apagar el dispositivo bajo prueba antes de establecer niveles y conexiones.
  - `tlDesconectado`: Evitar el cambio activo. Apagar el dispositivo bajo prueba antes de establecer niveles y conexiones.
- **IniciarPinesAltos**: Cadena opcional. Establece los pines en un estado de alta impedancia.
- **IniciarPinesBajos**: Cadena opcional. Establece los pines en un estado de baja impedancia.
- **IniciarPinesAltaImpedancia**: Cadena opcional. Establece los pines en un estado de alta impedancia.
- **HojaDeNivelesDePines**: Cadena opcional. Una hoja de niveles de pines.
- **CategoríaDC**: Cadena opcional.
- **SelectorDC**: Cadena opcional.
- **HojaDeConjuntoDeTiempos**: Cadena opcional.
- **CategoríaAC**: Cadena opcional.
- **SelectorAC**: Cadena opcional.
- **HojaDeConjuntoDeBordes**: Cadena opcional.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.