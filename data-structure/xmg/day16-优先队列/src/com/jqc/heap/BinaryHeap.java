package com.jqc.heap;


import java.util.Comparator;
//import com.jqc.printer.*;

public class BinaryHeap<E> extends AbstractHeap<E> {

//    private int size =0;
    private E[] elements;
    private static final int DEFAULT_CAPACITY = 10;
//    private Comparator<E> comparator;

    public BinaryHeap(E[] elements, Comparator<E> comparator){
        super(comparator);
        if (elements == null || elements.length == 0){
            this.elements = (E []) new Object[DEFAULT_CAPACITY];
        }else {
            size = elements.length;
            int capacity = Math.max(elements.length, DEFAULT_CAPACITY);
            this.elements = (E []) new Object[capacity];
            for (int i = 0 ; i < elements.length; i++) {
                this.elements[i] = elements[i];
            }
            heapify();
        }
    }

    public BinaryHeap(E[] elements)  {
        this(elements, null);
    }

    public BinaryHeap(Comparator<E> comparator){
//        this.elements = (E[]) new Object[DEFAULT_CAPACITY];
//        this.comparator = comparator;
        this(null, comparator);
    }
    public BinaryHeap(){
        this(null, null);
    }

//    @Override
//    public int size() {
//        return size;
//    }
//
//    @Override
//    public boolean isEmpty() {
//        return size == 0;
//    }

    @Override
    public void clear() {
        for (int i = 0; i < size; i++) {
            elements[i] = null;
        }
        size = 0;
    }

    @Override
    public void add(E element) {
        elementsNotNullCheck(element);
        ensureCapacity(size+1);
        elements[size++] = element;
        siftUp(size - 1);

    }

    @Override
    public E get() {
        emptyCheck();
        return elements[0];
    }

    @Override
    public E remove() {
        emptyCheck();
        // 删除其实就是删除堆顶元素，把堆数组中最后一个覆盖掉第一个元素，在下滤调整位置
        E fist = elements[0];
        elements[0] = elements[size-1];
        elements[size -1] = null;
        size--;
        siftDown(0);
        return fist;
    }

    @Override
    public E replace(E element) {
        elementsNotNullCheck(element);
        E root = null;
        if (size == 0){
            elements[0] = element;
            size++;
        }else {
            root = elements[0];
            elements[0] = element;
            siftDown(0);
        }
        return root;
    }

    // 批量建堆
    private void heapify() {
        // 自上而下的上滤
//        for (int i = 0; i < size; i++) {
//            siftUp(i);
//        }

        // 自下而上的下滤
        for (int i = (size >> 1) - 1; i >= 0; i--) {
            siftDown(i);
        }
    }
    // 上滤
    private void siftUp(int index){
        E element = elements[index];

        while (index > 0){
            int parentIndex = (index -1) / 2;
            E parentVal = elements[parentIndex];

            if (compare(parentVal, element) >= 0) return;
            // 如果父元素小于当前的element 那么就把父元素移动到子节点位置
            elements[index] = parentVal;
            index = parentIndex;
        }
        elements[index] = element;
    }

    private void ensureCapacity(int capacity) {
        int oldCapacity = elements.length;
        if (oldCapacity >= capacity) return;

        // 新容量为旧容量的1.5倍
        int newCapacity = oldCapacity + (oldCapacity >> 1);
        E[] newElements = (E[]) new Object[newCapacity];
        for (int i = 0; i < size; i++) {
            newElements[i] = elements[i];
        }
        elements = newElements;
    }

    // 下滤
    private void siftDown(int index) {
        E element = elements[index];
        int half = size >> 1;
        // 因为只有非叶子节点才会下滤的可能
        while (index < half){
            int childIndex = (index << 1) + 1;
            E child = elements[childIndex];
            int childRightIndex = childIndex + 1;

            // 如果右子节点小于size 而且右子节点的值大于左子节点的值
            if (childRightIndex < size && compare(elements[childRightIndex], child) > 0){
                child = elements[childRightIndex];
                childIndex = childRightIndex;
            }

            if (compare(element, child) >= 0) break;

            // child比较大的话 让他成为该child的父节点
            elements[index] = child;
            index = childIndex;
        }

        elements[index] = element;

    }

//    private int compare(E e1, E e2){
//        return comparator != null ? comparator.compare(e1, e2) : ((Comparable<E>)e1).compareTo(e2);
//    }

    private void emptyCheck() {
        if (size == 0){
            throw new IndexOutOfBoundsException("Heap is empty");
        }
    }

    private void elementsNotNullCheck(E element) {
        if (element == null) {
            throw new IllegalArgumentException("element must not be null");
        }
    }

}
