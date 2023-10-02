# TinyTimelapseCam - Mini Delay Camera Based on ESP32-S3

This is a mini delay camera based on ESP32-S3. You can use it to capture the drifting clouds during the day, the rotation of stars throughout the night, or the various crowds on city streets.

## Deploy Network Camera

Please refer to the [**Camera Usage**](https://wiki.dfrobot.com.cn/_SKU_DFR0975_FireBeetle_2_Board_ESP32_S3_Advanced_Tutorial#target_12) section for deployment, which will not be repeated here.

## Test Using Python to Call Streaming

```py title="StreamViewer.py"
# Call OpenCV library
import cv2

# Define camera address
camera_url = "http://192.168.31.203:81/stream"

# Create VideoCapture object
cap = cv2.VideoCapture(camera_url)

# Check if the camera is successfully opened
if not cap.isOpened():
    print("Unable to connect to the camera. Please check the camera address or network connection.")
    exit()

while True:
    # Read frame
    ret, frame = cap.read()

    # Check if the frame is successfully read
    if not ret:
        print("Unable to get frame.")
        break

    # Display preview
    cv2.imshow('Camera Preview', frame)

    # Press 'q' to exit preview
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
```

Note that the streaming address is the original IP address plus the suffix `:81/stream`. You can also right-click on the real-time display on the web page to copy the streaming address.

## Delay Camera

If the streaming test is successful, you can try the following delay camera program:

```py title="TimelapseCam.py"
import cv2
import numpy as np
import time
import os

nframes = 500  # Number of photos to take
interval = 0.00001  # Interval time (seconds)

# Need to change to the IP address of your ESP32
cap = cv2.VideoCapture('http://192.168.31.203:81/stream')

print("Delay camera started")
for i in range(nframes):
    # Capture image frame
    ret, img = cap.read()
    # Save image file
    if img is None:
        print("Unable to get image")
    else:
        cv2.imwrite('temp_destination/photos/img_' +
                    str(i + 1000).zfill(4) + '.png', img)
    # Wait for a period of time
    time.sleep(interval)
    print("Photo number:", i)

# Define the path of the photo folder
photos_path = "temp_destination/photos/"
# Create the folder if it does not exist
os.makedirs(photos_path, exist_ok=True)
# Get a list of photo file names
photos = os.listdir(photos_path)
# Sort the photos by name
photos.sort()
# Create a video writer object
video = cv2.VideoWriter("temp_destination/video.avi",
                        cv2.VideoWriter_fourcc(*"MJPG"), 100, (1280, 720))

# Traverse the photos
for photo in photos:
    # Read the photo as an image
    image = cv2.imread(photos_path + photo)
    # Resize the image to fit the video frame size
    image = cv2.resize(image, (1280, 720))
    # Write the image to the video
    video.write(image)

# Release the video writer object
video.release()
print("Time-lapse video generated successfully")

After running the program, you can find the generated video in the `temp_destination` folder. You can also modify the `nframes` and `interval` parameters to make the time-lapse camera suitable for different shooting scenarios.

## Troubleshooting and Suggestions

- If the live stream can be displayed on the web page but cannot be captured locally, it may be because only one stream can be opened at a time. Please try closing the web page.
- If you plan to shoot a video for a whole day, you can run the Python program on a low-power server or an old phone, so you don't have to keep your computer on all the time.

## References and Acknowledgements

- [ESP32-CAM Python stream OpenCV Example](https://www.hackster.io/onedeadmatch/esp32-cam-python-stream-opencv-example-1cc205)
- [Live Security Camera with UNIHIKER & FireBeetle 2 ESP32S3](https://www.hackster.io/pradeeplogu0/live-security-camera-with-unihiker-firebeetle-2-esp32s3-5d478e)

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.