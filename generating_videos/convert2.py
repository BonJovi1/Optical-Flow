# this converts the segmentation mask images into a video
import cv2
import numpy as np
import sys
import os
from collections import Counter 
from PIL import Image
from matplotlib import pyplot as plt

video_name = 'output-segmentation.avi'
images = [
"mask0",
"mask1",
"mask2",
"mask3",
"mask4",
"mask5",
"mask6"
]

name1 = '../output-masks/' + str(images[0]) + '.jpg'
print(name1)
frame = cv2.imread(name1)

height, width, layers = frame.shape
video = cv2.VideoWriter(video_name, 0, 4, (width,height))

for i in range(0,7):
    finalname = '../output-masks/' + str(images[i]) + '.jpg'
    video.write(cv2.imread(finalname))

cv2.destroyAllWindows()
video.release()