package Java;

import java.util.Stack;

public class validParentheses {

    public boolean isValid(String s) {
        Stack<Character> bracket = new Stack<>();
        for(int i=0; i<s.length(); i++){
            if(s.charAt(i) == '(' || s.charAt(i) =='{' || s.charAt(i) =='['){
                bracket.push(s.charAt(i));
            }
            if(s.charAt(i) == ')'){
                if (bracket.isEmpty()) return false;
                else if (bracket.peek() != '(') return false;
                else bracket.pop();
            } 
            else if(s.charAt(i) == '}'){
                if (bracket.isEmpty()) return false;
                else if (bracket.peek() != '{') return false;
                else bracket.pop();
            } 
            else if(s.charAt(i) == ']'){
                if (bracket.isEmpty()) return false;
                else if (bracket.peek() != '[') return false;
                else bracket.pop();
            }
        }
        if (!bracket.isEmpty()) return false;
        return true;
    }
    public static void main(String[] args){

    }
}

// string only contains '(', '[', and '{'
class Solution{
    public boolean isValid2(String s){
        Stack<Character> stack = new Stack();

        for(int i=0; i<s.length(); i++){
            char c = s.charAt(i);
            switch(c){
                case '(':
                    stack.push('(');
                    break;
                case '[':
                    stack.push('[');
                    break;
                case '{':
                    stack.push('{');
                // ')', ']', '}'
                default:
                    if(stack.isEmpty() || stack.pop() != c) return false;
                    break;
            }
        }
        // if empty -> true, not empty -> false
        return stack.isEmpty();
    }
}