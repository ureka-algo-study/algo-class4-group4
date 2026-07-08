import java.io.*;
import java.util.*;

public class Main {
    public static int n, m, S, T;
    public static List<List<Integer>> adjList = new ArrayList<>(); // S에서 시작
    public static List<List<Integer>> reverseAdjList = new ArrayList<>(); // T에서 시작

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        for (int i = 0; i <= n; i++) {
            adjList.add(new ArrayList<>());
            reverseAdjList.add(new ArrayList<>());
        }

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            adjList.get(x).add(y);
            reverseAdjList.get(y).add(x);
        }

        st = new StringTokenizer(br.readLine());
        S = Integer.parseInt(st.nextToken());
        T = Integer.parseInt(st.nextToken());

        // 목적지 정점에 도착하면 현서는 더 이상 움직이지 않는다.
        // 따라서 정점 v가 출근길, 퇴근길에 모두 포함되는지 확인하려면
        // S -> v, v -> T, T -> v, v -> S 총 4번 확인해야 한다.
        boolean[] reachFromS = bfs(S, adjList, T);        // S -> v, T에서 멈춤
        boolean[] canReachT  = bfs(T, reverseAdjList, 0); // v -> T, 제약 없음
        boolean[] reachFromT = bfs(T, adjList, S);        // T -> v, S에서 멈춤
        boolean[] canReachS  = bfs(S, reverseAdjList, 0); // v -> S, 제약 없음

        int cnt = 0;
        for (int v = 1; v <= n; v++) {
            if (v == S || v == T) 
                continue;

            if (reachFromS[v] && canReachT[v] && reachFromT[v] && canReachS[v]) 
                cnt++;
        }

        System.out.println(cnt);
    }

    // block == 0 이면 제약 없는 일반 BFS와 동일하게 동작
    public static boolean[] bfs(int start, List<List<Integer>> graph, int block) {
        boolean[] visited = new boolean[n + 1];
        Queue<Integer> queue = new LinkedList<>();
        visited[start] = true;
        queue.add(start);

        while (!queue.isEmpty()) {
            int cur = queue.poll();
            if (cur == block) 
                continue; // block 노드(S or T)에서는 더 뻗어나가지 않음
                
            for (int next : graph.get(cur)) {
                if (!visited[next]) {
                    visited[next] = true;
                    queue.add(next);
                }
            }
        }
        return visited;
    }
}