import java.util.HashMap;

class Solution {
    public int[] solution(String[] name, int[] yearning, String[][] photo) {
        
        HashMap<String,Integer> hashMap = new HashMap<String,Integer>();
        int score;
        int[] answer = new int[photo.length];
        
        for(int i=0; i < name.length; i++) {
            hashMap.put(name[i],yearning[i]);
        }
        
        System.out.println(hashMap);
        for(int i=0; i < photo.length; i++) {
            score = 0;
            for(int j=0; j < photo[i].length; j++) {
                if(hashMap.containsKey(photo[i][j])) {
                    score += hashMap.get(photo[i][j]);
                }
            }
            answer[i] = score;

        }
        
        return answer;
    }
}