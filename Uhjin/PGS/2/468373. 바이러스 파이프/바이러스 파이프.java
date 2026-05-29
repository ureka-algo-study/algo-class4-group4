import java.util.*;

class VirusPipe {
    int to;
    int type;

    public VirusPipe(int to, int type) {
        this.to = to;
        this.type = type;
    }
}

class Solution {
    public static int n, infection, k, answer;
    public static List<List<VirusPipe>> tree;
    public static int[] order;
    public static boolean[] infected;
    public static List<Integer> infectedList;

    public int solution(int n, int infection, int[][] edges, int k) {
        this.n = n;
        this.infection = infection;
        this.k = k;
        this.answer = 1;

        tree = new ArrayList<>();
        for (int i = 0; i <= n; i++) 
            tree.add(new ArrayList<>());

        for (int[] e : edges) {
            int a = e[0], b = e[1], type = e[2];
            tree.get(a).add(new VirusPipe(b, type));
            tree.get(b).add(new VirusPipe(a, type));
        }

        order = new int[k];
        infected = new boolean[n + 1];
        infectedList = new ArrayList<>();

        infected[infection] = true;
        infectedList.add(infection);

        backtrack(0, 0);

        return answer;
    }

    public void backtrack(int depth, int lastType) {
        if (depth == k) {
            answer = Math.max(answer, infectedList.size());
            return;
        }

        for (int type = 1; type <= 3; type++) {
            if (type == lastType) 
                continue;

            List<Integer> added = spread(type);
            backtrack(depth + 1, type);
            rollback(added);
        }
    }
    
    public List<Integer> spread(int type) {
        Queue<Integer> queue = new LinkedList<>();
        List<Integer> added = new ArrayList<>();
        
        for(int node : infectedList) {
            queue.offer(node);
        }
        
        while(!queue.isEmpty()) {
            int cur = queue.poll();
            
            for(VirusPipe next : tree.get(cur)) {
                if(next.type != type)
                    continue;
                if(infected[next.to])
                    continue;

                infected[next.to] = true;
                added.add(next.to);
                infectedList.add(next.to);
                queue.offer(next.to);
            }
        }
        
        return added;
    }
    
    public void rollback(List<Integer> added) {
        for (int i = 0; i <= added.size() - 1; i++) {
            int node = added.get(i);
            infected[node] = false;
            infectedList.remove(infectedList.size() - 1);
        }
    }
}