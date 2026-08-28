import java.util.*;
import java.io.*;

public class 출퇴근길 {

    public class Main {

        public static List<List<Integer>> adj = new ArrayList<>();
        public static Set<Integer> toSet = new HashSet<>();
        public static Set<Integer> fromSet = new HashSet<>();
        public static boolean[] visited;

        public static void main(String[] args) throws IOException {

            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            StringTokenizer st;

            st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int m = Integer.parseInt(st.nextToken());

            for (int i = 0; i <= n; i++) {
                adj.add(new ArrayList());
            }

            for (int i = 0; i < m; i++) {
                st = new StringTokenizer(br.readLine());
                int start = Integer.parseInt(st.nextToken());
                int end = Integer.parseInt(st.nextToken());
                adj.get(start).add(end);
            }

            st = new StringTokenizer(br.readLine());
            int S = Integer.parseInt(st.nextToken());
            int T = Integer.parseInt(st.nextToken());

            for (int start : adj.get(S)) {
                visited = new boolean[n+1];
                visited[S] = true;
                dfs(S, T, true);
            }

            for (int start : adj.get(T)) {
                visited = new boolean[n+1];
                visited[T] = true;
                dfs(T, S, false);
            }

            toSet.retainAll(fromSet);

            System.out.println(toSet.size());

        }

        public static void dfs(int curr, int goal, boolean to) {

            for (int next : adj.get(curr)) {
                if (next == goal) {
                    return;
                }

                if (!visited[next]) {
                    visited[next] = true;
                    if (to) {
                        toSet.add(next);
                    } else {
                        fromSet.add(next);
                    }

                    dfs(next, goal, to);
                }
            }

        }
    }



    public static class main2 {

        static int n, m;
        static int s, t;
        static StringTokenizer st = null;
        static List<Integer>[] edgeList;
        static List<Integer>[] edgeListR;

        public static void main(String[] args) throws IOException{

            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            st = new StringTokenizer(br.readLine());
            n = Integer.parseInt(st.nextToken());
            m = Integer.parseInt(st.nextToken());

            edgeList = new ArrayList[n + 1];
            edgeListR = new ArrayList[n + 1];

            for(int i = 1; i <= n; i++){
                edgeList[i] = new ArrayList<>();
                edgeListR[i] = new ArrayList<>();
            }

            for(int i = 0; i < m; i++){
                st = new StringTokenizer(br.readLine());
                int start = Integer.parseInt(st.nextToken());
                int end = Integer.parseInt(st.nextToken());

                edgeList[start].add(end);
                edgeListR[end].add(start);
            }

            st = new StringTokenizer(br.readLine());
            s = Integer.parseInt(st.nextToken());
            t = Integer.parseInt(st.nextToken());

            boolean[] fromS = new boolean[n + 1];
            boolean[] fromT = new boolean[n + 1];
            boolean[] toS = new boolean[n + 1];
            boolean[] toT = new boolean[n + 1];

            fromS[t] = true;

            fromT[s] = true;

            dfs(s, edgeList, fromS);
            dfs(s, edgeListR, toS);
            dfs(t, edgeList, fromT);
            dfs(t, edgeListR, toT);

            int count = 0;

            for(int i=1;i<=n;i++){
                if(fromS[i] && fromT[i] && toS[i] && toT[i]){
                    count++;
                }
            }

            System.out.println(count - 2);
        }

        private static void dfs(int cur, List<Integer>[] list, boolean[] visited){
            if(visited[cur]){
                return;
            }

            visited[cur] = true;
            for(Integer next: list[cur]){
                dfs(next, list, visited);
            }
        }

    }
}
