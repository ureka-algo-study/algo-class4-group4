public class P_150365 {

    int[] di = new int[]{1, 0, 0, -1};
    int[] dj = new int[]{0, -1, 1, 0};
    char[] charArr;
    char[] dir = {'d', 'l', 'r', 'u'};
    String answer = "";
    boolean flag = false;

    public String solution(int n, int m, int x, int y, int r, int c, int k) {
        charArr = new char[k];
        int distance = Math.abs(x - r) + Math.abs(y - c);

        if (distance > k || (k - distance) % 2 == 1) {
            answer = "impossible";
        } else {
            dfs(n, m, x, y, r, c, k, 0);
        }

        return answer;
    }

    public void dfs(int n, int m, int ci, int cj, int r, int c, int k, int idx) {

        if (idx >= k) {
            if(ci == r && cj == c) {
                answer = new String(charArr);
                flag = true;
            }
            return;
        }

        if(flag)
            return;

        int distance = Math.abs(ci - r) + Math.abs(cj - c);
        if (distance > k - idx) return;

        for (int d = 0; d < 4; d++) {
            int ni = ci + di[d];
            int nj = cj + dj[d];
            if (canGo(ni, nj, n, m)) {
                charArr[idx] = dir[d];
                dfs(n, m, ni, nj, r, c, k, idx+1);
            }
        }
    }

    public boolean canGo(int ni, int nj, int n, int m) {
        return 1 <= ni && ni <= n && 1 <= nj && nj <= m;
    }
}
