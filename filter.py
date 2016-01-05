#python内置函数--序列过滤filter
#过滤偶数保留奇数
# def is_odd(n):
# 	return n % 2 ==1
# l = list(filter(is_odd,[1,2,3,4,5,6,9,10,15,16,18,19]))
# print(l)


#过滤掉空字符串
# def filter_empty(s):
# 	return s and s.strip()
# l = list(filter(filter_empty,['A','','B',None,'C',""]))
# print (l)


#求素数
def _odd_iter():
	n = 1
	while True:
	 	n = n + 2
	 	yield n
def _not_divisible(n):
 	return lambda x : x % n > 0
def primes():
 	yield 2
 	it = _odd_iter()
 	while True:
 		n = next(it)
 		yield n
 		it = filter(_not_divisible(n),it)
for n in primes():
	if n < 100:
		print (n)
	else:
		break