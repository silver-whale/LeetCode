public class Leetcode283 {
    public void moveZeroes(int[] nums) {
        // 0이 아닐 때 증가
        // 마지막 0의 위치를 저장
        int zeroPos = 0;
        for(int i=0; i<nums.length; i++){
            if(nums[i] != 0){
                int tmp = nums[zeroPos];
                nums[zeroPos] = nums[i];
                nums[i] = tmp;
                zeroPos++;
            }
        }
    }
}
