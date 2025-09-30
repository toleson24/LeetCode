// runtime: 70.36%, memory: 6.09%
class Solution {
    public int longestConsecutive(int[] nums) {
        int _max = 0;
        Set<Integer> _set = new HashSet<>();
        for (int num : nums) {
            _set.add(num);
        }

        for (int num : _set) {
            if (!_set.contains(num - 1)) {
                int length = 1;

                while (_set.contains(num + length)) {
                    length++;
                }

                _max = Math.max(_max, length);
            }
        }

        return _max;
    }
}