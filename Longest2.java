public class Longest2 {
    public static String longestCommonPrefix(String[] strs){
        if (strs.length == 0) return "";

        String start = strs[0];

        for(int i=1; i<strs.length; i++){
            // if not exist = -1, if not prefix >= 0
            while(strs[i].indexOf(start) != 0){
                start = start.substring(0, start.length()-1);
            }
        }
        return start;
    }

    public static void main(String[] args){
        String[] strs = new String[]{"hi", "hello", "hell"};
        System.out.println(longestCommonPrefix(strs));
    }
}
