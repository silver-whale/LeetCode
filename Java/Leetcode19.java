package Java;

public class Leetcode19 {
    class ListNode {
       int val;
       ListNode next;
       ListNode() {}
       ListNode(int val) { this.val = val; }
       ListNode(int val, ListNode next) { this.val = val; this.next = next; }
    }

    // Sliding window technique
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode start = head;
        ListNode end = head;

        // i~j : size N window
        while(n>0 && end!= null){
            end = end.next;
            n -= 1;
        }

        // if there is only one element, remove that one
        if(end==null){head = head.next;}
        else{
            // window reaches the end
            while(end.next != null){
                start = start.next;
                end = end.next;
            }
            // remove the element at the start
            start.next = start.next.next;
        }
        return head;
    }
}

// if n=3
// 1 2 3 4 5
// <--->
// move the window until end
// 1 2 3 4 5
//     <--->
// remove the start