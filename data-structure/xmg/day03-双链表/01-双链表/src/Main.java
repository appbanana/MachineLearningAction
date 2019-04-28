import com.jqc.ArrayList;
import com.jqc.Person;
import com.jqc.Car;
import com.jqc.LinkList;
import com.jqc.Asserts;
import com.jqc.List;

public class Main {

    static void testList(List<Integer> list) {
        list.add(11);
        list.add(22);
        list.add(33);
        list.add(44);

        list.add(0, 55); // [55, 11, 22, 33, 44]
        list.add(2, 66); // [55, 11, 66, 22, 33, 44]
        list.add(list.size(), 77); // [55, 11, 66, 22, 33, 44, 77]

        list.remove(0); // [11, 66, 22, 33, 44, 77]
        list.remove(2); // [11, 66, 33, 44, 77]
//        list.remove(list.size() - 1); // [11, 66, 33, 44]
//
//        Asserts.test(list.indexOf(44) == 3);
//        Asserts.test(list.indexOf(22) == List.ELEMENT_NOT_FOUND);
//        Asserts.test(list.contains(33));
//        Asserts.test(list.get(0) == 11);
//        Asserts.test(list.get(1) == 66);
//        Asserts.test(list.get(list.size() - 1) == 44);

        System.out.println(list);
    }

    public static void main(String[] args) {

//        自定义动态数组
//        ArrayList array = new ArrayList(5);
//        array.add(5);
//        array.add(6);
//        array.add(66);
//        array.add(166);
//
//        array.set(0, 88);
//        array.set(array.size() - 1, 100);
//        array.remove(2);
//        System.out.println(array);
//        System.out.println(array.get(2));


        // 升级版 扩容 越界封装
//        ArrayList array = new ArrayList(5);
//        array.add(5);
//        array.add(6);
//        array.add(66);
//        array.add(166);
//
//        array.set(0, 88);
//        array.set(array.size() - 1, 100);
//        array.remove(2);
//
//        for (int i = 0; i < 20; i++) {
//            array.add(i);
//        }
//        System.out.println(array);

        // 再次升级 扩充数组功能，使数组可以存储各种数据类型的对象 null判断
        // remove 方法也进行优化
        // 引入泛型对象
        // 放到里面 同级文件可以直接访问
//        ArrayList array = new ArrayList(5);
//        ArrayList array = new ArrayList();

//        array.add(5);
//        array.add(6);
//        array.add(66);
//        array.add(new Person(12, "abc"));
//        array.add(new Car());
//
//        array.set(0, 88);
//        array.clear();
//        System.out.println(array);

//        LinkList<Integer> list = new LinkList<>();
//        list.add(1);
//        list.add(2);
//        list.add(0, 10);
//        list.add(0, 66);
//        list.remove(0);
//        System.out.println(list);

        testList(new LinkList<>());


    }
}
