# Consejos pequeños de Vue.js

## Eliminar el `#` de la URL

**Problema**: Al construir un proyecto con Vue.js, la URL contendrá un `#`, lo que afectará la apariencia.

**Solución**:

1. Busque globalmente la función `const router = new VueRouter({})` en el proyecto.
2. Agregue la declaración `mode: 'history'` dentro de la función.

## Referencias y agradecimientos

- [Cómo eliminar el `#` en un proyecto de Vue - Modo Historia](https://www.cnblogs.com/zhuzhenwei918/p/6892066.html)

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.