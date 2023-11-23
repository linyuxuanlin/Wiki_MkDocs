# Ignorar archivos específicos con gitignore

A veces, hay archivos que no queremos incluir en la gestión de versiones de Git, ni queremos que aparezcan constantemente en la lista de archivos no rastreados, como `node_modules`, algunas dependencias de desarrollo, registros de compilación, entre otros.

En estos casos, podemos crear un archivo llamado `.gitignore` donde enumeramos los archivos que deseamos ignorar.

## Normas

- Las líneas en blanco o aquellas que comienzan con el símbolo de comentario `#` son ignoradas por Git.
- Se utilizan patrones globales estándar para hacer coincidir archivos y directorios.
- Cuando un patrón de coincidencia termina con una barra diagonal inversa `/`, se refiere a un directorio.
- Para excluir archivos y directorios específicos de un patrón de coincidencia, puedes agregar un signo de exclamación `!` antes del patrón.

## Ejemplos

```gitignore
# Este es un comentario, Git lo ignorará

# Ignorar todos los archivos con formato .a
*.a

# No ignorar lib.a
!lib.a

# Ignorar el archivo TODO en la raíz del proyecto
/TODO

# Ignorar la carpeta build
build/

# Ignorar todos los archivos .txt en el directorio doc (sin incluir subdirectorios)
doc/*.txt

# Ignorar todos los archivos .txt en el directorio doc (incluyendo todos los subdirectorios)
doc/**/*.txt
```

## Referencias y Agradecimientos

- [zxhfighter/git-ignore.md](https://gist.github.com/zxhfighter/6320b9a08698bb8703ee)
- [github/gitignore](https://github.com/github/gitignore)

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.