package com.jqc.skiplist;

import org.omg.CORBA.PRIVATE_MEMBER;

import java.util.Comparator;

public class SkipList<K, V> {

    public static final int MAX_LEVEL = 32;
    public static final double P = 0.25;
    private int size;
    private Comparator<K> comparator;

    // 有效层数
    private int level;

    // 不放任何元素的节点
    private Node<K, V> first;

    public SkipList(Comparator<K> comparator) {
        this.comparator = comparator;
        first = new Node<>(null, null, MAX_LEVEL);
    }

    public SkipList() {
        this(null);
    }

    /**
     * 返回元素的个数
     * @return
     */
    public int size() {
        return size;
    }

    /**
     * 判断跳表是否为空
     * @return
     */
    public boolean isEmpty() {
        return size == 0;
    }

    /**
     * 根据key获取对应的value
     * @param key
     * @return
     */
    public V get(K key) {
        keyCheck(key);
        Node<K, V> node = first;
        for (int i = level - 1; i >= 0; i--) {
            int cmp = -1;
            while (node.nexts[i] != null && (cmp = compare(key, node.nexts[i].key)) > 0) {
                node = node.nexts[i];
            }
            if (cmp == 0) {
                Node<K, V> curNode = node.nexts[i];
                return curNode.value;
            }
        }
        return null;
    }
    /**
     * 跳表中添加key-value
     * @param key
     * @param value
     * @return
     */
    public V put(K key, V value) {
        keyCheck(key);
        Node<K, V> node = first;
        Node<K, V>[] prevs = new Node[level];
        for (int i = level - 1; i >= 0; i--) {
            int cmp = -1;
            while (node.nexts[i] != null && (cmp = compare(key, node.nexts[i].key)) > 0) {
                node = node.nexts[i];
            }
            if (cmp == 0) {
                // 存在则覆盖
                Node<K, V> curNode = node.nexts[i];
                V oldVal = curNode.value;
                node.nexts[i].value = value;
                return oldVal;
            }
            prevs[i] = node;
        }

        // 新节点的层数
        int newLevel = randomLevel();
        // 添加新节点
        Node<K, V> newNode = new Node<>(key, value, newLevel);
        for (int i = 0; i < newLevel; i++) {
            if (i >= level) {
                first.nexts[i] = newNode;
            }else {
                newNode.nexts[i] = prevs[i].nexts[i];
                prevs[i].nexts[i] = newNode;
            }
        }
        size++;
        // 更新跳表的有效层数
        level = Math.max(level, newLevel);
        return null;
    }

    public V remove(K key) {
        keyCheck(key);
        Node<K, V> node = first;
        Node<K, V>[] prevs = new Node[level];
        boolean exists = false;
        for (int i = level - 1; i >= 0; i--) {
            int cmp = -1;
            while (node.nexts[i] != null && (cmp = compare(key, node.nexts[i].key)) > 0) {
                node = node.nexts[i];
            }
            prevs[i] = node;
            if (cmp == 0) exists = true;
        }

        if (!exists) return null;
        // for循环结束 ndoe是要删除节点的前驱， 而且即将被删除的节点至少有一层
        // 需要被删除的节点
        Node<K, V> removedNode = node.nexts[0];

        // 设置后继 removedNode.nexts.length即为跳表的层数
        for (int i = 0; i < removedNode.nexts.length; i++) {
            prevs[i].nexts[i] = removedNode.nexts[i];
        }

        // 更新跳表层数 从头节点出发， 如果first节点指向的节点为null， 则level需要减1
        int newLevel = level;
        while (--newLevel > 0 && first.nexts[newLevel] == null) {
            level = newLevel;
        }

        size--;
        return removedNode.value;
    }


    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("一共" + level + "层").append("\n");
        for (int i = level - 1; i >= 0; i--) {
            Node<K, V> node = first;
            while (node.nexts[i] != null) {
                sb.append(node.nexts[i]);
                sb.append(" ");
                node = node.nexts[i];
            }
            sb.append("\n");
        }
        return sb.toString();
    }

    private int compare(K k1, K k2) {
        return comparator != null ? comparator.compare(k1, k2) : ((Comparable) k1).compareTo(k2);
    }

    /**
     * 随机生成层数
     * @return
     */
    private int randomLevel() {
        int level = 1;
        while (Math.random() < P && level < MAX_LEVEL) {
            level++;
        }
        return level;
    }

    private void keyCheck(K key) {
        if (key == null) {
            throw new IllegalArgumentException("key must not be null.");
        }
    }

    private static class Node<K, V> {
        K key;
        V value;
        Node<K, V>[] nexts;

        public Node(K key, V value, int level) {
            this.key = key;
            this.value = value;
            nexts = new Node[level];
        }

        @Override
        public String toString() {
            return key + ":" + value + "_" + nexts.length;
        }
    }
}
