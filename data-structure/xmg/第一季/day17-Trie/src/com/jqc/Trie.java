package com.jqc;

import java.util.HashMap;

public class Trie<V> {

    private int size;
    private Node<V> root;


    public int size(){
        return size;
    }

    public boolean isEmpty(){
        return size == 0;
    }

    public void clear(){
        size = 0;
        root = null;

    }

    public V get(String key){
        Node<V> node = node(key);
        return node == null ? null : node.value;

    }

    // 是否包含某个完整的字符串
    public boolean contains(String key){
        Node<V> node = node(key);
        return node(key) != null && node.word;
    }

    public V add(String key, V value){
        keyCheck(key);
        if (root == null) {
            root = new Node<>(null);
        }
        Node<V> node = root;
        int len = key.length();
        for (int i = 0; i < len; i++) {
            char c = key.charAt(i);
            boolean emptyChildren = node.children == null;
            Node<V> childNode = emptyChildren ? null : node.children.get(c);
            if (childNode == null){
                childNode = new Node<>(node);
                childNode.character = c;
                node.children = emptyChildren ? new HashMap<>() : node.children;
                node.children.put(c, childNode);
            }

            node = childNode;
        }

        if (node.word) {
            // 如果已经存在这个单词 直接覆盖
            V oldValue = node.value;
            node.value = value;
            return oldValue;
        }

        // 新增一个单词
        node.word = true;
        node.value = value;
        size++;
        return null;
    }

    public V remove(String key) {
        Node<V> node = node(key);
        // 如果node没找到 或者他不是单词的结尾 直接返回
        if (node == null || !node.word) return null;
        size--;
        V oldValue = node.value;

        // 如果还有其他子节点 把word置为false
        if (node.children != null && !node.children.isEmpty()){
            node.word = false;
            node.value = null;
            return oldValue;
        }

        Node<V> parent = null;
        while ((parent = node.parent) != null) {
            parent.children.remove(node.character);
            if (parent.word || !parent.children.isEmpty()) break;
            node = parent;
        }
        return oldValue;
    }

    public boolean startsWith(String prefix){
        keyCheck(prefix);

//        Node<V> node = root;
//        int len = prefix.length();
//        for (int i = 0; i < len; i++) {
//            char c = prefix.charAt(i);
//            node = node.getChildren().get(c);
//            if (node == null) return false;
//        }
//        return true;

        return node(prefix) != null;
    }

    private Node<V> node(String key) {
        keyCheck(key);

        Node<V> node = root;
        int len = key.length();
        for (int i = 0; i < len; i++) {
            if (node == null || node.children == null || node.children.isEmpty()) return null;
            char c = key.charAt(i);
            node = node.children.get(c);
        }
        return node;
    }

    private void keyCheck(String key) {
        if (key == null || key.length() == 0) {
            throw new IllegalArgumentException("key must not be empty");
        }
    }

    private static class Node<V> {
        HashMap<Character, Node<V>> children;
        V value;
        boolean word;
        Character character;
        Node<V> parent;

        public Node(Node<V> parent){
            this.parent = parent;
        }


//        public HashMap<Character, Node<V>> getChildren() {
//            return children == null ? (children = new HashMap<>()) : children;
//        }

    }
}
