class Leetcode713:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if not nums: return 0

        left = 0
        result = 1
        answer = 0

        for right in range(len(nums)):
            result *= nums[right]

            if result >= k:
                while left <= right and result >= k:
                    result /= nums[left]
                    left += 1
            
            # 이렇게 하면 이때까지의 Subarray의 개수를 저장할 수 있음
            answer += right - left + 1

        return answer