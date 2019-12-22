package com.jqc.sequence;

public class BruteForce {

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
        int ti = 0;
        int pi = 0;
        while ( pi < plen && ti < tlen) {
            if (textCharArr[ti] == patternCharArr[pi]) {
                // 如果匹配成功 ti，pi都向后移动一位
                ti++;
                pi++;
            }else {
                // 如果匹配失败，pi要归0， ti要在原来索引的基础上加1
                // 能走到这里，说明匹配失败，也同时表明他们目前公共子串长度为pi，
                // 我们只需要拿ti减去（pi - 1）就可以得到pi新的初始位置
                pi = 0;
                ti = ti - (pi - 1);
            }
        }

        return pi == plen ? ti - pi  : -1;
    }
}
