import cv2 as cv 



class Camera:
    global HEIGHT, WIDHT, x, y

    def move_camera(ch, x, y, HEIGHT, WIDHT): 
        if ch == ord('f'):
            HEIGHT -= 100
            WIDHT -= 100
        if ch == ord('g'):
            HEIGHT += 100
            WIDHT += 100
        if ch == ord('q'):
            cv.destroyAllWindows()
            #camera controls
        if ch == ord('h'):
            x -= 100
        if ch == ord('k'):
            x += 100
        if ch == ord('u'):
            y -= 100
        if ch == ord('j'):    
            y += 100
                
            