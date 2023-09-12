import java.util.*;

class Solution {
    int[] dx = {-1,1,0,0};
    int[] dy = {0,0,-1,1};
    
    public int solution(int[][] maps) {
        int answer = 0;
        int[][] visited = new int[maps.length][maps[0].length];
        bfs(maps,visited);
        answer = visited[maps.length-1][maps[0].length-1];
        
        if(answer == 0)
            return -1;
        else
            return answer;
    }
    
    public void bfs(int[][] maps, int[][] visited) {
        int x = 0;
        int y = 0;
        
        Queue<int[]> queue = new LinkedList<>();
        visited[x][y] = 1;
        queue.add(new int[]{x,y});
        
        while(!queue.isEmpty()) {
            int[] current = queue.remove();
            
            for(int i=0; i < 4; i++) {
                int nx = current[0] + dx[i];
                int ny = current[1] + dy[i];
                
                if(nx < 0 || ny < 0 || nx >= maps.length || ny >= maps[0].length)
                    continue;
                
                if(visited[nx][ny] == 0 && maps[nx][ny] == 1) {
                    visited[nx][ny] = visited[current[0]][current[1]] + 1;
                    queue.add(new int[]{nx,ny});
                }
            }
        }
    }
}