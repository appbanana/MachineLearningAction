package com.jqc.sort;

public class BubbleSort2<T extends Comparable<T>> extends Sort<T> {
    @Override
    protected void sort() {
        // 改进方案一: 这种改进主要针对已经排好序(eg:升序), 扫描一遍直接结束
        for (int end = array.length - 1; end > 0; end--) {
            boolean sorted = true;
            for (int begin = 1; begin <= end; begin++) {
                if (cmp(begin-1, begin) > 0) {
                    swap(begin-1, begin);
                    sorted = false;
                }
            }
            if (sorted) break;
        }
    }




}
