package com.jqc.union;

/**
 * 基于rank的优化 矮的服从高的
 */
public class UnionFind_QU_R extends UnionFind_QU {
    private int[] ranks;
    public UnionFind_QU_R(int capacity) {
        super(capacity);

        ranks = new int[capacity];
        // 初始化树的高度都为1
        for (int i = 0; i < capacity; i++) {
            ranks[i] = 1;
        }
    }

    /**
     * 合并数据集 矮的合并到高的上
     * @param v1
     * @param v2
     */
    @Override
    public void union(int v1, int v2) {
        int p1 = find(v1);
        int p2 = find(v2);
        if (p1 == p2) return;

        if (ranks[p1] < ranks[p2]) {
            parents[p1] = p2;
        } else if (ranks[p1] > ranks[p2]){
            parents[p2] = p1;
        }else {
            parents[p1] = p2;
            ranks[p2]+= 1;
        }
    }
}
