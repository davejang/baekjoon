import java.util.*;

class Solution {
    public int solution(int[] scoville, int K) {
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        int answer = 0;
        int y = 0;
        int x1 = 0;
        int x2 = 0;
        
        for(int i=0; i<scoville.length; i++) {
            pq.offer(scoville[i]);
        }
        
        if(pq.peek() >= K) {
            return 0;
        }
        
        while(pq.size() >= 2) {
            x1 = pq.poll();
            x2 = pq.poll();
            y = x1 + (x2 * 2);
            pq.offer(y);
            answer ++;
            
            if(pq.peek() >= K) {
                return answer;
            }
        }
        
        return -1;
    }
}