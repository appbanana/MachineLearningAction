# 利用abc模块实现抽象类
import abc
from typing import TypeVar

T = TypeVar('T')


class Visitor(object):
	def __init__(self, visitor):
		"""
		visitor 为lambda函数
		def test(key, value):
			print(key, value)
			return True if e == 10 else False

		:param visitor: lambda函数， 类似于上面形式的
		"""
		
		self.is_stop = False
		self.__visitor = visitor
	
	def visit(self, key, value) -> bool:
		return self.__visitor(key, value)
	

class BaseMap(metaclass=abc.ABCMeta):
	@abc.abstractmethod
	def size(self) -> int:
		"""
		返回map的长度
		:return:
		"""
		pass
	
	@abc.abstractmethod
	def is_empty(self) -> bool:
		"""
		判断map是否为空
		:return:
		"""
		pass
	
	@abc.abstractmethod
	def clear(self):
		"""
		判断map是否为空
		:return:
		"""
		pass
	
	@abc.abstractmethod
	def put(self, key, value) -> T:
		"""
		添加成功返回添加的value
		添加key：value到map中
		:param key: 键
		:param value: 值
		"""
		pass
	
	@abc.abstractmethod
	def remove(self, key) -> T:
		"""
		根据key返回对应的value
		:param key: 键
		:return: 返回值
		"""
		pass
	
	@abc.abstractmethod
	def get(self, key) -> T:
		"""
		根据key返回对应的value
		:param key: 键
		:return: 返回值
		"""
		pass
	
	@abc.abstractmethod
	def contains_key(self, key) -> bool:
		"""
		是否包含某个key
		:param key:
		:return:
		"""
		pass
	
	@abc.abstractmethod
	def contains_value(self,  value) -> bool:
		"""
		是否包含某个value
		:return:
		"""
		pass
	
	@abc.abstractmethod
	def traversal(self, visitor: Visitor):
		"""
		遍历
		def visit(key，value):
			print(key, value)
			return True if key == 10 else False
		:param visitor: lambda函数， 类似于上面形式的
		:return:
		"""
		pass
