"""
Image2dConv.py
author:Elaina
date:2023/11/13
description:calculate the convolution.
"""

def init(img):
    null_arr = [0 for i in range(len(img)+2)]
    img.insert(0, null_arr)
    for i in range(1, len(img), 1):
        img[i].insert(0, 0)
        img[i].append(0)
    img.append(null_arr)
    return img

def convolute(img_x, img_y, img, kernel, times):
    num = 0
    for i in range(len(kernel)):
        for j in range(len(kernel)):
            num += img[img_x+i][img_y+j] * kernel[i][j]
    return num

def Image2dConv(img, kernel):
    img = init(img)
    times = len(img) - len(kernel) + 1
    ans = [[0 for i in range(times)] for i in range(times)]
    for i in range(times):
        for j in range(times):
            ans[i][j] = convolute(i, j, img, kernel, times)
    return ans

img = [
    [1,1,1],
    [1,0,1],
    [1,1,1]
    ]
kernel = [
    [1,1,1],
    [1,1,1],
    [1,1,1]
    ]
print(Image2dConv(img, kernel))
