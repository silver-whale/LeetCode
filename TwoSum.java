import java.util.HashMap;
import java.util.Map;

// Use map <value, index> to use containsKey function
// Similar to 'in' in Python
public class TwoSum{

    static int[] twoSum(int[] nums, int target){
        Map<Integer, Integer> map = new HashMap<>();

        for(int i=0; i<nums.length; i++){
            int diff = target - nums[i];
            if(map.containsKey(diff)){
                return new int[]{i, map.get(diff)};
            }
            // key = value, value = index
            map.put(nums[i], i);
        }
        return null;
    }
    public static void main(String[] args){
        int[] input = new int[]{2, 7, 11, 15};
        int target = 9;

        TwoSum.twoSum(input, target);
    }
}

// 더하기 문제 : 결과값 - iteration value 형식으로 O(n)만에 해결할 수 있는지 확인한다