class Solution {
    public int findMin(int[] nums) {
        int left = 0;
        int right = nums.length - 1;

        while (left < right) {
            int mid = (int) (left + (right - left) / 2);

            if (nums[mid] < nums[right]) {
                right = mid;
            } else { // nums[mid] >= nums[right]
                left = mid + 1;
            }
        }

        return nums[left];
    }
}