import java.util.*;

class Solution {
    Queue<Integer> queue = new LinkedList<>();
    int completeDay = 0;
    int deployDay = 0;
    int count = 0;
    
    public int[] solution(int[] progresses, int[] speeds) {
        ArrayList<Integer> answer = new ArrayList<>();
        
        for(int i=0; i<progresses.length; i++) {
            completeDay = (int) Math.ceil((100 - progresses[i]) / (double) speeds[i]);
            
            if(!queue.isEmpty()){
                if(queue.peek() < completeDay) {
                    answer.add(queue.size());
                    while(!queue.isEmpty()) {
                        queue.poll();
                    }
                }
            }
            queue.add(completeDay);
        }
        
        if(!queue.isEmpty()){
            answer.add(queue.size());
        }
        
        return answer.stream().mapToInt(i -> i).toArray();
    }
}