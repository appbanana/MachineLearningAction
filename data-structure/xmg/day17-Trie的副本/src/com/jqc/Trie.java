package com.jqc;

import java.util.HashMap;

public class Trie<V> {

    private int size;
    private Node<V> root = new Node<>();


    public int size(){
        return size;
    }

    public boolean isEmpty(){
        return size == 0;
    }

    public void clear(){
        size = 0;
        root.getChildren().clear();

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
        Node<V> node = root;
        int len = key.length();
        for (int i = 0; i < len; i++) {
            char c = key.charAt(i);
            Node<V> childNode = node.getChildren().get(c);
            if (childNode == null){
                childNode = new Node<>();
                node.getChildren().put(c, childNode);
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

    public boolean startsWith(String prefix){
        keyCheck(prefix);

        Node<V> node = root;
        int len = prefix.length();
        for (int i = 0; i < len; i++) {
            char c = prefix.charAt(i);
            node = node.getChildren().get(c);
            if (node == null) return false;
        }
        return true;
    }

    private Node<V> node(String key) {
        keyCheck(key);

        Node<V> node = root;
        int len = key.length();
        for (int i = 0; i < len; i++) {
            char c = key.charAt(i);
            node = node.getChildren().get(c);
            if (node == null) return null;
        }
        return node.word ? node : null;
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


        public HashMap<Character, Node<V>> getChildren() {
            return children == null ? (children = new HashMap<>()) : children;
        }

    }
}
