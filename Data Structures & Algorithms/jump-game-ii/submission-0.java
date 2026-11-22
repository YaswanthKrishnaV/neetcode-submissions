class Solution {
    public int jump(int[] nums) {
        int jumps = 0, reach = 0, currEnd=0;

        for(int i =0;i<nums.length-1;i++){
            reach = Math.max(reach, i+ nums[i]);
            if(i==currEnd){
                jumps++;
                currEnd = reach;

                if(currEnd>nums.length){
                    break;
                }
            }
        }
        return jumps;
    }
}
