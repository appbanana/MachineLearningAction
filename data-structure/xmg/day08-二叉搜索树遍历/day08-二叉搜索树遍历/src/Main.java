//import tree.BinarySearchTree;

//package tree;

import printer.BinaryTrees;
import tree.BinarySearchTree;

import java.util.Comparator;
import tree.BinarySearchTree.Visitor;

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

        // 最终升级 使用java官方的Comparator
        BinarySearchTree<Person> bst2 = new BinarySearchTree<>(new Comparator<Person>() {
            @Override
            public int compare(Person o1, Person o2) {
                return o2.getAge() - o1.getAge();
            }
        });
        for (int i = 0; i < data.length; i++) {
            bst2.add(new Person(data[i]));
        }
        BinaryTrees.println(bst2);
    }

    // 测试 添加
    static void test3() {
        Integer data[] = new Integer[] {
                7, 4, 9, 2, 5
        };

        BinarySearchTree<Integer> bst = new BinarySearchTree<>();
        for (int i = 0; i < data.length; i++) {
            bst.add(data[i]);
        }

        BinaryTrees.println(bst);

        bst.add(10);
        bst.add(1);
        bst.add(5);
        BinaryTrees.println(bst);

    }
    // 测试 二叉搜索树的遍历
    static void test4() {
        BinarySearchTree<Integer> bst = new BinarySearchTree<>();
//		for (int i = 0; i < 6; i++) {
//			bst.add((int)(Math.random() * 100));
//		}
        Integer data[] = new Integer[] {
                7, 4, 9, 2, 5, 8, 11, 3, 12, 1
        };
        for (int i = 0; i < data.length; i++) {
            bst.add(data[i]);
        }
        BinaryTrees.println(bst);

        System.out.println("***------***");

        // 前序遍历
//		bst.preorderTraversal();

        // 改进后
//        bst.preorderTraversal(new Visitor<Integer>() {
//            @Override
//            public void visit(Integer element) {
//                System.out.println(element);
//            }
//        });
//        bst.preorder(new Visitor<Integer>() {
//            @Override
//            public void visit(Integer element) {
//                System.out.println(element);
//            }
//        });

        // 中序遍历
//        bst.inorder(new Visitor<Integer>() {
//            @Override
//            public void visit(Integer element) {
//                System.out.println(element);
//            }
//        });

//        bst.inorder1(new Visitor<Integer>() {
//            @Override
//            public void visit(Integer element) {
//                System.out.println(element);
//            }
//        });

        // 后序遍历
//        bst.postorder(new Visitor<Integer>() {
//            @Override
//            public void visit(Integer element) {
//                System.out.println(element);
//            }
//        });

//        bst.postorder1(new Visitor<Integer>() {
//            @Override
//            public void visit(Integer element) {
//                System.out.println(element);
//            }
//        });

        // 层序遍历
        bst.levelOrder(new Visitor<Integer>() {
            @Override
            public void visit(Integer element) {
                System.out.println(element);
            }
        });

    }

    // 测试完全二叉树  高度
    static void test5() {
        BinarySearchTree<Integer> bst = new BinarySearchTree<>();
		for (int i = 0; i < 6; i++) {
			bst.add((int)(Math.random() * 100));
		}
//        Integer data[] = new Integer[] {
//                7, 4, 9, 2, 5, 8, 11, 3, 12, 1
//        };
        Integer data[] = new Integer[] {
                7, 4, 9, 2, 5, 8, 11, 3, 1
        };
        for (int i = 0; i < data.length; i++) {
            bst.add(data[i]);
        }
        BinaryTrees.println(bst);

        System.out.println("***------***");
        System.out.println(bst.isComplete());
        System.out.println(bst.height());
        System.out.println(bst.height1());

        System.out.println(bst.toString());

    }

    // 测试前驱 后继
    static void test6() {
        BinarySearchTree<Integer> bst = new BinarySearchTree<>();
//        for (int i = 0; i < 6; i++) {
//            bst.add((int)(Math.random() * 100));
//        }
        Integer data[] = new Integer[] {
                7, 4, 9, 2, 5, 8, 11, 3, 12, 1
        };

        for (int i = 0; i < data.length; i++) {
            bst.add(data[i]);
        }
        BinaryTrees.println(bst);

        System.out.println("***------***");


    }
    public static void main(String[] args) {
        System.out.println("Hello World!");
//        test1();
//        test2();
//        test3();
//        test4();
//        test5();
        test6();
    }

}
