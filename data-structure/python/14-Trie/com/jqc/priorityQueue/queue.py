from com.jqc.heap.binaryHeap import BinaryHeap


class PriorityQueue(object):
    
    def __init__(self, cmp=None):
        self.__heap = BinaryHeap(cmp=cmp)
    
    def size(self) -> int:
        return self.__heap.size()
    
    def is_empty(self):
        return self.__heap.is_empty()
    
    def clear(self):
        self.__heap.clear()
    
    def en_queue(self, element):
        self.__heap.add(element)
    
    def de_queue(self):
        return self.__heap.remove()
    
    def front(self):
        return self.__heap.get()
