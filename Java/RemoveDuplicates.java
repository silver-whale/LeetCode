package Java;

public class RemoveDuplicates {
    public static int removeDuplicates(int[] nums){
        int k = 0;

        for(int i=0; i<nums.length; i++){
            if (i<nums.length-1 && nums[i] == nums[i+1]) continue;
            nums[k++] = nums[i];
        }
        return k;
    }

    public static void main(String[] args) {
        int[] nums = new int[]{1,1,2}; // Input array
        int[] expectedNums = new int[]{1,2}; // The expected answer with correct length

        int k = removeDuplicates(nums); // Calls your implementation

        // assert : raise error if statement is false
        assert k == expectedNums.length;
        for (int i = 0; i < k; i++) {
            assert nums[i] == expectedNums[i];
        }
    }
}
