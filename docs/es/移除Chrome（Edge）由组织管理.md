# Eliminar la administración de Chrome (Edge) por parte de la organización

## Pasos

1. Presiona `Win` + `R`, ingresa `regedit` para abrir el Editor del Registro.
2. Encuentra y elimina las siguientes carpetas:

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

- [¡Funciona! Solucionar "Chrome (o Edge) está administrado por tu organización" (en 3 pasos)](https://www.joshualowcock.com/guide/fix-chrome-is-managed-by-your-organization-in-3-steps/)

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.