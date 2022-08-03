class Leetcode209:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:  
        start, end = 0, 0
        answer = float('inf')
        sum = 0

        while start<=end and end<len(nums):
            sum += nums[end]
            # 여기서 end를 한 칸 옮겨주고
            end += 1
            # 합이 작아질 때까지 빼주는 것을 유의
            if sum>=target:
                while start<=end and sum>=target:
                    sum -= nums[start]
                    start += 1
                # 맨 앞의 값을 더해 줘서 결과값이 타겟보다 큰 최소값이 되도록 함
                answer = min(answer, end-start+1)

        # If no answer return 0
        return 0 if answer >= float('inf') else answer