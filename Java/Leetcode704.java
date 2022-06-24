package Java;

public class Leetcode704 {
    public int search(int[] nums, int target){
        if(nums.length == 1){
            return nums[0]==target ? 0 : -1;
        }

        int start = 0, end = nums.length-1;

        while(end >= start) {
            // int mid = start + (end - start)/2;
            int mid = (start + end) / 2;
            if(nums[mid] == target){
                return mid;
            }
            else if (nums[mid] > target){
                end = mid -1;
            }
            else{
                start = mid + 1;
            }
        }
        // 반환 없이 while문을 빠져나오면 값을 찾지 못한 것
        return -1;
    }

    public static void main(String[] args) {

    }
}


/*if(nums.length == 1){
            return nums[0] == target ? 0 : -1;
        }

        int start = 0;
        int end = nums.length - 1;

        while(end >= start){
            int mid = start + (end-start)/2;
            if(nums[mid] == target){
                return mid;
            }
            else if(nums[mid] < target){
                start = mid + 1;
            }
            else{
                end = mid - 1;
            }
        }
        return -1;
 */