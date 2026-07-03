import java.util.*;

class 무지의먹방라이브 {

    class Food {
        int time;
        int index;

        public Food(int time, int index) {
            this.time = time;
            this.index = index;
        }
    }

    Queue<Food> q = new PriorityQueue<>((f1, f2) -> {
        return f1.time - f2.time;
    });

    public int solution(int[] food_times, long k) {

        long totalTime = 0;
        for (int time : food_times) {
            totalTime += time;
        }
        if (totalTime <= k) return -1;

        for (int i = 0; i < food_times.length; i++) {
            q.offer(new Food(food_times[i], i + 1));
        }

        int prevFoodTime = 0;

        while(!q.isEmpty() && k >= (long)(q.peek().time - prevFoodTime) * q.size()) {
            int currFoodTime = q.peek().time;
            int diff = currFoodTime - prevFoodTime;

            k -= (long)diff * q.size();

            while (!q.isEmpty() && q.peek().time == currFoodTime) {
                q.poll();
            }

            prevFoodTime = currFoodTime;
        }

        List<Food> list = new ArrayList<>();
        while (!q.isEmpty()) {
            list.add(q.poll());
        }

        list.sort((f1, f2) -> {
            return f1.index - f2.index;
        });

        return list.get((int)(k % list.size())).index;

    }
}
