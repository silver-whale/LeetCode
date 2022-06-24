class leetcode704:
    def search(self, nums: List[int], target: int) -> int:
        start, last = 0, len(nums)-1

        while start<=last:
            mid = (start+last)//2
            if(nums[mid] == target):
                return mid
            elif(nums[mid]>target):
                last = mid - 1
            elif(nums[mid]<target):
                start = mid + 1

        return -1
