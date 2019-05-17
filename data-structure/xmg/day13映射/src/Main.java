import com.jqc.map.TreeMap;
import com.jqc.map.Map;
import com.jqc.map.Map.Visitor;
import com.jqc.file.Files;
import com.jqc.file.FileInfo;
import com.jqc.set.Set;
import com.jqc.set.TreeSet;

public class Main {

    static void test1() {
        Map<String, Integer> map = new TreeMap<>();
        map.put("c", 2);
        map.put("a", 5);
        map.put("b", 6);
        map.put("a", 8);

        map.traversal(new Visitor<String, Integer>() {
            public boolean visit(String key, Integer value) {
                System.out.println(key + "_" + value);
                return false;
            }
        });
    }

    static void test2() {
        FileInfo fileInfo = Files.read("/Users/apple/Desktop/src",
                new String[]{"java"});

        System.out.println("文件数量：" + fileInfo.getFiles());
        System.out.println("代码行数：" + fileInfo.getLines());
        String[] words = fileInfo.words();
        System.out.println("单词数量：" + words.length);

        Map<String, Integer> map = new TreeMap<>();
        for (int i = 0; i < words.length; i++) {
            Integer count = map.get(words[i]);
            count = (count == null) ? 1 : (count + 1);
            map.put(words[i], count);
        }

        for (int i = 0; i < words.length; i++) {
            map.containsKey(words[i]);
        }


//        map.traversal(new Visitor<String, Integer>() {
//            public boolean visit(String key, Integer value) {
//                System.out.println(key + "_" + value);
//                return false;
//            }
//        });
    }

    static void test3() {
        TreeSet<Integer> set = new TreeSet<>();
        Integer data[] = new Integer[] {
                39, 85, 21, 64, 34, 77, 59, 47, 97, 75, 44, 89, 23
        };
        for (int i = 0; i < data.length; i++) {
            set.add(data[i]);
        }

        set.traversal(new Set.Visitor<Integer>() {
            @Override
            public boolean visit(Integer element) {
                System.out.println(element);
                return false;
            }
        });
    }

    public static void main(String[] args) {
//        System.out.println("Hello World!");
//        test1();
//        test2();
//        Times.test("TreeMap", new Times.Task() {
//            public void execute() {
//                test2();
//            }
//        });

        // 红黑树 遍历 21, 23, 34, 39, 44, 47, 59, 64, 75, 77, 85, 89, 97
        test3();

    }
}
