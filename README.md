# GPlates_video
Simple script that makes video from a set of GPlates images.
You can find example of resulted video at https://youtu.be/0bu8CVB1KV4


This is my first GitHub project. I would appreciate if someone help me with improving it.

Script has to work with Python 2 and 3
OpenCV is necessary

How to work:

if you have only GPlates 2.0 and want to make a video from GPlates reconstruction images:
1. Setup Python 2.7.14. Simple way is install Miniconda from here - https://conda.io/miniconda.html
2. Run Anaconda Prompt from Start panel (Windows) and type
            conda install opencv-python
            conda install jupyter
3. download all files from this repository and unpack it to the home folder of miniconda  
(C:\Users\'your username'\ in windows, but you able to know home folder by take the next step and see what folder will be displayed)

4. run Jupyter-Notebook (Miniconda2) from start panel, open file example.ipynb and push Run button.
    
    That's all! You get simple example video how it works. This function also have some arguments that help you to change settings of video

    

Content:
images	- set of reconstruction images for example.py

GPlates_video.py	main script, has only one function reconstruction_to_video for now

example.ipynb -  make example video from 'images' folder files.


main function in GPlates_video.py -  reconstruction_to_video()

The input is a set of images, exported as screenshots or colour rasters from GPlates. 
The name of an each image has to contain reconstruction time of a frame (- %d in GPlates export settings)

The output is a video in avi format. 
