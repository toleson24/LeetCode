class Solution {
    public int evalRPN(String[] tokens) {
        Map<String, BiFunction<Integer, Integer, Integer>> operatorFunctions = new HashMap<>();
        operatorFunctions.put("+", (x, y) -> x + y );
        operatorFunctions.put("-", (x, y) -> x - y );
        operatorFunctions.put("*", (x, y) -> x * y );
        operatorFunctions.put("/", (x, y) -> x / y );
        Stack<String> stack = new Stack<>();

        for (String token: tokens) {
            if (operatorFunctions.containsKey(token)) {
                int op2 = Integer.parseInt(stack.pop());
                int op1 = Integer.parseInt(stack.pop());
                int temp = operatorFunctions.get(token).apply(op1, op2);

                token = Integer.toString(temp);
            }

            stack.push(token);
        }

        return Integer.parseInt(stack.pop());
    }
}