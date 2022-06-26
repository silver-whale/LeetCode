class Leetcode189:
    def reverse(self, N:List[int], s:int, e:int) -> None:
        while(s<e):
            N[s], N[e] = N[e], N[s]
            s += 1
            e -= 1

    def rotate(self, nums: List[int], k: int) -> None:
        l = len(nums)
        k = k % l
        if k:
            self.reverse(nums, 0, l-1)
            self.reverse(nums, 0, k-1)
            self.reverse(nums, k, l-1)

    