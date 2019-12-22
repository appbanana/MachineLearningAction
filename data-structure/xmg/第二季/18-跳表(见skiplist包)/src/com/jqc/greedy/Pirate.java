package com.jqc.greedy;

import java.util.Arrays;

/**
 * 最简单的海盗问题 看看最多能放多少件古董
 * @author appbanana
 * @date 2019/11/26
 */
public class Pirate {
    public static void main(String[] args) {
        // 古董的重量
        int[] weights = {3, 5, 4, 10, 7, 14, 2, 11};
        Arrays.sort(weights);
        int capacity = 30, weight = 0, count = 0;
        for (int i = 0; i < weights.length && weight < capacity; i++) {
            int newWeight = weight + weights[i];
            if (newWeight < capacity) {
                weight = newWeight;
                count++;
            }
        }
        System.out.println("一共选了" + count + "件古董");
    }
}
