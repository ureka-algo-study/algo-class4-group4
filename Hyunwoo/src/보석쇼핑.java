import java.util.*;

class 보석쇼핑 {

    public int[] solution(String[] gems) {

        Map<String, Integer> gemMap = new HashMap<>();
        Set<String> gemSet = new HashSet(Arrays.asList(gems));
        int size = gemSet.size();

        int minCount = 100000;
        int left = 0;
        int right = 0;
        int answerLeft = left;
        int answerRight = right;

        while (right < gems.length) {
            gemMap.put(gems[right], gemMap.getOrDefault(gems[right], 0) + 1);

            while (gemMap.size() == size) {
                if (minCount > right - left) {
                    answerLeft = left;
                    answerRight = right;
                    minCount = right - left;
                }

                if (gemMap.get(gems[left]) == 1) {
                    gemMap.remove(gems[left]);
                } else {
                    gemMap.put(gems[left], gemMap.get(gems[left]) - 1) ;
                }

                left++;
            }

            right++;
        }

        return new int[] {answerLeft+1, answerRight+1};
    }

}