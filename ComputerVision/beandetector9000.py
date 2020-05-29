import numpy as np
import cv2 as cv
import os


foto = 'foto1.bmp'
img = cv.imread(foto)
filterdImg = cv.bilateralFilter(img, 6, 30,30)
cv.imwrite('firstfilter.bmp', filterdImg)
for i in range(5):
    filterdImg = cv.bilateralFilter(filterdImg, 9-i, 75-(i*i),75-(i*i))


cv.imwrite('filteredbeans.bmp', filterdImg)
cv.waitKey(0)