package com.jqc;
import java.util.Arrays;

import com.jqc.tools.Asserts;
import com.jqc.tools.Integers;
import com.jqc.tools.Times;
import com.jqc.sort.Sort;
import com.jqc.sort.BubbleSort1;
import com.jqc.sort.BubbleSort2;
import com.jqc.sort.BubbleSort3;
import com.jqc.sort.HeapSort;
import com.jqc.sort.SelectionSort;
import com.jqc.sort.InsertionSort1;
import com.jqc.sort.InsertionSort2;
import com.jqc.sort.InsertionSort3;
import com.jqc.sort.MergeSort;

public class Main {

    public static void main(String[] args) {
        // 测试二分搜索
        testBinarySearch();
        Integer[] array = Integers.random(10000, 1, 10000);
        testSorts(array,
                new BubbleSort3(),
                new SelectionSort(),
                new HeapSort(),
                new InsertionSort1(),
                new InsertionSort2(),
                new InsertionSort3(),
                new MergeSort()
        );

    }

    static void testSorts(Integer[] array, Sort... sorts) {
        for(Sort sort: sorts) {
            Integer[] newArray = Integers.copy(array);
            sort.sort(newArray);
            Asserts.test(Integers.isAscOrder(newArray));
        }
        // 这就需要自定义比较器
        Arrays.sort(sorts);
        for(Sort sort: sorts) {
            System.out.println(sort);
        }
    }

    static void testBinarySearch() {
        int[] array = {2, 4, 8, 8, 8, 12, 14};
        // 二叉搜索有个问题就是当数组中有多个相同的元素 返回的索引不固定
//		Asserts.test(BinarySearch.search(array, 8) == 2);
		Asserts.test(BinarySearch.indexOf(array, 2) == 0);
		Asserts.test(BinarySearch.indexOf(array, 14) == 6);
		Asserts.test(BinarySearch.indexOf(array, 12) == 5);
    }


}
