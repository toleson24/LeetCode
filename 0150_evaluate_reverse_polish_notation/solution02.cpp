#include <cstdlib>
#include <stack>

// 20 Mar 2026 
// runtime: 100.00%, memory: 66.07% 
class Solution {
public:
    int operate(int x, int y, const string& op) {
        if (op == "+") 
            return x + y;
        else if (op == "-")
            return x - y;
        else if (op == "*") 
            return x * y;
        else // op == "/"
            return x / y;
    }

    int evalRPN(vector<string>& tokens) {
        stack<int> st;

        for (const string tok : tokens) {
            if (tok == "+" || tok == "-" || tok == "*" || tok == "/") {
                int y = st.top(); st.pop();
                int x = st.top(); st.pop();

                st.push(operate(x, y, tok));
            } else {
                st.push(stoi(tok));
            }
        }

        return st.top();
    }
};