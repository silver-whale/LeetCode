public class Leetcode189 {
    public void rotate(int[] nums, int k) {
        int len = nums.length;
        k = k % len;
        rotate(nums, 0, len-1);
        rotate(nums, 0, k-1);
        rotate(nums, k, len-1);

    }
    void rotate(int[] arr, int start, int end){
        while(start < end){
            int temp = arr[start];
            arr[start] = arr[end];
            arr[end] = temp;
            start++;
            end--;
        }
    }
}
