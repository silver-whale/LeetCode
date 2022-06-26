class Leetcode977:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        start = 0; end = len(nums)-1
        idx = len(nums)-1
        answer = [0 for i in range(len(nums))]

        while(start<=end):
            if nums[start]**2 >= nums[end]**2:
                answer[idx] = nums[start]**2
                start += 1
                idx -= 1
            else:
                answer[idx] = nums[end]**2
                end -= 1
                idx -= 1

        return answer