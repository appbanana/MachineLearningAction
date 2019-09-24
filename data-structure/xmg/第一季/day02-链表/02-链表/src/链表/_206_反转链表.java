package 链表;

/**
 * Created by apple on 2019/4/20.
 */
public class _206_反转链表 {

    public ListNode reverseList(ListNode head) {
        if (head == null || head.next == null) return head;

        ListNode newNode = reverseList(head.next);
        head.next.next = head;
        // 把之前head指向第二个的元素的线断掉
        head.next = null;
        return newNode;
    }

    public ListNode reverseList2(ListNode head) {
        if (head == null || head.next == null) return head;

        ListNode newNode = null;
        while (head != null){
            ListNode temp = head.next;
            head.next = newNode;
            newNode = head;
            head = temp;
        }

        return newNode;
    }
}
