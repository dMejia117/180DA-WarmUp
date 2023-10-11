import numpy as np
import cv2 as cv
*******Resources****************
#https://docs.opencv.org/4.x/da/d22/tutorial_py_canny.html
#https://docs.opencv.org/4.x/df/d9d/tutorial_py_colorspaces.html
#https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_video_display/py_video_display.html
cap = cv.VideoCapture(0)

while(1):

#code taken from 1 moments bounding box 
    _, frame = cap.read()
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    range_low = np.array([23, 100, 80])
    range_hi = np.array([56, 255, 255])
    mask = cv.inRange(hsv, range_low, range_hi)
    x,y,w,h = cv.boundingRect(mask)
    cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    cv.imshow('frame', frame)
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break

cv.destroyAllWindows()