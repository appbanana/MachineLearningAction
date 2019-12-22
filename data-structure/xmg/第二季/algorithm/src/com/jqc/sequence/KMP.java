package com.jqc.sequence;

public class KMP {

    /**
     * 串匹配
     * @param text  被匹配字符串
     * @param pattern 匹配字符串
     * @return 返回匹配字符串在text中的索引
     */
    public static int indexOf(String text, String pattern) {
        if (text == null || pattern == null) return -1;
        char[] textCharArr = text.toCharArray();
        char[] patternCharArr = pattern.toCharArray();
        int tlen = textCharArr.length;
        int plen = patternCharArr.length;
        // 如果长度为0 或者匹配字符串的长度大于被匹配字符串的长度， 直接返回-1
        if (tlen == 0 || plen == 0 || tlen < plen) return -1;
        // 利用匹配字符串求next数组（next表） 未优化
//        int[] next = next(pattern);
        // 优化后的next表
        int[] next = next2(pattern);
        int ti = 0;
        int pi = 0;
        while ( pi < plen && ti < tlen) {
            if (pi < 0 || textCharArr[ti] == patternCharArr[pi]) {
                // 如果匹配成功 ti，pi都向后移动一位
                ti++;
                pi++;
            }else {
                pi = next[pi];
            }
        }

        return pi == plen ? ti - pi  : -1;
    }

    /**
     * 构造next表
     * @param pattern 模式字符串（匹配字符串）
     * @return next数组
     */
    private static int[] next2(String pattern) {
        char[] chars = pattern.toCharArray();
        int[] next = new int[chars.length];
        next[0] = -1;
        // 索引 下面要根据索引i往next数组插入元素
        int i = 0;
        int n = -1;
        int imax = chars.length - 1;
        while (i < imax) {
            if (n < 0 || chars[i] == chars[n]) {
                ++i;
                ++n;
                if (chars[i] == chars[n]) {
                    next[i] = next[n];
                }else {
                    next[i] = n;
                }
            }else {
                n = next[n];
            }
        }
        return next;
    }
    /**
     * 构造next表
     * @param pattern 模式字符串（匹配字符串）
     * @return next数组
     */
    private static int[] next(String pattern) {
        char[] chars = pattern.toCharArray();
        int[] next = new int[chars.length];
        next[0] = -1;
        // 索引 下面要根据索引i往next数组插入元素
        int i = 0;
        int n = -1;
        int imax = chars.length - 1;
        while (i < imax) {
            if (n < 0 || chars[i] == chars[n]) {
                next[++i] = ++n;
            }else {
                n = next[n];
            }
        }
        return next;
    }
}
