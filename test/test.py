#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test.py
# @Author: Feng
# @Date  : 2018/10/9
# @Desc  :
import cv2
import numpy

path = "E:\\2.jpg"
img = cv2.imread(path)
print(img)
hight, width, depth = img.shape[0:3]

thresh = cv2.inRange(img, numpy.array([240, 240, 240]), numpy.array([255, 255, 255]))

kernel = numpy.ones((3, 3), numpy.uint8)

hi_mask = cv2.dilate(thresh, kernel, iterations=1)

specular = cv2.inpaint(img, hi_mask, 5, flags=cv2.INPAINT_TELEA)

cv2.namedWindow("Image", 0)
cv2.resizeWindow("Image", int(width/2), int(hight/2))
cv2.imshow("Image", img)


cv2.namedWindow("newImage", 0)
cv2.resizeWindow("newImage", int(width/2), int(hight/2))
cv2.imshow("newImage", specular)

cv2.waitKey(0)
cv2.destroyAllWindows()

