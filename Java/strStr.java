package Java;

public class strStr {
    public static int strStr(String haystack, String needle) {
        if (needle.isEmpty()) return 0;

        return haystack.indexOf(needle);
    }

    public static void main(String[] args){
        String haystack = "aaaaa";
        String needle = "bba";


        System.out.println(strStr(haystack, needle));
    }
}
