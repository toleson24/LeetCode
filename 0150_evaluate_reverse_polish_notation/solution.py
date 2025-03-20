class FailedSolution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack: List[str] = []
        operators = {"+", "-", "*", "/"}
        
        for token in tokens:
            if token in operators.keys():
                op2 = int(stack.pop())
                op1 = int(stack.pop())
                
                if token == "+":
                    token = op1 + op2
                elif token == "-":
                    token = op1 - op2
                elif token == "*":
                    token = op1 * op2
                elif token == "/":
                    temp = op1 / op2
                    # print(f"temp={temp}")
                    if abs(temp) < 1:
                        temp = 0
                    else:
                        temp = op1 // op2
                    token = temp
                
            stack.append(f"{token}")
            # print(stack)
            
        return int(stack.pop())
        
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack: List[str] = []
        oper_funcs = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: math.trunc(x / y)
        }
        
        for token in tokens:
            if token in oper_funcs.keys():
                op2 = int(stack.pop())
                op1 = int(stack.pop())

                token = oper_funcs[token](op1, op2)
                
            stack.append(f"{token}")
            
        return int(stack.pop())
        
        