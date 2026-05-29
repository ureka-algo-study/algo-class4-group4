import java.util.*;

class Solution {
    public static int[][] mask;
    public static int r, c;
    
    public int solution(int[][] board, int[][] skill) {
        int answer = 0;
        
        r = board.length;
        c = board[0].length;
        
        mask = new int[r + 1][c + 1];

        for (int[] s : skill) {
            int type = s[0];
            int r1 = s[1];
            int c1 = s[2];
            int r2 = s[3];
            int c2 = s[4];
            int degree = s[5];

            int val = (type == 1) ? -degree : degree;

            mask[r1][c1] += val;
            mask[r1][c2 + 1] -= val;
            mask[r2 + 1][c1] -= val;
            mask[r2 + 1][c2 + 1] += val;
        }
        
        for(int i = 0; i < r; i++){
            for(int j = 1; j <= c; j++){
                mask[i][j] += mask[i][j - 1];
            }
        }
        for(int j = 0; j <= c; j++){
            for(int i = 1; i <= r; i++){
                mask[i][j] += mask[i - 1][j];
            }
        }
        
        for(int i = 0; i < r; i++) {
            for(int j = 0; j < c; j++) {
                board[i][j] += mask[i][j];
                if(board[i][j] >= 1)
                    answer++;
            }
        }
        
        return answer;
    }
}