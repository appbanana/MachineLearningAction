package com.jqc;
import com.jqc.list.ArrayList;
import com.jqc.list.List;


/**
 * Created by apple on 2019/4/28.
 */
public class Stack<E> {

    private List<E> list = new ArrayList<>();

    public int size(){
        return list.size();
    }

    public boolean isEmpty(){
        return list.isEmpty();
    }

    // 入栈
    public void push(E element){
        list.add(element);
    }

    // 出栈
    public E  pop(){
        return list.remove(list.size() - 1);
    }

    // 出栈
    public E  top(E element){
        return list.get(list.size() - 1);
    }
}
