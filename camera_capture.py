# capture video from camera

import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('/home/moein/Documents/Computer Vision/output.avi',fourcc,20.0,(640,480))
while(cap.isOpened()):

    ret,frame = cap.read()
    if ret == True:
        frame = cv.flip(frame,0)

        out.write(frame)

        cv.imshow("camrea",frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv.destroyAllWindows()