from .map import BaseMap
from enum import Enum
from typing import TypeVar
import operator
from .map import Visitor
from com.jqc.queue.queue import Queue

T = TypeVar('T')

"""
思路"：使用红黑树来实现，又跟之前实现的红黑树不太一样，这次node直接存放key，value
"""


class Color(Enum):
	RED = 0
	BLACK = 1


class Node(object):
	def __init__(self, key, value, parent) -> None:
		"""
		自定义初始化
		:param key: 键
		:param value: 值
		:param parent: 父节点
		"""
		self.key = key
		self.value = value
		self.parent = parent
		self.color = Color.RED
		self.left = None
		self.right = None
	
	# def __str__(self):
	# 	parent_string = 'none'
	# 	if self.parent is not None:
	# 		parent_string = str(self.parent.element)
	# 	return str(self.element) + '_p(' + parent_string + ')'
	
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


class TreeMap(BaseMap):
	
	def __init__(self, comparator=None):
		self.__size = 0
		self.__root = None
		self.__comparator = comparator
	
	def size(self) -> int:
		return self.__size
	
	def is_empty(self) -> bool:
		return self.__size == 0
	
	def clear(self):
		self.__root = None
		self.__size = 0
	
	def put(self, key, value) -> T:
		"""
		添加key：value
		:param key:
		:param value:
		:return:
		"""
		self.__key_not_none_check(key)
		if self.__root is None:
			# 根节点为空，说明添加的是首节点
			self.__root = Node(key, value, None)
			self.__size += 1
			self.__after_add(self.__root)
			return
		
		node = self.__root
		while node is not None:
			cmp_result = self.__compare(key, node.key)
			# 记录上一次循环中的node
			parent = node
			if cmp_result > 0:
				node = node.right
			elif cmp_result < 0:
				node = node.left
			else:
				# key值一样的话，进行覆盖
				node.key = key
				old_val = node.value
				node.value = value
				return old_val
		
		new_node = Node(key, value, parent)
		# 根据比较结果来决定该node是parent的左子节点还是右子节点
		if cmp_result > 0:
			parent.right = new_node
		else:
			parent.left = new_node
		
		self.__size += 1
		self.__after_add(new_node)
	
	def remove(self, key) -> T:
		"""
		更具key值 删除对应的节点
		:param key:
		:return:
		"""
		node = self.__node(key)
		return self.__remove(node) if node else None
	
	def get(self, key) -> T:
		"""
		更具key值返回value
		:param key:
		:return:
		"""
		node = self.__node(key)
		return node.value if node else None
	
	def contains_key(self, key) -> bool:
		"""
		是否包含某个key
		:param key:
		:return:
		"""
		node = self.__node(key)
		return True if node else False
	
	def contains_value(self, value) -> bool:
		"""
		是否包含某个value
		:return:
		"""
		queue = Queue()
		queue.en_queue(self.__root)
		while not queue.is_empty():
			node = queue.de_queue()
			if node.value == value:
				return True
			if node.left:
				queue.en_queue(node.left)
			if node.right:
				queue.en_queue(node.right)
			
		return False
	
	def __remove(self, node: Node):
		"""
		删除对应的节点
		:param node:
		:return:
		"""
		if node is None:
			return
		
		old_val = node.value
		
		# 度为2的节点直接删除它的前驱或者后继
		# 在这里我们删除的是后继节点
		if node.has_two_children():
			# 找到后继节点
			s = self.__successor(node)
			# 将后继节点的值赋值给node
			node.key = s.key
			node.value = s.value
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
			# 删除之后调整使其满足红黑树性质
			self.__after_remove(replace_node)
		elif node.parent is None:
			# 删除的是度为0的根节点
			self.__root = None
			# 删除之后验证avl树
			self.__after_remove(node)
		else:
			# 删除度为0的节点
			if node == node.parent.left:
				node.parent.left = None
			else:
				node.parent.right = None
			# 删除之后调整使其满足红黑树性质
			self.__after_remove(node)
		return old_val
	
	def traversal(self, visitor: Visitor):
		"""
		遍历
		def test(key，value):
			print(key, value)
			return True if key == 10 else False
		:param visitor: lambda函数， 类似于上面形式的
		:return:
		"""
		assert visitor is not None, "visit不能为空，请传入一个lambda函数"
		self.__inorder_traversal(self.__root, visitor)
	
	def __inorder_traversal(self, node, visitor):
		if node is None or visitor.is_stop:
			return
		self.__inorder_traversal(node.left, visitor)
		if visitor.is_stop:
			return
		visitor.is_stop = visitor.visit(node.key, node.value)
		self.__inorder_traversal(node.right, visitor)
	
	@staticmethod
	def __key_not_none_check(element):
		"""
		校验传入的元素
		:param element:
		:return:
		"""
		if element is None:
			raise NameError('element 不能为None')
	
	def __compare(self, e1, e2):
		"""
		比较函数 如果外界有传自定义的比较函数，就使用自定义比较函数，如果没有传就使用系统自带的operator
		(ps:python3中没有cmp比较函数)
		:param e1:
		:param e2:
		:return:
		"""
		if self.__comparator is not None:
			#
			return self.__comparator(e1, e2)
		# 如果相等返回0 大于返回1 小于返回-1
		return 0 if operator.eq(e1, e2) else (1 if operator.gt(e1, e2) else -1)
	
	def __after_add(self, node: Node):
		"""
		修复红黑树的性质
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
			self.__after_add(self.__red(grand))
			return
		
		# 能走到这里， 叔父节点一定是黑色
		if parent.is_left_child():
			# L
			self.__red(grand)
			if node.is_left_child():
				# LL
				# self.__red(grand)
				self.__black(parent)
			# self.__rotate_right(grand)
			else:
				# LR
				# self.__red(grand)
				self.__black(node)
				self.__rotate_left(parent)
			# self.__rotate_right(grand)
			self.__rotate_right(grand)
		else:
			# R
			self.__red(grand)
			if node.is_right_child():
				# RR
				# self.__red(grand)
				self.__black(parent)
			# self.__rotate_left(grand)
			else:
				# RL
				# self.__red(grand)
				self.__black(node)
				self.__rotate_right(parent)
			# self.__rotate_left(grand)
			self.__rotate_left(grand)
	
	def __after_remove(self, node: Node) -> None:
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
				self.__rotate_right(parent)
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
					self.__after_remove(parent)
			
			else:
				# 黑兄弟至少有一个红色的子节点，说明黑兄弟有可以借的元素
				# 上面代码整理成下面的
				if self.__is_black(sibling.left):
					# 黑兄弟左子节点是黑色
					self.__rotate_left(sibling)
					sibling = parent.left
				
				# 黑兄弟左子节点是红色
				# 把兄弟节点染色，与父节点同色
				self.__color(sibling, self.__color_of(parent))
				self.__black(parent)
				self.__black(sibling.left)
				self.__rotate_right(parent)
		else:
			# 左边节点与右边节点对称
			# 删除的节点是右边黑色的子节点
			if self.__is_red(sibling):
				# 该删除的节点有红色的兄弟节点
				self.__black(sibling)
				self.__red(parent)
				self.__rotate_left(parent)
				# 旋转玩 更新兄弟节点
				sibling = parent.right
			
			# 下面处理的是删除节点的兄弟节点是黑色兄弟(sibling是黑兄弟)
			if self.__is_black(sibling.left) and self.__is_black(sibling.right):
				# 黑兄弟的两个节点都是黑色
				is_parent_black = self.__is_black(parent)
				self.__red(sibling)
				self.__black(parent)
				if is_parent_black:
					self.__after_remove(parent)
			
			else:
				if self.__is_black(sibling.right):
					self.__rotate_right(sibling)
					sibling = parent.right
				
				self.__color(sibling, self.__color_of(parent))
				self.__black(parent)
				self.__black(sibling.right)
				self.__rotate_left(parent)
	
	def __rotate_left(self, grand: Node):
		"""
		左旋转
		:param grand: 要旋转的节点
		:return:
		"""
		parent = grand.right
		child = parent.left
		
		grand.right = child
		parent.left = grand
		
		self.__after_rotate(grand, parent, child)
	
	def __rotate_right(self, grand: Node):
		"""
		右旋选
		:param grand: 要旋转的节点
		:return:
		"""
		parent = grand.left
		child = parent.right
		
		grand.left = child
		parent.right = grand
		
		# 封装后 直接使用这个方法代替下面一坨代码
		self.__after_rotate(grand, parent, child)
	
	def __after_rotate(self, grand: Node, parent: Node, child: Node):
		"""
		左旋，右旋之后的操作
		:param grand: 爷爷节点
		:param parent: 父节点
		:param child: 节点
		:return:
		"""
		# 更新grand，parent，child的父节点
		# 更新parent的父节点
		parent.parent = grand.parent
		
		if grand.is_left_child():
			# grand原来是它父节点的左子节点，就让grand.parent.left指向parent
			grand.parent.left = parent
		elif grand.is_right_child():
			# grand原来是它父节点的右子节点，就让grand.parent.right指向parent
			grand.parent.right = parent
		else:
			# grand既不是左子节点 又不是右子节点 如果grand的父节点是根节点
			self.__root = parent
		
		# 更新child, grand的父节点
		if child is not None:
			child.parent = grand
		grand.parent = parent
	
	def __node(self, key):
		"""
		根据传的的key值 获取对应node 节点
		:param key:
		:return:
		"""
		self.__key_not_none_check(key)
		node = self.__root
		while node is not None:
			cmp = self.__compare(key, node.key)
			if cmp == 0:
				return node
			if cmp > 0:
				node = node.right
			else:
				node = node.left
		return node
	
	@staticmethod
	def __predecessor(node: Node):
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
	def __successor(node: Node):
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
