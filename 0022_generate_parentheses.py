class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        parens = []
        stack = []

        def gen_parens(num_open, num_closed):
            if num_open == num_closed == n:
                parens.append("".join(stack))
                return
            
            if num_open < n:
                stack.append("(")
                gen_parens(num_open + 1, num_closed)
                stack.pop()
            
            if num_closed < num_open:
                stack.append(")")
                gen_parens(num_open, num_closed + 1)
                stack.pop()

        gen_parens(0, 0)

        return parens

        