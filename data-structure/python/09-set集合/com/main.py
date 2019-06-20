from com.jqc.set.listSet import ListSet
from com.jqc.set.treeSet import TreeSet

def visit(e):
	# print(e)
	return True if e == 10 else False

def test1():
	test_array = [5, 41, 66, 66, 66, 10, 28, 77, 79]
	cus_set = ListSet()
	for item in test_array:
		cus_set.add(item)
	print(cus_set)
	
	print(cus_set.is_contains(88))
	
	print(cus_set.remove(77))
	print(cus_set)
	print('----***----')
	print(cus_set.traversal())
	
	# 遍历到10 停止遍历
	print('----***----')
	print(cus_set.traversal(visit))

def test2():
	test_array = [5, 41, 66, 66, 66, 10, 28, 77, 79]
	cus_set = TreeSet()
	for item in test_array:
		cus_set.add(item)
	# print(cus_set)
	
	# print(cus_set.is_contains(88))
	#
	# print(cus_set.remove(77))
	# print(cus_set)
	
	# [41, 10, 77, 5, 28, 66, 79]
	print(cus_set.traversal())


# 在遍历到10的位置停止遍历
# [41, 10]
# print(cus_set.traversal(visit))




if __name__ == '__main__':
	# 测试ListSet
	test1()
	
	# 测试TreeSet
	# test2()
	

