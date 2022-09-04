class Leetcode213:
    def rob(self, nums) -> int:
        if not nums: return 0
        if len(nums) == 1: return nums[0]

        # 맨 첫번째 + 끝에서 -1번째
        prev, curr = 0, 0
        for i in range(len(nums)-1):
            tmp = curr
            curr, prev = max(curr, prev + nums[i]), tmp
        record = curr

        # 맨 마지막 + 앞에서부터 1번째
        prev, curr = 0, 0
        for i in range(len(nums)-1, 0, -1):
            tmp = curr
            curr, prev = max(curr, prev + nums[i]), tmp

        return max(record, curr)