#!/user/bin/env python
# -*- coding:utf-8 -*-

'a test module'

import sys

def test():
	args = sys.argv
	if len(args)==1:
		print ("Hello,word!")
	elif len(args)==2:
		print ("Hello,China")
	else:
		print ("haha")
if __name__ == '__main__':
	test()