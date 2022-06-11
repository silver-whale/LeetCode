package Java;

import java.lang.reflect.Array;
import java.util.Arrays;

public class test {
    public static void adjust(int[] nums){
        nums[0] = 5;
    }

    public static void main(String[] args){
        int[] nums = new int[]{1,2,3,4,5};
        System.out.println(Arrays.toString(nums));
        adjust(nums);
        System.out.println(Arrays.toString(nums));
    }
}
