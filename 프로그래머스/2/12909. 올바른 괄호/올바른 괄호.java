import java.util.*;

class Solution {
    Stack<Character> stack = new Stack<>();
    char c;
    
    boolean solution(String s) {
        boolean answer = true;
        
        for(int i=0; i<s.length(); i++) {
            c = s.charAt(i);
            if(c == '(') {
                stack.push(c);
            }
            if(c == ')') {
                if(stack.isEmpty()) {
                    return false;
                }
                else {
                    if(stack.peek() == '(') {
                        stack.pop();
                    }
                    else {
                        return false;
                    }
                }
            }
        }
        
        if(!stack.isEmpty()) {
            return false;
        }
        else {
            return true;
        }
    }
}