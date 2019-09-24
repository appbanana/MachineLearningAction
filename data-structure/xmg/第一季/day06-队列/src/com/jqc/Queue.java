package com.jqc;
import com.jqc.list.LinkList;
import com.jqc.list.List;


/**
 * Created by apple on 2019/4/28.
 */
public class Queue<E> {

    private List<E> list = new LinkList<>();

    public int size(){
        return list.size();
    }

    public boolean isEmpty(){
        return list.isEmpty();
    }

    // 入队列
    public void enQueue(E element){
        list.add(element);
    }

    // 出队列
    public E  deQueue(){
        return list.remove(0);
    }

    // 获取队列的头元素
    public E  front(){
        return list.get(0);
    }
}
