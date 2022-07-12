public class Leetcode46 {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> answer = new ArrayList<List<Integer>>();
        backtracking(answer, new ArrayList<Integer>(), nums);
        return answer;
    }

    public void backtracking(List<List<Integer>> answer, List<Integer> perm, int[] nums){
        if (perm.size()==nums.length){
            answer.add(new ArrayList<Integer>(perm));
            return;
        }

        for(int i=0; i<nums.length; i++){
            if (perm.contains(nums[i])){
                continue;
            }
            perm.add(nums[i]);
            backtracking(answer, perm, nums);
            perm.remove(perm.size()-1);
        }
    }
   
}
