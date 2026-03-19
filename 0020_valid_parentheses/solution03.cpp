#include <unordered_map>
#include <unordered_set>
#include <vector>

// runtime: 100.00%, memory: 99.31% 
class Solution {
public:
    bool isValid(string s) {
        int n = s.length();
        if (n < 2 || (n & 1)) 
            return false;

        string stack;
        stack.reserve(n);

        for (char ch : s) {
            if (ch == '(' || ch == '{' || ch == '[') {
                stack.push_back(ch);
            } else {
                if (stack.empty())
                    return false;
                char top = stack.back();
                if (ch == ')' && top == '(' || 
                    ch == '}' && top == '{' || 
                    ch == ']' && top == '[') {
                    stack.pop_back();
                } else {
                    return false;
                }
            }
        }

        return stack.empty();
    }
};