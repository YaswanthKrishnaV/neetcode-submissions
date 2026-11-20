class Solution {
    public int maxProduct(int[] nums) {
        if (nums.length ==1){
            return nums[0];
        }
        // int[] dp = new int[nums.length];
        int res = nums[0];
        int curMax = 1, curMin = 1;
        for(int num: nums){
            int tmp = curMax*num;
            curMax = Math.max(num, Math.max(tmp, curMin*num));
            curMin = Math.min(num, Math.min(tmp, curMin*num));
            res = Math.max(res, curMax);
        }
        return res;
    }

}
