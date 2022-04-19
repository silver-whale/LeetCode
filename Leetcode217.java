import java.util.HashSet;
import java.util.Set;

public class Leetcode217 {
    public boolean containsDuplicate(int[] nums) {
        // Hashset -> get instance's hashcode, if already exists -> Do not add
        Set<Integer> numbers = new HashSet<Integer>();
        for (int num : nums) {
            if (numbers.contains(num)) return true;
            numbers.add(num);
        }
        return false;
    }
}
