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

        // 接下来就是删除黑色的叶子节点  可能会产生下溢
        Node<E> parent = node.parent;
        // 为空的话 删除的则是根节点
        if (parent == null) return;
        // 判断删除的节点是left 还是right
        boolean left = parent.left == null || node.isLeftChild();
        Node<E> sibling = left ? parent.right : parent.left;
        if (left){
            // 删除的是左子节点
            if (isRed(sibling)){
                black(sibling);
                red(parent);
                rotateLeft(parent);
                sibling = parent.right;
            }

            // 下面是删除节点的兄弟节点是黑色
            if (isBlack(sibling.left) && isBlack(sibling.right)){
                // 没有红色子节点 父节点下溢
                boolean parentBlack = isBlack(parent);
                red(sibling);
                black(parent);
                if (parentBlack){
                    // 如果之前的父节点为黑色 还会产生下溢 接着执行删除
                    afterRemove(parent, null);
                }


            }else {
                System.out.println("-----parent-------");
                System.out.println(parent);
                // 兄弟节点中至少有一个红色节点

                if (isBlack(sibling.right)){
                    // 如果兄弟节点左边是黑色节点 需要先旋转一下
                    rotateRight(sibling);
                    sibling = parent.right;
                }
                // 兄弟节点继承父节点的颜色
                color(sibling, colorOf(parent));
                black(sibling.right);
                black(parent);
                rotateLeft(parent);


            }
        }else {
            // 删除黑色子节点是右子节点
            // 删除节点的兄弟节点是红色的情况
            // 将兄弟节点是红色的转化为黑色的 和下面黑色的兄弟节点的进行合并处理
            if (isRed(sibling)){
                black(sibling);
                red(parent);
                rotateRight(parent);
                sibling = parent.left;
            }

            // 下面是删除节点的兄弟节点是黑色
            if (isBlack(sibling.left) && isBlack(sibling.right)){
                // 没有红色子节点 父节点下溢
                boolean parentBlack = isBlack(parent);
                red(sibling);
                black(parent);
                if (parentBlack){
                    // 如果之前的父节点为黑色 还会产生下溢 接着执行删除
                    afterRemove(parent, null);
                }


            }else {
                // 兄弟节点中至少有一个红色节点

                if (isBlack(sibling.left)){
                    // 如果兄弟节点左边是黑色节点 需要先旋转一下
                    rotateLeft(sibling);
                    sibling = parent.left;
                }
                // 兄弟节点继承父节点的颜色
                color(sibling, colorOf(parent));
                black(sibling.left);
                black(parent);
                rotateRight(parent);

            }
        }




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
