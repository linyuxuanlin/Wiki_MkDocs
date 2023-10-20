```markdown
# TheHdw (El Hardware) 🚧

**TheHdw** es un objeto para acceder a propiedades y métodos relacionados con el hardware del sistema de pruebas.

## DCVI

```vbscript
TheHdw.DCVI
```

### Pines

```vbscript
TheHdw.DCVI.Pines(ListaDePines)
```

---

## TheHdw.PPMU

🚧

## TheHdw.Digital

### AplicarNivelesTiempo

Para cargar los datos de nivel y tiempo.

#### Uso

```vbscript
TheHdw.Digital.AplicarNivelesTiempo(ConectarTodosLosPines, CargarNiveles, CargarTiempo, ModoRelé, IniciarPinesAltos, IniciarPinesBajos, IniciarPinesAltoZ, HojaDeNivelesDePines, CategoríaDC, SelectorDC, HojaDeConjuntoDeTiempo, CategoríaAC, SelectorAC, HojaDeConjuntoDeBordes)
```

#### Parámetros

- **ConectarTodosLosPines**: Booleano opcional, valor predeterminado `False`.
  - `True`: Conectar todos los pines del dispositivo.
  - `False`: No conectar.
- **CargarNiveles**: Booleano opcional, valor predeterminado `False`.
  - `True`: Cargar valores de nivel.
  - `False`: No cargar.
- **CargarTiempo**: Booleano opcional, valor predeterminado `False`.
  - `True`: Cargar valores de tiempo.
  - `False`: No cargar.
- **ModoRelé**: `tlRelayMode` opcional, valor predeterminado `tlUnpowered`. Controla la conmutación en caliente de los relés.
  - `tlPowered`: Conmutación en caliente. No apagar el DUT antes de establecer niveles y conectar.
  - `tlUnpowered`: Evitar la conmutación en caliente. Apagar el DUT antes de establecer niveles y conectar.
- **IniciarPinesAltos**: Cadena opcional. Establecer los pines con estado alto.
- **IniciarPinesBajos**: Cadena opcional. Establecer los pines con estado bajo.
- **IniciarPinesAltoZ**: Cadena opcional. Establecer los pines con estado de impedancia.
- **HojaDeNivelesDePines**: Cadena opcional. Una hoja de niveles de pines.
- **CategoríaDC**: Cadena opcional.
- **SelectorDC**: Cadena opcional.
- **HojaDeConjuntoDeTiempo**: Cadena opcional.
- **CategoríaAC**: Cadena opcional.
- **SelectorAC**: Cadena opcional.
- **HojaDeConjuntoDeBordes**: Cadena opcional.
```

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.