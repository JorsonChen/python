print("please input yourname~")
name = input()
print("yourname is:"+name)
lenght = len(name) 
if lenght>15:
	print('yourname is too long!')
elif lenght>=8:
	print('yourname is good!')
elif lenght<4:
	print('yourname is bad!')
else:
	print('what you inputed is not a name')
print('Sorry!This is a bad program!')