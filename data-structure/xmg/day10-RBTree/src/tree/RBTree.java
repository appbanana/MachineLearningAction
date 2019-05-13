package tree;

import java.util.Comparator;

/**
 * Created by apple on 2019/5/13.
 */
public class RBTree<E> extends BBST<E> {
    private static final boolean RED = false;
    private static final boolean BLACK = true;

    public RBTree(){
        this(null);
    }

    public RBTree(Comparator<E> comparator) {
        super(comparator);
    }

    @Override
    protected void afterAdd(Node<E> node) {
        Node<E> parent = node.parent;
        // 如果添加的是跟节点 直接染成黑色就可以
        if (parent == null) {
            black(node);
            return;
        }
        // 如果父节点是黑色的 有4中情况 不用作任何处理
        if (isBlack(parent)) return;

        // 获取到叔父节点
        Node<E> uncle = parent.sibling();
        Node<E> grand = parent.parent;

        // 叔父节点是红色
        if (isRed(uncle)){
            black(parent);
            black(uncle);
            afterAdd(red(grand));
            return;
        }
        // 叔父节点是黑色
        if (parent.isLeftChild()){
            // L
            if (node.isLeftChild()){
                // LL
                black(parent);
                red(grand);
                rotateRight(grand);
            }else {
                // LR
                black(node);
                red(grand);
                rotateLeft(parent);
                rotateRight(grand);
            }
        }else {
            // R
            if (node.isLeftChild()){
                black(node);
                red(grand);
                // RL
                rotateRight(parent);
                rotateLeft(grand);
            }else {
                // RR
                black(parent);
                red(grand);
                rotateLeft(grand);
            }
        }

    }

    @Override
    protected void afterRemove(Node<E> node, Node<E> replacement) {
        // 如果删除的节点是红色 直接删掉就可以 不需要其他操作
        if (isRed(node)) return;

        // 接下来就是删除黑色的节点
        // 1) 黑色节点有2个红色的子节点 2）该黑色节点有1个红色的子节点 3) 该节点有0个红色的子节点

        // 第一种情况 如果删除的黑色节点有两个红色的子节点 实际上删除的是该黑色节点的前驱或者后继 这种请款暂不处理
        // 第二种情况 该黑色节点有1个红色的子节点 直接将替代的红色节点染成黑色
        if (isRed(replacement)){
            black(replacement);
            return;
        }

        // 接下来就是删除黑色的叶子节点

    }

    @Override
    protected Node<E> createNode(E element, Node<E> parent) {
        return new RBNode(element, parent);
    }

    public boolean isBlack(Node<E> node){
        return colorOf(node) == BLACK;
    }

    public boolean isRed(Node<E> node){
        return colorOf(node) == RED;
    }

    // 上色
    public Node<E> color(Node<E> node, boolean color){
        ((RBNode<E>)node).color = color;
        return node;
    }

    public Node<E> black(Node<E> node){
        return  color(node, BLACK);
    }

    public Node<E> red(Node<E> node){
        return  color(node, RED);
    }

    public boolean colorOf(Node<E> node){
        return node == null ? BLACK : ((RBNode<E>)node).color;
    }

    private class RBNode<E> extends Node<E>{
        boolean color = RED;

        public RBNode(E element, Node<E> parent) {
            super(element, parent);
        }

        @Override
        public String toString() {
            String str = "";
            if (color == RED) {
                str = "R_";
            }
            return str + element.toString();
        }
    }
}
