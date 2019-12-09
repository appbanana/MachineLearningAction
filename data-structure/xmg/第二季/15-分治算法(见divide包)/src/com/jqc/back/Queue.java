package com.jqc.back;

import java.util.Map;

/**
 * 8皇后问题
 * @author appbanana
 * @date 2019/11/21
 */
public class Queue {
    public static void main(String[] args) {
        new Queue().placeQueue(8);
    }

    // 索引代表行号 元素代表列号
    int[] cols;
    // 一共有多少种方法
    int ways;

    void placeQueue(int n) {
        if (n < 1) return;
        cols = new int[n];
        place(0);
        System.out.println(n + "皇后一共有" + ways + "种摆法");
    }

    /**
     * 从row行开始摆放皇后
     * @param row
     */
    void  place(int row) {
        if (row == cols.length) {
            ways++;
            show();
            return;
        }
        for (int col = 0; col < cols.length; col++) {
            if (isValid(row, col)) {
                cols[row] = col;
                place(row + 1);
            }
        }
    }

    /**
     * 判断row行col列是否可以摆放皇后
     * @param row
     * @param col
     * @return
     */
    boolean isValid(int row, int col) {
        for (int i = 0; i < row; i++) {
            if (cols[i] == col) {
//                System.out.println("[" + row + "][" + col + "]=false");
                return false;
            }

            // 斜率为正负1, 所以绝对值是相等的
            if (row - i == Math.abs(col - cols[i])) {
//                System.out.println("[" + row + "][" + col + "]=false");
                return false;
            }
        }
//        System.out.println("[" + row + "][" + col + "]=true");
        return true;
    }

    void show() {
        for (int row = 0; row < cols.length; row++) {
            for (int col = 0; col < cols.length; col++) {
                if (cols[row] == col) {
                    System.out.print("1 ");
                }else {
                    System.out.print("0 ");
                }
            }
            System.out.println();
        }
        System.out.println("------------------------------");
    }
}
