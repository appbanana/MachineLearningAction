import com.jqc.map.Map;
import com.jqc.map.HashMap;
import com.jqc.model.Person;
import com.jqc.model.Key;

import com.jqc.printer.BinaryTreeInfo;
import com.jqc.printer.BinaryTrees;

public class Main {
    static void test1() {
        String string = "jack";
        int hashcode = 0;
        for (int i = 0; i < string.length(); i++) {
            hashcode = hashcode * 31 + string.charAt(i);
            // 这两句等价 其实31 = 2^5 - 1 只不过位运算符操作更快
//            hashcode = (hashcode << 5) - hashcode + string.charAt(i);
        }
        System.out.println(hashcode);


    }
    static void test2() {
        // 如果想要这两个person一样 那你必须要重写hashCode和equals方法 这个还是主要看业务需求，看你想怎么来规定
        Person p1 = new Person(10, 1.67f, "jack");
        Person p2 = new Person(10, 1.67f, "jack");

        Map<Object, Object> map = new HashMap<>();
        map.put("jack", 1);
        map.put("rose", 2);
        map.put("jack", 3);
        map.put(6, 4);
        map.put(p1, 5);
        map.put(p2, 7);
        map.put(null, 6);

//        System.out.println(map.size());
//		System.out.println(map.remove("jack"));
//		System.out.println(map.get("jack"));
//		System.out.println(map.size());

//        System.out.println(map.containsKey(p1));
//        System.out.println(map.containsKey(null));
//        System.out.println(map.containsValue(6));
//        System.out.println(map.containsValue(1));

//        System.out.println(map.get(p1));

        map.traversal(new Map.Visitor<Object, Object>() {
            @Override
            public boolean visit(Object key, Object value) {
				System.out.println(key + "_" + value);
                return false;
            }
        });


    }

    static void test3() {
        HashMap<Object, Integer> map = new HashMap<>();
        for (int i = 1; i <= 19; i++) {
            map.put(new Key(i), i);
        }

        map.print();
        System.out.println(map.get(new Key(1)));

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
            test3();
    }
}
