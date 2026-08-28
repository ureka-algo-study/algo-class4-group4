import java.util.*;

class Solution {
    public int[] solution(int n, int[][] paths, int[] gates, int[] summits) {

        // 인접 리스트 graph 배열 구성
        List<int[]>[] graph = new List[n + 1];
        for (int i = 1; i <= n; i++) 
            graph[i] = new ArrayList<>();

        for (int[] path : paths) {
            graph[path[0]].add(new int[]{path[1], path[2]});
            graph[path[1]].add(new int[]{path[0], path[2]});
        }
        
        // gate와 summit을 Set으로 구분
        Set<Integer> gateSet   = new HashSet<>();
        Set<Integer> summitSet = new HashSet<>();
        // gates[], summits[] 배열을 각각 Set에 추가
        for(int i = 0; i < gates.length; i++)
            gateSet.add(gates[i]);
        
        for(int i = 0; i < summits.length; i++)
            summitSet.add(summits[i]);
        
        // intensity 배열 초기화
        int[] intensity = new int[n + 1];
        Arrays.fill(intensity, Integer.MAX_VALUE);
        // 모든 gate의 intensity는 0으로 설정
        for (int gate : gates)
            intensity[gate] = 0;
        
        // Multi-source Dijkstra 시작
        // PriorityQueue: {노드번호, 현재intensity} 기준으로 intensity 오름차순
        // 모든 gate를 큐에 넣고 시작
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[1] - b[1]);
        for(int gate : gates)
            pq.offer(new int[] {gate, 0});
        
        // Dijkstra
        while (!pq.isEmpty()) {
            int[] cur = pq.poll();
            int node = cur[0];
            int cost = cur[1];

            // 이미 더 좋은 경로로 처리된 노드면 스킵
            // cost와 intensity[node]를 비교
            if(cost > intensity[node])
                continue;

            // summit이면 더 이상 진행하지 않음
            // summitSet 활용 — 왜냐면 summit은 도착점이지 경유지가 아니기 때문
            if(summitSet.contains(node))
                continue;

            // 인접 노드 순회
            for (int[] next : graph[node]) {
                int nextNode = next[0];
                int edgeCost = next[1];
        
                // 핵심: 누적 합이 아닌 Math.max!
                int newIntensity = Math.max(cost, edgeCost);

                // newIntensity가 더 작을 때만 갱신 + 큐에 추가
                if (newIntensity < intensity[nextNode]) {
                    // intensity 배열 갱신하고 pq에 추가
                    intensity[nextNode] = newIntensity;
                    pq.offer(new int[]{nextNode, newIntensity});
                }
            }
        }
        
        // summits 중 intensity 최솟값 찾기
        // summit 번호 오름차순 정렬 후 순회
        // intensity가 같으면 번호가 작은 것 선택
        Arrays.sort(summits);
        
        int answerSummit = -1;
        int answerIntensity = Integer.MAX_VALUE;
        for (int summit : summits) {
            // intensity[summit]이 answerIntensity보다 작을 때만 갱신
            // 같을 때는 갱신 X → 오름차순 정렬 덕분에 번호 작은 게 자동으로 선택됨
            if(intensity[summit] < answerIntensity) {
                answerIntensity = intensity[summit];
                answerSummit = summit;
            }
        }
        
        return new int[]{answerSummit, answerIntensity};
    }
}