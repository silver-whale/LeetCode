package Java;

public class Leetcode2 {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode first = null;
        ListNode last = null;
        ListNode temp1 = l1;
        ListNode temp2 = l2;
        int carry = 0;

        while (temp1 != null || temp2 != null) {
            int calculated = (temp1 != null ? temp1.val : 0) + (temp2 != null ? temp2.val : 0) + carry;
            int value = calculated % 10;
            carry = calculated / 10;
            ListNode newNode = new ListNode(value);
            if (last == null) {
                first = last = newNode;
            } else {
                last.next = newNode;
                last = last.next;
            }
            if (temp1 != null)
                temp1 = temp1.next;
            if (temp2 != null)
                temp2 = temp2.next;
        }
        if (carry != 0) {
            ListNode newNode = new ListNode(carry);
            last.next = newNode;
        }
        return first;
    }
}
