# Cómo actualizar múltiples repositorios de Git de forma masiva

Cuando tienes muchos repositorios, puede volverse tedioso actualizarlos manualmente uno por uno. Con el método descrito en este artículo, podrás actualizar varios repositorios de Git de forma masiva.

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
root_dir="【to_be_replace[包含多个仓库的路径]】"
getdir $root_dir
```

2. Reemplaza `【to_be_replace[包含多个仓库的路径]】` con tu ruta, por ejemplo `C:\repos`.
3. Ejecuta el siguiente comando:

```shell
sh pull-master.sh
o
./pull-master.sh
```

o haz doble clic en `pull-master.sh` para ejecutarlo.

## Ejecución programada

1. Busca y abre el "Programador de tareas".
2. Haz clic en "Crear tarea".
   1. En la pestaña "General", ingresa un nombre para la tarea.
   2. En la pestaña "Desencadenadores", configura el período de ejecución.
   3. En la pestaña "Acciones", crea una nueva acción, ingresa el "Programa o script" (por ejemplo, `F:\pull-master.sh`), agrega argumentos (por ejemplo, `pull-master.sh`) y establece la "Comenzar en" (por ejemplo, `F:\`).
3. Prueba la ejecución, si no hay problemas, estará listo. (Si no funciona, puedes consultar [**Pull-Git-Repo.xml**](https://github.com/linyuxuanlin/File-host/blob/main/software-development/Pull-Git-Repo.xml))

## Implementación en un NAS de Synology

1. Coloca el script (por ejemplo, `github-pull.sh`) en cualquier ubicación de tu NAS.
2. Modifica la ruta de `root_dir` en `github-pull.sh` a la ubicación donde tienes tus repositorios de Git, por ejemplo `"/volume1/projects"`.
3. Ve a "Panel de control" - "Programador de tareas" - "Crear" - "Tarea programada" - "Script definido por el usuario". Configura el período de ejecución en las pestañas "Programación" y "Configuración de la tarea" y establece el comando para ejecutar el script (por ejemplo, `bash /volume1/stash/permanent/github-pull.sh`).
4. Puedes configurar la salida en "Configuración" y luego seleccionar la tarea y hacer clic en "Ejecutar" para probar la ejecución y ver los resultados en la ruta de salida configurada.

Si tienes que ingresar la contraseña cada vez, puedes ejecutar el siguiente comando (debes habilitar el directorio de inicio del usuario de antemano):

```shell
git config –global credential.helper store
```

Esto generará un archivo de texto local que almacenará tu nombre de usuario y contraseña. Cuando se te solicite ingresar la contraseña nuevamente, solo tendrás que hacerlo una vez y no tendrás que volver a ingresarla en el futuro.

## Referencias y agradecimientos

- [批量 git pull 小脚本](https://www.jianshu.com/p/42e8da5eb0af)
- [git 批量 pull_shell 脚本 -- 多个代码库批量 pull 最新 master 代码](https://blog.csdn.net/weixin_39618730/article/details/113024998)
- [Windows 定时执行 shell 脚本](https://blog.csdn.net/qq_40463753/article/details/84976977)

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.