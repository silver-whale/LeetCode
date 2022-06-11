package Java;

import java.lang.Math;

public class Leetcode53 {
    public int maxSubArray(int[] nums) {
        int maxSum = nums[0];
        int curSum = 0;

        for(int v:nums){
            if (curSum < 0){
                curSum = 0;
            }
            curSum += v;
            maxSum = Math.max(maxSum, curSum);
        }
        return maxSum;
    }
}
