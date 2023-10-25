# Solución al problema de pérdida de información de tiempo al exportar desde Google Fotos

Después de exportar desde Google Fotos utilizando Google Takeout, muchos archivos de fotos tienen su información de tiempo guardada en archivos `.json`. ¿Cómo podemos importar esta información y asociarla a las fotos correspondientes?

Para resolver este problema, vamos a crear un archivo Python llamado `update-data.py`:

```python
from win32file import CreateFile, SetFileTime, GetFileTime, CloseHandle
from win32file  import GENERIC_READ, GENERIC_WRITE, OPEN_EXISTING
from pywintypes import Time
import os,json,time

# Obtener todos los archivos con una extensión específica
def get_all_file(ext_name):
    file_list = []
    datanames = os.listdir()
    for dataname in datanames:
        if os.path.splitext(dataname)[1] == ext_name:  # Archivos con extensión .json en el directorio
            file_list.append(dataname)
    return file_list

# Leer el archivo json
def load_json(json_file_name):
    f = open(json_file_name,'r',encoding = 'UTF-8')
    text = f.read()
    dic = json.loads(text)
    return dic

def modifyFileTime(filePath, createTime, modifyTime, accessTime, offset):
    """
    Función para modificar las propiedades de tiempo de cualquier archivo. Formato de tiempo: YYYY-MM-DD HH:MM:SS, por ejemplo: 2019-02-02 00:01:02
    :param filePath: Ruta del archivo
    :param createTime: Tiempo de creación
    :param modifyTime: Tiempo de modificación
    :param accessTime: Tiempo de acceso
    :param offset: Desplazamiento de tiempo en segundos, formato tuple, en el mismo orden que los parámetros de tiempo
    """
    try:
        format = "%Y-%m-%d %H:%M:%S"  # Formato de tiempo
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
```

```python
def timeOffsetAndStruct(times, format, offset):
    return time.localtime(time.mktime(time.strptime(times, format)) + offset)

# Date conversion, converting Google's date to a numerical value
def time_format(data_string):
    print(data_string)
    year = data_string.split('年')[0]
    month = data_string.split('年')[1].split('月')[0]
    day = data_string.split('年')[1].split('月')[1].split('日')[0]
    add_flag = data_string.split('年')[1].split('月')[1].split('日')[1].find('下午')
    hour = data_string.split('年')[1].split('月')[1].split('日')[1].split('午')[1].split(':')[0]
    minute = data_string.split('年')[1].split('月')[1].split('日')[1].split('午')[1].split(':')[1]
    second = data_string.split('年')[1].split('月')[1].split('日')[1].split('午')[1].split(':')[2]
    if add_flag > 0:
        hour = str(int(hour)+12)
    return year + '-' + month + '-' +day +' ' + hour + ':'+ minute + ':' + second


if __name__ == '__main__':
    file_name_json = get_all_file('.json')                      # Get a list of all file names in the current directory

    for fnj in file_name_json:
        dic = load_json(fnj)                                        # Extract dictionary information
        st = dic['creationTime']['formatted']                       # Get the file date
        output_format = time_format(st)                             # Convert the date format

        file_name = fnj[0:-5]                                       # Get the corresponding photo name of the file
        print(file_name)
        offset = (0, 1, 2)
        # Modify the file date
        modifyFileTime(file_name, output_format, output_format, output_format,offset)
```

Este script se utiliza para modificar la fecha de creación de los archivos según el archivo JSON y luego importarla a las fotos con el mismo nombre.

Simplemente coloca este script en el directorio de cada álbum y ejecútalo. Después de la ejecución, la información de tiempo de las fotos se restaurará.

## Referencias y agradecimientos

- [Problema de pérdida de tiempo después de descargar las fotos de Google Photos](https://zhuanlan.zhihu.com/p/356718593)

> Dirección original del artículo: <https://wiki-power.com/>
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.