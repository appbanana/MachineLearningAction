from com.jqc.binaryTree.avlTree import AVLTree


def test():

	pass


if __name__ == '__main__':
	
	# def is_left_child(self) -> bool::
	# 	"""
	# 	# 妈蛋 搞了半天这写错了 打断点调了半天才发现 草...
	# 	# return self.parent is not None and self == self.left
	
	# test_array = [5, 41, 81, 86, 55, 10, 28, 19, 79, 12, 3, 21]
	test_array = [43, 21, 34, 81, 32, 46, 99, 69, 80, 67, 47]
	avl_Tree = AVLTree()
	for item in test_array:
		avl_Tree.add(item)
	# print(avl_Tree)
	# 层序遍历 结合MJ老师的这个网站来验证是否正确 参考网址：http://520it.com/binarytrees/
	# 第一组测试数据
	# [41, 10, 81, 5, 19, 55, 86, 3, 12, 28, 79, 21]
	# print(avl_Tree.level_order_tranversal())

	# 第二组数据 测试结果
	# [46, 34, 69, 21, 43, 67, 81, 32, 47, 80, 99]
	# print(avl_Tree.level_order_tranversal())
	
	# [47, 34, 69, 21, 43, 67, 81, 32, 80, 99]
	# avl_Tree.remove(46)
	# print(avl_Tree.level_order_tranversal())
	
	# [46, 34, 80, 21, 43, 67, 81, 32, 47, 99]
	# avl_Tree.remove(69)
	# print(avl_Tree.level_order_tranversal())
	
	# [46, 34, 69, 21, 43, 67, 81, 32, 47, 80]
	avl_Tree.remove(99)
	print(avl_Tree.level_order_tranversal())
