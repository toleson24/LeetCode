#include <cmath>
#include <cstdlib>
#include <stack>
#include <unordered_map>
#include <unordered_set>

int add_(int x, int y) { return x + y; }
int sub_(int x, int y) { return x - y; }
int mul_(int x, int y) { return x * y; }
int div_(int x, int y) { return trunc(x / y); }

// runtime: 37.73%, memory: 15.04% 
class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        unordered_set<string> operators = {"+", "-", "*", "/"};
        unordered_map<string, int(*)(int, int)> operations = {
            { "+", add_ }, 
            { "-", sub_ }, 
            { "*", mul_ }, 
            { "/", div_ },
        };
        stack<int> st;

        for (const string& tok : tokens) {
            // if (operators.find(tok) != operators.end()) {
            if (operators.contains(tok)) {
                int y = st.top(); st.pop();
                int x = st.top(); st.pop();

                int result = operations[tok](x, y);
                st.push(result);
            } else {
                st.push(stoi(tok));
            }
        }

        return st.top();
    }
};