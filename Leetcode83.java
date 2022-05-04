public class Leetcode83 {
    public ListNode deleteDuplicates(ListNode head) {
        if (head == null){
            return null;
        }

        ListNode prev = head;
        ListNode curr = head.next;

        while(curr != null){
            if (prev.val == curr.val){
                curr = curr.next;
                // Jump one node, remove later one
                prev.next = curr;
            }
            else{
                prev = prev.next;
                curr = curr.next;
            }
        }
        return head;
    }
}


 // Definition for singly-linked list.
class ListNode {
      int val;
      ListNode next;
      ListNode() {}
      ListNode(int val) { this.val = val; }
      ListNode(int val, ListNode next) { this.val = val; this.next = next; }
  }
