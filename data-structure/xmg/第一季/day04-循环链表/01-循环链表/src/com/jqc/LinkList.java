package com.jqc;

/**
 * Created by apple on 2019/4/20.
 */
public class LinkList<E> extends AbstractList<E> {

    private Node<E> first;
    private Node<E> last;

    private static class Node<E> {
        E element;
        Node<E> next;
        Node<E> prev;

        public Node(Node<E> prev, E element, Node<E> next){
            this.prev = prev;
            this.element = element;
            this.next = next;
        }

        @Override
        public String toString() {
            StringBuilder sb = new StringBuilder();

            if (prev != null) {
                sb.append(prev.element);
            } else {
                sb.append("null");
            }

            sb.append("_").append(element).append("_");

            if (next != null) {
                sb.append(next.element);
            } else {
                sb.append("null");
            }

            return sb.toString();
        }
    }

    @Override
    public void clear() {
        size = 0;
        first = null;
        last = null;
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
        if (index == size){
            Node<E> oldLast = last;
            last = new Node(oldLast, element, null);
            if (oldLast == null){
                // 第一次添加
                first = last;
            }else {
                // 上一次最后的一个节点的next指向新的last
                oldLast.next = last;
            }

        }else {
            Node<E> next = node(index);
            Node<E> prev = next.prev;
            Node<E> node = new Node(prev, element, next);
            next.prev = node;
            if (prev == null){
                first = node;
            }else {
                prev.next = node;
            }
        }


        size++;
    }

    @Override
    public E remove(int index) {
        rangeCheck(index);

        Node<E> node = node(index);
        Node<E> prev = node.prev;
        Node<E> next = node.next;

//        prev.next = next;
//        next.prev = prev;

        if (prev == null){ // 相当于index == 0 删除第一个
            first = next;
        }else {
            prev.next = next;
        }

        if (next == null){
            last = prev;
        }else {
            next.prev = prev;
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



    /**
     *  根据索引寻找node
     * @param index 索引
     * @return node
     */
    private Node<E> node(int index){
        rangeCheck(index);
        if (index < (size >> 1)){
            // index 小于size * 0.5 从后遍历
            Node<E> node = first;
            for (int i = 0; i < index; i++) {
                node = node.next;
            }
            return node;
        }else {
            Node<E> node = last;
            // 因为这里使用的是node。prev 所以是i>index
            for (int i = size - 1; i > index; i--) {
                node = node.prev;
            }
            return node;
        }

    }

    @Override
    public String toString() {
        StringBuilder string = new StringBuilder();
        string.append("size=").append(size).append(", [");
        Node<E> node = first;
        for (int i = 0; i < size; i++) {
            if (i != 0) {
                string.append(", ");
            }

            string.append(node);

            node = node.next;
        }
        string.append("]");
        return string.toString();
    }
}
