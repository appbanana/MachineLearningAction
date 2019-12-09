package com.jqc;

public class BinarySearch {
    /**
     * 二叉搜索
     * @param array  数组容器
     * @param element 待查找的元素
     * @return 返回索引, -1代表没找到
     */
    public static int indexOf(int[] array, int element) {
        if (array == null || array.length == 0) return -1;
        int begin = 0;
        int end = array.length;

        while (begin < end) {
            int mid = (begin + end) >> 1;
            if (element < array[mid]) {
                end = mid;
            }else if (element > array[mid]) {
                begin = mid + 1;
            }else {
                return mid;
            }
        }
        return -1;
    }
}
