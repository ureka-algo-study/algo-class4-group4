import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class P_12980 {

    // 숫자 N: 1이상 10억이하 --> 앞에서부터 1 더해가며 순회(dp): TLE
    // 순간이동 후 점프, 점프 후 순간이동 중 무엇이 최선을 보장하는 지 알 수 없음

    public static int solution(int n) {
        int ans = 0;

        // 뒤에서부터 홀수면 -1(점프), 짝수면 /2(순간이동) (greedy)
        while (n > 0) {
            if (n % 2 == 0)
                n /= 2;
            else {
                n--;
                ans++;
            }
        }
        return ans;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        System.out.println(solution(N));
    }
}