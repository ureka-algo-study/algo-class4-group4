import java.util.*;

class Solution {
    public int[] solution(String[] gems) {
        int[] answer = new int[2];

        Set<String> set = new HashSet<>();
        for (String gem : gems) {
            set.add(gem);
        }

        int gemsType = set.size();

        int left = 0;
        int len = Integer.MAX_VALUE;
        Map<String, Integer> map = new HashMap<>();

        for (int right = 0; right < gems.length; right++) {
            map.put(gems[right], map.getOrDefault(gems[right], 0) + 1);

            while (map.get(gems[left]) > 1) {
                map.put(gems[left], map.get(gems[left]) - 1);
                left++;
            }

            if (map.size() == gemsType && len > right - left) {
                len = right - left;
                answer[0] = left + 1;
                answer[1] = right + 1;
            }
        }

        return answer;
    }
}