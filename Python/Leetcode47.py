class Leetcode47:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, perm):
            if not nums:
                result.append(perm)
            for i in range(len(nums)):
                if i>0 and nums[i] == nums[i-1]:
                    continue
                dfs(nums[:i] + nums[i+1:], perm + [nums[i]])

        result = []
        nums.sort()
        dfs(nums, [])

        return result