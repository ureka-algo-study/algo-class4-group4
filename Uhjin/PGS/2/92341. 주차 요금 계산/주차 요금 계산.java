import java.util.*;

class Solution {
    public static Map<String, Integer> feeMap = new TreeMap<>(); // 총 주차시간 저장
    public static Map<String, Integer> inTimeMap = new HashMap<>(); // 입차시간 저장
    
    public int[] solution(int[] fees, String[] records) {
        int maxTime = getMinutes("23:59"); // 시간을 분으로 바꾸면 1439분
        
        for(String s : records) {
            String[] splitRecords = s.split(" ");
            
            int time = getMinutes(splitRecords[0]);
            String carNum = splitRecords[1];
            String type = splitRecords[2];
            
            if(type.equals("IN")) { // 입차시간 저장
                inTimeMap.put(carNum, time);
            } else { // 출차: 누적시간 계산
                int parked = time - inTimeMap.get(carNum);
                feeMap.put(carNum, feeMap.getOrDefault(carNum, 0) + parked);
                inTimeMap.remove(carNum);
            }
        }
        
        // 아직 출차 안한 차량들 자동 출차 처리
        for(String carNum : inTimeMap.keySet()) {
            int parked = maxTime - inTimeMap.get(carNum);
            feeMap.put(carNum, feeMap.getOrDefault(carNum, 0) + parked);
        }
        
        // TreeMap 순서대로 int[] 변환
        int[] answer = new int[feeMap.size()];
        int idx = 0;
        for(int time : feeMap.values()) {
            answer[idx++] = calFee(time, fees);
        }
        return answer;
    }
    
    public static int calFee(int time, int[] fees) {
        if(time <= fees[0]) 
            return fees[1];
        
        int extra = (time - fees[0] + fees[2] - 1) / fees[2]; // 올림
        return fees[1] + extra * fees[3];
    }
    
    public static int getMinutes(String time) {
        String[] times = time.split(":");
        return Integer.parseInt(times[0]) * 60 + Integer.parseInt(times[1]);
    }
}