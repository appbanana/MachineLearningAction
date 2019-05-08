//import tree.BinarySearchTree;

//package tree;

import printer.BinaryTrees;
import tree.BinarySearchTree;

import java.util.Comparator;
import tree.BinaryTree.Visitor;

public class Main {
    static void test1() {
        Integer data[] = new Integer[] {
                7, 4, 9, 2, 5, 8, 11, 3, 12, 1
        };

        BinarySearchTree<Integer> bst = new BinarySearchTree<>();
        for (int i = 0; i < data.length; i++) {
            bst.add(data[i]);
        }

        BinaryTrees.println(bst);

        bst.remove(7);

        BinaryTrees.println(bst);
    }

    public static void main(String[] args) {
        test1();
    }


}
