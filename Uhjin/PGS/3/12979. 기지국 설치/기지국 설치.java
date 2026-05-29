class Solution {
    public int solution(int n, int[] stations, int w) {
        int answer = 0;
        int start = 1;
        int range = w * 2 + 1; // 전파 범위

        for (int i = 0; i < stations.length; i++) {
            int left = stations[i] - w; // 기지국 범위의 왼쪽 끝
            int right = stations[i] + w; // 기지국 범위의 오른쪽 끝

            // 현재 위치가 기지국 범위의 왼쪽 끝 보다 작을 때 범위 계산
            if (start < left) {
                int cnt = (left - start) / range; // 새로 설치할 개수 확인
                int remain = (left - start) % range; // 새로 설치 후 범위 밖 남은 아파트 수 계산
                answer += cnt + (remain > 0 ? 1 : 0);
            }
            // 현재 위치를 기존 기지국 범위 오른쪽 끝 + 1로 이동
            start = right + 1;
        }

        // 남은 아파트가 있다면
        if (start <= n) {
            int cnt = (n - start + 1) / range;
            int remain = (n - start + 1) % range;
            if (remain == 0)
                answer += cnt;
            else
                answer += cnt + 1;
        }

        return answer;
    }
}