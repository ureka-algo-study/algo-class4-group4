import java.util.*;

class Solution {
    public static ArrayList<Integer>[] tree = new ArrayList[17];
    public static int[] Info;
    public static int answer = -1;
    
    public int solution(int[] info, int[][] edges) {
        
        Info = info;
        
        // 트리 구조 구현
        for(int i = 0; i < 17; i++){
            tree[i] = new ArrayList<>();
        }
        
        for(int i = 0; i < edges.length; i++){
            int parent = edges[i][0];
            int child = edges[i][1];
            tree[parent].add(child);
        }
        
        // 미방문 노드 저장을 위한 리스트
        ArrayList<Integer> notVisit = new ArrayList<>();
        notVisit.add(0);
        dfs(notVisit, 0, 0, 0);
        
        return answer;
    }
    
    public static void dfs(ArrayList<Integer> notVisit, int cur, int wolf, int sheep) {
        // 현재 위치가 양 or 늑대 확인
        if(Info[cur] == 0)
            sheep++;
        else
            wolf++;
        
        // 양의 수 <= 늑대의 수 이면 리턴
        if(sheep <= wolf)
            return;
        
        System.out.println(cur);
        // 기존의 답과 현재 양의 마리 수를 비교하여 더 큰 값 저장
        answer = Math.max(answer, sheep);
        
        // 미방문 노드 리스트에서 현재 노드를 제거하고 자식 노드들을 추가
        notVisit.remove(Integer.valueOf(cur)); // int 값인 cur을 그냥 넣으면 index로 인식하기에 객체로 wrapping
        notVisit.addAll(tree[cur]);
        
        for(int i = 0; i < notVisit.size(); i++) {
            int next = notVisit.get(i);
            ArrayList<Integer> getChild = new ArrayList<>(notVisit);
            dfs(getChild, next, wolf, sheep);
        }
    }
    
    
}