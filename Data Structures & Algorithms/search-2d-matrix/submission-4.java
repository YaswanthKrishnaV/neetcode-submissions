class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int r1 = matrix.length;
        int c = matrix[0].length;
        
        int l = 0, r = r1*c-1;

        while (l<=r){
            int mid = (l+r)/2;
            int row = mid/c, col = mid%c;
            int val = matrix[row][col];
            if (target==val){
                return true;
            }else if (val<target){
                l = mid +1;
            }else{
                r= mid-1;
            }

        }
        return false;
        
    }
}
