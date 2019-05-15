/**
 * Created by apple on 2019/5/6.
 */

package tree;

import java.util.Comparator;

public class BinarySearchTree<E> extends BinaryTree<E>{


    private Comparator<E> comparator;

    // 构造器
    public BinarySearchTree(){
        this(null);
    }

    public BinarySearchTree(Comparator<E> comparator){
        this.comparator = comparator;
    }

    public boolean contains(E element) {
        return node(element) != null;
    }

    public void add(E element){
        elementNotNullCheck(element);
        if (root == null){
            // 第一个节点为跟节点
//            root = new Node(element, null);
            root = createNode(element, null);

            // 添加完元素后进行 avl树调整
            afterAdd(root);
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
                // 相等的元素直接进行覆盖
                node.element = element;
                return;
            }
        }

        // 接下来我要执行添加节点功能，一方面我需要父节点，另一方面我需要知道添加到父节点的左边还是右边
//        Node<E> newNode = new Node<>(element, parent);
        Node<E> newNode = createNode(element, parent);
        if (cmp > 0){
            parent.right = newNode;
        }else{
            parent.left = newNode;
        }
        // 添加完元素后进行 avl树调整
        afterAdd(newNode);
        size++;


    }

    // 删除 其实删除的是他的前驱后继
    public void remove(E element) {
        remove(node(element));
    }


    // 真正的删除逻辑 使用前驱和后继都可以 这里使用后继进行替换要删除的节点
    // 删除节点 有三种类型 删除度为2的几点，此时删除的是它的前驱后后继 他的前驱或者后继只能是度为0或者度为1的节点
    // 删除度为1的节点 删除度为0的节点
    public void remove(Node<E> node) {
        if (node == null) return;
        size--;
        if (node.hasTwoChildren()){
            Node<E> s = successor(node);
            node.element = s.element;
            // 赋值为node  node就是接下来要删除的节点
            node = s;
        }

        // 接下来就是删除度为0或者为1的节点
        Node<E> replacement = (node.left != null) ? node.left : node.right;
        if (replacement != null) { // node是度为1的节点
            // 更改parent
            replacement.parent = node.parent;
            // 更改parent的left、right的指向
            if (node.parent == null) { // node是度为1的节点并且是根节点
                root = replacement;
            } else if (node == node.parent.left) {
                node.parent.left = replacement;
            } else { // node == node.parent.right
                node.parent.right = replacement;
            }

            // 删除节点之后的处理
            afterRemove(replacement);
        } else if (node.parent == null) { // node是叶子节点并且是根节点
            root = null;

            // 删除节点之后的处理
            afterRemove(node);
        } else { // node是叶子节点，但不是根节点
            if (node == node.parent.left) {
                node.parent.left = null;
            } else { // node == node.parent.right
                node.parent.right = null;
            }

            // 删除节点之后的处理
            afterRemove(node);
        }


    }

    /**
     * 添加node之后的调整
     * @param node 新添加的节点
     */
    protected void afterAdd(Node<E> node) { }

    /**
     * 删除node之后的调整
     * @param node 被删除的节点
     */
//    protected void afterRemove(Node<E> node) { }
    protected void afterRemove(Node<E> node) { }


    private Node<E> node(E element){
        Node<E> p = root;
        while (p != null){
            int cmp = compare(element, p.element);
            if (cmp == 0) return p;
            if (cmp > 0){
                p = p.right;
            }else if (cmp < 0){
                p = p.left;
            }
        }
        return null;
    }
    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        toString(root, sb, "");
        return super.toString();
    }

    private void toString(Node<E> node, StringBuilder sb, String prefix) {
        if (node == null) return;
        toString(node.left, sb, prefix + "L--");
        sb.append(prefix).append(node.element).append("\n");
        toString(node.right, sb, prefix + "R--");

    }

    private void elementNotNullCheck(E element) {
        if (element == null) {
            throw new IllegalArgumentException("element must not be null");
        }
    }

    /**
     * @return 返回值等于0，代表e1和e2相等；返回值大于0，代表e1大于e2；返回值小于于0，代表e1小于e2
     */
    private int compare(E e1, E e2) {
        if (comparator != null){
            return comparator.compare(e1, e2);
        }
        return ((Comparable<E>)e1).compareTo(e2);
    }

}
