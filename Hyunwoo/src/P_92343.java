import java.util.ArrayList;
import java.util.List;

public class P_92343 {
    List<List<Integer>> adj = new ArrayList<>();
    List<Integer> nextNodes = new ArrayList<>();
    int answer = 0;

    public int solution(int[] info, int[][] edges) {

        for (int i = 0; i < info.length; i++) {
            adj.add(new ArrayList<>());
        }

        for (int[] edge : edges) {
            int start = edge[0];
            int end = edge[1];
            adj.get(start).add(end);
        }

        for (int next : adj.get(0)) {
            nextNodes.add(next);
        }


        dfs(1, 0, info, nextNodes);

        return answer;
    }

    public void dfs(int sheep, int wolf, int[] info, List<Integer> nextNodes) {

        answer = Math.max(answer, sheep);

        for (int curr : nextNodes) {
            int nextSheep = sheep;
            int nextWolf = wolf;
            if (info[curr] == 0)
                nextSheep++;
            else
                nextWolf++;

            if (nextSheep <= nextWolf)
                continue;

            List<Integer> newNextNodes = new ArrayList(nextNodes);
            newNextNodes.remove(Integer.valueOf(curr));
            for (int next : adj.get(curr)) {
                newNextNodes.add(next);
            }

            dfs(nextSheep, nextWolf, info, newNextNodes);
        }


    }
}
