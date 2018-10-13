#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : picture_string2.py
# @Author: Feng
# @Date  : 2018/10/13
# @Desc  :

from PIL import Image
import argparse

# parser = argparse.ArgumentParser()

IMG = 'E:/00-工作/90-workspace/pysite/test/pic/ascii_dora.png'
WIDTH = 100
HEIGHT = 100

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")


# 将256灰度映射到70个字符上
def get_char(r, g, b, alpha=256):
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

    unit = (256.0 + 1) / length
    return ascii_char[int(gray / unit)]


if __name__ == "__main__":
    img = Image.open(IMG)
    img = img.resize((WIDTH, HEIGHT), Image.NEAREST)

    txt = ""

    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += get_char(*img.getpixel((j, i)))
        txt += '\n'

    print(txt)