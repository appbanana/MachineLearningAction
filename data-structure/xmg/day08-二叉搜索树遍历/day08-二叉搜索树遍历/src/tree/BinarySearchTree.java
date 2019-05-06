/**
 * Created by apple on 2019/5/6.
 */

package tree;

import printer.BinaryTreeInfo;
import java.util.Comparator;
import java.util.Stack;

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
                // 相等的元素直接进行覆盖
                node.element = element;
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

//    /**
//     * 前序遍历 根 左 右
//     */
//    public void preorderTraversal() {
//        preorderTraversal(root);
//    }
//
//    private void preorderTraversal(Node<E> node){
//        if (node == null) return;
//        System.out.println(node.element);
//        preorderTraversal(node.left);
//        preorderTraversal(node.right);
//
//    }

    /**
     * 递归实现 前序遍历 根 左 右 这次要想办法把元素传到外边 供用户使用
     */
    public void preorderTraversal(Visitor<E> visitor) {
        preorderTraversal(root, visitor);
    }

    private void preorderTraversal(Node<E> node, Visitor<E> visitor){
        if (node == null) return;
        visitor.visit(node.element);
        preorderTraversal(node.left, visitor);
        preorderTraversal(node.right, visitor);

    }
    /**
     * 迭代实现 前序遍历 根 左 右 这次要想办法把元素传到外边 供用户使用
     */
    public void preorder(Visitor<E> visitor){
        Stack stack = new Stack<>();
        Node<E> node = root;
        stack.push(node);
        while (!stack.isEmpty()){
            node = (Node<E>)stack.pop();
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
    public void inorder(Visitor<E> visitor) {
        inorder(root, visitor);
    }

    public void inorder(Node<E> node, Visitor<E> visitor) {
        if (node == null) return;
        inorder(node.left, visitor);
        visitor.visit(node.element);
        inorder(node.right, visitor);
    }

    /**
     * 迭代实现 中序遍历 左 根 右
     */
    public void inorder1(Visitor<E> visitor) {
        Stack stack = new Stack<>();
        Node<E> node = root;
        while (node != null || !stack.isEmpty()){
            if (node != null){
                stack.push(node);
                node = node.left;

            }else {
                Node<E> temp = (Node<E>)stack.pop();
                visitor.visit(temp.element);
                node = temp.right;
            }
        }
    }

    /**
     * 递归实现 后序遍历 左 右 根
     */
    public void postorder(Visitor<E> visitor) {
        postorder(root, visitor);
    }

    private void postorder(Node<E> node, Visitor<E> visitor) {
        if (node == null) return;
        postorder(node.left, visitor);
        postorder(node.right, visitor);
        visitor.visit(node.element);
    }

    /**
     * 迭代实现 后序遍历 左 右 根
     */
    public void postorder1(Visitor<E> visitor) {
        Stack stack = new Stack<>();
        Stack value_stack = new Stack<>();
        Node<E> node = root;
        stack.push(node);
        while (!stack.isEmpty()){
            Node<E> temp = (Node<E>)stack.pop();
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

    private void elementNotNullCheck(E element) {
        if (element == null) {
            throw new IllegalArgumentException("element must not be null");
        }
    }

    // 相当于block
    public static interface Visitor<E>{
        void visit(E element);
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
