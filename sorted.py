#排序算法
#普通排序
# l = [31,58,-14,29,0,-3,105]
# sl = sorted(l)
# print(sl)


#加入key值的排序(此时sorted是高阶函数)
# l = [31,58,-14,29,0,-3,105]
# sl = sorted(l,key=abs)
# print(sl)


#对字符串进行排序(按照ASCII大小排)
# l = ['hello','Hi','zoo','chen','~','nishishui']
# sl = sorted(l)
# print(sl)

#对字符串进行排序，忽略大小写(按照ASCII大小排)
# l = ['hello','Hi','zoo','chen','~','nishishui']
# sl = sorted(l,key=str.lower)
# print(sl)


#对字符串进行排序，忽略大小写，并且反向(按照ASCII大小排)
l = ['hello','Hi','zoo','chen','~','nishishui']
sl = sorted(l,key=str.lower,reverse=True)
print(sl)