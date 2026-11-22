class Solution {
    private int sum(int[] nums){
        int total =0;
        for(int n: nums){
            total+=n;
        }
        return total;
    }
    public int canCompleteCircuit(int[] gas, int[] cost) {
        if(sum(gas)<sum(cost)) return -1;
        
        int tank = 0, total=0, start=0;
        for(int i =0; i<gas.length;i++){
            int gain = gas[i]-cost[i];
            tank+=gain;
            total+=gain;

            if(tank<0){
                start = i+1;
                tank=0;
            }
        }
        return total>=0 ? start:-1;
        
    }
}
