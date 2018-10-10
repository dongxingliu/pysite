#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : video_to_pictures.py
# @Author: Feng
# @Date  : 2018/10/10
# @Desc  :

"""
读取视频转换成单帧图片集
"""
# --coding:utf-8--
import cv2

cap = cv2.VideoCapture("E:/75  - .mp4")

n = 1
# print(cap.read()[1])
#
# for im in cap.read()[1]:
#     cv2.imwrite("E:/1/" + str(n) + ".jpg", im)
#     n += 1
while True:
    # 读取帧
    ret, im = cap.read()
    # 设置帧
    if im is None:
        break

    gary = cv2.cvtColor(im, 10)
    # 显示帧
    # cv2.imshow("ccc", gary)
    if n % 2 == 0:
        cv2.imwrite("E:/1/" + str(n) + ".jpg", im)
    n += 1
    if cv2.waitKey(1) == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()

