
import printer.BinaryTrees;
import tree.RBTree;
import tree.AVLTree;



public class Main {

//    static void test1() {
//        Integer data[] = new Integer[] {
//                7, 4, 9, 2, 1
//        };
//
//        BinarySearchTree<Integer> bst = new BinarySearchTree<>();
//        for (int i = 0; i < data.length; i++) {
//            bst.add(data[i]);
//        }
//        BinaryTrees.println(bst);
//
//        bst.preorder(new Visitor<Integer>() {
//            public boolean visit(Integer element) {
//                System.out.print(element + " ");
//                return element == 2 ? true : false;
//            }
//        });
//        System.out.println();
//
//        bst.inorder(new Visitor<Integer>() {
//            public boolean visit(Integer element) {
//                System.out.print(element + " ");
//                return element == 4 ? true : false;
//            }
//        });
//        System.out.println();
//
//        bst.postorder(new Visitor<Integer>() {
//            public boolean visit(Integer element) {
//                System.out.print(element + " ");
//                return element == 4 ? true : false;
//            }
//        });
//        System.out.println();
//
//        bst.levelOrder(new Visitor<Integer>() {
//            public boolean visit(Integer element) {
//                System.out.print(element + " ");
//                return element == 9 ? true : false;
//            }
//        });
//        System.out.println();
//    }
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
