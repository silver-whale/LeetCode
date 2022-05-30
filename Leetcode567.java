public class Leetcode567 {
    public boolean checkInclusion(String s1, String s2) {
        if (s1==null || s2==null) {return false;}

        int L1 = s1.length();
        int L2 = s2.length();

        if(L1>L2) {return false;}

        int[] charCount = new int[26];

        for(char c1: s1.toCharArray()){
            charCount[c1 - 'a'] += 1;
        }

        int left=0, right=0;

        // Move the window
        while(left <= L2-L1){

            // Extend the window
            // window length < L1 and there is left character for extension
            while(right-left<L1 && charCount[s2.charAt(right)-'a']>=1){
                charCount[s2.charAt(right) - 'a'] -= 1;
                right += 1;
            }

            if(right-left == L1) {return true;}
            // if window length != L1 or no character for extension
            // move the window
            else{
                charCount[s2.charAt(left) - 'a'] += 1;
                left += 1;
            }
        }
        return false;
    }
}

// Count the alphabet in s1 and use them in s2.
// if window length is smaller then s1.length and there is left alphabet, extend the window
// else, move the window for 1 index.
