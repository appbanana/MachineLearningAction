from com.jqc.map.hashMap import HashMap
from com.jqc.map.map import Visitor
from com.jqc.map.testModel.person import Person
from com.jqc.map.testModel.key import Key
from com.jqc.map.testModel.subkey1 import SubKey1
from com.jqc.map.testModel.subkey2 import SubKey2
import unittest
import operator


def visit(key, value):
    print(key, "-", value)
    return False


def test1(map: HashMap):
    """
    测试具有相同属性的实例对象是否为同一个键,
    :param map:
    :return:
    """
    p1 = Person('abc', 18, 1.78)
    p2 = Person('abc', 18, 1.78)
    map.put(p1, '1')
    map.put(p2, '2')
    # 1
    print(map.size())


def test2(map: HashMap, test_unit):
    p1 = Person('abc', 18, 1.78)
    p2 = Person('abc', 18, 1.78)
    map.put(p1, 1)
    map.put(p2, 2)
    map.put('abc', 3)
    map.put('xyz', 4)
    map.put('abc', 5)
    map.put(None, 6)
    
    # visitor = Visitor(visit)
    # map.traversal(visitor)
    
    test_unit.assertTrue(map.size() == 4)
    test_unit.assertTrue(map.get('xyz') == 4)
    test_unit.assertTrue(map.get(None) == 6)
    test_unit.assertTrue(map.contains_key('abc'))
    test_unit.assertTrue(map.contains_value(2))
    test_unit.assertTrue(map.remove('abc') == 5)
    test_unit.assertTrue(map.size() == 3)


def test3(cus_map: HashMap, test_unit):
    for i in range(1, 20):
        cus_map.put(Key(i), i)
    cus_map.put(Key(4), 100)
    # print(cus_map.size())
    # print('***' * 10)
    # visitor = Visitor(visit)
    # cus_map.traversal(visitor)
    #
    test_unit.assertTrue(cus_map.size() == 19)
    test_unit.assertTrue(cus_map.get(Key(4)) == 100)
    test_unit.assertTrue(cus_map.get(Key(16)) == 16)
    test_unit.assertTrue(cus_map.get(Key(18)) == 18)


def test4(cus_map: HashMap, test_unit):
    for i in range(1, 21):
        cus_map.put(Key(i), i)
    # print(cus_map.size())
    # print('***' * 10)
    # visitor = Visitor(visit)
    # cus_map.traversal(visitor)
    # print(cus_map.get(Key(12)))
    # print('----end---end' * 5)

    for i in range(5, 8):
        cus_map.put(Key(i), i + 5)
    # print(cus_map.size())
    # print('***' * 10)
    # visitor = Visitor(visit)
    # cus_map.traversal(visitor)
    test_unit.assertTrue(cus_map.size() == 20)
    test_unit.assertTrue(cus_map.get(Key(4)) == 4)
    test_unit.assertTrue(cus_map.get(Key(5)) == 10)
    test_unit.assertTrue(cus_map.get(Key(6)) == 11)
    test_unit.assertTrue(cus_map.get(Key(7)) == 12)
    test_unit.assertTrue(cus_map.get(Key(8)) == 8)


def test5(cus_map: HashMap, test_unit):
    cus_map.put(None, 1)
    cus_map.put(object(), 2)
    cus_map.put('jack', 3)
    cus_map.put(10, 4)
    cus_map.put(object(), 5)
    cus_map.put('jack', 6)
    cus_map.put(10, 7)
    cus_map.put(None, 8)
    cus_map.put(10, None)
    test_unit.assertTrue(cus_map.size() == 5)
    test_unit.assertTrue(cus_map.get(None) == 8)
    test_unit.assertTrue(cus_map.get('jack') == 6)
    test_unit.assertTrue(cus_map.get(10) == None)
    test_unit.assertTrue(cus_map.get(object()) == None)
    test_unit.assertTrue(cus_map.contains_key(10))
    test_unit.assertTrue(cus_map.contains_key(None))
    test_unit.assertTrue(cus_map.contains_value(None))


def test6(cus_map: HashMap, test_unit):
    cus_map.put("jack", 1)
    cus_map.put("rose", 2)
    cus_map.put("jim", 3)
    cus_map.put("jake", 4)
    for i in range(1, 11):
        cus_map.put("test" + str(i), i)
        cus_map.put(Key(i), i)
    
    for i in range(5, 8):
        test_unit.assertTrue(cus_map.remove(Key(i)) == i)
    
    for i in range(1, 4):
        cus_map.put(Key(i), i + 5)
    
    test_unit.assertTrue(cus_map.size() == 21)
    test_unit.assertTrue(cus_map.get(Key(1)) == 6)
    test_unit.assertTrue(cus_map.get(Key(2)) == 7)
    test_unit.assertTrue(cus_map.get(Key(3)) == 8)
    test_unit.assertTrue(cus_map.get(Key(4)) == 4)
    test_unit.assertTrue(cus_map.get(Key(5)) == None)
    test_unit.assertTrue(cus_map.get(Key(6)) == None)
    test_unit.assertTrue(cus_map.get(Key(7)) == None)
    test_unit.assertTrue(cus_map.get(Key(8)) == 8)


def test7(cus_map: HashMap, test_unit):
    for i in range(1, 21):
        cus_map.put(Key(i), i)

    cus_map.put(SubKey2(1), 5)
    test_unit.assertTrue(cus_map.get(SubKey1(1)) == 5)
    test_unit.assertTrue(cus_map.get(SubKey2(1)) == 5)
    print(cus_map.size())
    test_unit.assertTrue(cus_map.size() == 20)

if __name__ == '__main__':
    """
    如果要实现hashmap, 自定义类一定要实现 __eq__方法和 __hash__
    另外要自己实现一个比较方法 eg:compare
    两个对象如果eq相等,则对应的hash一定相等反之不成立,hash值一样,不一定是同一个对象
    
    __eq__作用是是,当hash冲突时,判断两个key是否是同一个
    __hash__作用是方便找索引
    
    如果只实现只实现__eq__ 不实现__hash__, 相等的两个对象,hash值不一样,对应的索引可能不一样,会不稳定
    如果只实现只实现__hash__ 不实现__eq__, 相同属性的实例会当成不同的对象
    
    注意:__eq__用到对象的哪些属性,__hash__计算的时候也要用到这些属性,这两个方法一定要用相同的属性
    
    """
    
    test_unit = unittest.TestCase()
    
    # test1(HashMap())
    
    # test2(HashMap(), test_unit)
    # test3(HashMap(), test_unit)

    test4(HashMap(), test_unit)
    test5(HashMap(), test_unit)
    test6(HashMap(), test_unit)
    test7(HashMap(), test_unit)
    
    # k1 = Key(1)
    # k2 = SubKey2(1)
    # print(operator.eq(k1, k2))
    # print(operator.eq(k2, k1))
    # print(k1.__class__.__name__)
    # print(k1 == k2)
    # print()
    # print(issubclass(type(k1), type(k2)))
