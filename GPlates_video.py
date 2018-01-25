def GPlates_video(image_folder='images',video_name='GPlates_reconstruction.avi',fps=15, descending=True):
    import os
    import cv2
    import re
    ## 
    images = [img for img in os.listdir(image_folder)]
    
    # fonts settings
    font                   = cv2.FONT_HERSHEY_SIMPLEX
    bottomLeftCornerOfText = (10,30)
    fontScale             = 1
    fontColor              = (255,255,255)
    lineType               = 2

    # presettings of video
    frame = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, layers = frame.shape
    video = cv2.VideoWriter(video_name, -1, fps, (width,height))
    
    # descending=True means from older to younger ages
    if descending==True:
        images.sort(key=lambda x: -int(re.findall('(\d+)',x)[0]))
    else: images.sort(key=lambda x: int(re.findall('(\d+)',x)[0]))
    
    #make video from set of image
    
    for img in images:
        frame = cv2.imread(os.path.join(image_folder, img))
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



