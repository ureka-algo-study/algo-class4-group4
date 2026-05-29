import java.io.IOException;

public class P_12979 {
    public int solution(int n, int[] stations, int w) {
        int answer = 0;
        int curr = 1;
        int range = 2 * w + 1;

        for (int station : stations) {
            if (station - w > curr)
                answer += (station - curr - w - 1) / range + 1;
            curr = station + w + 1;
        }

        if (curr <= n)
            // (n - curr + 1): 남은 아파트 수, (x-1) / n + 1: 올림처리
            answer += (n - curr) / range + 1;

        return answer;
    }


    public void main(String[] args) throws IOException {

        System.out.println(solution(11, new int[] {4, 11}, 1));;

    }
}
