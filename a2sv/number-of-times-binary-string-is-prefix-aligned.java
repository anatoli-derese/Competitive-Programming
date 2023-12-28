class Solution {
    public int numTimesAllBlue(int[] flips) {
        int _max = -1;
        int count = 0;
        for (int i = 0; i < flips.length; i ++){
            _max = Math.max(_max, flips[i]);
            if (i+1 == _max){
                count++;
            }
        }
        return count;
        
    }
}