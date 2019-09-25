package com.jqc.sort;

public class BubbleSort1<T extends Comparable<T>> extends Sort<T> {
    @Override
    protected void sort() {
        for (int end = array.length - 1; end > 0; end--) {
            for (int begin = 1; begin <= end; begin++) {
                if (cmp(begin-1, begin) > 0) {
                    swap(begin-1, begin);
                }
            }
        }
    }




}
