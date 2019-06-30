from .binaryTree import Node
from .bbst import BBST
from enum import Enum
from com.jqc.queue.queue import Queue


class Color(Enum):
	RED = 0
	BLACK = 1


class RBNode(Node):
	def __init__(self, element, parent):
		"""
		自定义初始化
		:param element: 元素
		:param parent: 父节点
		"""
		super().__init__(element, parent)
		self.color = Color.RED
	
	def __str__(self):
		string = ''
		if self.color == Color.RED:
			string = 'R_'
		return string + str(self.element)


class RBTree(BBST):
	def __str__(self):
		string = ''
		queue = Queue()
		queue.en_queue(self._root)
		level_size = 1
		while not queue.is_empty():
			node = queue.de_queue()
			string += str(node)
			level_size -= 1
			string += ','
			if node.left is not None:
				queue.en_queue(node.left)
			if node.right is not None:
				queue.en_queue(node.right)
			if level_size == 0:
				level_size = queue.size()
				string += '\n'
		return string
	
	def create_node(self, element, parent) -> Node:
		"""
		重写父类方法，返回RBNode类型的
		:param element:
		:param parent:
		:return:
		"""
		return RBNode(element, parent)
	
	def after_add(self, node: RBNode) -> None:
		"""
		添加节点之后，修复红黑树的性质
		:param node:
		:return:
		"""
		parent = node.parent
		
		if parent is None:
			# node 是根节点，直接染黑
			self.__black(node)
			return
		
		if self.__is_black(parent):
			# 如果添加节点的父节点是黑色 不做任何处理
			return
		
		# 能走到这里，父节点是红色的
		# 获取添加节点的叔父节点和爷爷节点
		uncle = parent.sibling()
		grand = parent.parent
		
		if self.__is_red(uncle):
			# 叔父节点是红色，结合4阶B树，算上添加的节点，就会有4个节点
			# 不满足B树性质：非根节点元素个数 1 <= y <= 3，就会长生上溢
			self.__black(parent)
			self.__black(uncle)
			# 处理上溢
			self.after_add(self.__red(grand))
			return
		
		# 能走到这里， 叔父节点一定是黑色
		if parent.is_left_child():
			# L
			self.__red(grand)
			if node.is_left_child():
				# LL
				# self.__red(grand)
				self.__black(parent)
				# self._rotate_right(grand)
			else:
				# LR
				# self.__red(grand)
				self.__black(node)
				self._rotate_left(parent)
				# self._rotate_right(grand)
			self._rotate_right(grand)
		else:
			# R
			self.__red(grand)
			if node.is_right_child():
				# RR
				# self.__red(grand)
				self.__black(parent)
			# self._rotate_left(grand)
			else:
				# RL
				# self.__red(grand)
				self.__black(node)
				self._rotate_right(parent)
			# self._rotate_left(grand)
			self._rotate_left(grand)
	
	def after_remove(self, node: Node) -> None:
		"""
		删除节点，修复红黑树性质
		:param node:
		:return:
		"""
		# 真正被删除的节点一定是叶子节点
		if self.__is_red(node):
			# 能走到这里有两种情况：1）被删除的是红色叶子节点；2）被删除的是黑色节点但至少有一个红色叶子节点
			self.__black(node)
			return
		
		# 能走到这里 删除的一定是黑色叶子节点（ps：注意黑色节点和黑色叶子节点的区别）
		parent = node.parent
		if parent is None:
			# parent 为空，说明删除的是根节点
			return
		
		# 判断删除的节点是左还是右 不能使用node 这要结合4阶B树来理解 非根节点的子节点个数一定2 <= y <= 4
		is_left = parent.left is None or node.is_left_child()
		# 获取被删除节点的兄弟节点
		sibling = parent.right if is_left else parent.left
		
		if not is_left:
			# 右边节点
			# 删除的节点是右边黑色的叶子节点
			if self.__is_red(sibling):
				# 该删除的节点有红兄弟(红色的兄弟节点)
				self.__black(sibling)
				self.__red(parent)
				# 右旋转 把红红兄弟的黑儿子变成被删除节点的黑兄弟
				self._rotate_right(parent)
				# 旋转完毕 一定要更新被删除节点的兄弟节点 这样被删除的节点就有黑兄弟，就和下面处理黑兄弟的逻辑是一样的
				sibling = parent.left
			
			# 能走到这里，被删除节点的有黑兄弟(sibling是黑兄弟)
			if self.__is_black(sibling.left) and self.__is_black(sibling.right):
				# 黑兄弟的两个子节点都是黑色
				is_parent_black = self.__is_black(parent)
				self.__red(sibling)
				self.__black(parent)
				if is_parent_black:
					# 处理下溢
					self.after_remove(parent)
			
			else:
				# 黑兄弟至少有一个红色的子节点，说明黑兄弟有可以借的元素
				# 上面代码整理成下面的
				if self.__is_black(sibling.left):
					# 黑兄弟左子节点是黑色
					self._rotate_left(sibling)
					sibling = parent.left
				
				# 黑兄弟左子节点是红色
				# 把兄弟节点染色，与父节点同色
				self.__color(sibling, self.__color_of(parent))
				self.__black(parent)
				self.__black(sibling.left)
				self._rotate_right(parent)
		else:
			# 左边节点与右边节点对称
			# 删除的节点是右边黑色的子节点
			if self.__is_red(sibling):
				# 该删除的节点有红色的兄弟节点
				self.__black(sibling)
				self.__red(parent)
				self._rotate_left(parent)
				# 旋转玩 更新兄弟节点
				sibling = parent.right
			
			# 下面处理的是删除节点的兄弟节点是黑色兄弟(sibling是黑兄弟)
			if self.__is_black(sibling.left) and self.__is_black(sibling.right):
				# 黑兄弟的两个节点都是黑色
				is_parent_black = self.__is_black(parent)
				self.__red(sibling)
				self.__black(parent)
				if is_parent_black:
					self.after_remove(parent)
			
			else:
				if self.__is_black(sibling.right):
					self._rotate_right(sibling)
					sibling = parent.right
				
				self.__color(sibling, self.__color_of(parent))
				self.__black(parent)
				self.__black(sibling.right)
				self._rotate_left(parent)
	
	def __red(self, node: Node) -> Node:
		"""
		节点染红
		:param node:
		:return:
		"""
		return self.__color(node, Color.RED)
	
	def __black(self, node: Node) -> Node:
		"""
		节点染黑
		:param node:
		:return:
		"""
		return self.__color(node, Color.BLACK)
	
	@staticmethod
	def __color_of(node: Node) -> Color:
		"""
		返回传入节点的颜色
		:param node:
		:return:
		"""
		return Color.BLACK if node is None else node.color
	
	@staticmethod
	def __color(node: Node, color: Color) -> Node:
		if node is None:
			return None
		node.color = color
		return node
	
	def __is_black(self, node: Node) -> bool:
		"""
		判断节点是否是黑色
		:param node:
		:return:
		"""
		return self.__color_of(node) == Color.BLACK
	
	def __is_red(self, node: Node) -> bool:
		"""
		判断节点是否是红色
		:param node:
		:return:
		"""
		return self.__color_of(node) == Color.RED
