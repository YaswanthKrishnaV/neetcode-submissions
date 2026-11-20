class Solution {
    
    public int rob(int[] nums){
        if (nums.length ==1)
            return nums[0];
        return Math.max(nums[0],
               Math.max(helper(Arrays.copyOfRange(nums, 1, nums.length)),
               helper(Arrays.copyOfRange(nums, 0, nums.length - 1))));
    }
    private int helper(int[] nums){
        if (nums.length ==1)
            return nums[0];
        
        int rob1 = nums[0];
        int rob2 = Math.max(nums[0], nums[1]);

        for (int i=2; i<nums.length;i++){
            int temp = Math.max(rob2, nums[i] + rob1);
            rob1 = rob2;
            rob2 = temp;
        }
        return Math.max(rob1,rob2);
    }
}
