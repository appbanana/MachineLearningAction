public class Main {

    public static void main(String[] args) {
        // 哈希冲突是里面的元素可能是计算出来的hash值是一样，也可能是hash值不一样但是对应的索引是一样的

        // java hashmap key必须实现hashCode和equal方法
        // hashCode：如果不实现的话，会调用系统的hashCode，会默认
        // equal： 方法是当哈希冲突时，我们先根据key找到对应索引，
        // 在拿这个key和链表或者红黑树中的元素比较相等不相等，会调用你自己实现的equal方法，
        // 如果相等就覆盖，不相等就添加进去

        // 计算索引的时候会调用hashCode 哈希冲突的时候会调用equals
        System.out.println("Hello World!");
    }
}
