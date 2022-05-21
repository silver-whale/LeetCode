public class Leetcode557 {
    public String reverseWords(String s) {
        String[] words=s.split(" ");

        StringBuilder temp = new StringBuilder();

        for (int i = 0; i < words.length; i++) {
            temp.append(String.valueOf(new StringBuilder(words[i]).reverse()+" "));
        }

        return temp.toString().trim();
    }

    /*
    public String reverseWords(String s) {
        char[] str = s.toCharArray();
        int len = s.length(), i = 0, j = 0;
        while(i < len){
            while(i < len && str[i] == ' ') i++;
            j = i;
            while(i < len && str[i] != ' ') i++;
            reverse(str, j, i - 1);
        }
        return new String(str);
    }
    void reverse(char[] str, int s, int e){
        while(s < e){
            char temp = str[s];
            str[s++] = str[e];
            str[e--] = temp;
        }
    }
    */
}
