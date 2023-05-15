import cv2
import numpy as np

def get_limits(color):
    c = np.unit8([[color]]) # here insert the bgr values which you want
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)

    lower_limit = hsvC[0][0][0] - 10, 100, 100
    upper_limit = hsvC[0][0][0] + 10, 255, 255

    lower_limit = np.array(lower_limit, dtype=np.uint8)
    upper_limit = np.array(upper_limit, dtype=np.unit8)

    return lower_limit, upper_limit


a = np.arange(20)
print(a)