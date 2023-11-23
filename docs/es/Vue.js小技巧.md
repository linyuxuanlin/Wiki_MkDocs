# Consejos para Vue.js

## Eliminar el `#` de la URL

**Problema**: Al construir un proyecto con Vue.js, la URL puede contener un `#`, lo que afecta la apariencia.

**Solución**:

1. En el proyecto, busca globalmente la función `const router = new VueRouter({})`.
2. Dentro de la función, agrega la declaración: `mode: 'history'`

## Referencias y Agradecimientos

- [Cómo eliminar el `#` en un proyecto Vue --- Modo Historia](https://www.cnblogs.com/zhuzhenwei918/p/6892066.html)

> Dirección original del artículo: <https://wiki-power.com/>
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.