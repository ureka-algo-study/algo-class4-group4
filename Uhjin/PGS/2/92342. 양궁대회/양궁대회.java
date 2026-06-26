import java.util.*;

class Solution {
    private int[] lion = new int[11];
    private int[] arr = new int[11];
    private int max = Integer.MIN_VALUE;
    
    public int[] solution(int n, int[] info) {
        backTrack(0, n, info);
        
        if(max <= 0) {
            return new int[] {-1};
        }
        
        return lion;
    }
    
    public void backTrack(int idx, int remain, int[] info) {
        if(idx == 11) {
            arr[10] += remain; // 남은 화살 0점에 몰아주기
            int check = score(info);
            
            if(check > max) {
                max = check;
                lion = arr.clone();
            } else if(check == max) {
                // 동점이면 낮은 점수를 더 많이 맞힌 배열 선택
                for(int i = 10; i >= 0; i--){
                    if(arr[i] > lion[i]) {
                        lion = arr.clone();
                        break;
                    } else if (arr[i] < lion[i])
                        break;
                }
            }
            
            arr[10] -= remain;
            
            return;
        }
        
        if(info[idx] + 1 <= remain) {
            arr[idx] = info[idx] + 1;
            backTrack(idx + 1, remain - arr[idx], info);
            arr[idx] = 0;
        } 
        
        // 점수 포기
        backTrack(idx + 1, remain, info);
    }
    
    public int score(int[] info) {
        int apeach = 0;
        int lion = 0;
        
        for (int i = 0; i < arr.length; i++) {
            if (info[i] == 0 && arr[i] == 0) 
                continue; // 둘 다 0이면 skip
            if (arr[i] > info[i])
                lion += (10 - i);
            else
                apeach += (10 - i);
        }
        return lion - apeach;
    }
}