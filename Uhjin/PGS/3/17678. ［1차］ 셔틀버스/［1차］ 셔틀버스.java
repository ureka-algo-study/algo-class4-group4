import java.util.*;

class Solution {
    public StringBuilder solution(int n, int t, int m, String[] timetable) {
        // timetable 시간 순으로 정렬
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for (String time : timetable) {
            String[] getTime = time.split(":");
            pq.add(Integer.parseInt(getTime[0]) * 60 + Integer.parseInt(getTime[1]));
        }

        int busTime = 540;
        int lastBoard = 0;
        int result = 0;

        for (int i = 0; i < n; i++) {
            int cnt = 0;
            while (!pq.isEmpty() && pq.peek() <= busTime && cnt < m) {
                lastBoard = pq.poll();
                cnt++;
            }

            if (i == n - 1) {           // 막차 처리
                if (cnt == m)
                    result = lastBoard - 1;  // 만석 -> 마지막 탑승자보다 1분 일찍
                else
                    result = busTime;        // 자리 있음 -> 막차 시간에 맞춰 도착
            }

            busTime += t;
        }
        
        int hour = result / 60;
        int min = result % 60;
        
        StringBuilder sb = new StringBuilder();
        
        if(hour < 10)
            sb.append("0");
        sb.append(hour);
        
        sb.append(":");
        
        if(min < 10)
            sb.append("0");
        sb.append(min);

        return sb;
    }
}