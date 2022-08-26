class Leetcode40:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(nums, target, comb):
            if target<0: return
            if target == 0:
                result.append(comb)
                return

            for i in range(len(nums)):
                # 같은 값 무시
                if i>0 and nums[i]==nums[i-1]:
                    continue
                # 중복값 나와서는 안 됨
                dfs(nums[i+1:], target - nums[i], comb + [nums[i]])
            
        
        result = []
        dfs(sorted(candidates), target, [])

        return result
