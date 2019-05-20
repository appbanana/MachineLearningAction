package com.jqc.map;

import java.util.Comparator;
import java.util.Objects;

public class HashMap<K, V> implements Map<K, V> {

    private static final boolean RED = false;
    private static final boolean BLACK = true;
    private Comparator<K> comparator;
    private int size;
    private Node<K, V> root;

    private Node<K, V>[] table;
    private static final int DEFAULT_CAPACITY = 1 << 4;

    @Override
    public int size() {
        return size;
    }

    @Override
    public boolean isEmpty() {
        return size == 0;
    }

    @Override
    public void clear() {
        if (size == 0) return;
        for (int i = 0; i < table.length; i++) {
            table[i] = null;
        }
        size = 0;

    }

    @Override
    public V put(K key, V value) {
        return add(key, value);
    }

    @Override
    public V get(K key) {
        Node<K, V> node = node(key);
        return node != null ? node.value : null;
    }

    @Override
    public V remove(K key) {
        return remove(node(key));
    }

    @Override
    public boolean containsKey(K key) {
        return false;
    }

    @Override
    public boolean containsValue(V value) {
        return false;
    }

    @Override
    public void traversal(Visitor<K, V> visitor) {

    }

    private V add(K key, V value){
//        elementNotNullCheck(key);
        // 更具key 找到对应的索引 key-->hash值-->找到对应的索引
        int index = index(key);
        Node<K, V> root= table[index];
        if (root == null){
            // 第一个节点为跟节点
            root = new Node<>(key, value, null);
            table[index] = root;

            // 添加完元素后进行 avl树调整
            afterAdd(root);
            size++;
            return null;
        }

        // 暂存节点的父节点
        Node<K, V> parent = root;
        Node<K, V> node = root;
        int cmp = 0;
        int hash1 = (key == null) ? 0 : key.hashCode();
        while(node != null){
            cmp = compare(key, node.key, hash1, node.hash);
            parent = node;
            if (cmp > 0){
                node = node.right;
            }else if (cmp < 0){
                node = node.left;
            }else {
                // 相等的元素直接进行覆盖
                node.key = key;
                V oldValue = value;
                node.value = oldValue;
                return oldValue;
            }
        }

        // 接下来我要执行添加节点功能，一方面我需要父节点，另一方面我需要知道添加到父节点的左边还是右边
        Node<K, V> newNode = new Node<>(key, value, parent);
        if (cmp > 0){
            parent.right = newNode;
        }else{
            parent.left = newNode;
        }
        // 添加完元素后进行 avl树调整
        afterAdd(newNode);
        size++;

        return null;

    }

