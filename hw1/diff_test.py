from sympy import *
import math

real_marks = [[0,0], [27.5e-2, 5.8e-2], [21e-2, -8.3e-2]]
long_marks = [[1842, 1687], [1711, 2477], [2107, 2270]]
mid_marks = [[1075, 1398], [672, 3550], [1747, 3000]]
short_marks = [[1262, 466], [633, 3513], [2186, 2795]]
f = 4.73e-3
center = [3000/2, 4000/2]

O = [x,y,z]

vOa = [(long_marks[0][0]-center[0]) * 1.6e-6, (long_marks[0][1]-center[1]) * 1.6e-6]
vOb = [(long_marks[1][0]-center[0]) * 1.6e-6, (long_marks[1][1]-center[1]) * 1.6e-6]
Oa = (0.004751563300220614**2 + ((1.6e-6 * abs(center[0]-long_marks[0][0]))**2 + (1.6e-6 * abs(center[1]-long_marks[0][1]))**2))**0.5
Ob = (0.004751563300220614**2 + ((1.6e-6 * abs(center[0]-long_marks[1][0]))**2 + (1.6e-6 * abs(center[1]-long_marks[1][1]))**2))**0.5

print(Oa, Ob)

print(math.degrees(math.acos((vOa[0] * vOb[0] + vOa[1] * vOb[1])/(Oa*Ob))))

print()

x, y = symbols('x, y')
 
z = x**2+y**2+x*y+2
print(z)
result = z.subs({x: 1, y: 2})   # 用数值分别对x、y进行替换
print(result)
 
dx = diff(z, x)   # 对x求偏导
print(dx)
result = dx.subs({x: 1, y: 2})
print(result)
 
dy = diff(z, y)   # 对y求偏导
print(dy)
result = dy.subs({x: 1, y: 2})
print(result)
 
 
# subs函数可以将算式中的符号进行替换，它有3种调用方式：
# expression.subs(x, y) : 将算式中的x替换成y
# expression.subs({x:y,u:v}) : 使用字典进行多次替换
# expression.subs([(x,y),(u,v)]) : 使用列表进行多次替换