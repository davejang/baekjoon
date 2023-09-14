import java.util.*;

class Solution {
    public String solution(String[] cards1, String[] cards2, String[] goal) {
        String answer = "Yes";
        Queue<String> cardQueue1 = new LinkedList<>();
        Queue<String> cardQueue2 = new LinkedList<>();
        
        for(int i=0; i<cards1.length; i++) {
            cardQueue1.add(cards1[i]);
        }
        for(int i=0; i<cards2.length; i++) {
            cardQueue2.add(cards2[i]);
        }
        
        for(int i=0; i<goal.length; i++) {
            if(goal[i].equals(cardQueue1.peek())){
                cardQueue1.remove();
                continue;
            }
            if(goal[i].equals(cardQueue2.peek())){
                cardQueue2.remove();
                continue;
            }
            answer = "No";
        }
        

        return answer;
    }
}