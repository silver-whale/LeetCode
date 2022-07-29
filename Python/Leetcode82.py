class Leetcode82:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # head 이전의 더미 노드
        dummy = ListNode(0, head)
        prev = dummy
        curr = head

        while curr and curr.next:
            while curr.next and curr.val == curr.next.val:
                curr = curr.next
            # curr이 중복값이 아니면 pre, curr 한 칸씩 이동
            if prev.next == curr:
                prev = prev.next
            # curr이 중복값이라서 앞으로 갔으면 -> 중복값의 맨 마지막 부분을 가리키고 있음
            else:
                prev.next = curr.next

            curr = curr.next
        
        return dummy.next