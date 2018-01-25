# GPlates_video
Simple script that makes video from a set of GPlates images.
This is my first GitHub project. I would appreciate if someone help me with improving it.

Script has to work with Python 2 and 3, but tested with Python 3.
OpenCV is necessary

How to work:
if you have only GPlates 2.0 and just want to make a video from GPlates reconstruction images:
    2. open command line and type:
                pip install numpy
                pip install opencv-python
    3.download all files from this repository and unpack it
    4.run GPlates press F12, choose Run-script and choose file GPlates_video.py
    5. type in line after >>> : reconstruction_to_video()
    Now you have to get video by example  images in folder with GPlates_video.py
    

Content:
images	- set of reconstruction images for example.py

GPlates_video.py	main script, has only one function reconstruction_to_video for now

example.py -  make video from 'images' folder files.


main function in GPlates_video.py -  reconstruction_to_video()

The input is a set of images, exported as screenshots or colour rasters from GPlates. The name of an each image has to contain reconstruction time of a frame (- %d in GPlates export settings)

The output is a video in avi format. 
