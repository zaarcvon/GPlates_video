# GPlates_video
simple script that make video from set of GPlates images.

my first GitHub project. I would be appreciate if someone said wise words how to improve it.

Script get set of image exported as images or colour rasters. Images have to have reconstruction time of frame(rounded to integer) - %d in the names
The output is video in avi format. 

args of functions:
    image_folder - string, default='images' 
            Folder that contains images
    video_name - string, default='GPlates_reconstruction.avi' 
            Name of output video file
    fps -  integer, default=15
            Frame per seconds
    descending  - boolean, default=True
            Order of images. True means from older to younger ages.
 

