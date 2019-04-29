package com.jqc;

/**
 * Created by apple on 2019/4/20.
 */
public abstract class AbstractList<E> implements List<E> {

    protected int size;

    /**
     * 清除所有元素 因为这个方法在数组中和在链表中实现不同，所以不用单独拎出来
     */

    /**
     * 元素的数量
     * @return
     */
    public int size(){
        return size;
    }

    /**
     * 是否为空
     * @return
     */
    public boolean isEmpty(){
        return size == 0;
    }

    /**
     * 是否包含某个元素
     * @param element
     * @return
     */
    public boolean contains(E element){
        return indexOf(element) == ELEMENT_NOT_FOUND;
    }

    /**
     * 添加元素到尾部
     * @param element
     */
    public void add(E element){
        add(size, element);
    }


    protected void outOfBounds(int index){
        throw new IndexOutOfBoundsException("Index:" + index + ", Size:" + size);
    }

    protected void rangeCheck(int index){
        if (index < 0 || index >= size){
            outOfBounds(index);
        }
    }

    protected void rangeCheckForAdd(int index){
        if (index < 0 || index > size){
            outOfBounds(index);
        }
    }
}
