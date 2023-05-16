
import cv2
from PIL import Image
import numpy as np
from utils import get_limits

color = [0, 255, 0]# green in BGR color space
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_limit, upper_limit = get_limits(color=color)
    mask = cv2.inRange(hsvImage, lower_limit, upper_limit)

    mask_ = Image.fromarray(mask)

    bbox = mask_.getbbox()
    print(bbox)
    # if bbox is None:


    if bbox is not None:
        x1, y1, x2, y2 = bbox

        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)

    if ret:
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()

cv2.destroyAllWindows()
