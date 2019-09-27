package com.jqc.sort;

public class MergeSort<T extends Comparable<T>> extends Sort<T> {
    private T[] leftArray;

    @Override
    protected void sort() {
        leftArray = (T[]) new Comparable[array.length >> 1];
        sort(0, array.length);
    }

    /**
     * [begin, end) 范围的数据把元素分割成单个元素 然后对数据进行归排序
     * @param begin 开始点
     * @param end 结束点
     */
    private void sort(int begin, int end) {
        // 如果里面只有一个元素 直接返回
        if (end - begin < 2) return;
        int mid = (begin + end) >> 1;
        sort(begin, mid);
        sort(mid, end);
        merge(begin, mid, end);
    }

    /**
     * 将 [begin, mid) 和 [mid, end) 范围的序列合并成一个有序序列
     * @param begin
     * @param mid
     * @param end
     */
    private void merge(int begin, int mid, int end) {
        int li = 0, le = mid - begin;
        int ri = mid, re = end;
        int ai = begin;

        // 备份左边数组
        for (int i = li; i < le; i++) {
            leftArray[i] = array[begin + i];
        }
        while (li < le) {
            if (ri < re && cmpElement(array[ri], leftArray[li]) < 0) {
//                array[ai] = array[ri];
//                ri++;
//                ai++;
                // 上面三句可以整合成一句
                array[ai++] = array[ri++];
            }else {
                array[ai++] = leftArray[li++];
            }
        }
    }
}
