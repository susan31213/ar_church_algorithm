from sympy import *
import math

real_marks = [[0,0], [27.5e-2, 5.8e-2], [21e-2, -8.3e-2]]
long_marks = [[1842, 1687], [1711, 2477], [2107, 2270]]
mid_marks = [[1075, 1398], [672, 3550], [1747, 3000]]
short_marks = [[1262, 466], [633, 3513], [2186, 2795]]
f = 4.73e-3
center = [3000/2, 4000/2]

# O = [x,y,z]

ab = ((1.6e-6 * (long_marks[0][0]-long_marks[1][0])) ** 2 + (1.6e-6 * (long_marks[0][1]-long_marks[1][1])) ** 2) ** 0.5
Oa = (0.004751563300220614**2 + ((1.6e-6 * abs(center[0]-long_marks[0][0]))**2 + (1.6e-6 * abs(center[1]-long_marks[0][1]))**2))**0.5
Ob = (0.004751563300220614**2 + ((1.6e-6 * abs(center[0]-long_marks[1][0]))**2 + (1.6e-6 * abs(center[1]-long_marks[1][1]))**2))**0.5
aOb = acos((Oa**2+Ob**2-ab**2)/(2*Oa*Ob))
print(aOb)

# print(math.degrees(math.acos((vOa[0] * vOb[0] + vOa[1] * vOb[1])/(Oa*Ob))))

# print()

x, y, z = symbols('x y z')
AB = ((real_marks[0][0] - real_marks[1][0]) ** 2 + (real_marks[0][1] - real_marks[1][1]) ** 2) **0.5
print(AB)
OA = (x**2 + y**2 +z**2) ** 0.5
OB = ((x-real_marks[1][0])**2 + (y-real_marks[1][1])**2 + z**2) ** 0.5
# print(math.acos((OA**2+OB**2-AB**2)/(2*OA*OB)))
# diff = abs(math.acos((OA**2+OB**2-AB**2)/(2*OA*OB)) - math.acos((Oa**2+Ob**2-ab**2)/(2*Oa*Ob)))

# math.acos((OA**2+OB**2-AB**2)/(2*OA*OB)*math.pi
# math.acos((((x**2 + y**2 +z**2) ** 0.5)**2+(((x-real_marks[1][0])**2 + (y-real_marks[1][1])**2 + z**2) ** 0.5)**2-(((real_marks[0][0] - real_marks[1][0]) ** 2 + (real_marks[0][1] - real_marks[1][1]) ** 2) ** 0.5)**2)/(2*((x**2 + y**2 +z**2) ** 0.5)*(((x-real_marks[1][0])**2 + (y-real_marks[1][1])**2 + z**2) ** 0.5))*math.pi

X = 13.5
Y = 2
Z = 1.042275263067448
# AOB = acos(((x**2 + y**2 +z**2)+((x-27.5e-2)**2 + (y-5.8e-2)**2 + z**2)-AB**2)/(2*((x**2 + y**2 +z**2) ** 0.5)*(((x-27.5e-2)**2 + (y-5.8e-2)**2 + z**2) ** 0.5)))
angle_diff1 = acos(((x**2 + y**2 +z**2)+((x-0.275)**2 + (y-0.058)**2 + z**2)-0.2810498176480462**2)/(2*((x**2 + y**2 +z**2) ** 0.5)*(((x-0.275)**2 + (y-0.058)**2 + z**2) ** 0.5))) - 0.266775623611873
angle_diff2 = aOb - acos(((x**2 + y**2 +z**2)+((x-0.275)**2 + (y-0.058)**2 + z**2)-0.2810498176480462**2)/(2*((x**2 + y**2 +z**2) ** 0.5)*(((x-0.275)**2 + (y-0.058)**2 + z**2) ** 0.5)))
result = angle_diff1.subs({x: X, y: Y, z: Z})   # 用数值分别对x、y进行替换
print(result)
result = angle_diff2.subs({x: X, y: Y, z: Z})   # 用数值分别对x、y进行替换
print(result)



dx1 = diff(angle_diff1, x)   # 对x求偏导
dy1 = diff(angle_diff1, y)   # 对y求偏导
dz1 = diff(angle_diff1, z)
dx2 = diff(angle_diff2, x)   # 对x求偏导
dy2 = diff(angle_diff2, y)   # 对y求偏导
dz2 = diff(angle_diff2, z)

min_diff = 100
for k in range(20):
    if angle_diff1.subs({x: X, y: Y, z: Z}) >= 0:
        X += dx1.subs({x: X, y: Y, z: Z})
        Y += dy1.subs({x: X, y: Y, z: Z})
        Z += dz1.subs({x: X, y: Y, z: Z})
        print(X,Y,Z, angle_diff1.subs({x: X, y: Y, z: Z}))
    else: 
        X += dx2.subs({x: X, y: Y, z: Z})
        Y += dy2.subs({x: X, y: Y, z: Z})
        Z += dz2.subs({x: X, y: Y, z: Z})
        print(X,Y,Z, angle_diff2.subs({x: X, y: Y, z: Z}))
