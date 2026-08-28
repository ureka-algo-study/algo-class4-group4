class 양궁대회 {

    int scoreDiff = -1;
    int[] answerScore = new int[11];
    public int[] solution(int n, int[] info) {
        int[] answer = {};

        int[] score = new int[11];

        dfs(n, 0, 0, score, info);

        if (scoreDiff == -1) {
            answer = new int[] {-1};
        } else {
            answer = answerScore;
        }

        return answer;
    } // solution

    public void dfs(int n, int idx, int count, int[] score, int[] info) {

        if (idx == 11 || count == n) {

            score[10] += n - count;

            int apeach = 0;
            int lion = 0;
            int totalScore = 0;

            for (int i = 0; i <= 10; i++) {
                if (info[i] == 0 && score[i] == 0) {
                    continue;
                } else if (info[i] >= score[i]) {
                    apeach += 10 - i;
                } else {
                    lion += 10 - i;
                }
            } // for

            if (lion - apeach > 0) {

                if (scoreDiff < lion - apeach) {
                    scoreDiff = lion - apeach;
                    answerScore = score.clone();
                } else if (scoreDiff == lion - apeach) {
                    for (int j = 10; j >= 0; j--) {
                        if (score[j] > answerScore[j]) {
                            answerScore = score.clone();
                            break;
                        } else if (score[j] < answerScore[j]) {
                            break;
                        }
                    }
                }
            }


            score[10] -= n - count;

            return;

        } // if

        if (n - count >= info[idx] + 1) {
            score[idx] += info[idx] + 1;
            dfs(n, idx + 1, count + info[idx] + 1, score, info);
            score[idx] -= info[idx] + 1;
        } // if

        dfs(n, idx + 1, count, score, info);

    } // dfs
}