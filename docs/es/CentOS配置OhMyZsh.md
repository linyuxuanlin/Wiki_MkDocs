# Configuración de Oh My Zsh en CentOS

## Verificar la Shell actual

```shell
echo $SHELL
```

En la mayoría de los casos, esto devolverá `bin/bash`.

## Instalar zsh

```shell
yum install -y zsh
```

## Cambiar la Shell predeterminada a zsh

Debe ejecutar este comando como usuario root:

```shell
chsh -s /bin/zsh
```

## Instalar git

```shell
yum install -y git
```

## Instalar Oh My Zsh

### Automáticamente

```shell
sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
o
sh -c "$(wget https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O -)"
```

### Manualmente

Si no es posible instalarlo de la manera anterior (posiblemente debido a restricciones de red), puede hacerlo manualmente de la siguiente manera:

Descargar el código fuente:

```shell
git clone https://github.com/robbyrussell/oh-my-zsh.git ~/.oh-my-zsh
```

Copiar la configuración:

```shell
cp ~/.oh-my-zsh/templates/zshrc.zsh-template ~/.zshrc
```

## Cambiar el tema de Oh My Zsh

Listar todos los temas disponibles:

```shell
ls ~/.oh-my-zsh/themes
```

Modificar el tema:

```shell
vim ~/.zshrc
```

Cambie el tema predeterminado, que es `ZSH_THEME="robbyrussell"`, a uno de su elección.

## Reiniciar para que los cambios surtan efecto

```shell
reboot
```

## Referencias y Agradecimientos

- [CentOS 7: Instalación de zsh y configuración de Oh My Zsh](https://www.jianshu.com/p/4ce7d511bc13)
- [CentOS: Instalación de Oh My Zsh](https://www.jianshu.com/p/556ff130fc65)

> Dirección original del artículo: <https://wiki-power.com/>
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.