public class P_258711 {

    public int[] solution(int[][] edges) {

        int[] inDegree = new int[1000001];
        int[] outDegree = new int[1000001];

        int maxNode = 0;

        for (int[] edge : edges) {
            int start = edge[0];
            int end = edge[1];

            outDegree[start]++;
            inDegree[end]++;

            maxNode = Math.max(maxNode, Math.max(start, end));
        }

        int initNode = 0;
        int donutCount = 0;
        int stickCount = 0;
        int eightCount = 0;

        for (int i = 1; i <= maxNode; i++) {
            if (outDegree[i] >= 2 && inDegree[i] == 0) {
                initNode = i;
            }
            else if (outDegree[i] == 0 && inDegree[i] >= 1) {
                stickCount++;
            }
            else if (outDegree[i] == 2 && inDegree[i] >= 2) {
                eightCount++;
            }
        }

        int totalGraphs = outDegree[initNode];
        donutCount = totalGraphs - (stickCount + eightCount);

        return new int[]{initNode, donutCount, stickCount, eightCount};
    }

}
