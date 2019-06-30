import operator
from .hashMap import HashMap, Node
from .map import Visitor

"""
两条线串起来, 一条线是hashmap串起来, 第二条是是使用双链表按照先后顺序串起来
"""


class LinkNode(Node):
    def __init__(self, key, value, parent) -> None:
        super().__init__(key, value, parent)
        self.prev = None
        self.next = None


class LinkHashMap(HashMap):
    def __init__(self):
        super().__init__()
        # LinkHashMap的首尾节点
        self.first = None
        self.last = None
    
    def clear(self):
        super().clear()
        self.first = None
        self.last = None
    
    def contains_value(self, value):
        node = self.first
        while node:
            if operator.eq(node.value, value):
                return True
            node = node.next
        return False
    
    def traversal(self, visitor: Visitor):
        node = self.first
        while node:
            if visitor.visit(node.key, node.value):
                break
            node = node.next
    
    def create_node(self, key, value, parent):
        link_node = LinkNode(key, value, parent)
        if self.first is None:
            # 首结点添加
            self.first = link_node
            self.last = link_node
        else:
            self.last.next = link_node
            link_node.prev = self.last
            self.last = link_node
        
        return link_node
    
    def _after_remove(self, will_node: LinkNode, remove_node: LinkNode):
        #
        # node1 = will_node
        # node2 = remove_node
        if will_node != remove_node:
            # 说明删除的是度为2的节点 此时需要交换这两个节点
            # 交换prev节点
            node1_prev = will_node.prev
            node2_prev = remove_node.prev
            if node1_prev is None:
                self.first = remove_node
            else:
                node1_prev.next = remove_node
            if node2_prev is None:
                self.first = will_node
            else:
                node2_prev.next = will_node
            remove_node.prev = node1_prev
            will_node.prev = node2_prev
            
            # 交换next
            node1_next = will_node.next
            node2_next = remove_node.next
            # 交换next的prev
            if node1_next is None:
                self.last = remove_node
            else:
                node1_next.prev = remove_node
            if node2_next is None:
                self.last = will_node
            else:
                node2_next.prev = will_node

            will_node.next = node2_next
            remove_node.next = node1_next
            
        
        # 删除节点的前后节点
        prev_node = remove_node.prev
        next_node = remove_node.next
        if prev_node is None:
            self.first = next_node
        else:
            prev_node.next = next_node
        
        if next_node is None:
            self.last = prev_node
        else:
            next_node.prev = prev_node
