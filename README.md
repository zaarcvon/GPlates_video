# GPlates_video
Simple script that makes video from a set of GPlates images.
This is my first GitHub project. I would appreciate if someone help me with improving it.

Script has to work with Python 2 and 3, but tested with Python 3.
OpenCV is necessary

How to work:

if you have only GPlates 2.0 and want to make a video from GPlates reconstruction images:
1. Setup Python 2.7.14 you can do it with shell Miniconda from here - https://conda.io/miniconda.html
2. Run Anaconda Prompt from Start panel - Anaconda 2 (Windows) and type
            conda install opencv-python
            conda install jupyter
3. download all files from repository and unpack it to the home folder of miniconda  (C:\Users\'your username'\ in windows)
4. run Jupyter-Notebook (Miniconda2) from start panel, open file example.ipynb and push Run button.
    That's all! You get simple example how it works. This function also have some arguments that change resulted video.

    

Content:
images	- set of reconstruction images for example.py

GPlates_video.py	main script, has only one function reconstruction_to_video for now

example.py -  make video from 'images' folder files.


main function in GPlates_video.py -  reconstruction_to_video()

The input is a set of images, exported as screenshots or colour rasters from GPlates. The name of an each image has to contain reconstruction time of a frame (- %d in GPlates export settings)

The output is a video in avi format. 
