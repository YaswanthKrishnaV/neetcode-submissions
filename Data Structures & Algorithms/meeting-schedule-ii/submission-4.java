/**
 * Definition of Interval:
 * public class Interval {
 *     public int start, end;
 *     public Interval(int start, int end) {
 *         this.start = start;
 *         this.end = end;
 *     }
 * }
 */

class Solution {
    public int minMeetingRooms(List<Interval> intervals) {
        // Collections.sort(intervals, Comparator.comparingInt(i->i.start));
        // int res = 1;
        // int lastend = intervals.get(0)[1];
        // for(int i=1;i < intervals.size();i++){
        //     Interval i1 = intervals.get(i-1);
        //     Interval i2 = intervals.get(i);

        //     if(i1.end>i2.start && lastend<i2.start){
        //         res++;
        //         lastend = Math.
        //     }
        // }
        // return res;

        intervals.sort((a,b) -> a.start - b.start);
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();

        for(Interval interval: intervals){
            if(!minHeap.isEmpty() && minHeap.peek()<=interval.start){
                minHeap.poll();
            }
            minHeap.offer(interval.end);
        
        }
        return minHeap.size();

    }
}
