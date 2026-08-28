public class 아이템줍기 {

    int[][] board = new int[102][102];
    int[][] visited = new int[102][102];
    int[] di = {0, 1, 0, -1};
    int[] dj = {1, 0, -1, 0};

    int answer = Integer.MAX_VALUE;

    public int solution(int[][] rectangle, int characterX, int characterY, int itemX, int itemY) {



        for (int[] rect : rectangle) {
            for (int i = rect[0] * 2; i <= rect[2] * 2; i++) {
                for (int j = rect[1] * 2; j <= rect[3] * 2; j++) {
                    board[i][j] = 1;
                }
            }
        }

        for (int[] rect : rectangle) {
            for (int i = rect[0] * 2 + 1; i < rect[2] * 2; i++) {
                for (int j = rect[1] * 2 + 1; j < rect[3] * 2; j++) {
                    board[i][j] = 0;
                }
            }
        }

        dfs(characterX * 2, characterY * 2, itemX * 2, itemY * 2, 0);

        return answer / 2;
    }

    public void dfs(int ci, int cj, int itemX, int itemY, int count) {

        if (ci == itemX && cj == itemY) {
            answer = Math.min(answer, count);
            return;
        }

        visited[ci][cj] = 1;


        for (int d = 0; d < 4; d++) {
            int ni = ci + di[d];
            int nj = cj + dj[d];
            if (canGo(ni, nj)) {
                dfs(ni, nj, itemX, itemY, count + 1);
            }

        }
    }

    public boolean canGo(int ni, int nj) {
        if (ni < 0 || 102 <= ni || nj < 0 || 102 <= nj || board[ni][nj] == 0 || visited[ni][nj] == 1) {
            return false;
        }

        return true;
    }
}
