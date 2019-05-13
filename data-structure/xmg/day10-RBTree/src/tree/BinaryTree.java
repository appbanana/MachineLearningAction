package tree;

import printer.BinaryTreeInfo;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Stack;

/**
 * Created by apple on 2019/5/8.
 */
public class BinaryTree<E> implements BinaryTreeInfo {
    protected int size;
    protected Node<E> root;

    public int size(){
        return size;
    }

    public boolean isEmpty(){
        return size == 0;
    }

    public void clear(){
        root = null;
        size = 0;
    }



    /**
     * 递归实现 前序遍历 根 左 右 这次要想办法把元素传到外边 供用户使用
     */
    public void preorderTraversal(BinarySearchTree.Visitor<E> visitor) {
        preorderTraversal(root, visitor);
    }

    private void preorderTraversal(BinarySearchTree.Node<E> node, BinarySearchTree.Visitor<E> visitor){
        if (node == null) return;
        visitor.visit(node.element);
        preorderTraversal(node.left, visitor);
        preorderTraversal(node.right, visitor);

    }
    /**
     * 迭代实现 前序遍历 根 左 右 这次要想办法把元素传到外边 供用户使用
     */
    public void preorder(BinarySearchTree.Visitor<E> visitor){
        Stack stack = new Stack<>();
        BinarySearchTree.Node<E> node = root;
        stack.push(node);
        while (!stack.isEmpty()){
            node = (BinarySearchTree.Node<E>)stack.pop();
            visitor.visit(node.element);

            if (node.right != null){
                stack.push(node.right);

            }
            if (node.left != null){
                stack.push(node.left);
            }
        }

    }

    /**
     * 递归实现 中序遍历 左 根 右
     */
    public void inorder(BinarySearchTree.Visitor<E> visitor) {
        inorder(root, visitor);
    }

    public void inorder(BinarySearchTree.Node<E> node, BinarySearchTree.Visitor<E> visitor) {
        if (node == null) return;
        inorder(node.left, visitor);
        visitor.visit(node.element);
        inorder(node.right, visitor);
    }

    /**
     * 迭代实现 中序遍历 左 根 右
     */
    public void inorder1(BinarySearchTree.Visitor<E> visitor) {
        Stack stack = new Stack<>();
        BinarySearchTree.Node<E> node = root;
        while (node != null || !stack.isEmpty()){
            if (node != null){
                stack.push(node);
                node = node.left;

            }else {
                BinarySearchTree.Node<E> temp = (BinarySearchTree.Node<E>)stack.pop();
                visitor.visit(temp.element);
                node = temp.right;
            }
        }
    }

    /**
     * 递归实现 后序遍历 左 右 根
     */
    public void postorder(BinarySearchTree.Visitor<E> visitor) {
        postorder(root, visitor);
    }

    private void postorder(BinarySearchTree.Node<E> node, BinarySearchTree.Visitor<E> visitor) {
        if (node == null) return;
        postorder(node.left, visitor);
        postorder(node.right, visitor);
        visitor.visit(node.element);
    }

    /**
     * 迭代实现 后序遍历 左 右 根
     */
    public void postorder1(BinarySearchTree.Visitor<E> visitor) {
        Stack stack = new Stack<>();
        Stack value_stack = new Stack<>();
        BinarySearchTree.Node<E> node = root;
        stack.push(node);
        while (!stack.isEmpty()){
            BinarySearchTree.Node<E> temp = (BinarySearchTree.Node<E>)stack.pop();
            value_stack.push(temp.element);
            if (temp.left != null){
                stack.push(temp.left);
            }
            if (temp.right != null){
                stack.push(temp.right);
            }
        }

        while (!value_stack.isEmpty()){
            visitor.visit((E) value_stack.pop());
        }

    }
    /**
     * 迭代实现 层序遍历 第一层->第二层->第三层...
     */
    public void levelOrder(BinarySearchTree.Visitor<E> visitor) {
        if (root == null || visitor == null) return;

        Queue<BinarySearchTree.Node<E>> queue = new LinkedList<>();
        queue.offer(root);
        while (!queue.isEmpty()){
            BinarySearchTree.Node<E> temp = (BinarySearchTree.Node<E>)queue.poll();
            visitor.visit(temp.element);
            if (temp.left != null){
                queue.offer(temp.left);

            }
            if (temp.right != null){
                queue.offer(temp.right);
            }
        }

    }
    /**
     * 判断是否是完全二叉树
     */
    public boolean isComplete() {
        if (root == null) return false;
        Queue<BinarySearchTree.Node<E>> queue = new LinkedList<>();
        queue.offer(root);
        // 用来标记叶子节点
        boolean leaf = false;
        while (!queue.isEmpty()){
            BinarySearchTree.Node<E> node = queue.poll();

            if (leaf && !node.isLeaf()) return false;
            // 度为2的节点
            if (node.hasTwoChildren()){
                queue.offer(node.left);
                queue.offer(node.right);
            }else if (node.left == null && node.right != null){
                return false;
            }else {
                // 剩下的应该全是叶子节点
                leaf = true;
            }
        }
        return true;
    }

