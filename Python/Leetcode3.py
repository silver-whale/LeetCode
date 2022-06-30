class Leetcode3:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dict = {}
        answer = 0
        start = 0

        for i in range(len(s)):
            if s[i] not in dict:
                dict[s[i]] = i
            else:
                # 한 번 뒤로 밀린 start는 다시 앞으로 돌아올 수 없으므로
                # 기존의 start값과 중복된 문자 다음 인덱스를 비교
                start = max(start, dict[s[i]]+1)
                dict[s[i]] = i
            answer = max(answer, i - start + 1)
        
        return answer


