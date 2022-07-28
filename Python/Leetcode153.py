class Leetcode153:
    def findMin(self, nums: List[int]) -> int:
        if not nums: return 0

        start, end = 0, len(nums)-1

        # nums[start]<=nums[end] -> 값이 하나로 모일 때 or 꺾이는 지점을 찾았을 때 end
        while nums[start] > nums[end]:
            mid = (start+end)//2
            # 중간에 꺾이면 불가능 -> 무조건 오름차순
            if nums[mid] < nums[end]:
                # 해당 오름차순의 최솟값은 mid
                end = mid
            else:
                start = mid + 1
        return nums[start]