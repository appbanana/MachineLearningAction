package com.jqc;

/**
 * Created by apple on 2019/4/17.
 */
public class ArrayList {
    /**
     * 记录数组大小
     */
    private int size = 0;

    private static final int DEFAULT_CAPACITY = 10;
    private static final int ELEMENT_NOT_FOUND = -1;

    /**
     * 暂时保存数组元素
     */
    private int[] elements;

    public ArrayList(int capaticy){
        capaticy = (capaticy < DEFAULT_CAPACITY) ? DEFAULT_CAPACITY : capaticy;
        elements = new int[capaticy];
    }

    /**
     * 返回数组大小
     */
    public int size() {
        return size;
    }

    /**
     * 数组是否为空
     * @return
     */
    public boolean isEmpty(){
        return size == 0;
    }

    /**
     * 是否包含某个元素
     * @return
     */
    public boolean contains(int element){
        return indexOf(element) == ELEMENT_NOT_FOUND;
    }


    /**
     * 添加到尾部
     * @param element
     */
    public void add(int element){
        elements[size++] = element;
    }

    /**
     * 删除元素 并返回已经删除的元素
     * @param element
     */
    public int remove(int index){
        if (index <0 || index > size - 1) {
            throw new IndexOutOfBoundsException("Index:" + index + ", Size:" + size);
        }
        int old = elements[index];
        size--;
        return old;

    }

    /**
     * 改
     * @param element
     */
    public void set(int index, int element){
        if (index < 0 || index > size - 1) {
            throw new IndexOutOfBoundsException("Index:" + index + ", Size:" + size);
        }
        elements[index] = element;
    }

    /**
     * 根据索引获取元素
     * @param element
     */
    public int get(int index){
        if (index < 0 || index > size - 1) {
            throw new IndexOutOfBoundsException("Index:" + index + ", Size:" + size);
        }
        return elements[index];
    }

    /**
     * 查
     * @param element
     */
    public int indexOf(int element){
        for (int i = 0; i < size; i++) {
            if (elements[i] == element) {
                return i;
            }
        }
        return -1;
    }

    public void clear(){
        size = 0;
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
}
