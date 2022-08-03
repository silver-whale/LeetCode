class Leetcode438:
    def findAnagrams(self, s: str, p: str):
        if len(s) < len(p):
            return []

        dic1 = [0] * 26
        dic2 = [0] * 26

        result = []

        for i in range(len(p)):
            dic1[ord(p[i]) - ord('a')] += 1
            dic2[ord(s[i]) - ord('a')] += 1
        
        if dic1 == dic2:
            result.append(0)

        # Sliding window
        for i in range(1, len(s) - len(p) + 1):
            # 맨 앞의 값 삭제
            dic2[ord(s[i-1]) - ord('a')] -= 1
            # 맨 뒤의 값 추가
            dic2[ord(s[i+len(p)-1]) - ord('a')] += 1
            if dic1 == dic2:
                result.append(i)
        
        return result
        
