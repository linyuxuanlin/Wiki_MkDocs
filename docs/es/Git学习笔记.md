# Notas de aprendizaje de Git

## Instalación y configuración

Descargar el paquete de instalación: [**git-scm.com/downloads**](https://git-scm.com/downloads)

Configuración:

```shell
git config --global user.name "nombre de usuario"
git config --global user.email "correo@example.com"
```

## Sentencias básicas

![](https://img.wiki-power.com/d/wiki-media/img/20200216204934.png)

### Proceso básico

1. Cambiar al directorio especificado: `cd git-learning`
2. Inicializar el repositorio de Git: `git init`
3. Transferir archivos existentes / nuevos del **área de trabajo** al **área de preparación**:
   - `git add .`: agregar todos los archivos del área de trabajo
   - `git add xxx.xx`: agregar un archivo individual
4. Enviar actualizaciones al **branch de área de preparación**: `git commit -m "descripción"`
5. Cambiar a una versión específica: `git reset --hard commit_id`

### Sentencias comunes

- Ver cambios (solo se puede usar cuando el archivo está en el área de trabajo): `git diff`
- Ver el estado del repositorio: `git status`
- Ver el historial de envío (en orden de envío): `git log`, presione `q` para salir
- Ver el historial de comandos (todos los registros de envío): `git reflog`

## Repositorio remoto

### Convertir un proyecto local en remoto

Adecuado para casos en los que ya se tienen archivos de proyecto locales.

1. Crear una clave SSH: `ssh-keygen -t rsa -C "tu_correo@example.com"`
   - Reemplazar con tu correo electrónico, presionar Enter en todo momento
2. Abrir [**Configuración personal - Claves SSH y GPG**](https://github.com/settings/keys) en GitHub y agregar una nueva clave SSH
   - El título es arbitrario, la clave es el contenido del archivo `id_rsa.pub`
3. Crear un nuevo repositorio en GitHub, no seleccione `Initialize this repository with a README`
   - Si accidentalmente se inicializa el repositorio, primero hay que hacer pull: `git pull origin master`
4. Copiar la dirección SSH (por ejemplo: `git@github.com:linyuxuanlin/git-learning.git`) y ejecutar el comando en el repositorio local de Git: `git remote add origin git@server-name:user/repo-name.git`
5. Enviar el contenido local al repositorio remoto: `git push -u origin master`
   - Ingrese `yes` y presione Enter para continuar cuando aparezca el mensaje de confirmación
   - Como el repositorio remoto está vacío, al enviar la rama principal por primera vez, se agrega el parámetro `-u`, lo que hace que Git no solo envíe el contenido de la rama principal local al nuevo branch principal remoto, sino que también relacione la rama principal local y la rama principal remota. Esto simplifica los comandos de envío o extracción en el futuro.
6. Para cada envío futuro: `git push origin master`

### Convertir un proyecto remoto en local

Adecuado para comenzar desde cero o para desarrollar sobre el proyecto de otra persona.

1. Clonar el repositorio remoto: `git clone git@server-name:user/repo-name.git`

## Gestión de ramas

![](https://img.wiki-power.com/d/wiki-media/img/20200217195056.png)

Las ramas en Git son como universos paralelos en las películas de ciencia ficción. Mientras estás trabajando duro en aprender Git en tu computadora, en otro universo paralelo, estás trabajando duro en aprender SVN. Si estos universos paralelos no interfieren entre sí, no tendrán ningún impacto en ti. Pero en algún momento, estos universos paralelos se fusionan y resulta que has aprendido tanto Git como SVN.

¿Para qué sirven las ramas en la práctica? Supongamos que estás desarrollando una nueva función que tardará dos semanas en completarse. En la primera semana, has escrito el 50% del código. Si lo envías de inmediato, el repositorio incompleto impedirá que otros trabajen. Si esperas a que todo el código esté escrito antes de enviarlo, existe un gran riesgo de perder el progreso diario.

Ahora, con las ramas, no tienes que preocuparte. Creas una rama propia que nadie más puede ver y continúas trabajando en la rama original. Cuando quieras enviar el código, lo envías a tu propia rama. Cuando hayas terminado, lo fusionas con la rama original. De esta manera, es seguro y no afecta el trabajo de los demás.

1. Crear y cambiar a una nueva rama: `git switch -c nombre_rama`
   - `-c` significa crear y cambiar de rama
2. Ver la rama actual: `git branch`
3. Fusionar el contenido de la nueva rama con la rama principal: `git merge nombre_rama`
   - Cambia a la rama que deseas fusionar y luego usa el comando de fusión (por ejemplo, cambia a la rama principal y luego ejecuta el comando anterior).
   - Cuando Git no puede fusionar automáticamente las ramas, primero debes resolver los conflictos. Después de resolver los conflictos, envía el código y completa la fusión.
   - Resolver conflictos significa editar manualmente los archivos que Git no pudo fusionar y ajustarlos a lo que deseas. Luego, envía los cambios.
4. Eliminar una rama: `git branch -d nombre_rama`
5. Deshabilitar la fusión Fast forward de la rama: `git merge --no-ff -m "texto de confirmación" nombre_rama`
   - Como esta fusión creará un nuevo commit, agrega el parámetro `-m` para incluir la descripción del commit.
   - En el modo Fast forward, la información de la rama se pierde cuando se elimina.

## Guía de GitHub

Con la plataforma de GitHub, podemos descubrir proyectos de código abierto y construir un mundo de código abierto con desarrolladores de todo el mundo. Cuando encontramos un proyecto de código abierto excelente, podemos hacer un Fork en nuestra cuenta de GitHub (para tener permisos de lectura y escritura) y luego clonarlo en nuestro equipo para desarrollar. Después de completar el desarrollo, podemos enviar una solicitud de extracción en GitHub. Si el propietario del proyecto original cree que tus cambios son adecuados, se fusionarán con el proyecto de código abierto original.

### GitHub CLI

GitHub CLI es una herramienta de línea de comandos de GitHub que permite utilizar funciones como pull requests e issues en la línea de comandos. Descarga: [**cli.github.com**](https://cli.github.com/) GitHub CLI está actualmente en versión beta y vale la pena probarlo.

## Referencias y agradecimientos

- [Tutorial de Git - Liao Xuefeng](https://www.liaoxuefeng.com/wiki/896043488029600)
- [Cómo utilizar Git para la gestión de ramas en proyectos reales](https://blog.csdn.net/ShuSheng0007/article/details/80791849)
- [Un modelo de ramificación exitoso para Git](https://nvie.com/posts/a-successful-git-branching-model/)
- [git-cheatsheet.pdf](https://github.com/linyuxuanlin/File-host/blob/main/software-development/git-cheatsheet.pdf)
- [Pro Git](https://git-scm.com/book/zh/v2)
- [GitHub CLI - Manual](https://cli.github.com/manual/)
- [Más de 20 hermosas imágenes para adentrarse en el mundo de Git](https://mp.weixin.qq.com/s/oTtMQFEI9J5ymqt6SQ0PFg)

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
