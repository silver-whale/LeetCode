public class Leetcode278 {
    public boolean isBadVersion(int n){
        // Abstract Function
        return true;
    }
    public int firstBadVersion(int n) {
        // list starts from 1
        int left = 1, right = n;
        while(left < right){
            int mid = left + (right-left)/2;
            if(isBadVersion(mid)){
                right = mid;
            }
            else{
                left = mid + 1;
            }
        }
        return left;
    }
}
