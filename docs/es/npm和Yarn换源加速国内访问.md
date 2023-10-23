```markdown
# Cambiar la fuente de npm y Yarn para acelerar el acceso en China

## Antecedentes

Las direcciones de origen predeterminadas de npm y Yarn están en el extranjero, lo que ralentiza la velocidad de acceso en China.  
Para verificar la fuente de espejo actualmente en uso, ejecute el siguiente comando:

```shell
yarn config get registry
```

## Solución

Utilice el software cgr para cambiar rápidamente la fuente de espejo de npm y Yarn.

### Instalación de cgr

```shell
npm install -g cgr
```

### Listar las fuentes de espejo disponibles actualmente

```
cgr ls
```

### Seleccione una fuente de espejo para cambiar (por ejemplo, Taobao)

```
cgr use taobao
```

### Prueba de velocidad de acceso

```
cgr test taobao
```

## Referencias y Agradecimientos

- [Aceleración de Yarn en China: Cambio de fuente de espejo](https://learnku.com/articles/15976/yarn-accelerate-and-modify-mirror-source-in-china)
- [cgr: Cambio de registro | Gestor de registros de yarn y npm](https://www.npmjs.com/package/cgr)

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.
```

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.