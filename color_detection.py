import cv2
from PIL import Image
import numpy as np

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    print("ret value: " + str(ret))

    if ret:

        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()

cv2.destroyAllWindows()
