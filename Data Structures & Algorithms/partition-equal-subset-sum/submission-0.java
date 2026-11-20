class Solution {
    public boolean canPartition(int[] nums) {
        if(sum(nums)%2!=0){
            return false;
        }
        int target = sum(nums)/2;
        boolean[] dp = new boolean[target+1];
        dp[0]= true;
        for(int n:nums){
            for(int j=target;j>=n;j--){
                dp[j] = dp[j] || dp[j-n];
            }
        }

        return dp[target];

        
    }
    private int sum(int[] nums){
        int total =0;
        for(int n: nums){
            total+=n;
        }
        return total;
    }
}
