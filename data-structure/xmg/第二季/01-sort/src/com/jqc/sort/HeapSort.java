package com.jqc.sort;

public class HeapSort extends Sort {
    private int heapSize;

    @Override
    protected void sort() {
        heapSize = array.length;

        // 先批量建堆
        for (int i = (heapSize >> 1) -1; i >= 0; i--) {
            shiftDown(i);
        }
        // 交换第一个元素和最后一个元素的位置 shiftDown
        while (heapSize > 1) {
            swap(0, --heapSize);
            shiftDown(0);
        }

    }

    private void shiftDown(Integer index) {
        Integer element = array[index];
        int half = heapSize >> 1;

        while (index < half) {
            // index必须是非叶子节点
            int childIndex = (index << 1) + 1;
            int child = array[childIndex];

            int rightIndex = childIndex + 1;
            // 右子节点值大于左子节点值
            if (rightIndex < heapSize && cmpElement(array[rightIndex],  child) > 0) {
                childIndex = rightIndex;
                child = array[childIndex];
            }

            // 大于最大节点的值 直接结束
            if (cmpElement(element, child) >= 0) break;

            //
            array[index] = child;
            index = childIndex;

        }
        array[index] = element;
    }

    private void siftDown(int index) {
        Integer element = array[index];

        int half = heapSize >> 1;
        while (index < half) { // index必须是非叶子节点
            // 默认是左边跟父节点比
            int childIndex = (index << 1) + 1;
            Integer child = array[childIndex];

            int rightIndex = childIndex + 1;
            // 右子节点比左子节点大
            if (rightIndex < heapSize &&
                    cmpElement(array[rightIndex], child) > 0) {
                child = array[childIndex = rightIndex];
            }

            // 大于等于子节点
            if (cmpElement(element, child) >= 0) break;

            array[index] = child;
            index = childIndex;
        }
        array[index] = element;
    }


}
