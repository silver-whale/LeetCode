class Leetcode673:
    def findNumberOfLIS(self, nums: List[int]) -> int:

        # [가장 긴 배열의 길이, 가장 긴 배열의 개수]
        dp = [[1, 1] for i in range(len(nums))]
        longest = 1

        # for i, n in enumerate(nums)
        for i in range(len(nums)):
            curr_longest, count = 1, 0

            # 가장 긴 배열의 길이를 찾는다
            for j in range(i):
                if nums[i] > nums[j]:
                    curr_longest = max(curr_longest, dp[j][0] + 1)

            # 가장 긴 배열이 몇 개인지를 찾는다
            for j in range(i):
                if dp[j][0] == curr_longest-1 and nums[i]>nums[j]:
                    # 기존에 있던 배열들에서 하나만 추가된 거니까 개수는 같음
                    count += dp[j][1]
                    
            # 현재까지 가장 긴 길이와 그 개수를 저장한다        
            dp[i] = [curr_longest, max(count, dp[i][1])]
            longest = max(curr_longest, longest)
        
        return sum([d[1] for d in dp if d[0] == longest])
