package com.jqc;

/**
 * Created by apple on 2019/4/17.
 */
public class ArrayList<E> {
    /**
     * 记录数组大小
     */
    private int size = 0;

    private static final int DEFAULT_CAPACITY = 5;
    private static final int ELEMENT_NOT_FOUND = -1;

    /**
     * 暂时保存数组元素
     */
    private E[] elements;

    public ArrayList(int capacity){
        capacity = (capacity < DEFAULT_CAPACITY) ? DEFAULT_CAPACITY : capacity;
        // Object 是除了Object外所有对象的父类
        elements = (E[]) new Object[capacity];
    }

    /**
     * 返回数组大小
     */
    public int size() {
        return size;
    }

    /**
     * 数组是否为空
     */
    public boolean isEmpty(){
        return size == 0;
    }

    /**
     * 是否包含某个元素
     * @return bool值
     */
    public boolean contains(E element){
        return indexOf(element) == ELEMENT_NOT_FOUND;
    }


    /**
     * 添加到尾部
     * @param element 要添加的元素
     */
    public void add(E element){
//        ensureCapacity(size+1);
//
//
//        elements[size++] = element;
        add(size, element);

    }

    /**
     * 插入一个元素
     * @param index
     * @param element
     */
    public void add(int index, E element){
//        if (index < 0 || index > size -1){
//            // 数组越界
//            throw new IndexOutOfBoundsException("Index:" + index + ", Size:" + size);
//        }

        rangeCheckForAdd(index);
        ensureCapacity(size+1);
        // 插入 从尾部开始 元素依次往后移动
        for (int i = size-1; i >= index ; i--) {
            elements[i+1] = elements[i];
        }
        elements[index] = element;
        size++;

    }
    /**
     * 删除元素 并返回已经删除的元素
     * @param element
     */
    public E remove(int index){
//        if (index <0 || index > size - 1) {
//            throw new IndexOutOfBoundsException("Index:" + index + ", Size:" + size);
//        }
        rangeCheck(index);
        E old = elements[index];
        for (int i = index; i < size - 1; i++) {
            elements[i] = elements[i+1];
        }
//        size--;
        elements[--size] = null;
        return old;

    }

    /**
     * 改
     * @param element
     */
    public void set(int index, E element){
//        if (index < 0 || index > size - 1) {
//            throw new IndexOutOfBoundsException("Index:" + index + ", Size:" + size);
//        }
        rangeCheck(index);
        elements[index] = element;
    }

    /**
     * 根据索引获取元素
     * @param element
     */
    public E get(int index){
//        if (index < 0 || index > size - 1) {
//            throw new IndexOutOfBoundsException("Index:" + index + ", Size:" + size);
//        }
        rangeCheck(index);
        return elements[index];
    }

    /**
     * 查
     * @param element
     */
    public int indexOf(E element){
        if (element == null){
            for (int i = 0; i < size; i++) {
                if (elements[i] == null) return i;
            }
        }else {
            for (int i = 0; i < size; i++) {
                if (elements[i].equals(element)) {
                    return i;
                }
            }
        }
        return ELEMENT_NOT_FOUND;
    }

    public void clear(){
//        size = 0;

        // 这跟java的垃圾回收机制有关 当数组容器中存放的是对象，不用的时候需要考虑到把数组中元素置位null
        for (int i = 0; i < size; i++) {
            elements[i] = null;
        }
    }

    @Override
    public String toString() {
        StringBuilder string = new StringBuilder();
        string.append("size=").append(size).append(",[");
        for (int i = 0; i < size; i++) {
            if (i != 0){
                string.append(',');
            }
            string.append(elements[i]);
        }
        string.append(']');

        return string.toString();
    }

    /**
     * 扩容
     * @param capacity 原来的容量
     */
    private void ensureCapacity(int capacity){
        int oldCapacity = elements.length;
        if (oldCapacity >= capacity) return;
        // 开始扩容 新的容量为旧的容量的1.5倍 使用按位移动 效率更快
        // 这要加一个小括号 因为位运算的级别最低
        int newCapacity = oldCapacity + (oldCapacity >> 1);
        E[] newElements = (E[])new Object[newCapacity];

        // 把原来的元素拷贝过来
        for (int i = 0; i < size; i++) {
            newElements[i] = elements[i];
        }
        elements = newElements;
        System.out.println(oldCapacity + "扩容为" + newCapacity);

    }

    /**
     * 数组异常信息的封装
     * @param index
     */
    private void outOfBounds(int index){
        throw new IndexOutOfBoundsException("Index:" + index + ", Size:" + size);
    }

    private void rangeCheck(int index){
        if (index < 0 || index >= size){
            outOfBounds(index);
        }
    }

    private void rangeCheckForAdd(int index){
        if (index < 0 || index > size){
            outOfBounds(index);
        }
    }
}
