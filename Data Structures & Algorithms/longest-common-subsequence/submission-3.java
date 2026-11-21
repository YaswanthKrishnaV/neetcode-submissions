class Solution {
    public int longestCommonSubsequence(String text1, String text2) {
        if(text1.length()<text2.length()){
            String tmp = text1;
            text1 = text2;
            text2 = tmp;
        }
        int m = text1.length(), n= text2.length();

        int[] curr = new int[n+1];
        int[] prev = new int[n+1];

        for(int i =m-1;i>=0;i--){
            for(int j = n-1; j>=0;j--){
                if(text1.charAt(i)==text2.charAt(j)){
                    curr[j]= 1 + prev[j+1];
                }else{
                    curr[j] = Math.max(curr[j+1],prev[j]);
                }

            }
            int[] tmp = prev;
            prev = curr;
            curr = tmp;
        }

        return prev[0];

        
    }
}
