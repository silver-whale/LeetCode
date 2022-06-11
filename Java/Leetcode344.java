package Java;

public class Leetcode344 {
    public void reverseString(char[] s) {
        int first = 0, second = s.length-1;

        while(first<second){
            char tmp = s[first];
            s[first] = s[second];
            s[second] = tmp;
            first += 1;
            second -= 1;
        }
    }
}
