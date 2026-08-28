import java.util.*;

class Solution {
    public long solution(int cap, int n, int[] deliveries, int[] pickups) {
        long answer = 0;
        
        int dIdx = n - 1; // 가장 먼 배달
        int pIdx = n - 1; // 가장 먼 수거
        
        while(dIdx >= 0 || pIdx >= 0) {
            
            //이미 처리한 집은 건너뛰기
            while(dIdx >= 0 && deliveries[dIdx] == 0)
                dIdx--;
            while(pIdx >= 0 && pickups[pIdx] == 0)
                pIdx--;
            
            // 배달/수거 중 더 먼 집까지 왕복
            int dest = Math.max(dIdx, pIdx);
            if(dest < 0)
                break;
            answer += (long)(dest + 1) * 2;
            
            // 배달: 가장 먼 집부터 cap만큼 처리
            int boxes = cap;
            for(int i = dIdx; boxes > 0 && i >= 0; i--) {
                int taken = Math.min(deliveries[i], boxes);
                deliveries[i] -= taken;
                boxes -= taken;
                
                if(deliveries[i] == 0 && i == dIdx)
                    dIdx--;
            }
            
            // 수거: 가장 먼 집부터 cap만큼 처리
            boxes = cap;
            for(int i = pIdx; boxes > 0 && i >= 0; i--) {
                int taken = Math.min(pickups[i], boxes);
                pickups[i] -= taken;
                boxes -= taken;
                
                if(pickups[i] == 0 && i == pIdx)
                    pIdx--;
            }
        }
        
        return answer;
    }
}