import typing  # 需求导入这个库

# 生成复合类型, 这段代码请无视
FloatVector = typing.List[float]
StrList = typing.List[str]
MyT = typing.TypeVar('T')


class Person:
	def __init__(self, name, age):
		self._name = name
		self._age = age
	
	def get_name(self):
		return self._name
	
	def get_age(self):
		return self._age


class Py3TypehintTester:
	def test1(self, a: str, b: str, c: str) -> list:
		"""第一种需求

		很简单, 形式比较简洁

		:param a:
		:param b:
		:param c:
		:return:
		"""
		return [a, b, c]
	
	def test2(self, a: typing.List[str],
	          b: typing.List[str],
	          c: typing.Dict[str, int]) -> typing.Dict[str, str]:
		"""第二种需求

		比较简单, 需要先了解 typing 这个库

		:param a:
		:param b:
		:param c:
		:return:
		"""
		
		return {
			'str': 'str1'
		}
	
	def test3(self, p: Person):
		"""第三种需求

		比较简单

		:param p:
		:return:
		"""
		
		print(p.get_age())
	
	def test4(self, callback: typing.Callable[[str, int], str]):
		"""第四种需求

		稍复杂, 需要先仔细阅读下代码
		不过这种需求基本出现的频率不多, 倒也不影响大局

		:param callback:
		:return:
		"""
		
		s = 's'
		i = 1
		result = callback(s, i)
		print(result)  # 能推导为str
