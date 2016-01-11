#写文件
# f = open('/Users/Administrator/python/hello.txt','w') 
# f.write(',world!')
# f.close()

with open('/Users/Administrator/python/hello.txt','w') as f:
	f.write(',world2!')



# #try 方式
# try:
# 	f = open('/Users/Administrator/python/hello.txt','r')
# 	print(f.read())
# finally:
# 	if f:
# 		f.close()


#with 方式
with open('/Users/Administrator/python/hello.txt','r') as f:
	print(f.read())