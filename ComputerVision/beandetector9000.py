import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import os.path

fullpath = os.path.realpath(__file__)
pathdir = os.path.dirname(fullpath)
foto = pathdir + '/foto3.bmp'
img = cv.imread(foto)

imageHSV = cv.cvtColor(img,cv.COLOR_RGB2HSV)


image = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
filterdImg = cv.GaussianBlur(image,(5,5),0)
filterdImg = cv.bilateralFilter(image, 9, 30,30)
#cv.imwrite('firstfilter.bmp', filterdImg)


for i in range(10):
    filterdImg = cv.bilateralFilter(filterdImg, 1+i, 20+(i*i),20+(i*i))


ret, thr = cv.threshold(filterdImg, 0, 255, cv.THRESH_BINARY_INV+cv.THRESH_OTSU)

contours, hierarchy = cv.findContours(thr, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
contours = [cont for cont in contours if cv.contourArea(cont)>550]

colorimg = cv.cvtColor(filterdImg, cv.COLOR_GRAY2RGB)
hsv = cv.cvtColor(colorimg, cv.COLOR_RGB2HSV)
"""
for cnt in contours:   
    mask = np.zeros(filterdImg.shape, np.uint8)
    cv.drawContours(mask, [cnt],0,(255,255,255),-2)
    
    mean = cv.mean(imageHSV, mask= mask)
    if( cv.contourArea(cnt) > 35000 and cv.contourArea(cnt) < 60000 and mean[0]>109 and mean[0]<120):
        cv.drawContours(img, [cnt], 0, (0,255,0), 3)

img = cv.cvtColor(img, cv.COLOR_RGB2BGR)
plt.imshow(img)


"""
thrimg = cv.bitwise_and(imageHSV, imageHSV, mask=thr)
pltimg = cv.cvtColor(thrimg, cv.COLOR_HSV2BGR)
h,s,v = cv.split(thrimg)
#plt.imshow(pltimg, 'hsv')


Z = h.reshape((-1,3))
Z = np.float32(Z)

criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 10, 1.0)
K = 4
ret,label,center=cv.kmeans(Z,K,None,criteria,10,cv.KMEANS_RANDOM_CENTERS)
center = np.uint8(center)
res = center[label.flatten()]
res2 = res.reshape((h.shape))
cv.namedWindow('res2', cv.WINDOW_NORMAL)
cv.imshow('res2',res2)



plt.show()
cv.waitKey(0) 