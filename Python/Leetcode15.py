class Leetcode15:
    # 중복 제거: 오름차순 정렬해서 nums[n] == nums[n+1]이라면 같은 답이 나올 수밖에 없음 -> SKIP
    # a + b = target -> a = target - b
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        n = len(nums)
        result = []

        for i in range(n):
            # Remove duplicates
            if i>0 and nums[i] == nums[i-1]:
                continue

            # A + B = Target(0) - C
            target = nums[i]* -1

            start, end = i+1, n-1

            while start<end:
                if nums[start] + nums[end] == target:
                    result.append([nums[i], nums[start], nums[end]])
                    start = start + 1
                    # 이전에 start+1 -> start == start-1이 조건이 됨
                    # Remove Duplicates
                    while(start<end and nums[start] == nums[start-1]):
                        start += 1

                elif nums[start] + nums[end] < target:
                    start += 1
                else:
                    end -= 1
        return result