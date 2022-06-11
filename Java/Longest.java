package Java;// Using indexOf
// indexOf : Returns the first index where given character/string if found

public class Longest {
    public static String longestCommonPrefix(String[] strs){
        StringBuilder prefix = new StringBuilder();
        if (strs == null || strs.length == 0) return "";

        int min_length = Integer.MAX_VALUE;

        for(int i=0; i<strs.length; i++) min_length = Math.min(min_length, strs[i].length());

        int start = 0;
        int mid = 0;
        int end = min_length;

        while(end>=start){
            mid = (start + (end-start)) + 1/2;
            if(commonPrefix(strs, mid)){
                prefix.append(strs[0].substring(start, mid));
                start = mid+1;
            }
            else end = mid-1;
        }
        
        return prefix.toString();
    }

    static boolean commonPrefix(String[] strs, int mid){
        String s = strs[0].substring(0, mid);
        for(int i=1; i<strs.length; i++)
            if(!strs[i].startsWith(s)) return false;
        
        return true;
    }

    public static void main(String[] args){
        String[] strs = new String[]{"aalit", "lit", "ablitab"};
        System.out.println(longestCommonPrefix(strs));
    }
}
