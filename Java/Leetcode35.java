package Java;

public class Leetcode35 {
    public int searchInsert(int[] nums, int target) {
        if(nums.length == 1){
            if(nums[0] == target){
                return 0;
            }
            else{
                return nums[0]>=target ? 0 : 1;
            }
        }

        int start = 0, end = nums.length-1;

        while(start<=end){
            int mid = start + (end-start)/2;

            if(nums[mid] == target){
                return mid;
            }
            else if(nums[mid] > target){
                end = mid - 1;
            }
            else{
                start = mid + 1;
            }
        }
        return start;
    }
}
