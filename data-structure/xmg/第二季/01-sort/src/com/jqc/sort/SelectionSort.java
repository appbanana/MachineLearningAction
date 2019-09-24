package com.jqc.sort;

public class SelectionSort extends Sort {

    @Override
    protected void sort() {
        /**
         * 选择排序的主要思想 每轮找出最大值,然后与末尾元素交换
         */
        for (int end = array.length - 1; end > 0; end--) {
            Integer maxIndex = 0;
            for (int begin = 0; begin <= end; begin++) {
//                if (array[begin] > array[maxIndex]) {
                if (cmp(begin, maxIndex) > 0) {
                    maxIndex = begin;
                }
            }
//            Integer temp = array[end];
//            array[end] = array[maxIndex];
//            array[maxIndex] = temp;
            swap(maxIndex, end);
        }
    }
}
