# Cómo eliminar la gestión de Chrome (Edge) por parte de la organización

## Pasos

1. Presiona `Win` + `R` y escribe `regedit` para abrir el Editor del Registro.
2. Encuentra las siguientes carpetas y elimínalas:

Chrome:

```
HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Google\Chrome
HKEY_CURRENT_USER\SOFTWARE\Policies\Google\Chrome
```

Edge:

```
HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Edge
HKEY_CURRENT_USER\SOFTWARE\Policies\Microsoft\Edge
```

## Referencias y agradecimientos

- [¡Funciona! Solución de tres pasos para eliminar la gestión de Chrome (o Edge) por parte de la organización](https://www.joshualowcock.com/guide/fix-chrome-is-managed-by-your-organization-in-3-steps/)

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.