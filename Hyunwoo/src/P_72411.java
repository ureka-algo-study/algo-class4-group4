package Lv2;

import java.util.*;

public class P_72411 {
    Set<String> answerSet = new HashSet<>();    // answer에 중복되지 않게 저장하기 위한 Set
    int[] lengthCount = new int[11];            // 길이가 n인 문자열 중 최대 count를 저장하기 위한 배열
    char[] temp;                                // 조합 결과를 저장하기 위한 임시 배열
    Map<String, Integer> stringCountMap = new HashMap<>();

    // 모든 orders[i]에 대해 모든course[i]개의 조합을 구한다.
    public String[] solution(String[] orders, int[] course) {
        for (String order : orders) {
            char[] orderCharArr = order.toCharArray();  // String: 불변 -> 정렬할 수 있도록 char[]에 담아서 로직 수행
            Arrays.sort(orderCharArr);  // order: 정렬되지 않은 채로 입력될 수 있음. AB/BA와 같이 같은 메뉴 구성을 다른 경우로 count하지 않도록 정렬
            for (int c : course) {
                temp = new char[c];
                combination(orderCharArr, c, 0, 0);
            }
        }

        for (String s : stringCountMap.keySet())   //
            if (lengthCount[s.length()] < stringCountMap.get(s))
                lengthCount[s.length()] = stringCountMap.get(s);

        for (String s : stringCountMap.keySet())  // Line16: course안에 있는 숫자에 한해서 조합을 뽑아내기 때문에 길이 검증 필요x
            if (stringCountMap.get(s) == lengthCount[s.length()] && stringCountMap.get(s) > 1)
                answerSet.add(s);

        String[] answer = answerSet.toArray(new String[0]);
        Arrays.sort(answer);
        return answer;
    }

    public void combination(char[] orderCharArr, int c, int start, int idx) {
        if (idx == c) { // 길이가 c인 조합이 완성되면 해당 문자열의 count를 map에 더하기
            String s = new String(temp);
            if (stringCountMap.keySet().contains(s))   // stringCountMap.containsKey(s)로 바꿀 수 있음
                stringCountMap.put(s, stringCountMap.get(s) + 1);
            else
                stringCountMap.put(s, 1);
            // stringCountMap.put(s, stringCountMap.getOrDefault(s, 0) + 1);
            return;
        }

        for (int i = start; i < orderCharArr.length; i++) {
            temp[idx] = orderCharArr[i];
            combination(orderCharArr, c, i+1, idx+1);
        }
    }
}
