package Java;

public class Leetcode58 {
    public int lengthOfLastWord(String s) {
        int index = s.length()-1;
        int count = 0;
        while(index>=0 && s.charAt(index) == ' '){
            index -= 1;
        }
        while(index>=0 && s.charAt(index) != ' '){
            count += 1;
            index -= 1;
        }
        return count;
    }
}
