from com.jqc.dynamicArray import DynamicArray

"""
使用之前实现的动态数组来实现栈
也可以使用单链表来实现栈
"""


class Stack(object):
	def __init__(self):
		self.arrayList = DynamicArray()
	
	def __str__(self):
		string = ''
		for i in range(self.arrayList.size() - 1, -1, -1):
			string += str(self.arrayList.get(i))
			string += ','
		
		return string
	
	def size(self) -> int:
		"""
		返回栈的长度
		:return:
		"""
		return self.arrayList.size()
	
	def clear(self):
		"""
		清空栈
		:return:
		"""
		self.arrayList.clear()
	
	def is_empty(self) -> bool:
		"""
		返回栈是否为空
		:return: bool
		"""
		return self.arrayList.is_empty()
	
	def push(self, element):
		"""
		入栈
		:param element: 元素
		:return:
		"""
		self.arrayList.add(element)
	
	def pop(self):
		"""
		出栈
		:return:
		"""
		return self.arrayList.remove(self.arrayList.size() - 1)
	
	def top(self):
		"""
		查看栈顶部元素
		:return:
		"""
		return self.arrayList.get(self.arrayList.size() - 1)
