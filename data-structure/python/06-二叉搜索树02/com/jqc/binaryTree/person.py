"""
测试类
"""


class Person(object):
	def __init__(self, name, age):
		self.name = name
		self.age = age
	
	def __str__(self):
		return 'p_' + str(self.age)
