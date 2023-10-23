# Instalación y Desinstalación de Node.js y npm en MacOS

## Instalación

Puedes descargar Node.js desde [http://nodejs.cn/download/](http://nodejs.cn/download/).

## Desinstalación

Si has instalado Node.js con `homebrew`, puedes desinstalarlo con el siguiente comando:

```shell
brew uninstall node
```

Si has instalado Node.js usando el paquete `.pkg`, puedes desinstalarlo ejecutando:

```shell
sudo rm -rf /usr/local/{bin/{node,npm},lib/node_modules/npm,lib/node,share/man/*/node.*}
```

## Solución de Problemas

**Pregunta:** Después de cambiar el nombre de usuario en MacOS, ¿recibes un error de permisos insuficientes que dice `EACCES: permission denied`?

**Respuesta:** Para solucionar este problema, ejecuta la instalación de la siguiente manera:

```shell
sudo npm install -g appium --unsafe-perm=true --allow-root
```

Esto ejecutará la instalación en un modo no seguro que permitirá superar los problemas de permisos.

> Dirección original del artículo: <https://wiki-power.com/>
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.