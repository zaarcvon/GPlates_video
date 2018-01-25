def reconstruction_to_video(images_folder='images',output_video='GPlates_reconstruction.avi',fps=15, descending=True):
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

    Returns
    -------
    None
    
    Videofile in main folder
    """
    
    import os
    import cv2
    import re
    
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
    video = cv2.VideoWriter(output_video, -1, fps, (width,height))
    
    # descending=True means from older to younger ages
    if descending==True:
        images.sort(key=lambda x: -int(re.findall('(\d+)',x)[0]))
    else: images.sort(key=lambda x: int(re.findall('(\d+)',x)[0]))
    
    #make video from set of image
    
    for img in images:
        frame = cv2.imread(os.path.join(images_folder, img))
        # add text on a frame
        
        age=re.findall('(\d+)', img)[0]+' Ma'
        cv2.putText(frame,age, 
            bottomLeftCornerOfText, 
            font, 
            fontScale,
            fontColor,
            lineType)
        
        # add frame to video
        video.write(frame)

        cv2.destroyAllWindows()
    video.release()



