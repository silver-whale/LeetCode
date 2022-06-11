package Java;

public class PlusOne {
    public int[] plusOne(int[] digits) {
        int flag = 0;
        digits[digits.length-1] += 1;
        for(int i = digits.length - 1; i >= 0; i--) {
            digits[i] += flag;
            if(digits[i] > 9) {
                flag = 1;
                digits[i] %= 10;
            } else {
                flag = 0;
            }
        }

        if (flag==1){
            digits = new int [digits.length+1];
            digits[0] = 1;
        }
        return digits;
    }
    public static void main(String[] args){

    }
}