    private void afterAdd(Node<K, V> node) {
        Node<K, V> parent = node.parent;
        // 如果添加的是跟节点 直接染成黑色就可以
        if (parent == null) {
            black(node);
            return;
        }
        // 如果父节点是黑色的 有4中情况 不用作任何处理
        if (isBlack(parent)) return;

        // 获取到叔父节点
        Node<K, V> uncle = parent.sibling();
        Node<K, V> grand = parent.parent;

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

    private void rotateLeft(Node<K, V> grand) {

        Node<K, V> parent = grand.right;
        Node<K, V> child = parent.left;
        grand.right = child;
        parent.left = grand;

        afterRotate(grand, parent, child);

    }

    private void rotateRight(Node<K, V> grand) {
        Node<K, V> parent = grand.left;
        Node<K, V> child = parent.right;

        grand.left = child;
        parent.right = grand;

        afterRotate(grand, parent, child);

    }

    private void afterRotate(Node<K, V> grand, Node<K, V> parent, Node<K, V> child){
        // 让parent 成为新的跟节点
        parent.parent = grand.parent;
        if (grand.isLeftChild()){
            grand.parent.left = parent;
        }else if (grand.isRightChild()){
            grand.parent.right = parent;
        }else {
            root = parent;
        }

        // 更新child的parent
        if (child != null){
            child.parent = grand;
        }
        grand.parent = parent;
    }

    private int index(K key) {
        if (key == null) return 0;
        int hash = key.hashCode();
        return hash & (table.length - 1);

    }

    private int index(Node<K, V> node) {
        return node.hash & (table.length - 1);

    }

    private Node<K, V> node(K key) {
        Node<K, V> node = table[index(key)];
        int hash1 = key.hashCode();
        while (node != null){
            int cmp = compare(key, node.key, hash1, node.hash);
            if (cmp == 0) return node;
            if (cmp > 0) {
                node = node.right;
            }else if (cmp < 0){
                node = node.left;
            }
        }

        return null;
    }


    // 真正的删除逻辑 使用前驱和后继都可以 这里使用后继进行替换要删除的节点
    // 删除节点 有三种类型 删除度为2的几点，此时删除的是它的前驱后后继 他的前驱或者后继只能是度为0或者度为1的节点
    // 删除度为1的节点 删除度为0的节点
    private V remove(Node<K, V> node) {
        if (node == null) return null;
        size--;
        V oldValue = node.value;

        if (node.hasTwoChildren()){
            Node<K, V> s = successor(node);
            node.key = s.key;
            node.value = s.value;
            // 赋值为node  node就是接下来要删除的节点
            node = s;
        }

        // 接下来就是删除度为0或者为1的节点
        Node<K, V> replacement = (node.left != null) ? node.left : node.right;
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

        return oldValue;


    }

    private void afterRemove(Node<K, V> node) {
        // 如果删除的节点是红色 直接删掉就可以 不需要其他操作
//        if (isRed(node)) return;

        // 接下来就是删除黑色的节点
        // 1) 黑色节点有2个红色的子节点 2）该黑色节点有1个红色的子节点 3) 该节点有0个红色的子节点

        // 第一种情况 如果删除的黑色节点有两个红色的子节点 实际上删除的是该黑色节点的前驱或者后继 这种请款暂不处理
        // 第二种情况 该黑色节点有1个红色的子节点 直接将替代的红色节点染成黑色
        if (isRed(node)){
            black(node);
            return;
        }

        // 接下来就是删除黑色的叶子节点  可能会产生下溢
        Node<K, V> parent = node.parent;
        // 为空的话 删除的则是根节点
        if (parent == null) return;
        // 判断删除的节点是left 还是right
        boolean left = parent.left == null || node.isLeftChild();
        Node<K, V> sibling = left ? parent.right : parent.left;
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
                    afterRemove(parent);
                }


            }else {
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
                    afterRemove(parent);
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


    // 寻找当前节点的后继 node.right.left.left...
    private Node<K, V> successor(Node<K, V> node) {
        if (node == null) return null;
        Node<K, V> p = node.right;
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


    /**
         * @return 返回值等于0，代表e1和e2相等；返回值大于0，代表e1大于e2；返回值小于于0，代表e1小于e2
         */
    private int compare(K k1, K k2, int hash1, int hash2) {
        // 比较哈希值
        int result = hash1 - hash2;
        // 如果hash值不相等 直接返回
        if (result != 0) return result;

        // 如果两个值相等 直接返回0
        if (Objects.equals(k1, k2)) return 0;

        // 哈希值相等 但是不equals
        if (k1 != null && k2 != null){

            // 比较类名
            String k1cls = k1.getClass().getName();
            String k2cls = k2.getClass().getName();
            result = k1cls.compareTo(k2cls);
            if (result != 0) return result;

            if (k1 instanceof Comparable){
                return ((Comparable)k1).compareTo(k2);
            }
        }
        // 同一种类型，哈希值相等，但是不equals，但是不具备可比较性
        return System.identityHashCode(k1) - System.identityHashCode(k2);
    }

    private void elementNotNullCheck(K key) {
        if (key == null) {
            throw new IllegalArgumentException("key must not be null");
        }
    }

    private boolean isBlack(Node<K, V> node){
        return colorOf(node) == BLACK;
    }

    private boolean isRed(Node<K, V> node){
        return colorOf(node) == RED;
    }

    // 上色
    private Node<K, V> color(Node<K, V> node, boolean color){
        node.color = color;
        return node;
    }

    private Node<K, V> black(Node<K, V> node){
        return  color(node, BLACK);
    }

    private Node<K, V> red(Node<K, V> node){
        return  color(node, RED);
    }

    private boolean colorOf(Node<K, V> node){
        return node == null ? BLACK : node.color;
    }


    private class Node<K, V> {
        K key;
        V value;
        int hash; // key的hash值
        Node<K, V> left;
        Node<K, V> right;
        Node<K, V> parent;
        boolean color = RED;

        public Node( K key, V value, Node<K, V> parent) {
            this.key = key;
            this.value = value;
            this.parent = parent;
            this.hash = key == null ? 0 : key.hashCode();
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
        public Node<K, V> sibling() {
            if (isLeftChild()){
                return parent.right;
            }
            if (isRightChild()){
                return parent.left;
            }
            return null;
        }
    }

}
