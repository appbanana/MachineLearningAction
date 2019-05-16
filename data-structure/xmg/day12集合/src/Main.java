
import com.jqc.set.LinkSet;
import com.jqc.set.Set;
import com.jqc.set.Set.Visitor;
import com.jqc.set.TreeSet;
import com.jqc.file.FileInfo;
import com.jqc.file.Files;
//import Task;

public class Main {
    static void test1() {
//        Set<Integer> list = new LinkSet<>();
//        list.add(10);
//        list.add(11);
//        list.add(11);
//        list.add(12);
//        list.add(10);
//
//
//        list.traversal(new Visitor<Integer>() {
//            @Override
//            public boolean visit(Integer element) {
//                System.out.println(element);
//
//                return false;
//            }
//        });

        Set<Integer> treeSet = new TreeSet<>();
        treeSet.add(10);
        treeSet.add(11);
        treeSet.add(11);
        treeSet.add(12);
        treeSet.add(10);


        treeSet.traversal(new Visitor<Integer>() {
            @Override
            public boolean visit(Integer element) {
                System.out.println(element);

                return false;
            }
        });
    }
    static void testSet(Set<String> set, String[] words) {
        for (int i = 0; i < words.length; i++) {
            set.add(words[i]);
        }
        for (int i = 0; i < words.length; i++) {
            set.contains(words[i]);
        }
        for (int i = 0; i < words.length; i++) {
            set.remove(words[i]);
        }
    }

    static void test2() {
//        FileInfo fileInfo = Files.read("/Users/apple/Desktop/ThirdParty");
        FileInfo fileInfo = Files.read("/Users/apple/Desktop/src/java/util",
                new String[]{"java"});
        System.out.println("文件数量：" + fileInfo.getFiles());
        System.out.println("代码行数：" + fileInfo.getLines());
        String[] words = fileInfo.words();
        System.out.println("单词数量：" + words.length);

        Times.test("ListSet", new Times.Task() {
			public void execute() {
				testSet(new LinkSet<>(), words);
			}
		});

        Times.test("TreeSet", new Times.Task() {
            public void execute() {
                testSet(new TreeSet<>(), words);
            }
        });

    }

    public static void main(String[] args) {
//        System.out.println("Hello World!");
//        test1();
        test2();
    }
}
