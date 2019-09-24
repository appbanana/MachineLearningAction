//import tree.BinarySearchTree;

//package tree;

import printer.BinaryTrees;
import tree.BinarySearchTree;
import tree.Comparator;


public class Main {
//    static void test1() {
//        Integer data[] = new Integer[] {
//                7, 4, 9, 2, 5, 8, 11, 3, 12, 1
//        };
//
//        BinarySearchTree<Integer> bst = new BinarySearchTree<>();
//        for (int i = 0; i < data.length; i++) {
//            bst.add(data[i]);
//        }
//
//        BinaryTrees.println(bst);
//    }


    static void test2() {
        // 对于比较 不能在里面写死 尽量能够让外边能够自定义规则 第一种思路就是定义接口，让闯进来的模型去遵守这个interface，去实现这个接口
        // 缺点 还是只能定义一种比较逻辑 只不过在对应模型中实现
        Integer data[] = new Integer[] {
                7, 4, 9, 2, 5, 8, 11, 3, 12, 1
        };

        BinarySearchTree<Person> bst1 = new BinarySearchTree<>();
        for (int i = 0; i < data.length; i++) {
            bst1.add(new Person(data[i]));
        }

        BinaryTrees.println(bst1);

        // 这个较上一个的好处就是可以提供个性化比较服务
        BinarySearchTree<Person> bst2 = new BinarySearchTree<>(new Comparator<Person>() {
            @Override
            public int compareTo(Person e1, Person e2) {
                return e2.getAge() - e1.getAge();
            }
        });
        for (int i = 0; i < data.length; i++) {
            bst2.add(new Person(data[i]));
        }
        BinaryTrees.println(bst2);
    }

    public static void main(String[] args) {
        System.out.println("Hello World!");
//        test1();
        test2();
    }
}
