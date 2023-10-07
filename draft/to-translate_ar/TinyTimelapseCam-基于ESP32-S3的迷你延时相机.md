# TinyTimelapseCam - Mini cámara de lapso de tiempo basada en ESP32-S3

Esta es una mini cámara de lapso de tiempo basada en ESP32-S3, que se puede utilizar para capturar el movimiento de las nubes durante el día, el movimiento de las estrellas durante toda la noche, o para capturar la diversidad de personas en las calles de la ciudad.

## Despliegue de la cámara de red

Por favor, consulte la sección [**Uso de la cámara**](https://wiki.dfrobot.com.cn/_SKU_DFR0975_FireBeetle_2_Board_ESP32_S3_Advanced_Tutorial#target_12) para desplegar la cámara, no se repetirá aquí.

## Prueba de transmisión de flujo con Python

```py title="StreamViewer.py"
# Llamando a la biblioteca OpenCV
import cv2

# Definir la dirección de la cámara
camera_url = "http://192.168.31.203:81/stream"

# Crear un objeto VideoCapture
cap = cv2.VideoCapture(camera_url)

# Comprobar si la cámara se ha abierto correctamente
if not cap.isOpened():
    print("No se puede conectar a la cámara. Por favor, compruebe la dirección de la cámara o la conexión de red.")
    exit()

while True:
    # Leer el marco
    ret, frame = cap.read()

    # Comprobar si el marco se ha leído correctamente
    if not ret:
        print("No se puede obtener el marco.")
        break

    # Mostrar la vista previa de la cámara
    cv2.imshow('Vista previa de la cámara', frame)

    # Presione la tecla 'q' para salir de la vista previa
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar los recursos
cap.release()
cv2.destroyAllWindows()
```

Es importante tener en cuenta que la dirección de transmisión se basa en la dirección IP original, seguida del sufijo `:81/stream`. También puede hacer clic con el botón derecho del ratón en la imagen en tiempo real que se muestra en la página web para copiar la dirección de transmisión.

## Cámara de lapso de tiempo

Si la prueba de transmisión anterior es exitosa, puede probar el siguiente programa de cámara de lapso de tiempo:

```py title="TimelapseCam.py"
import cv2
import numpy as np
import time
import os

nframes = 500  # Número de fotos a tomar
interval = 0.00001  # Intervalo de tiempo (segundos)

# Cambiar por la dirección IP de su ESP32
cap = cv2.VideoCapture('http://192.168.31.203:81/stream')

print("Cámara de lapso de tiempo iniciada")
for i in range(nframes):
    # Capturar el marco de la imagen
    ret, img = cap.read()
    # Guardar la imagen en un archivo
    if img is None:
        print("No se puede obtener la imagen")
    else:
        cv2.imwrite('temp_destination/photos/img_' +
                    str(i + 1000).zfill(4) + '.png', img)
    # Esperar un tiempo
    time.sleep(interval)
    print("Número de foto:", i)

# Definir la ruta de la carpeta de fotos
photos_path = "temp_destination/photos/"
# Si la carpeta no existe, crearla
os.makedirs(photos_path, exist_ok=True)
# Obtener la lista de nombres de archivo de fotos
photos = os.listdir(photos_path)
# Ordenar las fotos por nombre
photos.sort()
# Crear objeto de escritura de video
video = cv2.VideoWriter("temp_destination/video.avi",
                        cv2.VideoWriter_fourcc(*"MJPG"), 100, (1280, 720))

# Recorrer las fotos
for photo in photos:
    # Leer la foto como imagen
    image = cv2.imread(photos_path + photo)
    # Ajustar el tamaño de la imagen para que se ajuste al tamaño del marco del video
    image = cv2.resize(image, (1280, 720))
    # Escribir la imagen en el video
    video.write(image)

# Liberar el objeto de escritura de video
video.release()
print("Video de lapso de tiempo generado")

Después de ejecutar el programa, puede encontrar el video generado en la carpeta "temp_destination". También puede modificar los parámetros "nframes" e "interval" para que la cámara de lapso de tiempo sea adecuada para diferentes escenarios de filmación.

## Solución de problemas y sugerencias

- Si la vista previa en la página web puede mostrar la imagen en tiempo real, pero no se puede capturar la transmisión en local, esto se debe a que solo se puede abrir una transmisión al mismo tiempo. Intente cerrar la página web.
- Si planea grabar un video durante todo el día, puede ejecutar el programa de Python en un servidor de bajo consumo de energía o en un teléfono móvil antiguo para que no tenga que mantener la computadora encendida todo el tiempo.

## Referencias y agradecimientos

- [ESP32-CAM Python stream OpenCV Example](https://www.hackster.io/onedeadmatch/esp32-cam-python-stream-opencv-example-1cc205)
- [Live Security Camera with UNIHIKER & FireBeetle 2 ESP32S3](https://www.hackster.io/pradeeplogu0/live-security-camera-with-unihiker-firebeetle-2-esp32s3-5d478e)

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.