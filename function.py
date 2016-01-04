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


# import math
# def move(x,y,step,angle=0):
# 	nx = x + step * math.cos(angle)
# 	ny = y - step * math.sin(angle)
# 	return nx,ny

# r = move(100,100,60,math.pi/6)
# print(r)


# def person(name,age,**kw):
# 	print ('name:',name,"age:",age,'other:',kw)

# person('cyw',25,sex='boy')


# 递归函数
# def fact(n):
# 	if n==1:
# 		return 1
# 	return n*fact(n-1)

# print(fact(100))



#尾递归函数（返回时调用本身）
# def fact(n):
# 	return fact_iter(n,1)
# def fact_iter(num,product):
# 	if num==1:
# 		return product
# 	return fact_iter(num-1,num*product)

# print(fact(5))
