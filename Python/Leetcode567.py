class Leetcode567:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if not s1 or not s2: return False

        l1, l2 = len(s1), len(s2)
        if l1>l2: return False

        charCount = [0] * 26

        for c1 in s1:
            charCount[ord(c1) - ord('a')] += 1

        left = right = 0

        while left <= l2 - l1:
            # 오른쪽으로 늘일 수 있으면 늘린다
            while (right - left < l1) and charCount[ord(s2[right]) - ord('a')] >= 1:
                charCount[ord(s2[right]) - ord('a')] -= 1
                right += 1
            
            if right - left == l1:
                return True
            # 더 이상 늘일 수 없어서 빠져나온 경우(조건만족 못 한 경우) -> 왼쪽 한 칸 옮겨서 반복
            else:
                charCount[ord(s2[left]) - ord('a')] += 1
                left += 1

        return False




        




        




# def checkInclusion(self, s1: str, s2: str) -> bool:
#     l1, l2 = len(s1), len(s2)
#     count1 = Counter(s1)

#     for i in range(l2 - l1 + 1):
#         count2 = Counter(s2[i:i+l1])
#         if count2 == count1:
#             return True

#     return False