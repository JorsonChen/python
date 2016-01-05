#迭代(in方式)
# d = {'a':1,'b':2,'c':3}
# for key in d:
# 	print (key)

#Python内置的enumerate函数可以把一个list变成索引-元素对
# for i, value in enumerate(['A', 'B', 'C']):
# 	print (i,value)

# for x, y in [(1, 1), (2, 4), (3, 9)]:
# 	print (x, y)

#生成列表
# l = [x * x for x in range(1,11) if x % 2 == 0]
# print(l)

#两个变量生成list
# d = {'x':'A','y':'B','z':'C'}
# l = [k + '=' + v for k,v in d.iteritems()]
# print(l)

#生成器
# g = (x * x for x in range(10))
# print (g)
# i = 0
# while i<10:
# 	print(next(g))
# 	i = i + 1

#高阶函数(一个函数可以接收另外一个函数)
def add(x,y,f):
	return f(x)+f(y)
print(add(-1,6,abs))

