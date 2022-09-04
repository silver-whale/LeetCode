class Leetcode198:
    def rob(self, nums: List[int]):
        if not nums: return 0

        prev, curr = 0, 0
        for n in nums:
            # [i-2] + [i] or [i-1]
            prev, curr = curr, max(prev + n, curr)
        
        return curr

    def dp(self, nums):
        if len(nums) == 0: return 0
        if len(nums) == 1: return nums[0]

        dp = [0] * (len(nums)+1)
        dp[1] = nums[0]

        for i in range(1, len(nums)):
            dp[i+1] = max(dp[i], dp[i-1] + nums[i])
        
        return dp[len(dp)-1]