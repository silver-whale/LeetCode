class Leetcode19:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        start = end = head

        # end 조건 들어가야 해서 while문 사용
        while n>0 and end:
            end = end.next
            n -= 1

        # 노드가 하나밖에 없으면 n이 1이라서 end가 none이 됨. 그래서 head.next=none이 되어 에러 없이 실행
        if not end:
            head = head.next
        else:
            while end.next:
                start = start.next
                end = end.next
            start.next = start.next.next
        return head
