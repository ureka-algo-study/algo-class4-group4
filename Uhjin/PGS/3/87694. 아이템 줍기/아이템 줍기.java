import java.util.*;

class Solution {
    static int[][] grid; // 0: 갈 수 x, 1: 갈 수 O
    static int SIZE = 200; // 좌표 값 두 배수
    
    static int[] dx = {1, -1, 0, 0};
    static int[] dy = {0, 0, 1, -1};
    
    public int solution(int[][] rectangle, int characterX, int characterY, int itemX, int itemY) {
        grid = new int[SIZE][SIZE];
        
        markRectangles(rectangle);
        
        int answer = bfs(characterX * 2, characterY * 2, itemX * 2, itemY * 2);
        
        return answer / 2;
    }
    
    static void markRectangles(int[][] rectangle) {
        for(int[] rect : rectangle) {
            int x1 = rect[0] * 2;
            int y1 = rect[1] * 2;
            int x2 = rect[2] * 2;
            int y2 = rect[3] * 2;
            
            for(int x = x1; x <= x2; x++) {
                for(int y = y1; y <= y2; y++){
                    boolean isBorder = (x == x1 || x == x2 || y == y1 || y == y2);
                    if(isBorder)
                        grid[x][y] = 1; // 일단 벽(이동 가능한 테두리)으로 표시
                }
            }
        }
        
        // 테두리 빼고 나머지는 0으로
        for(int[] rect : rectangle) {
            int x1 = rect[0] * 2;
            int y1 = rect[1] * 2;
            int x2 = rect[2] * 2;
            int y2 = rect[3] * 2;
            
            for (int x = x1 + 1; x < x2; x++) {
                 for (int y = y1 + 1; y < y2; y++) {
                     grid[x][y] = 0; // 내부는 못 지나감
                 }
            }
        }
    }
    
    static int bfs(int startX, int startY, int endX, int endY) {
        int[][] dist = new int[SIZE][SIZE];
        
        for(int i = 0; i < dist.length; i++){
            Arrays.fill(dist[i], -1);
        }
        
        Queue<int[]> queue = new LinkedList<>();
        queue.offer(new int[] {startX, startY});
        dist[startX][startY] = 0;
        
        while(!queue.isEmpty()) {
            int[] cur = queue.poll();
            int cx = cur[0];
            int cy = cur[1];
            
            if(cx == endX && cy == endY)
                break;
            
            for(int i = 0; i < 4; i++){
                int nx = cx + dx[i];
                int ny = cy + dy[i];
                
                if(nx < 0 || ny < 0 || nx >= SIZE || ny >= SIZE) // 범위 초과
                    continue;
                if(grid[nx][ny] != 1) // 테두리가 아닐 시
                    continue;
                if(dist[nx][ny] != -1) // 이미 방문한 곳일 시
                    continue;
                
                dist[nx][ny] = dist[cx][cy] + 1;
                queue.offer(new int[] {nx, ny});
            }
        }
        
        return dist[endX][endY];
    }
}