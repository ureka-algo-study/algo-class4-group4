class Solution {
    static int MOD = 10007;
    
    public int solution(int n, int[] tops) {
        int answer = 0;
        
        int green = (tops[0] == 0) ? 2 : 3;
        int purple = 1;
        
        for(int i = 1; i < n; i++){
            int nGreen = (tops[i] == 0) ? ( 2 * green + purple) : (3 * green + 2 * purple);
            int nPurple = green + purple;
            
            green = nGreen % MOD;
            purple = nPurple % MOD;
        }
        
        answer = (green + purple) % MOD;
        
        return answer;
    }
}

