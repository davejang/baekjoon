import java.util.*;

class Solution {
    public int solution(int n) {
        int[] dp = new int[100001];
        int answer;
        
        dp[0] = 0;
        dp[1] = 1;
        
        for(int i=2; i<n+1; i++) {
            dp[i] = (dp[i-1] + dp[i-2]) % 1234567;
        }
        
        answer = dp[n];
        
        return answer;
    }
}