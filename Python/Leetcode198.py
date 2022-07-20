class Leetcode198:
    def rob(self, nums: List[int]):
        prev, curr = 0, 0

        for house in nums:
            # [i-2]
            prev2 = prev
            # [i-1]
            prev = curr
            # [i-2]+[i] or [i-1]
            curr = max(prev2+house, prev)
        
        return curr
