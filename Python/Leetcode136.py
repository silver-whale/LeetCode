class Leetcode136:
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0

        # 같은 수끼리 xor하면 0이 됨
        for num in nums:
            xor ^= num
        
        return xor