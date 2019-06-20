from com.jqc.stack.stack import Stack
from com.jqc.queue.queue import Queue
from typing import TypeVar, List

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
	
	def is_left_child(self) -> bool:
		"""
		判断是否是左子节点
		:return:
		"""
		# 妈蛋 搞了半天这写错了 打断点调了半天才发现 草...
		# return self.parent is not None and self == self.left
		return self.parent is not None and self == self.parent.left
	
	def is_right_child(self) -> bool:
		"""
		判断是否是右子节点
		:return:
		"""
		return self.parent is not None and self == self.parent.right
	
	def sibling(self):
		"""
		返回兄弟节点
		:return:
		"""
		if self.is_left_child():
			return self.parent.right
		if self.is_right_child():
			return self.parent.left
		return None


class BinaryTree(object):
	
	def __init__(self):
		self._size = 0
		self._root = None
	
	def size(self) -> int:
		"""
		返回二叉树长度
		:return:
		"""
		return self._size
	
	def is_empty(self) -> bool:
		"""
		判断二叉树是否为空
		:return:
		"""
		return self._size == 0
	
	def clear(self) -> None:
		"""
		清空
		:return:
		"""
		self._size = 0
		self._root = None
	
	def preorder(self):
		"""
		前序 采用递归来实现
		:return:
		"""
		if self._root is None:
			return
		container = []
		self.__preorder_recursion(self._root, container)
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
		if self._root is None:
			return
		container = []
		self.__inorder_recursion(self._root, container)
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
		if self._root is None:
			return
		container = []
		self.__postorder_recursion(self._root, container)
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
		if self._root is None:
			return []
		
		container = []
		stack = Stack()
		stack.push(self._root)
		
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
		if self._root is None:
			return
		
		container = []
		stack = Stack()
		curr = self._root
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
		if self._root is None:
			return
		
		container = []
		stack = Stack()
		stack.push(self._root)
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
		if self._root is None:
			return
		container = []
		queue = Queue()
		queue.en_queue(self._root)
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
		if self._root is None:
			return False
		
		queue = Queue()
		queue.en_queue(self._root)
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
		if self._root is None:
			return 0
		level_size = 1
		tree_height = 0
		queue = Queue()
		queue.en_queue(self._root)
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
