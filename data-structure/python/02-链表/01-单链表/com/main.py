from com.jqc.link.linkList import LinkList

if __name__ == '__main__':
	# test_arr = [1, 2, 3, 6, 5, 4, 9, 8, 7]
	test_arr = [1, 2, 3, 6, 5, 4, None, 8, 7]
	link = LinkList()
	for item in test_arr:
		link.add(item)
	# print(len(test_arr))
	# print(link.size())
	# print(link)
	# print(link.remove(0))
	# print(link)
	# print(link.remove(3))
	# print(link)
	# print(link.remove(link.size()-1))
	print(link)
	print(link.index_of(None))
	print(link.contains(None))
	print(link.set(3, 66))
	print(link)
# print(link.remove(link.size() - 1))
