# TinyTimelapseCam - Mini cámara de lapso de tiempo basada en ESP32-S3

Esta es una mini cámara de lapso de tiempo basada en ESP32-S3 que puedes utilizar para capturar el movimiento de las nubes durante el día, las estrellas en movimiento durante toda la noche, o para capturar la diversidad de personas en las calles de la ciudad.

## Implementación de una cámara de red

Por favor, consulta la sección [**Uso de la cámara**](https://wiki.dfrobot.com.cn/_SKU_DFR0975_FireBeetle_2_Board_ESP32_S3_Advanced_Tutorial#target_12) para obtener instrucciones detalladas sobre cómo implementarla. No se proporcionarán detalles aquí.

## Prueba de transmisión utilizando Python

```py title="StreamViewer.py"
# Importar la biblioteca OpenCV
import cv2

# Definir la dirección de la cámara
camera_url = "http://192.168.31.203:81/stream"

# Crear un objeto VideoCapture
cap = cv2.VideoCapture(camera_url)

# Verificar si la cámara se abrió con éxito
if not cap.isOpened():
    print("No se puede conectar a la cámara. Por favor, verifica la dirección de la cámara o la conexión de red.")
    exit()

while True:
    # Leer un fotograma
    ret, frame = cap.read()

    # Verificar si se leyó el fotograma con éxito
    if not ret:
        print("No se pudo obtener el fotograma.")
        break

    # Mostrar la vista previa de la cámara
    cv2.imshow('Vista previa de la cámara', frame)

    # Salir de la vista previa al presionar la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar los recursos
cap.release()
cv2.destroyAllWindows()
```

Es importante tener en cuenta que la dirección de transmisión se compone de la dirección IP original seguida de ":81/stream". También puedes hacer clic con el botón derecho del ratón en la imagen en tiempo real en la página web para copiar la dirección de transmisión.

## Cámara de lapso de tiempo

Si la prueba de transmisión anterior fue exitosa, puedes probar el siguiente programa de cámara de lapso de tiempo:

```py title="TimelapseCam.py"
import cv2
import numpy as np
import time
import os

nframes = 500  # Número de fotos a tomar
interval = 0.00001  # Intervalo de tiempo (segundos)

# Cambia esto por la dirección IP de tu ESP32
cap = cv2.VideoCapture('http://192.168.31.203:81/stream')

print("Cámara de lapso de tiempo iniciada")
for i in range(nframes):
    # Capturar un fotograma de imagen
    ret, img = cap.read()
    # Guardar la imagen
    if img is None:
        print("No se puede obtener la imagen.")
    else:
        cv2.imwrite('temp_destination/photos/img_' +
                    str(i + 1000).zfill(4) + '.png', img)
    # Esperar un tiempo
    time.sleep(interval)
    print("Número de foto:", i)
```

```markdown
# Definición de la ruta de la carpeta de fotos
photos_path = "temp_destination/photos/"
# Si la carpeta no existe, créala
os.makedirs(photos_path, exist_ok=True)
# Obtención de la lista de nombres de archivos de fotos
photos = os.listdir(photos_path)
# Ordenar las fotos por nombre
photos.sort()
# Creación del objeto de escritura de video
video = cv2.VideoWriter("temp_destination/video.avi",
                        cv2.VideoWriter_fourcc(*"MJPG"), 100, (1280, 720))

# Recorrer las fotos
for photo in photos:
    # Leer la foto como una imagen
    image = cv2.imread(photos_path + photo)
    # Ajustar el tamaño de la imagen para que se adapte al tamaño de los fotogramas del video
    image = cv2.resize(image, (1280, 720))
    # Escribir la imagen en el video
    video.write(image)

# Liberar el objeto de escritura de video
video.release()
print("Creación de video de lapso de tiempo completada")
```

Después de ejecutar el programa, podrás encontrar el video generado en la carpeta `temp_destination`. También puedes ajustar los parámetros `nframes` e `interval` para que la cámara de lapso de tiempo se adapte a diferentes escenarios de captura.

## Solución de problemas y recomendaciones

- Si puedes ver el flujo en tiempo real en la versión web pero no puedes capturarlo localmente, esto se debe a que solo se puede abrir una transmisión en un momento dado. Intenta cerrar la página web.
- Si planeas capturar un video durante todo el día, puedes ejecutar el programa Python en un servidor de bajo consumo de energía o en un teléfono móvil antiguo. De esta manera, no tendrás que dejar la computadora encendida todo el tiempo.

## Referencias y Agradecimientos

- [Ejemplo de transmisión de ESP32-CAM con Python y OpenCV](https://www.hackster.io/onedeadmatch/esp32-cam-python-stream-opencv-example-1cc205)
- [Cámara de seguridad en vivo con UNIHIKER & FireBeetle 2 ESP32S3](https://www.hackster.io/pradeeplogu0/live-security-camera-with-unihiker-firebeetle-2-esp32s3-5d478e)

> Dirección original del artículo: <https://wiki-power.com/>
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.
```

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.