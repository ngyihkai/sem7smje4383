#pip install opencv-python

import numpy as np
import cv2 as cv

img= cv.imread("bottle.jpg",0)
cv.imshow("Image",img)
cv.waitKey(0)
cv.destroyAllWindows()

