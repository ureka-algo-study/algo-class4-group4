class 징검다리건너기 {
    public int solution(int[] stones, int k) {
        int left = 0;
        int right = 0;
        for (int stone : stones) {
            if (right < stone) {
                right = stone;
            }
        }

        return binarySearch(left, right, stones, k);
    }

    public int binarySearch(int left, int right, int[] stones, int k) {
        int mid = 0;
        while (left <= right) {
            mid = (left + right) / 2;

            int temp = 0;
            boolean flag = true;
            for (int stone : stones) {
                if (stone - mid < 0) {
                    temp++;
                } else {
                    temp = 0;
                }

                if (temp >= k) {
                    flag = false;
                    break;
                }
            }

            if (flag) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        return right;
    }
}