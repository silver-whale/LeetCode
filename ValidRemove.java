import java.util.Stack;

class ValidRemove {
    public static String minRemoveToMakeValid1(String s) {
        StringBuilder str = new StringBuilder(s);
        Stack<Integer> bracket = new Stack();

        for(int i=0; i<str.length(); i++){
            if(str.charAt(i) == '(')
                // Add 1 because of ~i later
                bracket.add(i+1);
            else if(str.charAt(i) == ')'){
                if(!bracket.empty() && bracket.peek() >= 0)
                    bracket.pop();
                else
                    // ~i returns 1's complement, and it's abs is 1 bigger than i
                    bracket.add(~i);
            }
        }
        
        while(!bracket.empty())
            str.deleteCharAt(Math.abs(bracket.pop()) - 1);

        return str.toString();
    }

    public static String minRemoveToMakeValid2(String s) {
        StringBuilder str = new StringBuilder(s);
        Stack<Integer> bracket = new Stack();
    
        for(int i=0; i<str.length(); i++){
            if (str.charAt(i) == '(') bracket.add(i);
            else if (str.charAt(i) == ')'){
                if (!bracket.empty()) bracket.pop();
                else str.setCharAt(i, ' ');
            }
        }

        while(!bracket.empty())
            str.setCharAt(bracket.pop(), ' ');

        String answer = new String(str.toString());
        return answer.replaceAll("\\s", "");
        
    }




    public static void main(String[] args){
        String answer = new String();
        // answer = minRemoveToMakeValid2("lee(t(c)o)de");
        // answer = minRemoveToMakeValid("a)b(c)d");
        answer = minRemoveToMakeValid2("))((");
        System.out.println(answer);
    }

}