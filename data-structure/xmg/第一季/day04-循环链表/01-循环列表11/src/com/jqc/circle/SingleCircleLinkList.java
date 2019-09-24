package com.jqc.circle;

import com.jqc.AbstractList;

/**
 * Created by apple on 2019/4/20.
 */
public class SingleCircleLinkList<E> extends AbstractList<E> {

    private Node<E> first;

    private static class Node<E> {
        E element;
        Node<E> next;

        public Node(E element, Node<E> next){
            this.element = element;
            this.next = next;
        }

        @Override
        public String toString() {
            StringBuilder string = new StringBuilder();
            string.append(element).append("_").append(next.element);
            return string.toString();
        }
    }

    @Override
    public void clear() {
        size = 0;
        first = null;
    }

    @Override
    public E set(int index, E element) {
        Node<E> node = node(index);
        E old = node.element;
        node.element = element;
        return old;
    }

    @Override
    public E get(int index) {
        return node(index).element;
    }

    /**
     * 更新元素
     * @param index 索引
     * @param element 元素
     */
    @Override
    public void add(int index, E element) {
        if (index == 0){
            Node<E> newFirst = new Node(element, first);
            Node<E> last = (size == 0) ? newFirst : node(size-1);
            last.next = newFirst;
            first = newFirst;
        }else {
            Node<E> pre = node(index-1);
            pre.next = new Node(element, pre.next);
        }
        size++;
    }

    @Override
    public E remove(int index) {
        rangeCheck(index);
        Node<E> node = first;
        if (index == 0){
            if (size == 1){
                first = null;
            }else {
                Node<E> last = node(size-1);
                first = first.next;
                last.next = first;
            }
        }else {
            Node<E> pre = node(index-1);
            node = pre.next;
            pre.next = node.next;
        }
        size--;
        return node.element;
    }

    @Override
    public int indexOf(E element) {
        if (element == null){
            Node<E> node = first;
            for (int i = 0; i < size; i++) {
                if (node.element == null) return i;
                node = node.next;
            }
        }else {
            Node<E> node = first;
            for (int i = 0; i < size; i++) {
                if (node.element.equals(element)) return i;
                node = node.next;
            }
        }
        return ELEMENT_NOT_FOUND;
    }


    @Override
    public String toString() {
        StringBuilder string = new StringBuilder();
        string.append("size=").append(size).append(",[");
        Node<E> node = first;
        for (int i = 0; i < size; i++) {
            if (i != 0){
                string.append(',');
            }
            string.append(node);
            node = node.next;
        }
        string.append(']');

        return string.toString();
    }

    /**
     *  根据索引寻找node
     * @param index 索引
     * @return node
     */
    private Node<E> node(int index){
        rangeCheck(index);
        Node<E> node = first;
        for (int i = 0; i < index; i++) {
            node = node.next;
        }
        return node;
    }
}
