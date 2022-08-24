class Leetcode90:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        # (result에 추가될 배열, 남은 숫자 배열)
        def dfs(num, nums):
            result.append(num)
            for i in range(len(nums)):
                if i>0 and nums[i] == nums[i-1]:
                    continue
                dfs(num + [nums[i]], nums[i+1:])
                
        result = []
        dfs([], sorted(nums))
        
        return result
        