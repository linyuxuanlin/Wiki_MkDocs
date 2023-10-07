# Ignorando archivos especiales con gitignore

Hay algunos archivos que no queremos incluir en la gestión de versiones de Git, y tampoco queremos que aparezcan constantemente en la lista de archivos sin seguimiento, como node_modules, algunas dependencias de desarrollo, registros de compilación, entre otros.

En estos casos, podemos crear un archivo `.gitignore` y listar los archivos que queremos ignorar.

## Reglas

- Las líneas vacías o las líneas que comienzan con el símbolo de comentario `#` serán ignoradas por Git.
- Se pueden utilizar patrones glob estándar.
- Si el patrón de coincidencia termina con una barra diagonal invertida (/), se ignorará el directorio.
- Para ignorar todos los archivos y directorios excepto los especificados en el patrón, se puede agregar el signo de exclamación (!) antes del patrón.

## Ejemplos

```gitignore
# Esta línea es un comentario y será ignorada por Git.

# Ignorar todos los archivos con formato .a
*.a

# No ignorar lib.a
!lib.a

# Ignorar el archivo TODO en la raíz del proyecto
/TODO

# Ignorar la carpeta build
build/

# Ignorar todos los archivos txt en el directorio doc (sin incluir subdirectorios)
doc/*.txt

# Ignorar todos los archivos txt en el directorio doc (incluyendo subdirectorios)
doc/**/*.txt
```

## Referencias y agradecimientos

- [zxhfighter/git-ignore.md](https://gist.github.com/zxhfighter/6320b9a08698bb8703ee)
- [github/gitignore](https://github.com/github/gitignore)

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.