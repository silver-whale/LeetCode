public class Leetcode167 {
    public int[] twoSum(int[] numbers, int target) {
        int first = 0, second = numbers.length - 1;
        int twoSum = -1;
        while(twoSum != target){
            twoSum = numbers[first] + numbers[second];
            if(twoSum > target){
                second -= 1;
            }
            else if(twoSum < target){
                first += 1;
            }
        }
        return new int[]{first+1, second+1};
    }
}