    /**
     * 迭代来实现 返回树的高度
     */
    public int height() {
        if (root == null) return 0;
        Queue<BinarySearchTree.Node<E>> queue = new LinkedList<>();
        queue.offer(root);
        int levelSize = 1;
        int height = 0;
        // 用来标记叶子节点
        while (!queue.isEmpty()){
            BinarySearchTree.Node<E> node = queue.poll();
            levelSize--;
            if (node.left != null){
                queue.offer(node.left);
            }
            if (node.right != null){
                queue.offer(node.right);
            }
            if (levelSize == 0){
                levelSize = queue.size();
                height += 1;
            }
        }
        return height;
    }

    /**
     * 递归来实现 返回树的高度
     */
    public int height1() {
        return height(root);
    }

    public int height(BinarySearchTree.Node<E> node) {
        if (node == null) return 0;
        return 1 + Math.max(height(node.left), height(node.right));
    }

    protected Node<E> createNode(E element, Node<E> parent){
        return new Node<>(element, parent);
    }
    // 寻找当前节点的前驱 node.left.right.right...
    protected Node<E> predecessor(Node<E> node) {
        if (node == null) return null;
        Node<E> p = node.left;
        // 这个可以看做在左子树中找前驱
        if (p != null){
            while (p.right != null){
                p = p.right;
            }
            return p;
        }
        //  左子树为空  这时返回的是当前节点的父节点
        while (node.parent != null && node == node.parent.left){
            node = node.parent;
        }

        // 当只有root节点时，node.parent == null
        return node.parent;
    }

    // 寻找当前节点的后继 node.right.left.left...
    protected Node<E> successor(Node<E> node) {
        if (node == null) return null;
        Node<E> p = node.right;
        // 这个可以看做在右子树中找后继
        if (p != null){
            while (p.left != null){
                p = p.left;
            }
            return p;
        }
        // 右子树为空 父节点不为空
        while (node.parent != null && node == node.parent.right){
            node = node.parent;
        }

        // 当只有root节点时，node.parent == null
        return node.parent;
    }

    // 相当于block
    public static interface Visitor<E>{
        void visit(E element);
    }



    protected static class Node<E> {
        E element;
        BinarySearchTree.Node<E> left;
        BinarySearchTree.Node<E> right;

        BinarySearchTree.Node<E> parent;
        public Node(E element, Node<E> parent) {
            this.element = element;
            this.parent = parent;
        }

        public boolean isLeaf(){
            return left == null && right ==null;
        }

        public boolean hasTwoChildren(){
            return left != null && right != null;
        }

        public boolean isLeftChild(){
            return parent != null && this == parent.left;
        }

        public boolean isRightChild(){
            return parent != null && this == parent.right;
        }

        // 返回兄弟节点
        public Node<E> sibling() {
            if (isLeftChild()){
                return parent.right;
            }
            if (isRightChild()){
                return parent.left;
            }
            return null;
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
//        BinarySearchTree.Node<E> myNode = (Node<E>)node;
//        String parentString = "null";
//        if (myNode.parent != null) {
//            parentString = myNode.parent.element.toString();
//        }
//        return myNode.element + "_p(" + parentString + ")";
        return node;
    }
}
