public class Leetcode69 {
    public int mySqrt(int x) {
        long start = 0;
        long end = x;
        long mid = start + (end - start) / 2;
        long answer = -1;

        while(start <= end){
            long square = mid * mid;

            if(square == x) return (int)mid;

            if(square < x){
                answer = mid;
                start = mid + 1;
            }
            else{
                end = mid -1;
            }
            mid = start + (end - start)/2;
        }
        return (int)answer;
    }
}
