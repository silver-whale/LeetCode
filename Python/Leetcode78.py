class Leetcode78:
    def subsets(self, nums):
        res = [[]]
        for n in nums:
            for i in range(len(res)):
                res.append(res[i] + [n])

        return res