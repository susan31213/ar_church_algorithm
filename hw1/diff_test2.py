import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


real_marks = [[0,0], [27.5e-2, 5.8e-2], [21e-2, -8.3e-2]]
long_marks = [[1842, 1687], [1711, 2477], [2107, 2270]]
mid_marks = [[1075, 1398], [672, 3550], [1747, 3000]]
short_marks = [[1262, 466], [633, 3513], [2186, 2795]]
f = 4.73e-3
center = [3000/2, 4000/2]

# O = [x,y,z]

ab = ((1.6e-6 * (short_marks[0][0]-short_marks[1][0])) ** 2 + (1.6e-6 * (short_marks[0][1]-short_marks[1][1])) ** 2) ** 0.5
Oa = (0.004813778412990528**2 + ((1.6e-6 * abs(center[0]-short_marks[0][0]))**2 + (1.6e-6 * abs(center[1]-short_marks[0][1]))**2))**0.5
Ob = (0.004813778412990528**2 + ((1.6e-6 * abs(center[0]-short_marks[1][0]))**2 + (1.6e-6 * abs(center[1]-short_marks[1][1]))**2))**0.5
aOb = math.acos((Oa**2+Ob**2-ab**2)/(2*Oa*Ob))

bc = ((1.6e-6 * (short_marks[1][0]-short_marks[2][0])) ** 2 + (1.6e-6 * (short_marks[1][1]-short_marks[2][1])) ** 2) ** 0.5
Oc = (0.004813778412990528**2 + ((1.6e-6 * abs(center[0]-short_marks[2][0]))**2 + (1.6e-6 * abs(center[1]-short_marks[2][1]))**2))**0.5
bOc = math.acos((Ob**2+Oc**2-bc**2)/(2*Oc*Ob))

ac = ((1.6e-6 * (short_marks[0][0]-short_marks[2][0])) ** 2 + (1.6e-6 * (short_marks[0][1]-short_marks[2][1])) ** 2) ** 0.5
aOc = math.acos((Oa**2+Oc**2-ac**2)/(2*Oc*Oa))

AB = ((real_marks[0][0] - real_marks[1][0]) ** 2 + (real_marks[0][1] - real_marks[1][1]) ** 2) **0.5
BC = ((real_marks[2][0] - real_marks[1][0]) ** 2 + (real_marks[2][1] - real_marks[1][1]) ** 2) **0.5
AC = ((real_marks[0][0] - real_marks[2][0]) ** 2 + (real_marks[0][1] - real_marks[2][1]) ** 2) **0.5

# x, y, z = 0.15, 0.8, 1.04
x, y, z = (real_marks[1][0]+real_marks[2][0])/3, (real_marks[1][1]+real_marks[2][1])/3, 0.27177850571148077
step = 0.001
moves = [[x, y, z+step], [x+step, y, z+step], [x, y+step, z+step], [x+step, y+step, z+step], [x-step, y+step, z+step], [x-step, y, z+step], [x, y-step, z+step], [x+step, y-step, z+step], [x-step, y-step, z+step],
        [x+step, y, z], [x, y+step, z], [x+step, y+step, z], [x-step, y+step, z], [x-step, y, z], [x, y-step, z], [x+step, y-step, z], [x-step, y-step, z],
        [x, y, z-step], [x+step, y, z-step], [x, y+step, z-step], [x+step, y+step, z-step], [x-step, y+step, z-step], [x-step, y, z-step], [x, y-step, z-step], [x+step, y-step, z-step], [x-step, y-step, z-step]]
moves = [[x, y, z+step], [x+step, y, z], [x, y+step, z], [x, y, z-step], [x-step, y, z], [x, y-step, z]]
min_error = 1000
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
            xx.append(m[0])
            yy.append(m[1])
            zz.append(m[2])
            print(t, m, abs(error))
    
    # if abs(last_error + min_error) < step*0.1:
    #     print('adjust step')
    #     step *= 0.1
    last_error = min_error
    x = ans[0]
    y = ans[1]
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(xx, yy, zz)
ax.legend()

plt.show()
