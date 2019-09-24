import com.jqc.ArrayList;


public class Main {

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


        // 升级版 扩容 null 判断 越界封装
        ArrayList array = new ArrayList(5);
//        array.add(5);
//        array.add(6);
//        array.add(66);
//        array.add(166);
//
//        array.set(0, 88);
//        array.set(array.size() - 1, 100);
//        array.remove(2);

        for (int i = 0; i < 20; i++) {
            array.add(i);
        }
        System.out.println(array);

    }
}
