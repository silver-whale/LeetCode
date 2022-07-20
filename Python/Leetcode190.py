class Leetcode190:
    def reverseBits(self, n: int) -> int:
        res = 0

        # n의 오른쪽부터 res의 왼쪽으로 보낸다
        for i in range(32):
            # 해당 자릿수가 있으면
            if n&1:
                # 반대쪽 위치(31-i)로 보낸다
                res += 1 << (31-i)
            n = n>>1
        return res
