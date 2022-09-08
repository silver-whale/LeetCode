class Leetcode5:
    def longestPalindrome(self, string):
        """
        Substring(start, end) is a palindrom if Substring(start+1, end-1) is a palindrom and string[start] == string[end]
        """

        # Same if reversed
        if string == string[::-1]: return string

        # start는 리턴할 값, length는 한 번 변경된 후로는 substring 길이(+1)
        start, length = 0, 1

        # i는 substring의 맨 끝 인덱스
        for i in range(1, len(string)):

            # left-1 | left | i | right
            left, right = i-length, i+1
            
            # s1 -> 홀수, s2 -> 짝수
            s1, s2 = string[left-1:right], string[left: right]

            # 홀수 대칭일 경우 -> 앞뒤로 한 칸씩 증가시킨다(+2)
            # 만약 홀수 대칭이 3 3 3 이런 식으로 모두 같은 값이면 이미 이전 i 루프에서 짝수 대칭으로 걸러졌음
            if left-1 >=0 and s1 == s1[::-1]:
                start, offset = left-1, offset+2

            # left-1<0 or s1 != s1[::-1], 즉 s1이 조건을 만족하지 않음
            # 한 칸 증가시켜서 홀수 대칭인지를 판별해야 함
            elif s2==s2[::-1]:
                start, offset = left, offset + 1

            # 만약 위의 두 if문을 만족하지 않는다면 i를 증가시켜 시작지점을 옮긴다

        return string[start:start+offset]
   
    
def longestPalindrome2(string):
    """
    Substring(start, end) is a palindrom if Substring(start+1, end-1) is a palindrom and string[start] == string[end]
    """

    N = len(string)
    dp = [[False] * N for i in range(N)]
    # The start and end index of the longest substring
    resStart, resEnd = 0, 0

    # One letter -> Palindrom
    for i in range(N):
        dp[i][i] = True


    # Two letter -> Palindrom if string[i]==string[i+1]
    for i in range(N-1):
        if string[i] == string[i+1]:
            dp[i][i+1] = True
            if not resStart and not resEnd:
                resStart, resEnd = i, i+1
    
    # Longer than 2
    for offset in range(2, N):
        # Symmetrically
        # 0 -> N-1 / 1 -> N-2 / 2 -> N-3
        for start in range(N-offset):
            # N-offset + offset = N 
            end = start + offset

            if dp[start+1][end-1] and string[start]==string[end]:
                dp[start][end] = True
                if resEnd - resStart < end - start:
                    resStart, resEnd = start, end
    
    return string[resStart:resEnd+1]

