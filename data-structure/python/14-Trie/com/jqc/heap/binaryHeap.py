from .abstractHeap import AbstractHeap
import math


class BinaryHeap(AbstractHeap):
    __DEFAULT_CAPACITY = 1 << 4
    
    def __init__(self, cmp=None, elements=None):
        super().__init__(cmp)
        if elements is None:
            self.__elements = [None] * BinaryHeap.__DEFAULT_CAPACITY
        else:
            size = len(elements)
            capacity = size if size > BinaryHeap.__DEFAULT_CAPACITY else BinaryHeap.__DEFAULT_CAPACITY
            self.__elements = [None] * capacity
            self.__elements[:capacity] = elements[:capacity]
            self.__heapify()
    
    def __str__(self):
        string = '['
        for index in range(self._size):
            string += str(self.__elements[index])
            if index != self._size - 1:
                string += ','
        string += ']'
        return string
    
    # def __str__(self):
    #
    #     container = []
    #     length = 32
    #     string_array = [' '] * length
    #     string_array[(length >> 1)] = str(self.__elements[0])
    #     height = math.ceil(math.log2(self._size)) + 1
    #     last_array = string_array
    #     for i in range(1, height):
    #         string_array = [' '] * length
    #         total_num = 2 ** i
    #         # print('i=', str(i))
    #         # print(last_array)
    #
    #         # 每一行的首元素索引
    #         first_index = total_num - 1
    #         for j in range(0, total_num):
    #
    #             child_index = first_index + j
    #             if child_index > self._size - 1:
    #                 break
    #             parent_index = (child_index - 1) >> 1
    #             parent_element = str(self.__elements[parent_index])
    #             # print('---------', str(i), parent_element, type(parent_element))
    #             temp_index = last_array.index(parent_element)
    #             element = self.__elements[child_index]
    #             if element is None:
    #                 continue
    #             elif child_index % 2 == 0:
    #                 # 右子节点
    #                 string_array[temp_index + i] = str(element)
    #             else:
    #                 string_array[temp_index - i] = str(element)
    #         print(last_array)
    #         container.append(string_array)
    #         last_array = string_array
    #
    #     return 'temp'
    
    def clear(self):
        self.__elements = [None for _ in self.__elements]
        self._size = 0
    
    def add(self, element):
        """
        添加元素
        :param element:
        :return:
        """
        self.__element_not_none_check(element)
        self.__ensure_capacity(self._size + 1)
        self.__elements[self._size] = element
        # 上滤操作
        self.__shift_up(self._size)
        self._size += 1
    
    def get(self):
        """
        获得堆顶元素
        :return:
        """
        self.__empty_check()
        return self.__elements[0]
    
    def remove(self):
        """
         删除堆顶元素
        :return:
        """
        # 把最后一个元素放到最前面 然后下滤
        self.__empty_check()
        first_element = self.__elements[0]
        self.__elements[0] = self.__elements[self._size - 1]
        self.__elements[self._size - 1] = None
        self._size -= 1
        # 下滤操作
        self.__shift_dowm(0)
        return first_element
    
    def replace(self, element):
        """
        删除堆顶元素,同时插入一个新元素
        :param element:
        :return:
        """
        self.__element_not_none_check(element)
        root = None
        if self._size == 0:
            self.__elements[0] = element
            self._size += 1
        else:
            root = self.__elements[0]
            self.__elements[0] = element
            self.__shift_dowm(0)
        return root
    
    def __shift_up(self, index):
        """
        上滤,找到首次比添加元素小的那个位置
        :return:
        """
        element = self.__elements[index]
        while index > 0:
            parent_index = (index - 1) >> 1
            
            parent_element = self.__elements[parent_index]
            
            cmp_result = self.compare(element, parent_element)
            if cmp_result > 0:
                self.__elements[index] = parent_element
                index = parent_index
            else:
                break
        self.__elements[index] = element
    
    def __shift_dowm(self, index):
        """
        下滤操作
        :param index:
        :return:
        """
        # 以为有一半的是叶子节点,如果到叶子节点,就没必要下滤
        half = self._size >> 1
        element = self.__elements[index]
        
        while index < half:
            # 左子节点值
            child_index = (index << 1) + 1
            child_element = self.__elements[child_index]
            if child_index + 1 < self._size \
                    and self.compare(self.__elements[child_index + 1], child_element) > 0:
                # 右子节点的值比较大
                child_index = child_index + 1
                child_element = self.__elements[child_index]
            
            if self.compare(element, child_element) > 0:
                break
            
            self.__elements[index] = child_element
            
            index = child_index
        self.__elements[index] = element
    
    def __empty_check(self):
        """
        验证堆是否为空
        :return:
        """
        if self.is_empty():
            raise NameError('index out of bounds, 堆为空')
    
    @staticmethod
    def __element_not_none_check(element):
        """
        添加元素不能为空
        :param elements:
        :return:
        """
        
        if element is None:
            raise NameError('添加元素不能为空')
    
    def __ensure_capacity(self, capacity):
        """
        扩容
        :param capacity:
        :return:
        """
        old_len = len(self.__elements)
        if old_len >= capacity:
            return
        new_capacity = old_len + (old_len >> 1)
        print('扩容', old_len, new_capacity)
        new_data = [None] * new_capacity
        new_data[:self._size] = self.__elements[:self._size]
        self.__elements = new_data
    
    def __heapify(self):
        """
        批量建堆
        :return:
        """
        # 自上而下的上滤
        # for i in range(self._size):
        #     self.__shift_up(i)
        
        # 自下而上的下滤
        half = self._size >> 1
        for i in range(half, -1, -1):
            self.__shift_dowm(i)
