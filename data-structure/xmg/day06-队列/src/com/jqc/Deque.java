package com.jqc;

import com.jqc.list.LinkList;
import com.jqc.list.List;

/**
 * Created by apple on 2019/4/28.
 */
public class Deque<E> {

    private List<E> list = new LinkList();

    public int size(){
        return list.size();
    }

    public boolean isEmpty(){
        return list.isEmpty();
    }

    // 从队头入队列
    public void enQueueFront(E element){
        list.add(0, element);
    }

    // 从队尾入队列
    public void enQueueRear(E element){
        list.add(element);
    }

    // 从对头出队列
    public E  deQueueFront(){
        return list.remove(0);
    }

    // 从对尾出队列
    public E  deQueueRear(){
        return list.remove(list.size()-1);
    }

    // 获取队列的头元素
    public E  front(){
        return list.get(0);
    }

    // 获取队列的头元素
    public E  rear(){
        return list.get(list.size() - 1);
    }
}
