from com.jqc.linkList.doubleLinkList import LinkList

if __name__ == '__main__':
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
