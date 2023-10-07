# Solución al problema de pérdida de información de tiempo al exportar desde Google Fotos

Después de exportar desde Google Fotos con Google Takeout, mucha información de tiempo de las fotos se guarda en archivos `.json`. ¿Cómo podemos importar esta información para que coincida con las fotos correspondientes?

Cree un nuevo archivo de Python llamado `update-data.py`:

```python
from win32file import CreateFile, SetFileTime, GetFileTime, CloseHandle
from win32file  import GENERIC_READ, GENERIC_WRITE, OPEN_EXISTING
from pywintypes import Time
import os,json,time

# Obtener nombres de archivo con una extensión específica
def get_all_file(ext_name):
    file_list = []
    datanames = os.listdir()
    for dataname in datanames:
        if os.path.splitext(dataname)[1] == ext_name:  # archivos con extensión .json en el directorio
            file_list.append(dataname)
    return file_list

# Leer archivo json
def load_json(json_file_name):
    f = open(json_file_name,'r',encoding = 'UTF-8')
    text = f.read()
    dic = json.loads(text)
    return dic

def modifyFileTime(filePath, createTime, modifyTime, accessTime, offset):
    """
    Utilizado para modificar las propiedades de tiempo de cualquier archivo, formato de tiempo: YYYY-MM-DD HH:MM:SS, por ejemplo: 2019-02-02 00:01:02
    :param filePath: nombre del archivo
    :param createTime: tiempo de creación
    :param modifyTime: tiempo de modificación
    :param accessTime: tiempo de acceso
    :param offset: segundos de desplazamiento de tiempo, formato de tupla, en el orden correspondiente a los parámetros de tiempo
    """
    try:
        format = "%Y-%m-%d %H:%M:%S"  # formato de tiempo
        cTime_t = timeOffsetAndStruct(createTime, format, offset[0])
        mTime_t = timeOffsetAndStruct(modifyTime, format, offset[1])
        aTime_t = timeOffsetAndStruct(accessTime, format, offset[2])

        fh = CreateFile(filePath, GENERIC_READ | GENERIC_WRITE, 0, None, OPEN_EXISTING, 0, 0)
        createTimes, accessTimes, modifyTimes = GetFileTime(fh)

        createTimes = Time(time.mktime(cTime_t))
        accessTimes = Time(time.mktime(aTime_t))
        modifyTimes = Time(time.mktime(mTime_t))
        SetFileTime(fh, createTimes, accessTimes, modifyTimes)
        CloseHandle(fh)
        return 0
    except:
        return 1

El siguiente script tiene como objetivo modificar la fecha de creación de archivos según la información contenida en un archivo JSON y luego importar la foto correspondiente con el mismo nombre.

Simplemente coloque este script en el directorio de cada álbum y ejecútelo. Después de la ejecución, la información de tiempo de las fotos se actualizará.

## Referencias y agradecimientos

- [Problema de pérdida de tiempo después de descargar fotos de Google Photos](https://zhuanlan.zhihu.com/p/356718593)

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.