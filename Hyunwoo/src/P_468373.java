package Lv2;

import java.util.*;

public class P_468373 {

//    public void main(String[] args) {
//        int n = 7;
//        int infection = 6;
//        int[][] edges = new int[][] {
//                {1, 2, 3},
//                {1, 4, 3},
//                {4, 5, 1},
//                {5, 6, 1},
//                {3, 6, 2},
//                {3, 7, 2}};
//        int k = 3;
//        System.out.println(solution(n, infection, edges, k));
//    }

    List<Integer> infectedNodes = new ArrayList<>();
    List<List<Node>> nodes = new ArrayList<>();
    int[] comb;
    int answer = 0;

    public int solution(int n, int infection, int[][] edges, int k) {
        infectedNodes.add(infection);
        for (int i = 0; i <= 3; i++)
            nodes.add(new ArrayList<>());

        for (int[] edge : edges) {
            int s = edge[0];
            int e = edge[1];
            int t = edge[2];
            nodes.get(t).add(new Node(s, e));
            nodes.get(t).add(new Node(e, s));
        }

        comb = new int[k];
        combination(0, k, infection, n);

        return answer;
    }

    public void combination(int idx, int k, int start, int n) {
        if (idx == k) {
            answer = Math.max(answer, bfs(start, n));
            return;
        }

        for (int pipe = 1; pipe <= 3; pipe++) {
            if (idx == 0 || comb[idx-1] != pipe) {
                comb[idx] = pipe;
                combination(idx+1, k, start, n);
            }

        }
    }

    public int bfs(int start, int n) {
        infectedNodes = new ArrayList<>();
        boolean[] visited = new boolean[n+1];
        infectedNodes.add(start);
        visited[start] = true;
        for (int pipe : comb) {
            Deque<Integer> newInfectedNode = new ArrayDeque<>();
            for(Node node : nodes.get(pipe)) {
                if (visited[node.from] && !visited[node.to]) {
                    visited[node.to] = true;
                    infectedNodes.add(node.to);
                    newInfectedNode.add(node.to);
                }
            }

            while (!newInfectedNode.isEmpty()) {
                int curr = newInfectedNode.poll();
                for(Node node : nodes.get(pipe)) {
                    if (node.from == curr && !visited[node.to]) {
                        visited[node.to] = true;
                        infectedNodes.add(node.to);
                        newInfectedNode.add(node.to);
                    }
                }
            }
        }
        return infectedNodes.size();
    }

    public class Node {
        int from;
        int to;
        public Node(int from, int to) {
            this.from = from;
            this.to = to;
        }
    }
}
