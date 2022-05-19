public class Leetcode189 {
    public void rotate(int[] nums, int k) {
        int len = nums.length;
        k = k % len;
        // reverse the array
        rot(nums, 0, len-1);
        // reverse the array from 0 to k-1
        rot(nums, 0, k-1);
        // reverse the rest array
        rot(nums, k, len-1);
    }

    void rot(int[] arr, int start, int end){
        while(start < end){
            int temp = arr[start];
            arr[start] = arr[end];
            arr[end] = temp;
            start++;
            end--;
        }
    }
}

// Array reverse: Use two pointer
// Shift: Divide into three steps