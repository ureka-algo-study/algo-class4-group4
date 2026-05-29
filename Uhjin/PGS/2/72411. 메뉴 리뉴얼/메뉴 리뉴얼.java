import java.util.*;

class Solution {
    Map<String, Integer> map = new HashMap<>();

    public String[] solution(String[] orders, int[] course) {
        for (int i = 0; i < orders.length; i++) {
            char[] arr = orders[i].toCharArray();
            Arrays.sort(arr);
            orders[i] = new String(arr);
        }

        List<String> answer = new ArrayList<>();

        for (int len : course) {
            map.clear();

            for (String order : orders) {
                if (order.length() >= len) {
                    comb(order, "", 0, len);
                }
            }

            // map에서 최댓값 찾고, 2 이상인 것만 answer에 추가
            int max = 0;
            for(int v : map.values())
                max = Math.max(max, v);
            
            if(max >= 2) {
                for(Map.Entry<String, Integer> entry : map.entrySet()) {
                    if(entry.getValue() == max)
                        answer.add(entry.getKey());
                }
            }
        }

        Collections.sort(answer);
        return answer.toArray(new String[0]);
    }

    public void comb(String order, String cur, int idx, int targetLen) {
        if(cur.length() == targetLen) {
            map.put(cur, map.getOrDefault(cur, 0) + 1);
            return;
        }
        
        for(int i = idx; i < order.length(); i++) {
            comb(order, cur + order.charAt(i), i + 1, targetLen);
        }
    }
}