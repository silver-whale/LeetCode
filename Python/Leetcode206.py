from contextlib import nullcontext
from email import header


class Leetcode206:
    def reverseList(self, head):
        if not head or not head.next: return head

        prev = None
        front = head
        back = head.next

        while back:
            # Set pointer
            front.next = prev

            # move pointers
            prev = front
            front = back
            back = back.next
        
        front.next = prev

        return front

