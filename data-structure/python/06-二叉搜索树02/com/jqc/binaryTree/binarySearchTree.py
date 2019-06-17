"""
二叉搜索树
"""
from com.jqc.stack.stack import Stack
from com.jqc.queue.queue import Queue
from typing import Callable, TypeVar, Generic, List
import operator

T = TypeVar('T')


class Node(object):
	def __init__(self, element, parent) -> None:
		"""
		自定义初始化
		:param element: 元素
		:param parent: 父节点
		"""
		self.element = element
		self.parent = parent
		self.left = None
		self.right = None
	
	def __str__(self):
		parent_string = 'none'
		if self.parent is not None:
			parent_string = str(self.parent.element)
		return str(self.element) + '_p(' + parent_string + ')'
	
	def is_leaf(self) -> bool:
		"""
		判断是否是叶子节点
		:return:
		"""
		return self.left is None and self.right is None
	
	def has_two_children(self) -> bool:
		"""
		判断是否是度为2的节点
		:return:
		"""
		return self.left is not None and self.right is not None


class BinarySearchTree(object):
	
	def __init__(self, comparator=None):
		self.__size = 0
		self.__root = None
		self.__comparator = comparator
	
	def __str__(self):
		"""
		自定义输出函数 中序遍历输出
		:return:
		"""
		self.inorder()
		container = []
		self.__to_string(self.__root, container, '')
		string = ''
		for item in container:
			string += item
		return string

	def __to_string(self, node: Node, container: list, prefix: str):
		"""
		中序遍历输出
		"""
		if node is None:
			return
		self.__to_string(node.left, container, prefix + 'L---')
		container.append(prefix)
		container.append(str(node.element))
		container.append('\n')
		self.__to_string(node.right, container, prefix + 'R---')
	
	# def __str__(self):
	# 	string = ''
	# 	if self.__root is None:
	# 		return ''
	# 	level_size = 1
	# 	queue = Queue()
	# 	self.__root.blank_num = 20
	# 	queue.en_queue(self.__root)
	# 	# parent_blank_num = 20
	# 	prefix = ' '
	# 	# child_num = 0
	# 	while not queue.is_empty():
	# 		node = queue.de_queue()
	# 		# node.blank_num = parent_blank_num
	# 		string += prefix * node.blank_num
	# 		string += str(node.element)
	#
	# 		level_size -= 1
	# 		if node.left is not None:
	# 			queue.en_queue(node.left)
	# 			node.bank_num = node.blank_num - 1
	#
	# 		if node.right is not None:
	# 			queue.en_queue(node.right)
	# 			node.bank_num = node.blank_num + 1
	#
	# 		if level_size == 0:
	# 			level_size = queue.size()
	# 			string += '\n'
	#
	# 	return string

	def size(self) -> int:
		"""
		返回二叉树长度
		:return:
		"""
		return self.__size
	
	def is_empty(self) -> bool:
		"""
		判断二叉树是否为空
		:return:
		"""
		return self.__size == 0
	
	def clear(self) -> None:
		"""
		清空
		:return:
		"""
		self.__size = 0
		self.__root = None
	
	def contains(self, element) -> bool:
		"""
		是否包含某个元素
		:param element:
		:return:
		"""
		return self.__node(element) is not None

	
	def add(self, element) -> None:
		"""
		添加元素
		:param element:
		:return:
		"""
		self.__element_not_none_check(element)
		# 添加第一个节点 第一个节点即为根节点
		if self.__root is None:
			self.__root = Node(element, None)
			self.__size += 1
			return
		
		# 不是第一个节点
		node = self.__root
		while node is not None:
			# 暂时保存上一个节点 上一个节点即为下一个的父节点 下面会用到
			parent = node
			# 记录比较的大小
			# cmp = element - node.element
			cmp = self.__compare(element, node.element)
			if cmp > 0:
				# 大于 往右子树找
				node = node.right
			elif cmp < 0:
				# 小于0 往左子树找
				node = node.left
			else:
				return
		new_node = Node(element, parent)
		
		if cmp > 0:
			parent.right = new_node
		else:
			parent.left = new_node
		self.__size += 1
	
	def remove(self, element) -> T:
		"""
		删除元素对应的节点
		:param element:
		:return:
		"""
		return self.__remove(self.__node(element))

		
	def __remove(self, node: Node):
		"""
		删除节点
		:param node:
		:return:
		"""
		if node is None:
			return
		
		old_val = node.element
		
		# 度为2的节点直接删除它的前驱或者后继
		# 在这里我们删除的是后继节点
		if node.has_two_children():
			# 找到后继节点
			s = self.successor(node)
			# 将后继节点的值赋值给node的element
			node.element = s.element
			# 接下来让node指向s(后继节点)
			node = s
		
		# 下面删除就是度为0或者度为1的节点, 删除度为1的节点 直接让其子节点取代, 删除度为0的指点，直接删除即可
		replace_node = node.left if node.left else node.right
		if replace_node is not None:
			# 删除度为1的节点
			replace_node.parent = node.parent
			if node.parent is None:
				# 删除的是度为1的根节点
				self.__root = replace_node
			elif node == node.parent.left:
				node.parent.left = replace_node
			else:
				node.parent.right = replace_node
			
		elif node.parent is None:
			# 删除的是度为0的根节点
			self.__root = None
		else:
			# 删除度为0的节点
			if node == node.parent.left:
				node.parent.left = None
			else:
				node.parent.right = None
			
		return old_val
	
	def preorder(self):
		"""
		前序 采用递归来实现
		:return:
		"""
		if self.__root is None:
			return
		container = []
		self.__preorder_recursion(self.__root, container)
		return container
	
	def __preorder_recursion(self, node: Node, array: list):
		"""
		递归实现前序遍历
		:param node:
		:param array:
		:return:
		"""
		if node is None:
			return
		array.append(node.element)
		self.__preorder_recursion(node.left, array)
		self.__preorder_recursion(node.right, array)
	
	def inorder(self):
		"""
		中序递归实现
		:return:
		"""
		if self.__root is None:
			return
		container = []
		self.__inorder_recursion(self.__root, container)
		return container
	
	def __inorder_recursion(self, node: Node, array: list):
		if node is None:
			return
		self.__inorder_recursion(node.left, array)
		array.append(node.element)
		self.__inorder_recursion(node.right, array)
	
	def postorder(self):
		"""
		后序递归实现
		:return:
		"""
		if self.__root is None:
			return
		container = []
		self.__postorder_recursion(self.__root, container)
		return container
	
	def __postorder_recursion(self, node: Node, array: list):
		if node is None:
			return
		self.__postorder_recursion(node.left, array)
		self.__postorder_recursion(node.right, array)
		array.append(node.element)
	
	# def preorder_traversal(self, cmp=None) -> List[T]:
	def preorder_traversal(self) -> List[T]:
		"""
		前序
		:return:
		"""
		if self.__root is None:
			return []
		
		container = []
		stack = Stack()
		stack.push(self.__root)
		
		while not stack.is_empty():
			node = stack.pop()
			container.append(node.element)
			# if cmp(node.element): break
			if node.right is not None:
				stack.push(node.right)
			if node.left is not None:
				stack.push(node.left)
		return container
	
	def inorder_traversal(self) -> List[T]:
		"""
		中序遍历
		:return:
		"""
		if self.__root is None:
			return
		
		container = []
		stack = Stack()
		curr = self.__root
		while curr or not stack.is_empty():
			if curr is not None:
				stack.push(curr)
				curr = curr.left
			else:
				node = stack.pop()
				container.append(node.element)
				curr = node.right
		return container
	
	def postorder_traversal(self) -> List[T]:
		"""
		后序遍历
		:return:
		"""
		if self.__root is None:
			return
		
		container = []
		stack = Stack()
		stack.push(self.__root)
		prev = None
		while not stack.is_empty():
			# 取出栈最顶端的元素
			node = stack.top()
			if node.is_leaf() or (prev and prev.parent == node):
				prev = stack.pop()
				container.append(prev.element)
			else:
				if node.right is not None:
					stack.push(node.right)
				if node.left is not None:
					stack.push(node.left)
		return container
	
	def level_order_tranversal(self) -> List[T]:
		"""
		层序遍历
		:return:
		"""
		if self.__root is None:
			return
		container = []
		queue = Queue()
		queue.en_queue(self.__root)
		# 如果队列不为空 进入循环
		while not queue.is_empty():
			node = queue.de_queue()
			container.append(node.element)
			if node.left is not None:
				queue.en_queue(node.left)
			if node.right is not None:
				queue.en_queue(node.right)
		
		return container
	
	def is_complete(self) -> bool:
		"""
		是否是完全二叉树
		:return:
		"""
		if self.__root is None:
			return False
		
		queue = Queue()
		queue.en_queue(self.__root)
		is_leaf = False
		while not queue.is_empty():
			node = queue.de_queue()
			if is_leaf and not node.is_leaf():
				return False
			
			if node.left is not None:
				# 左子树不为空 入队
				queue.en_queue(node.left)
			elif node.right is not None:
				# 能走到这里 说左子树为空，右子树不为空， 则不是完全二叉树
				return False
			
			if node.right is not None:
				# 如果右子树不为空，入队
				queue.en_queue(node.right)
			else:
				# 如果右子树为空，则后面的节点必须都是叶子节点
				is_leaf = True
		
		return True
	
	def height(self) -> int:
		"""
		计算树的高度
		:return: 树的高度
		"""
		if self.__root is None:
			return 0
		level_size = 1
		tree_height = 0
		queue = Queue()
		queue.en_queue(self.__root)
		while not queue.is_empty():
			node = queue.de_queue()
			level_size -= 1
			if node.left is not None:
				queue.en_queue(node.left)
			
			if node.right is not None:
				queue.en_queue(node.right)
			
			if level_size == 0:
				level_size = queue.size()
				tree_height += 1
		return tree_height
	
	@staticmethod
	def predecessor(node: Node):
		"""
		寻找前驱节点
		:return:
		"""
		if node is None:
			return None
		node = node.left
		# 左子节点存在 一路向右寻找
		if node:
			while node.right is not None:
				node = node.right
			return node
		
		# 左子树为空 从他的祖先节点找前驱节点
		while node.parent is not None and node == node.parent.left:
			node = node.parent
		return node.parent
	
	@staticmethod
	def successor(node: Node):
		"""
		寻找前驱节点
		:return:
		"""
		if node is None:
			return None
		node = node.right
		# 右子节点存在 一路向左寻找
		if node:
			while node.left is not None:
				node = node.left
			return node
		
		# 左子树为空 从他的祖先节点找前驱节点
		while node.parent is not None and node == node.parent.right:
			node = node.parent
		return node.parent
	
	@staticmethod
	def __element_not_none_check(element):
		"""
		校验传入的元素
		:param element:
		:return:
		"""
		if element is None:
			raise NameError('element 不能为None')
	
	def __compare(self, e1, e2):
		"""
		比较函数 如果外界有传自定义的比较函数，就使用自定义比较函数，如果没有传就使用系统自带的比较函数
		在这里我使用的是减法，为正前者大，为负，后者大。(ps:python3中没有cmp比较函数)
		:param e1:
		:param e2:
		:return:
		"""
		if self.__comparator is not None:
			#
			return self.__comparator(e1, e2)
		# python3 中取消cmp比较函数，python3中使用operator代替，operator中有很多比较函数，可以参考
		# 个人认为这里可以直接写成e1 - e2
		return operator.sub(e1, e2)
	
	def __node(self, element):
		"""
		根据传的的元素 获取对应node 节点
		:param element:
		:return:
		"""
		self.__element_not_none_check(element)
		node = self.__root
		while node is not None:
			cmp = self.__compare(element, node.element)
			if cmp == 0:
				return node
			if cmp > 0:
				node = node.right
			else:
				node = node.left
		return node
