import java.util.*;

class Solution {
    public int[] solution(int[][] edges) {
        int[] answer = new int[4];
        
        // 노드의 개수 구하기
        int maxNode = 0;
        for(int[] edge : edges)
            maxNode = Math.max(maxNode, Math.max(edge[0], edge[1]));
        
        int[] in = new int[maxNode + 1];
        int[] out = new int[maxNode + 1];
        
        for(int i = 0; i < edges.length; i++) {
            in[edges[i][1]]++;
            out[edges[i][0]]++;
        }
        
        // 생성노드 구하기
        for(int i = 1; i <= maxNode; i++) {
            if(in[i] == 0 && out[i] >= 2) {
                answer[0] = i;
                break;
            }
        }
        
        for(int i = 1; i <= maxNode; i++) {
            // 막대 모양
            if(in[i] >= 1 && out[i] == 0)
                answer[2]++;
            // 8자 모양
            else if(in[i] >= 2 && out[i] >= 2) {
                answer[3]++;
            }
        }
        
        // 도넛은 생성 노드에서 나가는 간선 개수 - 다른 모양의 그래프의 개수
        answer[1] = out[answer[0]] - answer[2] - answer[3];
        
        return answer;
        
        
    }
}