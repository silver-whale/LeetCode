class Leetcode66:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1, -1, -1):
            # 만약 해당 자리가 9가 아니면 그냥 1 더하고 끝남
            # 해당 자리가 9이면 올림이 시행되어야 하니까 else문에는 break가 없음
            if digits[i] != 9:
                digits[i] += 1
                break
            else:
                digits[i] = 0
        if digits[0] == 0:
            digits.insert(0, 1)
        return digits
