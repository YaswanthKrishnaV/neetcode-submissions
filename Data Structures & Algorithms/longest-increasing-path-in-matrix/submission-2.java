class Solution {
    int[][] directions = {{-1,0},{1,0},{0,-1},{0,1}};
    int[][] dp;

    private int dfs(int[][] matrix, int r, int c, int prevVal){
        int ROWS = matrix.length, COLS = matrix[0].length;
        if (r < 0 || r >= ROWS || c < 0 ||
            c >= COLS || matrix[r][c] <= prevVal) {
            return 0;
        }
        if(dp[r][c]!=-1) return dp[r][c];
        int res =1;
        for(int[] d: directions){
            res = Math.max(res, 1+ dfs(matrix, r+d[0], c+d[1],matrix[r][c]));
        }
        return dp[r][c]= res;
    }

    public int longestIncreasingPath(int[][] matrix) {
        int rows = matrix.length, cols = matrix[0].length;
        int lip = 0;
        dp = new int[rows][cols];
        for(int i=0;i<rows;i++){
            for(int j=0;j<cols;j++){
                dp[i][j] = -1;
            }
        }
        for(int r=0;r<rows;r++){
            for(int c=0;c<cols;c++){
                lip = Math.max(lip, dfs(matrix, r,c, Integer.MIN_VALUE));
            }
        }
        return lip;     
    }
}
