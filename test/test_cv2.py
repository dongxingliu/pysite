#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test_cv2.py
# @Author: Feng
# @Date  : 2018/10/10
# @Desc  :

import cv2 as cv

def access_pixels(frame):
    print(frame.shape)  # shape内包含三个元素：按顺序为高、宽、通道数
    height = frame.shape[0]
    weight = frame.shape[1]
    channels = frame.shape[2]
    print("weight : %s, height : %s, channel : %s" % (weight, height, channels))

    for row in range(height):  # 遍历高
        for col in range(weight):  # 遍历宽
            for c in range(channels):  # 便利通道
                pv = frame[row, col, c]
                frame[row, col, c] = 255 - pv  # 全部像素取反，实现一个反向效果
    cv.imshow("fanxiang", frame)

def access_pixels2(frame):
    print(frame.shape)  # shape内包含三个元素：按顺序为高、宽、通道数
    height = frame.shape[0]
    weight = frame.shape[1]
    channels = frame.shape[2]
    print("weight : %s, height : %s, channel : %s" % (weight, height, channels))

    for row in range(height):  # 遍历高
        for col in range(weight):  # 遍历宽
            for c in range(channels):  # 便利通道
                if col <= weight/2:
                    print("-"*50+"\nweight:%s height:%s  channels:%s \nrow:%s col:%s c:%s\n" % (weight, height, channels, row, col, c))
                    pv = frame[row, col, c]
                    frame[row, col, c] = frame[row, weight-col-1, c]  # 全部像素取反，实现一个反向效果
                    frame[row, weight-col-1, c] = pv
    cv.imshow("fanxiang", frame)


image = "./pic/1.png"
src = cv.imread(image)
cv.imshow("Picture", src)
access_pixels2(src)
cv.waitKey(0)
