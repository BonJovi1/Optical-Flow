# this converts the original bedroom images into a video
import cv2
import numpy as np
import sys
import os
from collections import Counter 
from PIL import Image
from matplotlib import pyplot as plt

video_name = 'raw-images.avi'
images = [
"frame0",
"frame20",
"frame40",
"frame60",
"frame80",
"frame100",
"frame120"
]

name1 = '../frames/' + str(images[0]) + '.jpg'
print(name1)
frame = cv2.imread(name1)
height, width, layers = frame.shape
video = cv2.VideoWriter(video_name, 0, 4, (width,height))

for i in range(0,7):
    finalname = '../frames/' + str(images[i]) + '.jpg'
    video.write(cv2.imread(finalname))

cv2.destroyAllWindows()
video.release()