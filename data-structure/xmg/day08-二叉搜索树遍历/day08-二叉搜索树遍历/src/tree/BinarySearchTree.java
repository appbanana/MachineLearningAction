/**
 * Created by apple on 2019/5/6.
 */

package tree;

import printer.BinaryTreeInfo;
import java.util.Comparator;
import java.util.LinkedList;
import java.util.Stack;
import java.util.Queue;

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
        root = null;
        size = 0;
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

    // 删除 其实删除的是他的前驱后继
    public void remove(E element) {
        remove(node(element));
    }

    public boolean contains(E element) {
        return node(element) != null;
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
        Node<E> replacement = node.left != null ? node.left : node.right;
        if (replacement == null){
            // replacement 为空说明此时节点的度为0，这时是要删除度为0的节点
            if (node == node.parent.left){
                node.parent.left = null;
            }else {
                node.parent.right = null;
            }
        }else if (node.parent == null){
            // 要删除度为1的节点 切为根节点
            root = null;
        }else {
            // node的度为1 但不是根节点
            replacement.parent = node.parent;
            if (node.parent == null){
                root = replacement;
            }else if (node == node.parent.left){
                node.parent.left = replacement;
            }else {
                node.parent.right = replacement;
            }
        }

    }
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
    /**
     * 迭代实现 层序遍历 第一层->第二层->第三层...
     */
    public void levelOrder(Visitor<E> visitor) {
        if (root == null || visitor == null) return;

        Queue<Node<E>> queue = new LinkedList<>();
        queue.offer(root);
        while (!queue.isEmpty()){
            Node<E> temp = (Node<E>)queue.poll();
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
        Queue<Node<E>> queue = new LinkedList<>();
        queue.offer(root);
        // 用来标记叶子节点
        boolean leaf = false;
        while (!queue.isEmpty()){
            Node<E> node = queue.poll();

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
        Queue<Node<E>> queue = new LinkedList<>();
        queue.offer(root);
        int levelSize = 1;
        int height = 0;
        // 用来标记叶子节点
        while (!queue.isEmpty()){
            Node<E> node = queue.poll();
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

    public int height(Node<E> node) {
        if (node == null) return 0;
        return 1 + Math.max(height(node.left), height(node.right));
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

    // 寻找当前节点的前驱 node.left.right.right...
    private Node<E> predecessor(Node<E> node) {
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
    private Node<E> successor(Node<E> node) {
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
    private static class Node<E> {
        E element;
        Node<E> left;
        Node<E> right;

        Node<E> parent;
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
        Node<E> myNode = (Node<E>)node;
        String parentString = "null";
        if (myNode.parent != null) {
            parentString = myNode.parent.element.toString();
        }
        return myNode.element + "_p(" + parentString + ")";
    }
}
