class Leetcode11:
    def maxArea(self, height: List[int]) -> int:
        start, end = 0, len(height)-1

        answer = 0

        while start<end:
            if height[start] <= height[end]:
                answer = max(answer, height[start] * (end-start))
                start += 1
            else:
                answer = max(answer, height[end] * (end-start))
                end -= 1
        return answer