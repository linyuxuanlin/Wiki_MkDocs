# Instalación y desinstalación de Node.js y npm (MacOS)

## Instalación

[http://nodejs.cn/download/](http://nodejs.cn/download/)

## Desinstalación

Si se instaló a través de `homebrew`:

```shell
brew uninstall node
```

Si se instaló a través de un paquete `.pkg`:

```shell
sudo rm -rf /usr/local/{bin/{node,npm},lib/node_modules/npm,lib/node,share/man/*/node.*}
```

## Solución de problemas

P: Después de cambiar el nombre de usuario en MacOS, aparece el mensaje de error "EACCES: permission denied". 
R: Ejecute `sudo npm install -g appium --unsafe-perm=true --allow-root` en modo no seguro. 

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.