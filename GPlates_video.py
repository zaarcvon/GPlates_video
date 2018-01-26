def reconstruction_to_video(images_folder='images',output_video='GPlates_reconstruction.avi',fps=15, descending=True,chart=True ,chart_width=150):
    """
    Make video from set of reconstruction images

    Parameters
    ----------
    images_folder : string, default  'images' 
        folder that contains images 
    output_video : string, default  'GPlates_reconstruction.avi' 
        name of output video file 
    fps - integer, default  15 
        Frame per seconds 
    descending - boolean, default True
        Order of images. True - from older to younger ages.
    chart - boolean, default True
        Make a chart with a running line on a left side of a frames
    chart_width - int, default 150
        Width of a chart

    Returns
    -------
    None
    
    Videofile in main folder
    """
    
    import os
    import cv2
    import re
    import numpy
    
    images = [img for img in os.listdir(images_folder)]
    
    # fonts settings
    font                   = cv2.FONT_HERSHEY_SIMPLEX
    bottomLeftCornerOfText = (10,30)
    fontScale             = 1
    fontColor              = (255,255,255)
    lineType               = 2

    # presettings of video
    frame = cv2.imread(os.path.join(images_folder, images[0]))
    height, width, layers = frame.shape
    
        # if chart file doesn't exist in a main directory
    if os.path.isfile('chart.jpg')==False: 
        chart=False
        
        #get chart and set size as in a frame        
    if chart==True: 
        width+=chart_width
        scale = cv2.imread('chart.jpg')
        scale = cv2.resize(scale,(chart_width,height))
    
    video = cv2.VideoWriter(output_video, -1, fps, (width,height))
    
    # descending=True means from older to younger ages
    if descending==True:
        images.sort(key=lambda x: -int(re.findall('(\d+)',x)[0]))
    else: images.sort(key=lambda x: int(re.findall('(\d+)',x)[0]))
       
    
    # main process    
    for img in images:
        age=re.findall('(\d+)', img)[0]   # get age from filename
        frame = cv2.imread(os.path.join(images_folder, img)) 
        
		#  add text on a frame
        cv2.putText(frame,age+' Ma', 
            bottomLeftCornerOfText, 
            font, 
            fontScale,
            fontColor,
            lineType)
        
        
        # add frame to video
        video.write(frame)

        cv2.destroyAllWindows()
    video.release()



