public class Leetcode977 {
    public int[] sortedSquares(int[] nums) {
        int left = 0, right = nums.length-1;
        int idx = nums.length-1;
        int[] result = new int[nums.length];

        while(left<=right){
            int lvalue = nums[left]*nums[left];
            int rvalue = nums[right]*nums[right];

            if(lvalue>rvalue){
                result[idx] = lvalue;
                left += 1;
            }
            else{
                result[idx] = rvalue;
                right -= 1;
            }
            idx-=1;
        }
        return result;
    }
}
