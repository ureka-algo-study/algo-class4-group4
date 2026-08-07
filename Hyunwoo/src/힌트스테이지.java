public class 힌트스테이지 {

    boolean hintUsed[];
    int answer = Integer.MAX_VALUE;

    public int solution(int[][] cost, int[][] hint) {

        hintUsed = new boolean[hint.length];

        dfs(0, cost, hint);

        return answer;
    }

    public void dfs(int curr, int[][] cost, int[][] hint) {
        if (curr >= hint.length) {
            answer = Math.min(answer, calScore(cost, hint));
            return;
        }

        hintUsed[curr] = true;
        dfs(curr + 1, cost, hint);

        hintUsed[curr] = false;
        dfs(curr + 1, cost, hint);

    }

    public int calScore(int[][] cost, int[][] hint) {

        int totalCost = 0;
        int[] myHints = new int[cost.length];

        for (int stage = 0; stage < cost.length; stage++) {



            if (stage < hint.length && hintUsed[stage]) {
                totalCost += hint[stage][0];

                for (int i = 1; i < hint[stage].length; i++) {
                    myHints[hint[stage][i] - 1]++;
                }
            }

            int useHint = Math.min(myHints[stage], cost[stage].length - 1);

            totalCost += cost[stage][useHint];
        }

        return totalCost;
    }
}
