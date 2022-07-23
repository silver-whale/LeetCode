# array를 두 부분으로 나눠서 우리가 어느 쪽에 위치해 있는지만 알면 찾기 쉽다.
# ex) 3456 012, target=0 -> 중간값=6
# 중간값 6은 0보다 크다. 그렇다면 그 왼쪽 값들은? -> 제일 첫 번째인 4를 0과 비교함으로써 타겟값이 왼쪽에 있는지 아니면 오른쪽 부분으로 넘어갔는지를 알 수 있다.

# 일차함수 그리듯 하면 이해 쉬움

class Leetcode33:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if nums[0]==target else -1

        start = 0
        end = len(nums)-1

        while(start<end):
            if nums[start] == target: return start
            if nums[end] == target: return end

            mid = (start+end)//2

            if nums[mid]==target:
                return mid 
            elif nums[mid]>target:
                # 중간값이 타겟보다 크고 시작값은 타겟보다 작음 -> 무조건 그 사이에 타겟이 있음
                if nums[start] < target:
                    end = mid - 1

                # 중간값이 타겟보다 큰데 시작값도 타겟보다 큼 -> 중간에 끊어졌다 올라왔는지 아니면 그냥 통째로 타겟보다 큰 오름차순인지를 알아야 함
                else:
                    # 통째로 오름차순인 경우 -> 타겟은 사이에 없음
                    if nums[mid] >= nums[start]:
                        start = mid + 1
                    # 중간에 끊어졌다 올라온 경우 -> 타겟은 이 사이에 있음
                    else:
                        end  = mid - 1
            else:
                # 중간값이 타겟보다 작고 시작값은 타겟보다 큰 경우 -> 이 사이에는 타겟이 없음
                if nums[start]>target:
                    start = mid + 1

                # 중간값이 타겟보다 작고 시작값이 타겟보다 작음 -> 중간에 끊겨서 올라오는지 아니면 통째로 타겟보다 작은 오름차순인지 알아야 함
                else:
                    # 통째로 타겟보다 작은 오름차순 -> 타겟 없음
                    if nums[start]<=nums[mid]:
                        start = mid + 1
                    # 중간에 끊겼음 -> 타겟 있음
                    else:
                        end = mid - 1

        return -1