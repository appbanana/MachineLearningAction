package tree;
import java.util.Comparator;


/**
 * Created by apple on 2019/5/8.
 */
public class AVLTree<E> extends BBST<E> {

    public AVLTree(){
        this(null);
    }

    public AVLTree(Comparator<E> comparator) {
        super(comparator);
    }

    @Override
    protected void afterAdd(Node<E> node) {

        // 因为添加节点只会导致他的祖父节点 或者的祖父的上一级到时失衡 所以要寻找到失衡的那个节点
        while ((node = node.parent) != null){

            // 要判断节点是否平衡
            if (isBalanced(node)){
                // 平衡的话 更新高度
                updateHeight(node);

            }else {
                // 重新恢复平衡
                rebalance(node);
                break;
            }
        }
    }

    @Override
    protected void afterRemove(Node<E> node) {
        // 因为删除节点只会导致他的父节点或者祖父...节点 或者的祖父的上一级到时失衡 所以要寻找到失衡的那个节点
        while ((node = node.parent) != null){

            // 要判断节点是否平衡
            if (isBalanced(node)){
                // 平衡的话 更新高度
                updateHeight(node);

            }else {
                // 重新恢复平衡
                rebalance(node);
            }
        }
    }

    // 二叉搜索树是否平衡
    public boolean isBalanced(Node<E> node){
        return Math.abs(((AVLNode<E>)node).balanceFactor()) <= 1;
    }

    @Override
    protected Node<E> createNode(E element, Node<E> parent) {
        return new AVLNode<>(element, parent);
    }

    @Override
    protected void afterRotate(Node<E> grand, Node<E> parent, Node<E> child) {
        super.afterRotate(grand, parent, child);
        updateHeight(parent);
        updateHeight(grand);
    }

    private void updateHeight(Node<E> node){
        ((AVLNode<E>)node).updateHeight();
    }

    private void rebalance(Node<E> grand){
        // 不平衡的话 要进行旋转
        Node<E> parent = ((AVLNode<E>)grand).tallerChild();
        Node<E> node = ((AVLNode<E>)parent).tallerChild();
        if (parent.isLeftChild()){
            if (node.isLeftChild()){
                // LL 右旋
                rotateRight(grand);
                System.out.println("---LL--");
            }else {
                // LR 先左旋 在右旋
                rotateLeft(parent);
                rotateRight(grand);
                System.out.println("---LR--");

            }
        }else {
            if (node.isLeftChild()){
                // RL 先右旋 在左旋
                rotateRight(parent);
                rotateLeft(grand);
                System.out.println("---RL--");

            }else {
                // RR 左旋
                System.out.println(grand.element);

                rotateLeft(grand);
                System.out.println("---RR--");

            }
        }
    }

    private static class AVLNode<E> extends Node<E> {
        int height = 1;

        public AVLNode(E element, Node<E> parent) {
           super(element, parent);
        }

        // 返回平衡因子
        public int balanceFactor(){
            int leftHeight = left == null ? 0 : ((AVLNode<E>)left).height;
            int rightHeight = right == null ? 0 : ((AVLNode<E>)right).height;
            return leftHeight - rightHeight;
        }

        // 更新节点高度
        public void updateHeight(){
            int leftHeight = left == null ? 0 : ((AVLNode<E>)left).height;
            int rightHeight = right == null ? 0 : ((AVLNode<E>)right).height;
            height = 1 + Math.max(leftHeight, rightHeight);
        }

        public Node<E> tallerChild(){
            int leftHeight = left == null ? 0 : ((AVLNode<E>)left).height;
            int rightHeight = right == null ? 0 : ((AVLNode<E>)right).height;
            if (leftHeight > rightHeight) return left;
            if (rightHeight > leftHeight) return right;
            // 如果相等的话 当前节点是左子树 就返回左节点 否则 返回右节点
            return isLeftChild() ? left : right;
        }

        @Override
        public String toString() {
            String parentString = "null";
            if (parent != null) {
                parentString = parent.element.toString();
            }
            return element + "_p(" + parentString + ")_h(" + height + ")";
        }

    }

}
