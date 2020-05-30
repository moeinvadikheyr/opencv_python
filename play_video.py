# play video from file

import cv2 as cv
import numpy as np

cap = cv.VideoCapture('/home/moein/Downloads/drop.avi')

while(cap.isOpened()):
    ret,frame = cap.read()

    gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)

    cv.imshow("video",frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()