# this converts the flow tracking images into a video
import cv2
import numpy as np
import sys
import os
from collections import Counter 
from PIL import Image
from matplotlib import pyplot as plt

video_name = 'output-tracking.avi'
images = [
"260",
"270",
"280",
"290",
"300",
"310",
"320",
"330",
]

name1 = '../output-tracking/' + str(images[0]) + '.jpg'
print(name1)
frame = cv2.imread(name1)
height, width, layers = frame.shape
video = cv2.VideoWriter(video_name, 0, 10, (width,height))

for i in range(0,len(images)):
    finalname = '../output-tracking/' + str(images[i]) + '.jpg'
    video.write(cv2.imread(finalname))

cv2.destroyAllWindows()
video.release()