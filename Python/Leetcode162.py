class Leetcode162:
    def findPeakElement(self, nums: List[int]) -> int:
        start, end = 0, len(nums)-1

        while start<end:
            mid = (start+end)//2
            # 증가하는 부분 -> 오른쪽에 피크가 있음 
            if nums[mid] < nums[mid+1]:
                # mid+1이 더 크기 때문에 start = mid + 1
                start = mid + 1
            # 감소하는 부분 -> 왼쪽에 피크가 있음 
            # mid가 최댓값일 수 있음
            else:
                end = mid
        return start