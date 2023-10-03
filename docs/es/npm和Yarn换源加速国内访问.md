# npm y Yarn: acelerando el acceso en China a través del cambio de origen

## Contexto

Las fuentes predeterminadas de npm y Yarn se encuentran en el extranjero, lo que ralentiza el acceso en China.  
El siguiente comando muestra el origen del espejo actualmente en uso:

```shell
yarn config get registry
```

## Solución

Utilice el software cgr para cambiar rápidamente el origen del espejo de npm y Yarn.

### Instalar cgr

```shell
npm install -g cgr
```

### Enumerar los orígenes del espejo disponibles actualmente

```
cgr ls
```

### Seleccione un origen del espejo para cambiar (taobao)

```
cgr use taobao
```

### Prueba de velocidad de acceso

```
cgr test taobao
```

## Referencias y agradecimientos

- [yarn 国内加速，修改镜像源](https://learnku.com/articles/15976/yarn-accelerate-and-modify-mirror-source-in-china)
- [cgr -- change registry | yarn & npm registry manager](https://www.npmjs.com/package/cgr)

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.