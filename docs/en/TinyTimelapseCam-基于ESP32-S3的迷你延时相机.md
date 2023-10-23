# TinyTimelapseCam - Mini Delay Camera Based on ESP32-S3

This is a mini delay camera based on ESP32-S3 that allows you to capture the drifting clouds during the day, the celestial movements throughout the night, and the diverse array of people on city streets.

## Deploying the Network Camera

Please refer to the [**Camera Usage**](https://wiki.dfrobot.com.cn/_SKU_DFR0975_FireBeetle_2_Board_ESP32_S3_Advanced_Tutorial#target_12) section for deployment details. We won't delve into it here.

## Testing with Python to Access the Stream

```python title="StreamViewer.py"
# Import the OpenCV library
import cv2

# Define the camera URL
camera_url = "http://192.168.31.203:81/stream"

# Create a VideoCapture object
cap = cv2.VideoCapture(camera_url)

# Check if the camera is successfully opened
if not cap.isOpened():
    print("Unable to connect to the camera. Please check the camera URL or network connection.")
    exit()

while True:
    # Read a frame
    ret, frame = cap.read()

    # Check if the frame is successfully read
    if not ret:
        print("Unable to get a frame.")
        break

    # Display the preview
    cv2.imshow('Camera Preview', frame)

    # Press 'q' to exit the preview
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
```

Please note that the streaming address is the original IP followed by `:81/stream` as a suffix. You can also right-click on the real-time video display on the web page to copy the streaming address.

## Delay Camera

If the streaming test was successful, you can now try the following program for the delay camera:

```python title="TimelapseCam.py"
import cv2
import numpy as np
import time
import os

nframes = 500  # Number of photos to take
interval = 0.00001  # Time interval (seconds)

# Change to the IP address of your ESP32
cap = cv2.VideoCapture('http://192.168.31.203:81/stream')

print("Delay camera is starting")
for i in range(nframes):
    # Capture an image frame
    ret, img = cap.read()
    # Save the image file
    if img is None:
        print("Unable to capture an image")
    else:
        cv2.imwrite('temp_destination/photos/img_' +
                    str(i + 1000).zfill(4) + '.png', img)
    # Wait for a period of time
    time.sleep(interval)
    print("Photo number:", i)
```

```markdown
# Define the path for the photo folder
photos_path = "temp_destination/photos/"
# Create the folder if it doesn't exist
os.makedirs(photos_path, exist_ok=True)
# Retrieve the list of photo file names
photos = os.listdir(photos_path)
# Sort photos by name
photos.sort()
# Create a video writing object
video = cv2.VideoWriter("temp_destination/video.avi",
                        cv2.VideoWriter_fourcc(*"MJPG"), 100, (1280, 720))

# Iterate through the photos
for photo in photos:
    # Read the photo as an image
    image = cv2.imread(photos_path + photo)
    # Resize the image to fit the video frame size
    image = cv2.resize(image, (1280, 720))
    # Write the image to the video
    video.write(image)

# Release the video writing object
video.release()
print("Time-lapse video generation completed")
```

After running the program, you can find the generated video in the `temp_destination` folder. You can also modify the `nframes` and `interval` parameters to make the time-lapse camera suitable for different shooting scenarios.

## Troubleshooting and Suggestions

- If the live feed can be displayed on the web but cannot be captured locally, it's because only one stream can be opened at a time. Try closing the web page.
- If you intend to capture a video for an entire day, consider running the Python program on a low-power server or an old smartphone to avoid keeping your computer on all the time.

## References and Acknowledgments

- [ESP32-CAM Python stream OpenCV Example](https://www.hackster.io/onedeadmatch/esp32-cam-python-stream-opencv-example-1cc205)
- [Live Security Camera with UNIHIKER & FireBeetle 2 ESP32S3](https://www.hackster.io/pradeeplogu0/live-security-camera-with-unihiker-firebeetle-2-esp32s3-5d478e)

> Original: <https://wiki-power.com/>
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.
```

Please note that I've translated the content while maintaining the original markdown format. If you have any further questions or need additional assistance, please feel free to ask.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.