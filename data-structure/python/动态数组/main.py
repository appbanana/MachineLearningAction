# import list.dynamicArray
from list.dynamicArray import DynamicArray


if __name__ == '__main__':
	# array = list.dynamicArray.DynamicArray()
	array = DynamicArray()
	for i in range(20):
		array.add(i)
	
	print(array)
	print(array.size())
	# array.clear()
	print('*****' * 10)
	# print(array)
# 	# print(array.remove(0))
	print(array.remove(0))
	print(array.remove(array.size()-1))
	print('****' * 10)
	print(array.set(0, 66))
	print(array)
	print('****' * 10)
	print(array.get(1))

	

	
