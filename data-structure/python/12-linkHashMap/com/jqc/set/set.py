import abc


class BaseSet(metaclass=abc.ABCMeta):
	@abc.abstractmethod
	def size(self) -> int:
		pass
	
	@abc.abstractmethod
	def is_empty(self) -> bool:
		pass
	
	@abc.abstractmethod
	def is_contains(self) -> bool:
		pass
	
	@abc.abstractmethod
	def add(self, element):
		pass
	
	@abc.abstractmethod
	def remove(self, element):
		pass
	
	@abc.abstractmethod
	def traversal(self):
		pass
