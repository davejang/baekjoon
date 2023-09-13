import java.util.*;

class Solution {
    public String[] solution(String[] players, String[] callings) {
        String[] answer = new String[players.length];
        HashMap<String,Integer> hashMap = new HashMap<>();
        
        for(int i=0; i<players.length; i++) {
            hashMap.put(players[i],i);
        }
        
        for(int i=0; i<callings.length; i++) {
            String goPlayer = callings[i];
            int goPlayerRank = hashMap.get(goPlayer);
            
            String backPlayer = players[goPlayerRank-1];
            
            players[goPlayerRank-1] = goPlayer;
            players[goPlayerRank] = backPlayer;
            
            hashMap.put(goPlayer,goPlayerRank-1);
            hashMap.put(backPlayer,goPlayerRank);
        }
        
        return players;
    }
}