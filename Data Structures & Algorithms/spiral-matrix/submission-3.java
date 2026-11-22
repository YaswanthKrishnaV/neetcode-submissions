class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        int top =0, left =0;
        int bottom = matrix.length-1;
        int right = matrix[0].length-1;
        List<Integer> res = new ArrayList<>();

        while(top<=bottom && left<=right){
            for(int l = left; l<=right;l++){
                res.add(matrix[top][l]);
            }
            top++;
            for(int t = top;t<=bottom;t++){
                res.add(matrix[t][right]);
            }
            right--;
            if(top > bottom || left>right){
                break;
            }
            for(int r = right;r>=left;r--){
                res.add(matrix[bottom][r]);
            }
            bottom--;
            for(int b = bottom;b>=top;b--){
                res.add(matrix[b][left]);
            }
            left++;
        }
        return res;
    }
}
