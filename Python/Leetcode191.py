class Leetcode191:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')