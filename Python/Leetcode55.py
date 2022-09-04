class Leetcode55:
    def canJump(self, nums: List[int]) -> bool:
        N = len(nums)
        if N<=1: return True

        end = N-1

        for i in range(N-2, -1, -1):
            # 현재 인덱스 + 최대 점프값이 end보다 크다 -> 도달 가능하다
            if i + nums[i] >= end:
                end = i
        return end == 0
            