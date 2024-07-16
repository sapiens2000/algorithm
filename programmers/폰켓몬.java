import java.util.*;

class Solution {
    public int solution(int[] nums) {
        int answer = 0;
        int max = nums.length / 2;
        
        HashSet<Integer> numSet = new HashSet<>();
        
        for(int num : nums) {
            numSet.add(num);
        }
        
        if(numSet.size() > max){
            return max;
        }else{
            return numSet.size();
        }
    }
}