# Cómo actualizar múltiples repositorios de Git en masa

Cuando tienes muchos repositorios, actualizarlos manualmente uno por uno puede ser tedioso. Con el método descrito en este artículo, puedes actualizar múltiples repositorios de Git en masa.

## Pasos

1. Crea un archivo de script llamado `pull-master.sh` y pega el siguiente código:

```shell title="pull-master.sh"
#!/bin/bash

function showMsg()
 {
   echo -e "\033[32m$1\033[0m"
 }

function getdir(){
    for element in `ls $1`
    do
        dir_or_file=$1"/"$element
        if [ -d $dir_or_file ]
        then
            cd $1"/"$element
            showMsg 'git pull '$element
            git pull
        else
            echo $dir_or_file
        fi
    done
}
root_dir="【ruta que contiene múltiples repositorios】"
getdir $root_dir
```

2. Reemplaza `【ruta que contiene múltiples repositorios】` con tu propia ruta, por ejemplo `C:\repos`.
3. Ejecuta el comando:

```shell
sh pull-master.sh
o
./pull-master.sh
```

O simplemente haz doble clic en `pull-master.sh` para ejecutarlo.

## Ejecución programada

1. Busca y abre `Programador de tareas`.
2. Haz clic en `Crear tarea`.
   1. En la pestaña `General`, escribe un nombre para la tarea.
   2. En la pestaña `Desencadenadores`, establece la frecuencia de ejecución.
   3. En la pestaña `Acciones`, crea una nueva acción, escribe el `Programa o script` (por ejemplo, `F:\pull-master.sh`), agrega los argumentos (por ejemplo, `pull-master.sh`), y establece el `Comenzar en` (por ejemplo, `F:\`).
3. Prueba la ejecución. Si no hay problemas, la tarea se ejecutará automáticamente según la frecuencia establecida. (Si no funciona, consulta [**Pull-Git-Repo.xml**](https://github.com/linyuxuanlin/File-host/blob/main/software-development/Pull-Git-Repo.xml)).

## Implementación en un NAS de Synology

1. Coloca el script (por ejemplo, `github-pull.sh`) en cualquier ruta en el NAS.
2. Modifica la ruta `root_dir` en `github-pull.sh` a la ruta donde colocaste tus repositorios de Git (por ejemplo, `"/volume1/projects"`).
3. En `Panel de control` - `Programador de tareas` - `Nueva tarea` - `Tarea definida por el usuario`, configura la frecuencia de ejecución y el comando para ejecutar el script (por ejemplo, `bash /volume1/stash/permanent/github-pull.sh`).
4. En `Configuración`, configura la salida y luego selecciona la tarea y haz clic en `Ejecutar` para probar la ejecución. Puedes abrir la ruta de salida configurada para ver los resultados.

Si necesitas ingresar la contraseña cada vez, puedes ejecutar el siguiente comando (debes habilitar el directorio de inicio del usuario de antemano):

```shell
git config –global credential.helper store
```

Esto creará un archivo de texto local que almacena tu nombre de usuario y contraseña. La próxima vez que necesites ingresar la contraseña, solo necesitas hacerlo una vez y no tendrás que ingresarla de nuevo.

## Referencias y agradecimientos

- [批量 git pull 小脚本](https://www.jianshu.com/p/42e8da5eb0af)
- [git 批量 pull_shell 脚本 -- 多个代码库批量 pull 最新 master 代码](https://blog.csdn.net/weixin_39618730/article/details/113024998)
- [Windows 定时执行 shell 脚本](https://blog.csdn.net/qq_40463753/article/details/84976977)

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.