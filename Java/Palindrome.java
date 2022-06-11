package Java;

class Palindrome {
    public static boolean isPalindrome(int x) {
        if(x<0) return false;
        
        int rev = 0;
        int temp = x;
        
        while(temp>0){
            rev *= 10;
            rev += temp%10;
            temp = temp/10;
            
        }
        
        System.out.println(rev);
        
        if (rev==x) return true;
        
        return false;
    }


    public static void main(String[] args){
        int value = 121;
        isPalindrome(value);
    }
}