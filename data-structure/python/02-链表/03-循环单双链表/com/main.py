from com.jqc.linkList.doubleLinkList import LinkList
from com.jqc.circleLink.singleCircleLinkList import SingleLinkList
from com.jqc.circleLink.doubleCircleLinkList import DoubleCircleLinkList


def test1():
	"""
	测试双链表
	"""
	double_list = LinkList()
	for item in range(1, 9):
		double_list.add(item)
	# size=8, [None_1_2,1_2_3,2_3_4,3_4_5,4_5_6,5_6_7,6_7_8,7_8_None]
	print(double_list)
	
	# 在首，中间，尾部测试插入
	print(double_list.insert(0, -1))
	# size=9, [None_-1_1,-1_1_2,1_2_3,2_3_4,3_4_5,4_5_6,5_6_7,6_7_8,7_8_None]
	print(double_list)
	
	print(double_list.insert(9, 9))
	# size=10, [None_-1_1,-1_1_2,1_2_3,2_3_4,3_4_5,4_5_6,5_6_7,6_7_8,7_8_9,8_9_None]
	print(double_list)
	
	print(double_list.insert(2, 66))
	# size=11, [None_-1_1,-1_1_66,1_66_2,66_2_3,2_3_4,3_4_5,4_5_6,5_6_7,6_7_8,7_8_9,8_9_None]
	print(double_list)
	
	# 测试更新
	print(double_list.set(2, 88))
	# size=11, [None_-1_1,-1_1_88,1_88_2,88_2_3,2_3_4,3_4_5,4_5_6,5_6_7,6_7_8,7_8_9,8_9_None]
	print(double_list)
	
	# 删除首节点
	# -1
	print(double_list.remove(0))
	# size=10, [None_1_88,1_88_2,88_2_3,2_3_4,3_4_5,4_5_6,5_6_7,6_7_8,7_8_9,8_9_None]
	print(double_list)
	
	# 删除尾节点
	# 9
	print(double_list.remove(double_list.size() - 1))
	# size=9, [None_1_88,1_88_2,88_2_3,2_3_4,3_4_5,4_5_6,5_6_7,6_7_8,7_8_None]
	print(double_list)
	
	# 删除中间节点
	# 2
	print(double_list.remove(2))
	# size=8, [None_1_88,1_88_3,88_3_4,3_4_5,4_5_6,5_6_7,6_7_8,7_8_None]
	print(double_list)


def test2():
	"""
	测试单循环链表
	"""
	single_list = SingleLinkList()
	for item in range(1, 9):
		single_list.add(item)
	# size=8, [1_2,2_3,3_4,4_5,5_6,6_7,7_8,8_1]
	print(single_list)
	
	# 在循环单链表首部 中间 尾部插入元素测试
	print(single_list.insert(0, 6))
	# size=9, [6_1,1_2,2_3,3_4,4_5,5_6,6_7,7_8,8_6]
	print(single_list)
	
	print(single_list.insert(2, 66))
	# size=10, [6_1,1_66,66_2,2_3,3_4,4_5,5_6,6_7,7_8,8_6]
	print(single_list)
	
	print(single_list.insert(single_list.size(), 88))
	# size=9, [6_1,1_2,2_3,3_4,4_5,5_6,6_7,7_8,8_6]
	print(single_list)
	
	# 在循环列表的首部， 中间，尾部删除测试'
	print(single_list.remove(0))
	# size=10, [1_66,66_2,2_3,3_4,4_5,5_6,6_7,7_8,8_88,88_1]
	print(single_list)
	
	print(single_list.remove(2))
	# size=9, [1_66,66_3,3_4,4_5,5_6,6_7,7_8,8_88,88_1]
	print(single_list)
	
	print(single_list.remove(single_list.size() - 1))
	# size=8, [1_66,66_3,3_4,4_5,5_6,6_7,7_8,8_1]
	print(single_list)


if __name__ == '__main__':
	# test1()
	# test2()
	double_list = DoubleCircleLinkList()
	# size=1, [0_0_0]
	double_list.add(0)
	print(double_list)
	for item in range(1, 9):
		double_list.add(item)
	# size=9, [8_0_1,0_1_2,1_2_3,2_3_4,3_4_5,4_5_6,5_6_7,6_7_8,7_8_0]
	print(double_list)
	
	# 在循环单链表首部 中间 尾部插入元素测试
	print(double_list.insert(0, 6))
	# size=10, [8_6_0,6_0_1,0_1_2,1_2_3,2_3_4,3_4_5,4_5_6,5_6_7,6_7_8,7_8_6]
	print(double_list)

	print(double_list.insert(2, 66))
	# size=11, [8_6_0,6_0_66,0_66_1,66_1_2,1_2_3,2_3_4,3_4_5,4_5_6,5_6_7,6_7_8,7_8_6]
	print(double_list)

	print(double_list.insert(double_list.size(), 88))
	# size=12, [88_6_0,6_0_66,0_66_1,66_1_2,1_2_3,2_3_4,3_4_5,4_5_6,5_6_7,6_7_8,7_8_88,8_88_6]
	print(double_list)
	
	# 在循环列表的首部， 中间，尾部删除测试'
	print(double_list.remove(0))
	# size=11, [88_0_66,0_66_1,66_1_2,1_2_3,2_3_4,3_4_5,4_5_6,5_6_7,6_7_8,7_8_88,8_88_0]
	print(double_list)
	
	print(double_list.remove(2))
	# size=10, [88_0_66,0_66_2,66_2_3,2_3_4,3_4_5,4_5_6,5_6_7,6_7_8,7_8_88,8_88_0]
	print(double_list)

	print(double_list.remove(double_list.size() - 1))
	# size=9, [8_0_66,0_66_2,66_2_3,2_3_4,3_4_5,4_5_6,5_6_7,6_7_8,7_8_0]
	print(double_list)
