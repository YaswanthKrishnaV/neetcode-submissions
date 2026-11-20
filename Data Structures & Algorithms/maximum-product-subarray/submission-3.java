class Solution {
    public int maxProduct(int[] nums) {
        if (nums.length ==1){
            return nums[0];
        }
        int res = nums[0];
        int curMax = 1, curMin = 1;
        for(int num: nums){
            int tmp1 = curMax*num;
            int tmp2 = curMin*num;
            curMax = Math.max(num, Math.max(tmp1, tmp2));
            curMin = Math.min(num, Math.min(tmp1, tmp2));
            res = Math.max(res, curMax);
        }
        return res;
    }

}
