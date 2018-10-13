#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : picture_string.py
# @Author: Feng
# @Date  : 2018/10/13
# @Desc  :


import cv2

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")


# 将灰度值转为字符
def get_char(gray_number):
    length = len(ascii_char)
    unit = (256.0 + 1) / length
    return ascii_char[int(gray_number / unit)]


if __name__ == '__main__':
    image1 = cv2.imread('./pic/touxiang.jpg')
    image = cv2.resize(image1, (110, 110))
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    txt = ""
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            # 对打开的图片的每个坐标的灰度值做判断，
            # 用get_char()获取该颜色灰度值对应的字符，然后拼接成字符串txt
            txt += get_char(gray[i, j])
        txt += '\n'
    print(txt)

    # 字符画输出到文件中
    f = open('output.txt', 'w')
    f.write(txt)
