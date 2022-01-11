import cv2 as cv
import numpy as np
import os
from time import time
from PIL import ImageGrab
import os
import face_recognition
os.environ["CUDA_VISIBLE_DEVICES"] = "0"
class WindowCapture:
    font                   = cv.FONT_HERSHEY_SIMPLEX
    bottomLeftCornerOfText = (10,50)
    fontScale              = 1
    fontColor              = (255,255,255)
    lineType               = 2
    loop_time = time()
    counter = 0 
    while(True):    
        loop_time = time()
        screenshot = ImageGrab.grab(bbox=(0,0,1920,1080))
        screenshot = np.array(screenshot)
        screenshot = cv.cvtColor(screenshot, cv.COLOR_RGB2BGR)#cv.cvtColor(screenshot, cv.COLOR_RGB2BGR)#screenshot[:, :, ::-1].copy()  # cv.cvtColor(screenshot, cv.COLOR_RGB2BGR)
        line = cv.line(screenshot, (0,300), (800, 300), (0, 255, 0), thickness=2)
        FPS = (1/(time()-loop_time))
        screenshot = cv.putText(screenshot,'FPS {}'.format(1/(time()-loop_time)),bottomLeftCornerOfText,1,2,(230, 230, 255))
        loop_time = time()
        screenshot = cv.putText(screenshot,str(counter),(30,80),1,2,(0, 0, 255))
        face_locations = face_recognition.face_locations(screenshot)
        for rect in face_locations:
            img = cv.rectangle(screenshot, (rect[3], rect[0]), (rect[1], rect[2]), (0, 0, 255), thickness=2)
        if cv.waitKey(1) == ord('q'):
            cv.destroyAllWindows()
            break
        if cv.waitKey(1) == ord('w'):
            counter += 1
        cv.imshow('Computer Vision', screenshot)  
        #print('FPS {}'.format(1/(time()-loop_time)))
        
    print('Done')
WindowCapture.screenshot()