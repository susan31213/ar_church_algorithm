import numpy as numpy
import cv2
import math, sys

def find_marks(img):
    marks = [[0,0],[0,0],[0,0]]
    found = 0
    for i in range(img.shape[0]):
        if i % 100 == 0:
            print('.', end='')
            sys.stdout.flush()
        for j in range(img.shape[1]):
            if img[i][j][0] == 0 and img[i][j][1] == 0 and img[i][j][2] == 255:
                marks[0][0] = i
                marks[0][1] = j
                found += 1
            if img[i][j][0] == 0 and img[i][j][1] == 100 and img[i][j][2] == 255:
                marks[1][0] = i
                marks[1][1] = j
                found += 1
            if img[i][j][0] == 255 and img[i][j][1] == 0 and img[i][j][2] == 0:
                marks[2][0] = i
                marks[2][1] = j
                found += 1
        if found == 3:
            print('')
            break
    return marks

def church2D(real, photo, f):
    f = f
    h1 = math.sqrt(math.pow(real[0][0]-real[1][0], 2) + math.pow(real[0][1]-real[1][1], 2)) * 1.0e-2
    h2 = math.sqrt(math.pow(photo[0][0]-photo[1][0], 2) + math.pow(photo[0][1]-photo[1][1], 2)) * 1.6e-6
    s1 = 0
    s2 = f

    last_s1 = -1
    while True:
        s1 = h1/h2 * s2
        s2 = 1.0/(1.0/f - 1.0/s1)
        if last_s1 - s1 == 0:
            break
        else:
            last_s1 = s1

    return s1

# read images
long_img = cv2.imread('Long.png')
mid_img = cv2.imread('Mid.png')
short_img = cv2.imread('Short.png')

# find marks
real_marks = [[0,0], [27.5, 5.8], [21, -8.3]]
# print('searching long marks', end='')
# sys.stdout.flush()
# long_marks = find_marks(long_img)
# print('searching mid marks', end='')
# sys.stdout.flush()
# mid_marks = find_marks(mid_img)
# print('searching short marks', end='')
# sys.stdout.flush()
# short_marks = find_marks(short_img)
long_marks = [[1842, 1687], [1711, 2477], [2107, 2270]]
mid_marks = [[1075, 1398], [672, 3550], [1747, 3000]]
short_marks = [[1262, 466], [633, 3513], [2186, 2795]]

# church's algorithm with given png
long_s = church2D(real_marks, long_marks, 4.73e-3)
mid_s = church2D(real_marks, mid_marks, 4.73e-3)
short_s = church2D(real_marks, short_marks, 4.73e-3)
print('Long.png:  {0} m\nMid.png:   {1} m\nShort.png: {2} m'.format(long_s, mid_s, short_s))



