from com.jqc.binaryTree.rbTree import RBTree
import const
def test():
	const.PI = 3.14
	print(const.PI)
	const.PI = 3.1415
	print(const.PI)
	pass


if __name__ == '__main__':
	test_array = [5, 41, 81, 86, 55, 10, 28, 19, 79, 12, 3, 21]
	rbTree = RBTree()
	for item in test_array:
		rbTree.add(item)

	# 自定义输出，使用的是层序遍历
	# 这个要结合MJ老师的这个网站来验证是否正确 参考网址：http://520it.com/binarytrees/
	"""
	41,
	10,81,
	5,R_19,55,86,
	R_3,12,28,R_79,
	R_21,
	"""
	# print(rbTree)
	
	"""
	41,
	10,81,
	5,R_19,55,86,
	R_3,12,28,R_79,
	"""
	# 直接删除红色叶子节点
	# rbTree.remove(21)
	# print(rbTree)
	
	# 删除黑色节点
	"""
	41,
	10,79,
	5,R_19,55,81,
	R_3,12,28,
	R_21,
	"""
	rbTree.remove(86)
	print(rbTree)
	
	# [46, 34, 69, 21, 43, 67, 81, 32, 47, 80]
	# rbTree.remove(99)
	# print(rbTree.level_order_tranversal())
