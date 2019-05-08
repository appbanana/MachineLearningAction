
import printer.BinaryTrees;
import tree.AVLTree;



public class Main {
    static void test1() {
        Integer data[] = new Integer[] {
//                7, 4, 9, 2, 5, 11, 3, 12, 1
                7, 4, 9, 2, 5, 11, 3, 12

        };

        AVLTree<Integer> avl = new AVLTree<>();
        for (int i = 0; i < data.length; i++) {
            avl.add(data[i]);

             System.out.println("【" + data[i] + "】");
             BinaryTrees.println(avl);
             System.out.println("---------------------------------------");
        }

        BinaryTrees.println(avl);

//        bst.remove(7);
//
//        BinaryTrees.println(bst);
    }

    public static void main(String[] args) {
        test1();
    }


}
