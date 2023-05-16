import cv2
from PIL import Image
from utils import get_limits



color = [0, 255, 0]  # coloe in BGR color space
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_limit, upper_limit = get_limits(color=color)
    mask = cv2.inRange(hsvImage, lower_limit, upper_limit)

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        bbox = cv2.boundingRect(contour)
        if bbox[2] > 0 and bbox[3] > 0:
            x, y, w, h = bbox
            frame = cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    if ret:
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()

cv2.destroyAllWindows()