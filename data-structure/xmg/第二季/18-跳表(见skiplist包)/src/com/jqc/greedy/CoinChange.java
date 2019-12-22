package com.jqc.greedy;

import java.util.Arrays;

/**
 * 贪心算法解决换零钱问题 零钱数量最少
 * @author appbanana
 * @date 2019/11/26
 */
public class CoinChange {
    public static void main(String[] args) {
//        coinChange2();

		coinChange(new Integer[] {25, 10, 5, 1}, 41);

//        coinChange(new Integer[] {25, 20, 5, 1}, 41);
    }
    static void coinChange(Integer[] faces, int money) {
        // 零钱按面值大小将序排序
        Arrays.sort(faces, (Integer num1, Integer num2) -> num2 - num1);
        int i = 0, count = 0;
        while (i < faces.length) {
            if (money < faces[i]) {
                // 如果money小于
                i++;
                continue;
            }

            System.out.println("面值为" + faces[i] + "的零钱");
            money -= faces[i];
            count++;
        }

        System.out.println("使用零钱的数量" + count);

    }

    static void coinChange2() {
        int[] faces = {25, 5, 20, 1};
        int money = 41, count = 0;
        Arrays.sort(faces);
        for (int i = faces.length - 1; i >= 0; i--) {
            while (money >= faces[i]) {
                System.out.println("面值" + faces[i]);
                money -= faces[i];
                count++;
            }
        }
        System.out.println("找零钱数量" + count);
    }

}