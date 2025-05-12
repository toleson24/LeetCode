class Solution {
    public int singleNumber(int[] nums) {
        Map<Integer, Boolean> map = new HashMap<>();
        int single = -1;
        for (int i = 0;  i < nums.length; i++) { //int j = nums.length; i < nums.length, j >= 0; i++; j--
            if (map.getOrDefault(nums[i], null) == null)
                map.put(nums[i], false);
            else
                map.put(nums[i], true);
        }
        for (int i = 0; i < nums.length; i++) {
            if (map.get(nums[i]) == false)
                single = nums[i];
        }
        return single;
    }
}