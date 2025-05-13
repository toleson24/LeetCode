// runtime: 99.94%, memory: 35.41%
class Solution {
    public int singleNumber(int[] nums) {
        int single = 0;
        for (int n : nums) {
            single ^= n;
        }
        return single;
    }
}