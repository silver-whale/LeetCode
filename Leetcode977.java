public class Leetcode977 {
    public int[] sortedSquares(int[] nums) {
        int left = 0, right = nums.length-1;
        // 뒤에서부터 채워 나가는 이유 -> 제곱값은 무조건 양수, 최대값을 찾아서 뒤에서부터 채워 나가야 함
        int idx = nums.length-1;
        int[] answer = new int[nums.length];
        while(left <= right){
            int lvalue = nums[left]*nums[left];
            int rvalue = nums[right]*nums[right];

            if(lvalue>=rvalue){
                answer[idx] = lvalue;
                left += 1;
            }
            else{
                answer[idx] = rvalue;
                right -= 1;
            }
            idx -= 1;
        }
        return answer;
    }
}
