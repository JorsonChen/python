class Student(object):

	def __init__(self, name, score):
		#self.__name = name #私有变量，外部不可访问
		self.name = name
		self.score = score

	def print_score(self):
		print('%s: %s' % (self.name, self.score))

	def get_grade(self):
		if self.score >= 90:
			return "A"
		elif self.score >=60:
			return "B"
		else:
			return "C"

# cyw = Student('cyw',60)
# cyz = Student('cyz',70)

# cyw.print_score()	
# cyz.print_score()
# print(cyz.get_grade())	
#print(cyz.name)	


#类的继承	
class Student1(Student):
	#继承后再自己定义方法
	def study(self):
		print("I'am studing python!")

ccc = Student1('ccc',80)
#ccc.print_score()		
ccc.study()		