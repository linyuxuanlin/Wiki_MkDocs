# Configuración de Proxy en Git

## Fuente del Problema

La velocidad de `git clone` y `git pull` es demasiado lenta en China.

## Solución

### 1. Configuración dentro del software de proxy

1. Marque la opción `Permitir conexiones desde la red local` en el software de proxy.
2. Tome nota del número de puerto (por ejemplo, 1080).
3. Active el modo `Global`.

### 2. Configuración global de proxy en Git

```shell
git config --global http.proxy http://127.0.0.1:【número_de_puerto】
git config --global https.proxy https://127.0.0.1:【número_de_puerto】

# Ejemplo:
git config --global http.proxy http://127.0.0.1:10808
git config --global https.proxy https://127.0.0.1:10808

# Si lo anterior no funciona, intente usar el puerto socks5:
git config --global http.proxy socks5://127.0.0.1:【número_de_puerto】
git config --global https.proxy socks5://127.0.0.1:【número_de_puerto】

# Si desea aplicar el proxy solo a GitHub, sin afectar los repositorios nacionales (no se recomienda para usuarios no familiarizados con archivos de configuración):
git config --global http.https://github.com.proxy https://127.0.0.1:【número_de_puerto】
git config --global https.https://github.com.proxy https://127.0.0.1:【número_de_puerto】

# Para aplicar el proxy solo a GitLab, sin afectar los repositorios nacionales (no se recomienda para usuarios no familiarizados con archivos de configuración):
git config --global https.https://https://gitlab.com.proxy https://127.0.0.1:1080
```

Configuración en Ubuntu:

```shell
git config --global http.https://github.com.proxy socks5://127.0.0.1:10808
```

### Ver la ruta del archivo de configuración

```
git config --list --show-origin
```

### Restablecer

Si no desea utilizar un proxy, puede restaurar la configuración utilizando el siguiente método:

```shell
git config --global --unset http.proxy
git config --global --unset https.proxy
```

## Referencias y Agradecimientos

- [**Superar la lentitud en git clone y git pull**](https://c.lanmit.com/czxt/Linux/16965.html)

> Dirección original del artículo: <https://wiki-power.com/>
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.