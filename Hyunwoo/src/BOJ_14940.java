import java.util.*;
import java.io.*;

public class BOJ_14940 {
    static int N, M;
    static int[][] board;
    static boolean[][] visited;
    static int[][] dist;
    static int[] di = {0, -1, 0, 1};
    static int[] dj = {1, 0, -1, 0};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb;

        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        board = new int[N][M];
        visited = new boolean[N][M];
        dist = new int[N][M];

        int si = 0;
        int sj = 0;
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
                if (board[i][j] == 2) {
                    si = i;
                    sj = j;
                }
            }
        }

        bfs(si, sj);

        sb = new StringBuilder();
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (visited[i][j]) {
                    sb.append(dist[i][j]).append(" ");
                } else if (board[i][j] == 0) {
                    sb.append(0).append(" ");
                } else {
                    sb.append(-1).append(" ");
                }
            }
            sb.append("\n");
        }

        System.out.println(sb);

    }

    public static void bfs(int si, int sj) {
        Queue<Pos> q = new ArrayDeque<>();
        q.add(new Pos(si, sj));
        visited[si][sj] = true;
        while (!q.isEmpty()) {
            Pos curr = q.poll();
            int ci = curr.i;
            int cj = curr.j;
            for (int d = 0; d < 4; d++) {
                int ni = ci+di[d];
                int nj = cj+dj[d];
                if (0 <= ni && ni < N && 0 <= nj && nj < M && board[ni][nj] != 0 && !visited[ni][nj]) {
                    dist[ni][nj] = dist[ci][cj] + 1;
                    visited[ni][nj] = true;
                    q.add(new Pos(ni, nj));
                }
            }
        }
    }

    public static class Pos {
        int i;
        int j;
        public Pos(int i, int j) {
            this.i = i;
            this.j = j;
        }
    }
}
