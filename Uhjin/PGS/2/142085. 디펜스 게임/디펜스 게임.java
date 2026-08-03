import java.util.*;

class Solution {
    public int solution(int n, int k, int[] enemy) {
        int answer = 0;
        
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        
        for(int e : enemy) {
            if(k > 0) {
                pq.offer(e);
                k--;
            } else {
                int num = pq.poll();
                
                if(num < e) {
                   pq.offer(e);
                    n -= num;
                } else {
                    n -= e;
                    pq.offer(num);
                }
                
                if(n < 0)
                    break;
            }
            answer++;
        }
        
        return answer;
    }
}