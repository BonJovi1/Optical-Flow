# Optical-Flow
Implementing the Lucas Kanade algorithm to compute the optical flow between images. Using the flow to also detect, segment and track objects in videos. \
Assignment-5, Computer Vision, Spring 2020

The jupyter notebook takes a long time to load on Github. Check out the code on [**nbviewer**](https://nbviewer.jupyter.org/github/BonJovi1/Optical-Flow/blob/master/code.ipynb).

The Middlebury [optical flow dataset](http://vision.middlebury.edu/flow/data/) was used for this purpose. We implement the Lucas Kanade algorithm to obtain the flow between the images. We also use optical flow to obtain the segmentation masks of moving objects, which are present in `output-masks` and to track objects in a video.  

