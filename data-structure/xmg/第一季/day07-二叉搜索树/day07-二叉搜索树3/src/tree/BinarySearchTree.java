/**
 * Created by apple on 2019/5/6.
 */

package tree;

import printer.BinaryTreeInfo;
import java.util.Comparator;

public class BinarySearchTree<E> implements BinaryTreeInfo{

    private int size;
    private Node<E> root;
    private Comparator<E> comparator;

    // 构造器
    public BinarySearchTree(){
        this(null);
    }

    public BinarySearchTree(Comparator<E> comparator){
        this.comparator = comparator;
    }

    public int size(){
        return size;
    }

    public boolean isEmpty(){
        return size == 0;
    }

    public void clear(){
    }

    public void add(E element){
        elementNotNullCheck(element);
        if (root == null){
            // 第一个节点为跟节点
            root = new Node(element, null);
            size++;
            return;
        }

        // 暂存节点的父节点
        Node<E> parent = root;
        Node<E> node = root;
        int cmp = 0;
        while(node != null){
            cmp = compare(element, node.element);
            parent = node;
            if (cmp > 0){
                node = node.right;
            }else if (cmp < 0){
                node = node.left;
            }else {
                // 相等 先暂不处理
                return;
            }
        }

        // 接下来我要执行添加节点功能，一方面我需要父节点，另一方面我需要知道添加到父节点的左边还是右边
        Node<E> newNode = new Node<>(element, parent);
        if (cmp > 0){
            parent.right = newNode;
        }else{
            parent.left = newNode;
        }
        size++;

    }

    public void remove(E element) {

    }

    /**
     * @return 返回值等于0，代表e1和e2相等；返回值大于0，代表e1大于e2；返回值小于于0，代表e1小于e2
     */
    private int compare(E e1, E e2) {
        // 第一种方法：直接在里面写死比较逻辑
//        return (Integer)e1 - (Integer)e2;

        // 第二种使用接口，让传进来的模型去遵守这个协议，去实现这个协议
//        return e1.compareTo(e2);

        // 第三种方法改进 如果你传comparator 优先使用comparator 如果你没有传 使用自定义的Comparable
        if (comparator != null){
//            return comparator.compareTo(e1, e2);
            return comparator.compare(e1, e2);
        }
        return ((Comparable<E>)e1).compareTo(e2);
    }

    public boolean contains(E element) {
        return false;
    }

    private void elementNotNullCheck(E element) {
        if (element == null) {
            throw new IllegalArgumentException("element must not be null");
        }
    }


    private static class Node<E> {
        E element;
        Node<E> left;
        Node<E> right;

        Node<E> parent;
        public Node(E element, Node<E> parent) {
            this.element = element;
            this.parent = parent;
        }
    }

    @Override
    public Object root() {
        return root;
    }

    @Override
    public Object left(Object node) {
        return ((Node<E>)node).left;
    }

    @Override
    public Object right(Object node) {
        return ((Node<E>)node).right;
    }

    @Override
    public Object string(Object node) {
        return ((Node<E>)node).element;
    }
}
