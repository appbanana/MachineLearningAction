from com.jqc.stack.stack import Stack
from com.jqc.queue.queue import Queue


def test1():
	"""
	测试栈
	:return:
	"""
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


def test2():
	"""
	测试队列
	:return:
	"""
	queue = Queue()
	queue.en_queue(3)
	queue.en_queue(6)
	queue.en_queue(9)
	queue.en_queue(12)
	# 3,6,9,12,
	print(queue)
	# 3
	print(queue.de_queue())
	# 6,9,12,
	print(queue)
	# 6
	print(queue.front())


if __name__ == '__main__':
	# test1()
	test2()
