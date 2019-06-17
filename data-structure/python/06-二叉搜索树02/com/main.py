# import typing
from com.jqc.binaryTree.binarySearchTree import BinarySearchTree
from com.jqc.binaryTree.person import Person
from com.jqc.binaryTree.binarySearchTree import Node


# 测试闭包
# def comparator():
# 	def compare(e1, e2):
# 		return e2 - e1
#
# 	return compare


def test1():
	"""
	测试递归和非递归 前，中，后序遍历
	:return:
	"""
	# 递归来实现
	# 前序遍历
	# [5, 3, 41, 10, 28, 19, 12, 21, 81, 55, 79, 86]
	print(bst.preorder())
	print('*' * 30)
	
	# 中序遍历
	# [3, 5, 10, 12, 19, 21, 28, 41, 55, 79, 81, 86]
	print(bst.inorder())
	print('*' * 30)
	
	# 后序遍历
	# [3, 12, 21, 19, 28, 10, 79, 55, 86, 81, 41, 5]
	print(bst.postorder())
	print('*' * 30)
	
	# 二叉树 非递归实现
	# 前序遍历
	# [5, 3, 41, 10, 28, 19, 12, 21, 81, 55, 79, 86]
	print(bst.preorder_traversal())
	print('*' * 30)
	
	# 中序遍历
	# [3, 5, 10, 12, 19, 21, 28, 41, 55, 79, 81, 86]
	print(bst.inorder_traversal())
	print('*' * 30)
	
	# 后序遍历
	# [3, 12, 21, 19, 28, 10, 79, 55, 86, 81, 41, 5]
	print(bst.postorder_traversal())
	print('*' * 30)
	
	# 层序遍历
	# [5, 3, 41, 10, 81, 28, 55, 86, 19, 79, 12, 21]
	print(bst.level_order_tranversal())


def test2():
	test_array = [5, 41, 81, 86, 55, 10, 28, 19, 79, 12, 3, 21]
	bst = BinarySearchTree()
	for item in test_array:
		bst.add(item)
	
	"""
	L---3
	5
	R---L---10
	R---L---R---L---L---12
	R---L---R---L---19
	R---L---R---L---R---21
	R---L---R---28
	R---41
	R---R---L---55
	R---R---L---R---79
	R---R---81
	R---R---R---86
	"""
	print(bst)
	# 测试递归和非递归 前，中，后序遍历
	# test1()
	print(bst.is_complete())
	# 6 见图片 img/01-二叉搜索树.png
	print(bst.height())


def test3():
	# 自定义比较函数
	def compare(e1, e2):
		return e2 - e1
	
	test_array = [5, 41, 81, 86, 55, 10, 28, 19, 79, 12, 3, 21]
	bst = BinarySearchTree(compare)
	# 这还可以使用lambda匿名函数
	# bst = BinarySearchTree(lambda e1, e2: e2 - e1)
	for item in test_array:
		bst.add(item)
	print(bst)
	print(bst.level_order_tranversal())


def test4():
	# 测试自定义类 使用匿名函数
	bst = BinarySearchTree(lambda p1, p2: p2.age - p1.age)
	person1 = Person('abc', 18)
	bst.add(person1)
	
	person2 = Person('abc', 6)
	bst.add(person2)
	
	person3 = Person('abc', 25)
	bst.add(person3)
	
	person4 = Person('abc', 30)
	bst.add(person4)
	
	person5 = Person('abc', 66)
	bst.add(person5)
	
	print(bst)


if __name__ == '__main__':
	# test1()
	# test2()
	# 测试自定义比较函数
	# test3()
	
	# 测试自定义类 使用匿名函数
	# test4()
	
	test_array = [5, 41, 81, 86, 55, 10, 28, 19, 79, 12, 3, 21]
	bst = BinarySearchTree()
	for item in test_array:
		bst.add(item)
	print(bst)
	# [5, 3, 41, 10, 81, 28, 55, 86, 19, 79, 12, 21]
	print(bst.level_order_tranversal())
	print('****' * 10)
	# # 删除叶子节点
	# bst.remove(21)
	# # [5, 3, 41, 10, 81, 28, 55, 86, 19, 79, 12]
	# print(bst.level_order_tranversal())

	# 删除度为1的节点
	# bst.remove(10)
# 	# # [5, 3, 41, 28, 81, 19, 55, 86, 12, 21, 79]
# 	# print(bst.level_order_tranversal())

	# 删除度为2的节点
	# bst.remove(41)
	# # [5, 3, 55, 10, 81, 28, 79, 86, 19, 12, 21]
	# print(bst.level_order_tranversal())
	
	# 删除根节点
	bst.remove(5)
	# [10, 3, 41, 28, 81, 19, 55, 86, 12, 21, 79]
	print(bst.level_order_tranversal())
