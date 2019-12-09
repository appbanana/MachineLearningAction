package com.jqc.greedy.plus;

/**
 * 模型 古董模型
 * @author appbanana
 * @date 2019/11/26
 */
public class Article {
    // 重量
    public int weight;
    // 价值
    public int value;
    // 价值密度
    public double valueDensity;

    public Article(int weight, int value) {
        this.weight = weight;
        this.value = value;
        this.valueDensity = value * 1.0 / weight;
    }

    @Override
    public String toString() {
        return "Article{" +
                "weight=" + weight +
                ", value=" + value +
                ", valueDensity=" + valueDensity +
                '}';
    }
}
