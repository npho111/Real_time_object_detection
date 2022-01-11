import cv2 as cv
import numpy as np
import os
from time import time

#from PIL import ImageGrab
from mss.linux import MSS as mss
#opencv window capture class   
cv.startWindowThread()
HEIGHT, WIDHT = 512, 512
SIDES, UPDOWN = 0, 0
x, y = 0, 0
def move_camera(ch): 
    global x, y , HEIGHT, WIDHT
    if ch == ord('f'):
        HEIGHT -= 100
        WIDHT -= 100
    if ch == ord('g'):
        HEIGHT += 100
        WIDHT += 100
        #camera controls
    if ch == ord('h'):
        x -= 100
    if ch == ord('k'):
        x += 100
    if ch == ord('u'):
        y -= 100
    if ch == ord('j'):    
        y += 100
    
class WindowCapture:
    font                   = cv.FONT_HERSHEY_SIMPLEX
    bottomLeftCornerOfText = (10,50)
    fontScale              = 1
    fontColor              = (255,255,255)
    lineType               = 2
    counter = 0 
    loop_time = time()
    while(True):   
        global x, y, HEIGHT, WIDHT 
        
        
        with mss(display=":0.0") as sct:
            screenshot = sct.grab({"top": y, "left": x, "width": WIDHT, "height": HEIGHT})
        #screenshot = ImageGrab.grab(bbox=(SIDES + x,UPDOWN + y, HEIGHT + x, WIDHT + y))
        screenshot = np.array(screenshot)
        screenshot = cv.cvtColor(screenshot, cv.COLOR_RGB2BGR)
        #line = cv.line(screenshot, (0, int(WIDHT/2)), (HEIGHT, int(WIDHT/2)), (0, 255, 0), thickness=2)        
        #face_locations = face_recognition.face_locations(screenshot)
        #for rect in face_locations:
        #    img = cv.rectangle(screenshot, (rect[3], rect[0]), (rect[1], rect[2]), (0, 0, 255), thickness=2)
        ch = cv.waitKey(1)
        move_camera(ch)
        screenshot = cv.putText(screenshot,str(counter),(30,80),1,2,(0, 0, 255))
        FPS = (1/(time()-loop_time))
        screenshot = cv.putText(screenshot,'FPS {}'.format(FPS),
                                bottomLeftCornerOfText,1,2,(0,255,255))
        cv.imshow('Computer Vision', screenshot)  
        if ch == ord('q'):
            cv.destroyAllWindows()
            break
        loop_time = time()
    print('Done')





