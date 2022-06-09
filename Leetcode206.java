public class Leetcode206 {
    public ListNode reverseList(ListNode head) {
        if(head==null || head.next == null){return head;}

        // Think like reversing the 'pointers'
        // Change the directions of pointers
        // last saves the remaining values when the link is deleted
        ListNode prev = null, curr = head, last = head.next;

        while(last != null){
            // reverse pointer
            curr.next = prev;
            // move prev and curr
            prev = curr;
            curr = last;
            last = last.next;
        }

        curr.next = prev;
        return curr;
    }
}
