package com.jqc.Circle;

import com.jqc.list.LinkList;
import com.jqc.list.List;

/**
 * Created by apple on 2019/4/28.
 */
public class CircleDeque<E> {


    private E[] elements;
    private int front;
    private int size;
    private static final int DEFAULT_CAPACITY = 10;


    public CircleDeque(){
        elements = (E[])new Object[DEFAULT_CAPACITY];
    }

    public int size(){
        return size;
    }

    public boolean isEmpty(){
        return size == 0;
    }


    // 从队头入队列
    public void enQueueFront(E element){
        ensureCapacity(size+1);
        // 对头添加 front要减1 这个还要转换为真正的下标
//        front = front -1;
        front = index(-1);
        elements[front] = element;
        size++;
    }

    // 从队尾入队列
    public void enQueueRear(E element){
        ensureCapacity(size+1);
        elements[(front + size) % elements.length] = element;
        size++;
    }

    // 从对头出队列
    public E deQueueFront(){
        E element = elements[front];
        elements[front] = null;
        size--;
//        front = front + 1;
        // 这个要进行转换
        front = index(1);
        return element;
    }

    // 从对尾出队列
    public E deQueueRear(){
        int realIndex = index(size -1);
        E element = elements[realIndex];
        elements[realIndex] = null;
        size--;
        // 这个要进行转换
        return element;
    }

    // 获取队列的头元素
    public E front(){
        return elements[front];
    }

    // 获取队列的头元素
    public E  rear(){
        return elements[front + size -1];
    }


    @Override
    public String toString() {
        StringBuilder string = new StringBuilder();
        string.append("capcacity=").append(elements.length)
                .append(" size=").append(size)
                .append(" front=").append(front)
                .append(", [");
        for (int i = 0; i < elements.length; i++) {
            if (i != 0) {
                string.append(", ");
            }

            string.append(elements[i]);
        }
        string.append("]");
        return string.toString();
    }

    // 将当前的索引换算成真实的索引
    private int index(int index){
        index += front;
        if (index < 0){
            index = index + elements.length;
        }
//        return index % elements.length;
        return index - (index >= elements.length ? elements.length : 0);

    }

    // 扩容
    private void ensureCapacity(int capacity) {
        int oldCapacity = elements.length;
//        if (capacity <= oldCapacity) return;
        if (oldCapacity >= capacity) return;

        int newCapacity = oldCapacity + (oldCapacity >> 1);

        E[] newElements = (E[])new Object[newCapacity];
        for (int i = 0; i < size; i++) {
            newElements[i] = elements[index(i)];
        }
        elements = newElements;
        // 要将front置位0
        front = 0;
    }
    
}
