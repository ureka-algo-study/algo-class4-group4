import java.io.IOException;

public class P_12979_TLE {
    public int solution(int n, int[] stations, int w) {

        // 시간제한 1초: 마지노선 1억번
        // N: 200,000,000 이하의 자연수 --> TLE
        int answer = 0;
        int range = 2 * w + 1;
        boolean[] flag = new boolean[n+1];
        // 1~N까지 전파가 닿는 아파트 true
        for (int station : stations)
            for (int s = station - w; s <= station + w; s++)
                if (1 <= s && s <= n)
                    flag[s] = true;

        int temp = 0;
        for (int i = 1; i <= n; i++) {
        // N까지 순회하며 전파가 닿지 않는 아파트 만날 때마다 temp에 +1씩 저장
            if (!flag[i])
                temp++;
            else if (temp != 0) {
                // 기지국 1개당 2*w+1만큼 전파 전달 가능
                answer += ((temp - 1) / range) + 1;
                temp = 0;
            }
        }
        // 마지막 남은 아파트 처리
        if (temp != 0) answer += ((temp - 1) / range) + 1;

        return answer;
    }


    public void main(String[] args) throws IOException {

        System.out.println(solution(11, new int[] {4, 11}, 1));;

    }
}
