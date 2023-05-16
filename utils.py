import cv2
import numpy as np


def get_limits(color):

    # we will insert the color in BGR format
    # "c" is a single pixel, its data type is 8 bit unsigned integer
    c = np.uint8([[color]])  


    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)

    # Adjust the range of the hue channel
    hue_range = 15
    lower_hue = hsvC[0][0][0] - hue_range
    upper_hue = hsvC[0][0][0] + hue_range

    # Adjust the thresholds of the saturation and value channels
    saturation_thresh = 100
    value_thresh = 100
    lowerLimit = np.array([lower_hue, saturation_thresh, value_thresh], dtype=np.uint8)
    upperLimit = np.array([upper_hue, 255, 255], dtype=np.uint8)

    return lowerLimit, upperLimit

