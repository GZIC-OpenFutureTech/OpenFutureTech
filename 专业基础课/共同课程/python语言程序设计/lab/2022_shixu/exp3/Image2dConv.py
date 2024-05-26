"""
Image2dConv.py
author:张辰旭
date:2023.04.04
description:Implementation of basic convolution with 2D picture information as an example
"""
def make_append(img,m,append):
    result = [[0 for _ in range(0,m+2*append)] for _ in range(0,m+2*append)]
    for i in range(0,m+2*append-1):
        for j in range(0, m + 2 * append - 1):
            if (i <= append-1) or (i >= m+append) or (j <= append-1) or (j >= m+append):
                result[i][j] = 0
            else:
                result[i][j] = img[i-append][j-append]
    return result


def Image2dConv(img, kernel):
    m = len(img)
    n = len(kernel)
    output = [[0 for _ in range(m)] for _ in range(m)]
    append = n // 2
    img2 = make_append(img,m,append)
    for i in range(m):
        for j in range(m):
            add = 0
            for a in range(i,i+n):
                for b in range(j,j+n):
                    add += kernel[a-i][b-j]*img2[a][b]
            output[i][j] = add
    return output

img = [[1,1,1],[1,0,1],[1,1,1]]
kernel = [[1,1,1],[1,1,1],[1,1,1]]
output = Image2dConv(img, kernel)
print(output)