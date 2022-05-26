import java.util.HashSet;
import java.util.Set;

public class Leetcode3 {
    public int lengthOfLongestSubstring(String s) {
        Set<Character> set = new HashSet<>();
        int start = 0;
        int answer = 0;
        for(int last = 0; last < s.length(); last++){
            while(set.contains(s.charAt(last))){
                set.remove(s.charAt(start++));
            }
            set.add(s.charAt(last));
            answer = Math.max(answer, last - start + 1);
        }
        return answer;
    }
}


