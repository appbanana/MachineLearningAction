package com.jqc.sort;

public class InsertionSort3<T extends Comparable<T>> extends Sort<T> {

    /**
     * 思路: 优化方案二 采用二分搜索查找待插入的位置,相比上一种优化, 是减少了比较次数, 挪动次数还是一样的
     */
    @Override
    protected void sort() {
        for (int begin = 1; begin < array.length; begin++) {
            T val = array[begin];
            int insertIndex = search(begin);
//            for (int i = begin - 1; i >= insertIndex; i--) {
//                array[begin] = array[begin - 1];
//            }
            // 这个方法和上面的功能是一样的 但是下面这个效率高
            for (int i = begin; i > insertIndex ; i--) {
                array[begin] = array[begin - 1];
            }
            array[insertIndex] = val;
        }
    }

    /**
     * 查找待插入的位置
     * @param index
     * @return
     */
    private int search(int index) {
        int begin = 0;
        int end = index;
        while (begin < end) {
            int mid = (begin + end) >> 1;
            if (cmpElement(array[index], array[mid]) < 0) {
                end = mid;
            }else {
                begin = mid + 1;
            }
        }
        return begin;
    }
}
