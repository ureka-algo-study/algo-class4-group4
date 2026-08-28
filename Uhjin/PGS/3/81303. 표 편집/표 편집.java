import java.util.*;

class Node {
    public int preNum; // 위쪽 행 (-1이면 맨 위)
    public int postNum; // 아래쪽 행 (n이면 맨 아래)
    
    public Node(int preNum, int postNum) {
        this.preNum = preNum;
        this.postNum = postNum;
    }
    
    
}

class Solution {
    
    public static Node[] nodes;
    public static Stack<Integer> deleted = new Stack<>();
    
    public String solution(int n, int k, String[] cmd) {
        
        nodes = new Node[n];
        
        for(int i = 0; i < n; i++){
            nodes[i] = new Node(i-1, i+1);
        }
        
        int cur = k;
        
        for(String command : cmd) {
            char op = command.charAt(0);
            
            if(op == 'U') {
                
                int x = Integer.parseInt(command.substring(2));
                for(int i = 0; i < x; i++)
                    cur = nodes[cur].preNum;
                
            } else if (op == 'D') {
                
                int x = Integer.parseInt(command.substring(2));
                for(int i = 0; i < x; i++)
                    cur = nodes[cur].postNum;
                
            } else if (op == 'C') {
                
                deleted.push(cur);
                
                if(nodes[cur].preNum != -1)
                    nodes[nodes[cur].preNum].postNum = nodes[cur].postNum;
                
                if(nodes[cur].postNum != n)
                    nodes[nodes[cur].postNum].preNum = nodes[cur].preNum;
                
                cur = (nodes[cur].postNum == n) ? nodes[cur].preNum : nodes[cur].postNum;
                
            } else { // 'Z'
                
                int r = deleted.pop();
                
                if(nodes[r].preNum != -1) 
                    nodes[nodes[r].preNum].postNum = r;
                    
                if(nodes[r].postNum != n)
                    nodes[nodes[r].postNum].preNum = r;
                
            }
        } // for
        
        char[] result = new char[n];
        Arrays.fill(result, 'O');
        while(!deleted.isEmpty()) {
            result[deleted.pop()] = 'X';
        }
        
        return new String(result);
    }
}