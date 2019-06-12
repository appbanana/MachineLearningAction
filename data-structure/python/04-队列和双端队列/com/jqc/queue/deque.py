from com.jqc.linkList.doubleLinkList import LinkList

"""
使用双链表来实现双端队列
"""


class Deque(object):
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
	
	def is_empty(self) -> bool:
		"""
		返回队列是否为空
		:return: bool
		"""
		return self.linkList.is_empty()
	
	def en_queue_front(self, element):
		"""
		从队头入队列
		:param element: 元素
		:return:
		"""
		self.linkList.insert(0, element)
	
	def en_queue_rear(self, element):
		"""
		从队尾入队列
		:param element: 元素
		:return:
		"""
		self.linkList.add(element)
	
	def de_queue_front(self):
		"""
		从队头出队列
		:return:
		"""
		return self.linkList.remove(0)
	
	def de_queue_rear(self):
		"""
		从队尾出队列
		:return:
		"""
		return self.linkList.remove(self.size() - 1)
	
	def front(self):
		"""
		查看队列头部元素
		:return:
		"""
		return self.linkList.get(0)
	
	def rear(self):
		"""
		查看队列尾部元素
		:return:
		"""
		return self.linkList.get(self.size() - 1)
