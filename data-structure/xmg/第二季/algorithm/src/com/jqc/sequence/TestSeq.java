package com.jqc.sequence;

import com.jqc.tools.Asserts;

public class TestSeq {
    public static void main(String[] args) {
        // 测试蛮力匹配
        testBruteForce();
        // 测试优化后的蛮力匹配
        testBruteForce1();
        // 测试KMP算法
        testKMP();
    }

    public static void testBruteForce() {
        Asserts.test(BruteForce.indexOf("Hello World", "H") == 0);
        Asserts.test(BruteForce.indexOf("Hello World", "d") == 10);
        Asserts.test(BruteForce.indexOf("Hello World", "or") == 7);
        Asserts.test(BruteForce.indexOf("Hello World", "abc") == -1);
    }

    public static void testBruteForce1() {
        Asserts.test(BruteForce1.indexOf("Hello World", "H") == 0);
        Asserts.test(BruteForce1.indexOf("Hello World", "d") == 10);
        Asserts.test(BruteForce1.indexOf("Hello World", "or") == 7);
        Asserts.test(BruteForce1.indexOf("Hello World", "abc") == -1);
    }
    public static void testKMP() {
        Asserts.test(KMP.indexOf("Hello World", "H") == 0);
        Asserts.test(KMP.indexOf("Hello World", "d") == 10);
        Asserts.test(KMP.indexOf("Hello World", "or") == 7);
        Asserts.test(KMP.indexOf("Hello World", "abc") == -1);
    }
}
