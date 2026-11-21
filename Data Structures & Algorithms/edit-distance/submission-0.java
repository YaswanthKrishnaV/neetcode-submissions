class Solution {
    public int minDistance(String word1, String word2) {
        if(word1.length() < word2.length()){
            String tmp = word1;
            word1=word2;
            word2 = tmp;
        }
        int m = word1.length(), n= word2.length();
        int[][] dp = new int[m+1][n+1];

        for (int j = 0; j <= n; j++) {
            dp[m][j] = n - j;
        }
        for (int j = 0; j <= m; j++) {
            dp[j][n] = m - j;
        }

        
        for(int i=m-1;i>=0;i--){
            for(int j=n-1;j>=0;j--){
                if(word1.charAt(i)==word2.charAt(j)){
                    dp[i][j] = dp[i+1][j+1];
                }else{
                    dp[i][j] = 1 + Math.min(dp[i+1][j+1],Math.min(dp[i+1][j],dp[i][j+1]));
                }
            }
        }
        return dp[0][0];
    }
}
