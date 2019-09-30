package com.jqc.sort;

public class BubbleSort3<T extends Comparable<T>> extends Sort<T> {
    @Override
    protected void sort() {
        // 改进方案三: 这个是在方案二的基础进一步改进, 主要针对数组部分有序的情况
        for (int end = array.length - 1; end > 0; end--) {
            Integer sortedIndex = 1;
            for (int begin = 1; begin <= end; begin++) {
                if (cmp(begin-1, begin) > 0) {
                    swap(begin-1, begin);
                    sortedIndex = begin;
                }
            }
            end = sortedIndex;
        }
    }




}
