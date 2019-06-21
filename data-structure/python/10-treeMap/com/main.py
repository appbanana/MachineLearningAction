from com.jqc.map.treeMap import TreeMap
from com.jqc.map.map import Visitor


def visit(key, value):
	print(key, value)
	# return True if key == 'c' else False
	return False


if __name__ == '__main__':
	visitor = Visitor(visit)
	cus_map = TreeMap()
	cus_map.put("c", 2)
	cus_map.put("a", 5)
	cus_map.put("b", 6)
	cus_map.put("a", 8)
	cus_map.put("e", None)
	cus_map.put("f", 8)
	
	# print(cus_map)
	print('-----*****-----')
	cus_map.traversal(visitor)
	
	print('-----*****-----')
	print(cus_map.contains_value(None))
	print(cus_map.get('a'))
	
	print('-----*****-----')
	print(cus_map.remove('a'))
	cus_map.traversal(visitor)
