from com.jqc.linkList.doubleLinkList import LinkList

"""
使用双链表来实现队列
"""


class Queue(object):
	def __init__(self):
		self.linkList = LinkList()
	
	def __str__(self):
		string = ''
		for i in range(0, self.linkList.size()):
			string += str(self.linkList.get(i))
			string += ','
		
		return string
	
	def size(self) -> int:
		"""
		返回队列的长度
		:return:
		"""
		return self.linkList.size()
	
	def clear(self):
		"""
		清空
		:return:
		"""
		self.linkList.clear()
	
	def is_empty(self) -> bool:
		"""
		返回队列是否为空
		:return: bool
		"""
		return self.linkList.is_empty()
	
	def en_queue(self, element):
		"""
		入队列
		:param element: 元素
		:return:
		"""
		self.linkList.add(element)
	
	def de_queue(self):
		"""
		出队列
		:return:
		"""
		return self.linkList.remove(0)
	
	def front(self):
		"""
		查看队列头部元素
		:return:
		"""
		return self.linkList.get(0)
