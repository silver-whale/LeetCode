public class Leetcode77{
    public List<List<Integer>> combine(int n, int k) {
        List<List<Integer>> answer = new ArrayList<List<Integer>>();
        backtracking(answer, new ArrayList<Integer>(), 1, n, k);
        return answer;
    }

    public void backtracking(List<List<Integer>> answer, List<Integer> combi, int start, int n, int k){
        if (combi.size()==k){
            answer.add(new ArrayList<Integer>(combi));
            return;
        }
        
        for(int i=start; i<=n; i++){
            combi.add(i);
            backtracking(answer, combi, i+1, n, k);
            combi.remove(combi.size()-1);
        }
    }
}