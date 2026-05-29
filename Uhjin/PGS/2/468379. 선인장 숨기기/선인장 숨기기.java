import java.util.*;

class Solution {
    public int[] solution(int m, int n, int h, int w, int[][] drops) {
        int noRain = drops.length + 1;
        int[][] desert = new int[m][n];
        
        for(int i = 0; i < m; i++){
            Arrays.fill(desert[i], noRain);
        }
        
        for(int i = 0; i < drops.length; i++){
            int y = drops[i][0];
            int x = drops[i][1];
            desert[y][x] = i + 1;
        }
        
        int col = n - w + 1;
        int[][] rowMin = new int[m][col];
        
        for(int r = 0; r < m; r++){
            Deque<Integer> dq = new ArrayDeque<>();
            for(int c = 0; c < n; c++){
                while(!dq.isEmpty() && desert[r][dq.peekLast()] >= desert[r][c])
                    dq.pollLast();
                
                dq.addLast(c);
                
                while(!dq.isEmpty() && dq.peekFirst() <= c - w)
                    dq.pollFirst();
                
                if(c >= w - 1)
                    rowMin[r][c - w + 1] = desert[r][dq.peekFirst()];
            }
        }
        
        int row = m - h + 1;
        int[][] rectMin = new int[row][col];
        
        for(int c = 0; c < col; c++){
            Deque<Integer> dq = new ArrayDeque<>();
            for(int r = 0; r < m; r++) {
                while(!dq.isEmpty() && rowMin[dq.peekLast()][c] >= rowMin[r][c])
                    dq.pollLast();
                
                dq.addLast(r);
                
                while(!dq.isEmpty() && dq.peekFirst() <= r - h)
                    dq.pollFirst();
                
                if(r >= h - 1)
                    rectMin[r - h + 1][c] = rowMin[dq.peekFirst()][c];
            }
        }
        
        int max = -1;
        int[] answer = new int[2];
        
        for(int r = 0; r < row; r++){
            for(int c = 0; c < col; c++){
                if(rectMin[r][c] > max) {
                    max = rectMin[r][c];
                    answer[0] = r;
                    answer[1] = c;
                }
            }
        }
        
        return answer;
    }
}