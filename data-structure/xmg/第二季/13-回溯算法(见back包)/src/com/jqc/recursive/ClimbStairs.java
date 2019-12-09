package com.jqc.recursive;

/**
 * @author appbanana
 * @date 2019/11/18
 */
public class ClimbStairs {

    public static void main(String[] args) {

    }

    /**
     * 爬楼梯跟斐波那契数列很像
     * @param n
     * @return
     */
    int climbStairs(int n) {
        if (n <= 2) return n;
        return climbStairs(n - 1) + climbStairs(n - 2);
    }
}
