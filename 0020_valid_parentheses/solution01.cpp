#include <unordered_map>
#include <unordered_set>
#include <vector>

// runtime: 100.00%, memory: 15.02% 
class Solution {
public:
    bool isValid(string s) {
        int l = s.length();
        if (l < 2 || l % 2 == 1) {
            return false;
        }

        unordered_set<char> parens = {')', '}', ']'};
        unordered_map<char, char> pairs = { 
            {')', '('}, {'}', '{'}, {']', '['}};
        vector<char> stack;

        for (char ch : s) {
            if (stack.size() > 0 && parens.contains(ch)) {
                if (stack.back() == pairs[ch]) {
                    stack.pop_back();
                } else {
                    stack.push_back(ch);
                }
            } else {
                stack.push_back(ch);
            }
        }

        return stack.size() == 0;
    }
};