public class Leetcode278 {
    public boolean isBadVersion(int n){
        // Abstract Function
        return true;
    }
    public int firstBadVersion(int n) {
        if(n==1){
            return 1;
        }

        int left = 1, right = n;

        while(left < right){
            int mid = left + (right - left)/2;
            if(isBadVersion(mid)){
                // 이 중앙이 처음 잘못된 것일 수 있으므로 mid를 포함해야 함
                right = mid;
            }
            else{
                left = mid + 1;
            }
        }
        // last turn: mid = left, if isBadVersion(mid) -> right = mid(=left) else -> left = mid + 1
        return left;
    }
}


/*
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
 */