# load and display image by matplotlib library

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread("/home/moein/Documents/Computer Vision/lena.jpg", 0)
plt.imshow(img , cmap = 'gray',interpolation = 'bicubic')
plt.xticks([]) , plt.yticks([]) # to hide tick values
plt.show()

