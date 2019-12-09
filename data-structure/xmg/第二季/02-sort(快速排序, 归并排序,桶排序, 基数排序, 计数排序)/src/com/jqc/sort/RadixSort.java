package com.jqc.sort;

/**
 * 基数排序 基数排序是基于计数排序完成的
 */
public class RadixSort extends Sort<Integer> {
    @Override
    protected void sort() {
//        sort0();
        sort1();
    }

    /**
     * 基数排序的第一种思路
     */
    private void sort0() {
        // 找出最大值
        int max = array[0];
        for (int i = 0; i < array.length; i++) {
            if (array[i] > max) {
                max = array[i];
            }
        }

        // 个位数: array[i] / 1 % 10 = 3
        // 十位数：array[i] / 10 % 10 = 9
        // 百位数：array[i] / 100 % 10 = 5
        // 千位数：array[i] / 1000 % 10 = ...
        for (int divider = 1; divider <= max; divider *= 10) {
            countSort(divider);
        }
    }

    /**
     * 计数排序
     * @param devider 权重
     */
    private void countSort(int devider) {
        // 开辟内存空间 总共最多有10个数 所以开辟10个内存空间
        int[] counts = new int[10];

        // 统计每个整数(个位, 十位, 百位...)出现的次数
        for (int i = 0; i < array.length; i++) {
            counts[array[i] / devider % 10]++;
        }

        // 统计整数累计出现的次数
        for (int i = 1; i < counts.length; i++) {
            counts[i] += counts[i - 1];
        }

        int[] newArray = new int[array.length];
        for (int i = array.length; i >= 0; i--) {
            newArray[--counts[array[i] / devider % 10]] = array[i];
        }

        // 将排好序的数组放到原数组中
        for (int i = 0; i < array.length; i++) {
            array[i] = newArray[i];
        }
    }

    /**
     * 基数排序的第二种思路 使用二维数组来完成
     */
    private void sort1() {
        // 找出最大值
        int max = array[0];
        for (int i = 0; i < array.length; i++) {
            if (array[i] > max) {
                max = array[i];
            }
        }

        // 桶数组
        int[][] buckets = new int[10][array.length];
        int[] bucketsSize = new int[buckets.length];
        for (int diveider = 1; diveider <= max; diveider *= 10) {
            for (int i = 0; i < array.length; i++) {
                int num = array[i] / diveider % 10;
                buckets[num][bucketsSize[num++]] = array[i];
            }
            int index = 0;
            for (int i = 0; i < buckets.length; i++) {
                for (int j = 0; j < bucketsSize[i]; j++) {
                    array[index++] = buckets[i][j];
                }
                bucketsSize[i] = 0;
            }
        }

        
    }
}

