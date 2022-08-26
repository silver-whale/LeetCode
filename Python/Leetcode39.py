class Leetcode39:
    def combinationSum(self, candidates, target):
        def dfs(nums, target, comb):
            if target < 0: return
            if target == 0:
                result.append(comb)

            for i in range(len(nums)):
                # 같은 수 선택 가능하기 때문에 i:로 들어감
                dfs(nums[i:], target - nums[i], comb + [nums[i]])

        result = []
        dfs(candidates, target, [])
        return result