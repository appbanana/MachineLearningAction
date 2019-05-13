
import printer.BinaryTrees;
import tree.RBTree;
import tree.AVLTree;



public class Main {


    static void test2() {
        Integer data[] = new Integer[] {
				67, 52, 92, 96, 53, 95, 13, 63, 34, 82, 76, 54, 9, 68, 39
        };

        RBTree<Integer> avl = new RBTree<>();
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
        test2();
    }


}
