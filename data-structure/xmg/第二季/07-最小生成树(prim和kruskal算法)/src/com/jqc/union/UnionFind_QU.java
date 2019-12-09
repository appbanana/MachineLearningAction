package com.jqc.union;

public class UnionFind_QU extends UnionFind {

    public UnionFind_QU(int capacity) {
        super(capacity);
    }

    /**
     * 通过链条找到根节点
     * @param v
     * @return
     */
    @Override
    public int find(int v) {
        rangeCheck(v);
        while (parents[v] != v) {
            v = parents[v];
        }
        return v;
    }

    /**
     * 合并数据集 让v1的根节点指向v2的根节点
     * @param v1
     * @param v2
     */
    @Override
    public void union(int v1, int v2) {
        int p1 = find(v1);
        int p2 = find(v2);

        if (p1 == p2) return;
        parents[p1] = p2;
    }
}
