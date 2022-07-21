# Binary Search = while
class Leetcode34:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = self.leftSearch(nums, target)
        end = self.rightSearch(nums, target)
        return [start, end]

    def leftSearch(self, nums, target):
        start = 0
        end = len(nums) - 1
        result = -1

        while start<=end:
            mid = (start+end)//2
            if nums[mid]>target:
                end = mid - 1
            elif nums[mid]<target:
                start = mid + 1
            else:
                result = mid
                # 가장 왼쪽의 값을 찾아야 함
                end = mid - 1
        return result

    def rightSearch(self, nums, target):
        start = 0
        end = len(nums) - 1
        result = -1
        
        while (start<=end):
            mid = (start+end)//2
            if nums[mid]>target:
                end = mid - 1
            elif nums[mid]<target:
                start = mid + 1
            else:
                result = mid
                # 가장 오른쪽의 값을 찾아야 함
                start = mid + 1
        return result