# Configuración de Oh My Zsh en CentOS

## Verificar la shell actual

```Shell
echo $SHELL
```

Por lo general, devolverá `bin/bash`

## Instalar zsh

```shell
yum install -y zsh
```

## Cambiar la shell predeterminada a zsh

Debe ejecutar este comando como usuario root:

```shell
chsh -s /bin/zsh
```

## Instalar git

```shell
yum install -y git
```

## Instalar Oh My Zsh

### Automático

```shell
sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
o
sh -c "$(wget https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O -)"
```

### Manual

Si no se puede instalar de la manera anterior (posiblemente debido a un bloqueo), se puede instalar manualmente de la siguiente manera:

Descargar el código fuente:

```shell
git clone https://github.com/robbyrussell/oh-my-zsh.git ~/.oh-my-zsh
```

Copiar la configuración:

```shell
cp ~/.oh-my-zsh/templates/zshrc.zsh-template ~/.zshrc
```

## Cambiar el tema de Oh My Zsh

Listar todos los temas:

```shell
ls ~/.oh-my-zsh/themes
```

Cambiar el tema:

```shell
vim ~/.zshrc
```

Cambiar el tema predeterminado `ZSH_THEME="robbyrussell"` por el que prefiera.

## Reiniciar para que surta efecto

```shell
reboot
```

## Referencias y agradecimientos

- [centos7 安装 zsh 配置 oh-my-zsh](https://www.jianshu.com/p/4ce7d511bc13)
- [CentOs 安装 oh my zsh](https://www.jianshu.com/p/556ff130fc65)

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.