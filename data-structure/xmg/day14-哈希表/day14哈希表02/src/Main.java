import com.jqc.map.HashMap;
import com.jqc.model.Key;
import com.jqc.model.SubKey1;
import com.jqc.model.SubKey2;
import com.jqc.file.Files;
import com.jqc.file.FileInfo;

public class Main {
//    static void test1() {
//        String string = "jack";
//        int hashcode = 0;
//        for (int i = 0; i < string.length(); i++) {
//            hashcode = hashcode * 31 + string.charAt(i);
//            // 这两句等价 其实31 = 2^5 - 1 只不过位运算符操作更快
////            hashcode = (hashcode << 5) - hashcode + string.charAt(i);
//        }
//        System.out.println(hashcode);
//
//
//    }
//    static void test2() {
//        // 如果想要这两个person一样 那你必须要重写hashCode和equals方法 这个还是主要看业务需求，看你想怎么来规定
//        Person p1 = new Person(10, 1.67f, "jack");
//        Person p2 = new Person(10, 1.67f, "jack");
//
//        Map<Object, Object> map = new HashMap<>();
//        map.put("jack", 1);
//        map.put("rose", 2);
//        map.put("jack", 3);
//        map.put(6, 4);
//        map.put(p1, 5);
//        map.put(p2, 7);
//        map.put(null, 6);
//
////        System.out.println(map.size());
////		System.out.println(map.remove("jack"));
////		System.out.println(map.get("jack"));
////		System.out.println(map.size());
//
////        System.out.println(map.containsKey(p1));
////        System.out.println(map.containsKey(null));
////        System.out.println(map.containsValue(6));
////        System.out.println(map.containsValue(1));
//
////        System.out.println(map.get(p1));
//
//        map.traversal(new Map.Visitor<Object, Object>() {
//            @Override
//            public boolean visit(Object key, Object value) {
//				System.out.println(key + "_" + value);
//                return false;
//            }
//        });
//
//
//    }

//    static void test3() {
//        HashMap<Object, Integer> map = new HashMap<>();
//        for (int i = 1; i <= 19; i++) {
//            map.put(new Key(i), i);
//        }
//
//        map.print();
//        System.out.println(map.get(new Key(1)));
//
//    }

    static void test2(HashMap<Object, Integer> map) {
        for (int i = 1; i <= 20; i++) {
            map.put(new Key(i), i);
        }
        for (int i = 5; i <= 7; i++) {
            map.put(new Key(i), i + 5);
        }


        Asserts.test(map.size() == 20);
        Asserts.test(map.get(new Key(4)) == 4);
        Asserts.test(map.get(new Key(5)) == 10);
        Asserts.test(map.get(new Key(6)) == 11);
        Asserts.test(map.get(new Key(7)) == 12);
        Asserts.test(map.get(new Key(8)) == 8);
    }

    static void test3(HashMap<Object, Integer> map) {
        map.put(null, 1); // 1
        map.put(new Object(), 2); // 2
        map.put("jack", 3); // 3
        map.put(10, 4); // 4
        map.put(new Object(), 5); // 5
        map.put("jack", 6);
        map.put(10, 7);
        map.put(null, 8);
        map.put(10, null);
        Asserts.test(map.size() == 5);
        Asserts.test(map.get(null) == 8);
        Asserts.test(map.get("jack") == 6);
        Asserts.test(map.get(10) == null);
        Asserts.test(map.get(new Object()) == null);
        Asserts.test(map.containsKey(10));
        Asserts.test(map.containsKey(null));
        Asserts.test(map.containsValue(null));
        Asserts.test(map.containsValue(1) == false);
    }

    static void test4(HashMap<Object, Integer> map) {
        map.put("jack", 1);
        map.put("rose", 2);
        map.put("jim", 3);
        map.put("jake", 4);
        for (int i = 1; i <= 10; i++) {
            map.put("test" + i, i);
            map.put(new Key(i), i);
        }
        for (int i = 5; i <= 7; i++) {
            Asserts.test(map.remove(new Key(i)) == i);
        }
        for (int i = 1; i <= 3; i++) {
            map.put(new Key(i), i + 5);
        }
        Asserts.test(map.size() == 21);
        Asserts.test(map.get(new Key(1)) == 6);
        Asserts.test(map.get(new Key(2)) == 7);
        Asserts.test(map.get(new Key(3)) == 8);
        Asserts.test(map.get(new Key(4)) == 4);
        Asserts.test(map.get(new Key(5)) == null);
        Asserts.test(map.get(new Key(6)) == null);
        Asserts.test(map.get(new Key(7)) == null);
        Asserts.test(map.get(new Key(8)) == 8);
    }

    static void test5(HashMap<Object, Integer> map) {
        for (int i = 1; i <= 20; i++) {
            map.put(new SubKey1(i), i);
        }
        map.put(new SubKey2(1), 5);
        Asserts.test(map.get(new SubKey1(1)) == 5);
        Asserts.test(map.get(new SubKey2(1)) == 5);
        Asserts.test(map.size() == 20);
    }

    static void test1() {
        String filepath = "/Users/apple/Desktop/src/java";
        FileInfo fileInfo = Files.read(filepath, null);
        String[] words = fileInfo.words();

        System.out.println("总行数：" + fileInfo.getLines());
        System.out.println("单词总数：" + words.length);
        System.out.println("-------------------------------------");

//		java.util.HashMap<String, Integer> map = new java.util.HashMap<>();
//
//		for (String word : words) {
//			Integer count = map.get(word);
//			count = count == null ? 0 : count;
//			map.put(word, count + 1);
//		}
//		System.out.println(map.size()); // 17188

        HashMap<String, Integer> map = new HashMap<>();
        Times.test(map.getClass().getName(), new Times.Task() {
            @Override
            public void execute() {
                for (String word : words) {
                    Integer count = map.get(word);
                    count = count == null ? 0 : count;
                    map.put(word, count + 1);
                }
                System.out.println(map.size()); // 17188

                int count = 0;
                for (String word : words) {
                    Integer i = map.get(word);
                    count += i == null ? 0 : i;
                    map.remove(word);
                }
                Asserts.test(count == words.length);
                Asserts.test(map.size() == 0);
            }
        });
    }

    public static void main(String[] args) {
        // 哈希冲突是里面的元素可能是计算出来的hash值是一样，也可能是hash值不一样但是对应的索引是一样的

        // java hashmap key必须实现hashCode和equal方法
        // hashCode：如果不实现的话，会调用系统的hashCode，会默认
        // equal： 方法是当哈希冲突时，我们先根据key找到对应索引，
        // 在拿这个key和链表或者红黑树中的元素比较相等不相等，会调用你自己实现的equal方法，
        // 如果相等就覆盖，不相等就添加进去

        // 计算索引的时候会调用hashCode 哈希冲突的时候会调用equals
//        System.out.println("Hello World!");

//        test1();
//            test2();
//            test3();

//        // afterRotate 在这个方法里面忘记改root
//        test2(new HashMap<>());
//        test3(new HashMap<>());
//        // 在remove(Node<K, V> node) 忘记修改index(node)
//        test4(new HashMap<>());

        test1();
    }
}
