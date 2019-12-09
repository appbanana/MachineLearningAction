package com.jqc.recursive;

/**
 * @author appbanana
 * @date 2019/11/18
 */
public class TailCall {

    public static void main(String[] args) {
        System.out.println(facttorial(5));
    }

    /**
     * n阶乘 尾递归优化
     * @param n
     * @return
     */
    static int facttorial(int n) {
        return facttorial(n, 1);
    }

    static int facttorial(int n, int result) {
        if (n <= 1) return result;
        return facttorial(n -1, result * n);
    }
}
