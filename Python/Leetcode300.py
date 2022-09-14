class Leetcode300:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums: return 0

        n = len(nums)
        dp = [1] * n

        for i in range(1, n):
            for j in range(i):

                # 연속될 숫자일 필요 없음
                if nums[i]>nums[j]:
                    # 기존 값 or 이전 값 + 한 칸(nums[i])
                    dp[i] = max(dp[i], dp[j]+1)

        return max(dp)