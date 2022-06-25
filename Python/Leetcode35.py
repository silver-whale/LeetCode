from bisect import bisect


class Leetcode35:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0; end = len(nums)-1

        while(start<=end):
            mid = (start+end)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return start

    def fastAnswer(self, nums:List[int], target:int)->int:
        for i in range(len(nums)):
            if nums[i]==target:
                return i
            # bisect.left/right(list, value): list에서 value를 삽입할 왼쪽/오른쪽 위치 반환
            return bisect.bisect_left(nums,target)