package Lv3;

import java.util.*;

public class P_92344 {

    public int solution(int[][] board, int[][] skill) {
        int N = board.length;
        int M = board[0].length;
        int[][] degreeBoard = new int[N][M];
        int answer = 0;

        for (int tc = 0; tc < skill.length; tc++) {
            int type = skill[tc][0] == 1 ? -1 : 1;  // 공격타입이면 degree에 -1 곱해서 더하기
            int r1 = skill[tc][1];
            int c1 = skill[tc][2];
            int r2 = skill[tc][3];
            int c2 = skill[tc][4];
            int degree = skill[tc][5];

            // 2차원 누적합 로직
            degreeBoard[r1][c1] += degree * type;
            if (r2 < N-1) { degreeBoard[r2+1][c1] -= degree * type; }
            if (c2 < M-1) { degreeBoard[r1][c2+1] -= degree * type; }
            if (r2 < N-1 && c2 < M-1) { degreeBoard[r2+1][c2+1] += degree * type; }
        }

        /* TLE 1: 행 방향 누적합보다 열 방향 누적합을 먼저 하면 오답
        for (int i = 0; i < N; i++)
            for (int j = 1; j < M; j++)
                degreeBoard[i][j] += degreeBoard[i][j-1];
         */

        for (int i = 1; i < N; i++)
            for (int j = 0; j < M; j++)
                degreeBoard[i][j] += degreeBoard[i-1][j];

        for (int i = 0; i < N; i++)
            for (int j = 1; j < M; j++)
                degreeBoard[i][j] += degreeBoard[i][j-1];

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                board[i][j] += degreeBoard[i][j];
                if (board[i][j] > 0)
                    answer++;
            }
        }

         /* TLE 2: degreeBoard값을 board에 합치는 동시에 정답 처리하지 않으면 오답
        for (int i = 0; i < N; i++)
            for (int j = 0; j < M; j++)
                board[i][j] += degreeBoard[i][j];

        for (int i = 0; i < N; i++)
            for (int j = 0; j < M; j++)
                if (board[i][j] > 0)
                    answer++;
        */

        return answer;
    }
}
