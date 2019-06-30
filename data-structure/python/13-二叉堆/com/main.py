import unittest

from com.jqc.heap.binaryHeap import BinaryHeap


def test1():
    array = [70, 33, 17, 64, 13, 80, 94, 56, 65, 49, 18]
    heap = BinaryHeap()
    for item in array:
        heap.add(item)
    print(heap)
    
    print(heap.remove())
    print(heap)


def test2():
    array = [8, 29, 58, 100, 44, 52, 94, 3, 59, 14, 72]
    heap = BinaryHeap()
    for item in array:
        heap.add(item)
    heap.replace(66)


def test3():
    # 最小堆
    array = [8, 29, 58, 100, 44, 52, 94, 3, 59, 14, 72]
    heap = BinaryHeap(lambda e1, e2: e2 - e1)
    for item in array:
        heap.add(item)


if __name__ == '__main__':
    
    # test1()
    # test2()
    # test3()
    # top K 问题
    array = [29, 68, 82, 43, 78, 99, 24, 80, 7, 81, 15, 50, 29, 61, 78, 68, 86, 38,\
             97, 72, 25, 51, 89, 58, 36, 12, 73, 65, 94]
    heap = BinaryHeap(cmp=lambda e1, e2: e2 - e1)
    k = 3
    for i in range(len(array)):
        if i < 3:
            heap.add(array[i])
        elif array[i] > heap.get():
            heap.replace(array[i])
    print(heap)
