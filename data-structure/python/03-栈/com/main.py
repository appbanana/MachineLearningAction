
from com.jqc.stack.stack import Stack


if __name__ == '__main__':
	# test1()
	# test2()
	# test3()
	stack = Stack()
	stack.push(3)
	stack.push(6)
	stack.push(9)
	stack.push(12)
	# 12,9,6,3,
	print(stack)
	# 12
	print(stack.pop())
	# 9,6,3,
	print(stack)
	# 9
	print(stack.top())

	
