import com.jqc.heap.BinaryHeap;
import com.jqc.printer.BinaryTrees;

public class Main {

    public static void main(String[] args) {
        Integer[] data = { 40, 48, 57, 83, 16, 50, 9, 19};
        BinaryHeap<Integer> heap = new BinaryHeap<>();
        for (int i = 0; i < data.length; i++) {
            heap.add(data[i]);
        }
        BinaryTrees.println(heap);
    }
}
