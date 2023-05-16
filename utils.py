import cv2
import numpy as np


def get_limits(color):

    # we will insert the color in BGR format
    # "c" is a single pixel, its data type is 8 bit unsigned integer
    c = np.uint8([[color]])  


    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)
     
    lowerLimit = hsvC[0][0][0] - 10, 100, 100
    upperLimit = hsvC[0][0][0] + 10, 255, 255

    lowerLimit = np.array(lowerLimit, dtype=np.uint8)
    upperLimit = np.array(upperLimit, dtype=np.uint8)

    return lowerLimit, upperLimit