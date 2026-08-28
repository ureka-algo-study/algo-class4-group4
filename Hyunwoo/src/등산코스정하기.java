import java.util.*;

class Solution {

    boolean[] canGo;
    List<List<Node>> adj = new ArrayList<>();
    boolean[] isGate;
    boolean[] isSummit;
    int[] maxWeight;

    static class Node {
        int to;
        int weight;
        public Node(int to, int weight) {
            this.to = to;
            this.weight = weight;
        }
    }

    public int[] solution(int n, int[][] paths, int[] gates, int[] summits) {
        maxWeight = new int[n+1];
        for (int i = 0; i <= n; i++) {
            maxWeight[i] = Integer.MAX_VALUE;
        }

        isGate = new boolean[n+1];
        isSummit = new boolean[n+1];

        for (int gate : gates) {
            isGate[gate] = true;
        }

        for (int summit : summits) {
            isSummit[summit] = true;
        }

        for (int i = 0; i <= n; i++) {
            adj.add(new ArrayList<>());
        }

        for (int[] path : paths) {
            int s = path[0];
            int e = path[1];
            int w = path[2];
            adj.get(s).add(new Node(e, w));
            adj.get(e).add(new Node(s, w));
        }

        return dijkstra(gates, summits);
    }

    public int[] dijkstra(int[] gates, int[] summits) {
        Queue<Node> pq = new PriorityQueue<>((o1, o2) -> {
            return o1.weight - o2.weight;
        });

        for (int gate : gates) {
            maxWeight[gate] = 0;
            pq.offer(new Node(gate, 0));
        }

        while (!pq.isEmpty()) {
            Node currNode = pq.poll();
            int curr = currNode.to;

            if (isSummit[curr])
                continue;

            if (currNode.weight > maxWeight[curr])
                continue;

            for (Node nextNode : adj.get(curr)) {
                if (isGate[nextNode.to])
                    continue;

                int newWeight = Math.max(maxWeight[curr], nextNode.weight);
                if (newWeight < maxWeight[nextNode.to]) {
                    maxWeight[nextNode.to] = newWeight;
                    pq.offer(new Node(nextNode.to, newWeight));
                }
            }
        }

        Arrays.sort(summits);
        int tempSummit = -1;
        int tempIntensity = 10000001;
        for (int summit : summits) {
            if (maxWeight[summit] < tempIntensity) {
                tempSummit = summit;
                tempIntensity = maxWeight[summit];
            }
        }

        return new int[] {tempSummit, tempIntensity};

    }
}