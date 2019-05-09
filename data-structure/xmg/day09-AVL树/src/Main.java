
import printer.BinaryTrees;
import tree.AVLTree;



public class Main {
//    static void test1() {
//        Integer data[] = new Integer[] {
////                7, 4, 9, 2, 5, 11, 3, 12, 1
//                7, 4, 9, 2, 5, 11, 3, 10
//
//        };
//
//        AVLTree<Integer> avl = new AVLTree<>();
//        for (int i = 0; i < data.length; i++) {
//            avl.add(data[i]);
//
//             System.out.println("【" + data[i] + "】");
//             BinaryTrees.println(avl);
//             System.out.println("---------------------------------------");
//        }
//
//        BinaryTrees.println(avl);
//
//    }

    static void test2() {
        Integer data[] = new Integer[] {
				67, 52, 92, 96, 53, 95, 13, 63, 34, 82, 76, 54, 9, 68, 39
        };

        AVLTree<Integer> avl = new AVLTree<>();
        for (int i = 0; i < data.length; i++) {
            avl.add(data[i]);
            System.out.println("【" + data[i] + "】");
            BinaryTrees.println(avl);
            System.out.println("---------------------------------------");
        }

        System.out.println("---------remove-----------------remove-------remove------");

        for (int i = 0; i < data.length; i++) {
			avl.remove(data[i]);
			System.out.println("【" + data[i] + "】");
			BinaryTrees.println(avl);
			System.out.println("---------------------------------------");
		}


        // BinaryTrees.println(avl);

    }

    public static void main(String[] args) {
//        test1();
        test2();
    }


}
