# GPlates_video
Simple script that makes video from a set of GPlates images.
This is my first GitHub project. I would appreciate if someone help me with improving it.

Script has to work with Python 2 and 3, but tested with Python 3.
OpenCV is necessary

Content:
images	- set of reconstruction images for example.py

GPlates_video.py	main script, has only one function reconstruction_to_video for now

example.py -  make video from 'images' folder files.

README.md

For now script has only one function:
    reconstruction_to_video

The input is a set of images, exported as screenshots or colour rasters. The name of an each image has to contain reconstruction time of a frame (rounded to integer) - %d in GPlates export settings

The output is a video in avi format. 

**Signature:** 

```
reconstruction_to_video(images_folder='images', output_video='GPlates_reconstruction.avi',fps=15,descending=True)
```

**Parameters:**
    
`images_folder` - string, default='images', folder that contains images
`output_video` - string, default='GPlates_reconstruction.avi', name of output video file
`fps` - integer, default=15, frame per seconds
`descending`  - boolean, default=True,  order of images. True means from older to younger ages.

