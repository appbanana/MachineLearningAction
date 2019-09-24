package com.jqc.sort;
import java.text.DecimalFormat;

public abstract class Sort implements Comparable<Sort> {
    protected Integer[] array;
    private int cmpCount;
    private int swapCount;
    private long time;
    private DecimalFormat fmt = new DecimalFormat("#.00");


    public void sort(Integer[] array) {
        if (array == null || array.length < 2) return;
        this.array = array;

        long begin = System.currentTimeMillis();
        sort();
        time = System.currentTimeMillis() - begin;
    }

    // 子类排序 具体实现方法 子类必须实现
    protected abstract void sort();

    /**
     *
     * @param index1 第一个索引
     * @param index2 第二个索引
     * @return 当array[index1] < arrray[index2], 返回小于0 ;
     * 当array[index1] = arrray[index2], 返回 等于0 ;
     * 当array[index1] > arrray[index2], 返回大于0 ;
     */
    protected int cmp(Integer index1, Integer index2) {
        cmpCount++;
        return array[index1] - array[index2];
    }

    /**
     * 两个元素比较大小
     * @param e1 第一个元素
     * @param e2 第二个元素
     * @return e1 > e2, 返回大于0; e1 = e2, 返回等于0; e1 < e2, 返回小于0
     */
    protected int cmpElement(Integer e1, Integer e2) {
        return e1 - e2;
    }

    protected void swap(Integer index1, Integer index2) {
        swapCount++;
        Integer temp = array[index1];
        array[index1] = array[index2];
        array[index2] = temp;
    }

    @Override
    public int compareTo(Sort o) {
        int result = (int)(time - o.time);
        if (result != 0) return result;
        result = cmpCount - o.cmpCount;
        if (result != 0) return result;

        return swapCount - o.swapCount;
    }

    @Override
    public String toString() {
        String timeStr = "耗时:" + (time / 1000) + "s(" + time + "ms)";
        String compareCountStr = "比较:" + numberString(cmpCount);
        String swapCountStr = "交换:" + numberString(swapCount);
        return "【" + getClass().getSimpleName() + "】\n"
                + timeStr + "\t"
                + compareCountStr + "\t"
                + swapCountStr + "\t";
//                + "------------------------------------";

    }

    private String numberString(int number) {
        if (number < 10000) return "" + number;
        if (number < 100000000) return fmt.format(number / 10000) + "万";
        return fmt.format(number / 100000000) + "亿";
    }

}
