public class Leetcode784 {
    public List<String> letterCasePermutation(String s) {
        List<String> answer = new ArrayList<String>(); 
        backtracking(answer, s.toCharArray(), 0);
        return answer;
    }

    public void backtracking(List<String> answer, char[] str, int index){
        if (index==str.length){
            answer.add(new String(str));
            return;
        }
        if (Character.isLetter(str[index])){
            str[index] = Character.toUpperCase(str[index]);
            backtracking(answer, str, index+1);
            str[index] = Character.toLowerCase(str[index]);
            backtracking(answer, str, index+1);
        }
        else{
            backtracking(answer, str, index+1);
        }
    }
}

// String -> Char: toCharArray
// Character.isLetter/toUpperCase/toLowerCase
// Char -> String: new String(array)
