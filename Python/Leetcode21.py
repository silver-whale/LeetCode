class Leetcode21:
    def mergeTwoLists(self, list1, list2):

        # Head: 맨 처음을 가르키도록 유지하기 위함
        # Cur: 이동하면서 값을 추가하기 위함
        head = cur = ListNode(0)

        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        cur.next = list1 or list2

        return head.next