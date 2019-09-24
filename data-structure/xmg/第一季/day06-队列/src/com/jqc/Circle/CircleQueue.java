package com.jqc.Circle;

//import com.jqc.list.LinkList;
//import com.jqc.list.List;

/**
 * Created by apple on 2019/4/28.
 */
public class CircleQueue<E> {
    private E[] elements;
    private int front;
    private int size;
    private static final int DEFAULT_CAPACITY = 10;


    public CircleQueue(){
        elements = (E[])new Object[DEFAULT_CAPACITY];
    }

    public int size(){
        return size;
    }

    public boolean isEmpty(){
        return size == 0;
    }

    // 入队列
    public void enQueue(E element){
        ensureCapacity(size+1);
//        elements[(front + size) % elements.length] = element;
        elements[index(size)] = element;
        size++;
    }

    // 出队列
    public E  deQueue(){
        E element = elements[front];
        elements[front] = null;
//        front = (front + 1) % elements.length;
        front = index(1);
        size--;
        return element;
    }

    // 获取队列的头元素
    public E  front(){
        return elements[front];
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
        return (front + index) % elements.length;
    }

    // 扩容
    private void ensureCapacity(int capacity) {
        int oldCapacity = elements.length;
        if (capacity <= oldCapacity) return;
        int newCapacity = oldCapacity + (oldCapacity >> 1);

        E[] newElements = (E[])new Object[newCapacity];
        for (int i = 0; i < elements.length; i++) {
//            newElements[i] = elements[(front + i) % elements.length];
            newElements[i] = elements[index(i)];
        }
        elements = newElements;
        // 要将front置位0
        front = 0;
    }
}
