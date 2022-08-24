class Leetcode78:
    def subsets(self, nums):
        result = [[]]
        for num in nums:
            result += [r + [num] for r in result]

        return result