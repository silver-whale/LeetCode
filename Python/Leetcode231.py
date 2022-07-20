class Leetcode231:
    def isPowerOfTwo(self, n):
        # n and -> n이 0일 경우를 처리
        # 2의 제곱수면 최상위 비트만 1이여야 함 -> n-1은 최상위 비트만 0, &하면 0000 -> not 하면 true
        # 2의 제곱수가 아니면 not 시 false 나옴
        return n and not(n & n-1)