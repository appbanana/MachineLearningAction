package com.jqc;
import com.jqc.tools.Integers;
import com.jqc.tools.Times;

import java.util.Arrays;

public class Main {

    public static void main(String[] args) {
        testBubble();
    }

    static void testBubble(){
//        Integer[] array = Integers.random(10, 1, 20);
//        System.out.println(Arrays.toString(array));
//        bubbleSort1(array);
//        System.out.println(Arrays.toString(array));
//
////        Integer[] array2 = Integers.ascOrder(1, 10);
//        Integer[] array2 = Integers.random(10, 1, 20);
//        System.out.println(Arrays.toString(array2));
//        bubbleSort2(array2);
//        System.out.println(Arrays.toString(array2));
//
//        Integer[] array3 = Integers.tailAscOrder(1, 20, 5);
//        System.out.println(Arrays.toString(array3));
//        bubbleSort3(array3);
//        System.out.println(Arrays.toString(array3));

        Integer[] array4 = Integers.tailAscOrder(1, 10000, 2000);
        Times.test("bubbleSort1", () -> {
            bubbleSort1(Integers.copy(array4));
        });

        Times.test("bubbleSort2", () -> {
            bubbleSort2(Integers.copy(array4));
        });

        Times.test("bubbleSort3", () -> {
            bubbleSort3(Integers.copy(array4));
        });
    }

    static void bubbleSort1(Integer[] array){
        /**
         * 冒泡排序 原理 比较相邻两个元素的大小, 如果前一个比后一个大的话,交换顺序 每一轮筛选出剩下数据的最大值
         */
        for (int i = array.length - 1; i > 0; i--) {
            for (int j = 1; j <= i; j++) {
                if (array[j - 1] > array[j]) {
                    int temp = array[j - 1];
                    array[j - 1] = array[j];
                    array[j] = temp;
                }
            }
        }
    }

    static void bubbleSort2(Integer[] array){
        /**
         * 优化版1  如果数组已经是升序的话 扫描一次就直接结束
         */
        for (int i = array.length - 1; i > 0; i--) {
            boolean sorted = true;
            for (int j = 1; j <= i; j++) {
                if(array[j - 1] > array[j]){
                    Integer temp = array[j - 1];
                    array[j - 1] = array[j];
                    array[j] = temp;
                    sorted = false;
                }
            }
            if (sorted) break;
        }
    }

    static void bubbleSort3(Integer[] array) {
        /***
         * 冒泡排序 优化2 这个主要针对数组部分有序的情况
         */

        for (int i = array.length - 1; i > 0; i--) {
            // 初始值在数组完全有序时有用
            Integer sortedIndex = 1;
            for (int j = 1; j <= i; j++) {
                if (array[j - 1] > array[j]) {
                    Integer temp = array[j - 1];
                    array[j - 1] = array[j];
                    array[j] = temp;
                    sortedIndex = j;
                }
            }
            i = sortedIndex;
        }

    }



}
