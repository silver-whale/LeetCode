class Leetcode198:
    def rob(self, nums: List[int]):
        if not nums: return 0

        prev, curr = 0, 0
        for n in nums:
            # [i-2] + [i] or [i-1]
            prev, curr = curr, max(prev + n, curr)
        
        return curr
