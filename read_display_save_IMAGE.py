# in this program i load and display an image and write it on a new path

import cv2 as cv
import sys
import numpy as np

img = cv.imread("/home/moein/Documents/Computer Vision/lena.jpg",cv.IMREAD_GRAYSCALE)
if img is None:
    sys.exit("could not read the image!")
cv.namedWindow("image",cv.WINDOW_AUTOSIZE)
cv.imshow("image",img)
key = cv.waitKey(0)
if key == 27:
    cv.destroyAllWindows()
elif key == ord('s'):
    cv.imwrite("/home/moein/Documents/Computer Vision/newImage.jpg",img)
    cv.destroyAllWindows()