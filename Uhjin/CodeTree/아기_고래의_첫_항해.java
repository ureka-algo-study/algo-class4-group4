package Uhjin.CodeTree;

import java.util.*;
import java.io.*;

public class 아기_고래의_첫_항해 {
    public static int N, r, c, d;
    public static int[][] map;
    public static boolean[][] visited;

    public static int[] dx = { 0, 0, 0, -1, 1 }; // 왼쪽, 오른쪽
    public static int[] dy = { 0, -1, 1, 0, 0 }; // 위, 아래

    public static int[][] changeDir = {
            { 0, 0, 0, 0, 0 },
            { 0, 1, 3, 4, 2 }, // dir1 (위)
            { 0, 2, 4, 3, 1 }, // dir2 (아래)
            { 0, 3, 2, 1, 4 }, // dir3 (왼쪽)
            { 0, 4, 1, 2, 3 }, // dir4 (오른쪽)
    };

    static class Node {
        int r, c, dist, dir;

        Node(int r, int c, int dist, int dir) {
            this.r = r;
            this.c = c;
            this.dist = dist;
            this.dir = dir;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        r = Integer.parseInt(st.nextToken()) - 1;
        c = Integer.parseInt(st.nextToken()) - 1;
        d = Integer.parseInt(st.nextToken());

        visited = new boolean[N][N];
        map = new int[N][N];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        simulation();
    }

    public static void simulation() {
        visited[r][c] = true;
        System.out.println(r + 1 + " " + (c + 1));

        for (int k = 0; k < N * N; k++) {
            if (explore()) {
                System.out.println(r + 1 + " " + (c + 1));
                continue;
            }

            Node next = getNextStep();
            if (next == null)
                return;

            r = next.r;
            c = next.c;
            d = next.dir;
            visited[r][c] = true;

            System.out.println(r + 1 + " " + (c + 1));
        }
    }

    public static boolean explore() {
        for (int i = 1; i <= 4; i++) {
            int dir = changeDir[d][i];
            int nr = r + dy[dir];
            int nc = c + dx[dir];

            if (nr < 0 || nc < 0 || nr >= N || nc >= N)
                continue;
            if (map[nr][nc] == 1 || visited[nr][nc])
                continue;

            r = nr;
            c = nc;
            d = dir;
            visited[r][c] = true;
            return true;
        }
        return false;
    }

    public static Node getNextStep() {
        boolean[][] seen = new boolean[N][N];
        Queue<Node> q = new ArrayDeque<>();
        q.add(new Node(r, c, 0, 0)); // dir 초기값 0 (미사용)
        seen[r][c] = true;

        List<Node> candidates = new ArrayList<>();

        // BFS 탐색 순서: {LEFT,DOWN,RIGHT,UP} = {3,2,4,1}
        int[] priorityDir = { 3, 2, 4, 1 };

        while (!q.isEmpty()) {
            Node cur = q.poll();

            for (int pd : priorityDir) {
                int nr = cur.r + dy[pd];
                int nc = cur.c + dx[pd];

                if (nr < 0 || nc < 0 || nr >= N || nc >= N)
                    continue;
                if (seen[nr][nc] || map[nr][nc] == 1)
                    continue;

                seen[nr][nc] = true;

                int dir;
                if (nr - cur.r == -1)
                    dir = 1; // UP
                else if (nr - cur.r == 1)
                    dir = 2; // DOWN
                else if (nc - cur.c == 1)
                    dir = 4; // RIGHT
                else
                    dir = 3; // LEFT

                Node next = new Node(nr, nc, cur.dist + 1, dir);
                candidates.add(next);
                q.add(next);
            }
        }

        Node best = null;
        for (Node node : candidates) {
            if (visited[node.r][node.c])
                continue;
            if (best == null ||
                    node.dist < best.dist ||
                    (node.dist == best.dist && node.r < best.r) ||
                    (node.dist == best.dist && node.r == best.r && node.c < best.c)) {
                best = node;
            }
        }
        return best;
    }
}