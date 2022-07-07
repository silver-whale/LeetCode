class Leetcode46:
    def permute(self, nums):
        answer = []

        def backtrack(perm, nums):
            if len(perm)==len(nums):
                answer.append(perm.copy())
                return
            
            for i in range(len(nums)):
                if nums[i] in perm:
                    continue
                perm.append(nums[i])
                backtrack(perm, nums)
                perm.pop()

        backtrack([], nums)
        return answer