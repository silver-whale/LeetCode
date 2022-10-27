import java.util.*;

class Solution {
    
    static Set<Integer> sets = new HashSet<>();
    
    public int solution(String numbers) {
        char[] nums = numbers.toCharArray();
        boolean[] visited = new boolean[nums.length];
        
        dfs("", 0, nums, visited);
        
        return sets.size();
    }
    
    public void dfs(String current, int index, char[] nums, boolean[] visited){
        if(current!=""){
            int curInt = Integer.parseInt(current);
            if(isPrime(curInt)){
                sets.add(curInt);
            }
        }
        
        if(index == nums.length) return;
        
        for(int i=0; i<nums.length; i++){
            if (!visited[i]){
                visited[i] = true;
                dfs(current + nums[i], index + 1, nums, visited);
                visited[i] = false;
            }
        }
    }
    
    public boolean isPrime(int n){
        if(n==0 || n==1){
            return false;
        }
        
        for(int i=2; i*i<=n; i++){
            if(n%i==0){
                return false;
            }
        }
        return true;
    }
    
}