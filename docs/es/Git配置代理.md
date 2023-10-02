# Configuración de proxy en Git

## Origen del problema

La velocidad de `git clone` y `git pull` es demasiado lenta en China.

## Solución

### 1. Configuración en el software de proxy

1. Marque la opción "Permitir conexiones de la red local" en el software de proxy.
2. Tome nota del número de puerto (por ejemplo: 1080).
3. Active el "modo global".

### 2. Configuración global de proxy http en Git

```shell
git config --global http.proxy http://127.0.0.1:【número de puerto】
git config --global https.proxy https://127.0.0.1:【número de puerto】

# Por ejemplo:
git config --global http.proxy http://127.0.0.1:10808
git config --global https.proxy https://127.0.0.1:10808

# Si lo anterior no funciona, intente usar el puerto socks5:
git config --global http.proxy socks5://127.0.0.1:【número de puerto】
git config --global https.proxy socks5://127.0.0.1:【número de puerto】

# Si solo desea usar el proxy para GitHub y no afectar los repositorios locales (no recomendado si no está familiarizado con los archivos de configuración):
git config --global http.https://github.com.proxy https://127.0.0.1:【número de puerto】
git config --global https.https://github.com.proxy https://127.0.0.1:【número de puerto】

# Si solo desea usar el proxy para GitLab y no afectar los repositorios locales (no recomendado si no está familiarizado con los archivos de configuración):
git config --global https.https://https://gitlab.com.proxy https://127.0.0.1:1080
```

Configuración en Ubuntu:

```shell
git config --global http.https://github.com.proxy socks5://127.0.0.1:10808
```

### Ver la ruta del archivo de configuración

```
git config –list –show-origin
```

### Desactivar el proxy

Si no desea utilizar un proxy, puede desactivarlo con los siguientes comandos:

```shell
git config --global --unset http.proxy
git config --global --unset https.proxy
```

## Referencias y agradecimientos

- [**Conquista la lentitud de git clone y git pull**](https://c.lanmit.com/czxt/Linux/16965.html)

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.