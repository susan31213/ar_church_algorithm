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

    return s1, s2

def church(real, photo, f, init_z, center=[3000/2, 4000/2], plot=False):

    ab = ((1.6e-6 * (photo[0][0]-photo[1][0])) ** 2 + (1.6e-6 * (photo[0][1]-photo[1][1])) ** 2) ** 0.5
    Oa = (f**2 + ((1.6e-6 * abs(center[0]-photo[0][0]))**2 + (1.6e-6 * abs(center[1]-photo[0][1]))**2))**0.5
    Ob = (f**2 + ((1.6e-6 * abs(center[0]-photo[1][0]))**2 + (1.6e-6 * abs(center[1]-photo[1][1]))**2))**0.5
    aOb = math.acos((Oa**2+Ob**2-ab**2)/(2*Oa*Ob))

    bc = ((1.6e-6 * (photo[1][0]-photo[2][0])) ** 2 + (1.6e-6 * (photo[1][1]-photo[2][1])) ** 2) ** 0.5
    Oc = (f**2 + ((1.6e-6 * abs(center[0]-photo[2][0]))**2 + (1.6e-6 * abs(center[1]-photo[2][1]))**2))**0.5
    bOc = math.acos((Ob**2+Oc**2-bc**2)/(2*Oc*Ob))

    ac = ((1.6e-6 * (photo[0][0]-photo[2][0])) ** 2 + (1.6e-6 * (photo[0][1]-photo[2][1])) ** 2) ** 0.5
    aOc = math.acos((Oa**2+Oc**2-ac**2)/(2*Oc*Oa))

    AB = ((real[0][0] - real[1][0]) ** 2 + (real[0][1] - real[1][1]) ** 2) **0.5
    BC = ((real[2][0] - real[1][0]) ** 2 + (real[2][1] - real[1][1]) ** 2) **0.5
    AC = ((real[0][0] - real[2][0]) ** 2 + (real[0][1] - real[2][1]) ** 2) **0.5


    x, y, z = (real_marks[1][0]+real_marks[2][0])/3, (real_marks[1][1]+real_marks[2][1])/3, init_z
    step = 0.001
    moves = [[x, y, z+step], [x+step, y, z+step], [x, y+step, z+step], [x+step, y+step, z+step], [x-step, y+step, z+step], [x-step, y, z+step], [x, y-step, z+step], [x+step, y-step, z+step], [x-step, y-step, z+step],
            [x+step, y, z], [x, y+step, z], [x+step, y+step, z], [x-step, y+step, z], [x-step, y, z], [x, y-step, z], [x+step, y-step, z], [x-step, y-step, z],
            [x, y, z-step], [x+step, y, z-step], [x, y+step, z-step], [x+step, y+step, z-step], [x-step, y+step, z-step], [x-step, y, z-step], [x, y-step, z-step], [x+step, y-step, z-step], [x-step, y-step, z-step]]
    moves = [[x, y, z+step], [x+step, y, z], [x, y+step, z], [x, y, z-step], [x-step, y, z], [x, y-step, z]]
    min_error = 1000
    ans = []
    iteration = 0

    xx = []
    yy = []
    zz = []

    oscillation = 0
    last_error = 0
    for t in range(10000):
        moves = [[x, y, z+step], [x+step, y, z+step], [x, y+step, z+step], [x+step, y+step, z+step], [x-step, y+step, z+step], [x-step, y, z+step], [x, y-step, z+step], [x+step, y-step, z+step], [x-step, y-step, z+step],
                [x, y, z], [x+step, y, z], [x, y+step, z], [x+step, y+step, z], [x-step, y+step, z], [x-step, y, z], [x, y-step, z], [x+step, y-step, z], [x-step, y-step, z],
                [x, y, z-step], [x+step, y, z-step], [x, y+step, z-step], [x+step, y+step, z-step], [x-step, y+step, z-step], [x-step, y, z-step], [x, y-step, z-step], [x+step, y-step, z-step], [x-step, y-step, z-step]]
        for m in moves:
            OA = (m[0]**2 + m[1]**2 + m[2]**2) ** 0.5
            OB = ((m[0]-real_marks[2][0])**2 + (m[1]-real_marks[2][1])**2 + m[2]**2) ** 0.5
            OC = ((m[0]-real_marks[2][0])**2 + (m[1]-real_marks[2][1])**2 + m[2]**2) ** 0.5
            AOB = math.acos((OA**2+OB**2-AB**2)/(2*OA*OB))
            BOC = math.acos((OB**2+OC**2-BC**2)/(2*OC*OB))
            AOC = math.acos((OA**2+OC**2-AC**2)/(2*OA*OC))
            # error = abs(AOB-aOb) + abs(BOC-bOc) + abs(AOC-aOc)
            error = abs(AOB-aOb)

            if abs(min_error) > abs(error):
                min_error = error
                ans = m
                iteration = t
                if plot:
                    xx.append(m[0])
                    yy.append(m[1])
                    zz.append(m[2])
                
        
        # if abs(last_error + min_error) < step*0.1:
        #     print('adjust step')
        #     step *= 0.1
        last_error = min_error
        x = ans[0]
        y = ans[1]
    print(t, m, abs(error))
    if plot:
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        ax.plot(xx, yy, zz)
        ax.legend()
        plt.show()

    return m, abs(error)

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
long_s1, long_s2 = church2D(real_marks, long_marks, 4.73e-3)
mid_s1, mid_s2 = church2D(real_marks, mid_marks, 4.73e-3)
short_s1, short_s2 = church2D(real_marks, short_marks, 4.73e-3)
print('Distance\nLong.png:  {0} m\nMid.png:   {1} m\nShort.png: {2} m'.format(long_s1, mid_s1, short_s1))
print('Focus\nLong.png:  {0} m\nMid.png:   {1} m\nShort.png: {2} m'.format(long_s2, mid_s2, short_s2))

long_cam, long_err = church(real_marks, long_marks, long_s2, long_s1)
mid_cam, mid_err = church(real_marks, mid_marks, mid_s2, mid_s1)
short_cam, short_err = church(real_marks, short_marks, short_s2, short_s1)





