// April 24, 2023
// runtime: 87.95%, memory: 99.37%
class Solution {
    public boolean containsDuplicate(int[] nums) {
        if (nums.length <= 0)
            return false;
        Map<Integer, Boolean> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            if (map.getOrDefault(nums[i], null) == null)
                map.put(nums[i], false);
            else
                return true;
        }
        return false;
    }
}