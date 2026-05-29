package Uhjin.BOJ;

import java.io.*;
import java.util.*;

public class boj_14940_쉬운최단거리 {

    public static int n, m, startX, startY;
    public static int[][] map, result;
    public static Queue<int[]> queue = new LinkedList<>();
    public static boolean[][] visited;
    public static int[] dx = { 0, 0, -1, 1 };
    public static int[] dy = { -1, 1, 0, 0 };
    public static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        visited = new boolean[n][m];
        map = new int[n][m];
        result = new int[n][m];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                int num = Integer.parseInt(st.nextToken());
                map[i][j] = num;
                if (num == 2) {
                    startX = j;
                    startY = i;
                }
            }
        }

        navigation(startX, startY);

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (visited[i][j] && map[i][j] == 1) {
                    sb.append(result[i][j]).append(" ");
                } else if (!visited[i][j] && map[i][j] == 1) {
                    sb.append(-1 + " ");
                } else {
                    sb.append(0).append(" ");
                }
            }
            sb.append("\n");
        }

        System.out.println(sb.toString());

    }

    public static void navigation(int sx, int sy) {
        queue.add(new int[] { sy, sx });
        visited[sy][sx] = true;
        result[sy][sx] = 0;

        while (!queue.isEmpty()) {
            int[] current = queue.poll();
            int cy = current[0];
            int cx = current[1];

            for (int i = 0; i < 4; i++) {
                int nx = cx + dx[i];
                int ny = cy + dy[i];

                if (nx >= 0 && ny >= 0 && nx < m && ny < n && map[ny][nx] == 1 && !visited[ny][nx]) {
                    visited[ny][nx] = true;
                    result[ny][nx] = result[cy][cx] + 1;
                    queue.add(new int[] { ny, nx });
                }
            }
        }
    }

}
