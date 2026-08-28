import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

class P_81303 {

    public static class Node {
        int num;
        Node prev;
        Node next;

        public Node(int num) {
            this.num = num;
        }
    }

    Deque<Integer> cancelStack = new ArrayDeque<>();
    Node[] nodeArr;
    boolean[] isCanceled;

    public String solution(int n, int k, String[] cmd) {
        String answer = "";

        nodeArr = new Node[n];
        isCanceled = new boolean[n];

        for (int i = 0; i < n; i++) {
            Node node = new Node(i);
            nodeArr[i] = node;
        }

        for (int i = 0; i < n; i++) {
            Node node = nodeArr[i];
            if (i > 0) {
                node.prev = nodeArr[i - 1];
            }

            if (i < n-1) {
                node.next = nodeArr[i + 1];
            }
        }

        Node currNode = nodeArr[k];
        for (String command : cmd) {
            StringTokenizer st = new StringTokenizer(command);
            char task = st.nextToken().charAt(0);

            if (task == 'U') {
                int idx = Integer.parseInt(st.nextToken());
                for (int i = 0; i < idx; i++)
                    currNode = currNode.prev;
            } else if (task == 'D') {
                int idx = Integer.parseInt(st.nextToken());
                for (int i = 0; i < idx; i++)
                    currNode = currNode.next;
            } else if (task == 'C') {
                if (currNode.next != null)
                    currNode.next.prev = currNode.prev;
                if (currNode.prev != null)
                    currNode.prev.next = currNode.next;
                cancelStack.push(currNode.num);
                isCanceled[currNode.num] = true;
                currNode = currNode.next == null ? currNode.prev : currNode.next;
            } else if (task == 'Z' && !cancelStack.isEmpty()) {
                int recoverIdx = cancelStack.pop();
                Node recoverNode = nodeArr[recoverIdx];
                if (recoverNode.next != null) {
                    recoverNode.next.prev = recoverNode;
                }
                if (recoverNode.prev != null) {
                    recoverNode.prev.next = recoverNode;
                }

                isCanceled[recoverIdx] = false;
            }

        }

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            if (isCanceled[i]) {
                sb.append('X');
            } else {
                sb.append('O');
            }
        }

        answer = sb.toString();
        return answer;
    }
}
