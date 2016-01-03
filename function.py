#系统函数
# r = 4 ;
# S = str(3.14 * r * r) ;
# print(S)



#自定义函数
# def my_abs(x):
# 	if x >= 0:
# 		return x
# 	else:
# 		return -x

# total = 30
# print(my_abs(total))

import math
def move(x,y,step,angle=0):
	nx = x + step * math.cos(angle)
	ny = y - step * math.sin(angle)
	return nx,ny

r = move(100,100,60,math.pi/6)
print(r)