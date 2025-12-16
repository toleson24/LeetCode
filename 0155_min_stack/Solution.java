// runtime: 73.40%, memory: 100.00% 
class MinStack {
    List<Integer> values;
    List<Integer> indices;
    int min;
    int minIndex;

    public MinStack() {
        this.values = new LinkedList<>();
        this.indices = new LinkedList<>();
        this.min = Integer.MAX_VALUE;
        this.minIndex = -1;
    }

    // 4, 7, 2, 6, 5, 8, 1
    // 0, 1, 0, 1, 2, 3, 0
    
    public void push(int val) {
        this.values.add(0, val);
        if (val < min) {
            this.min = val;
            this.minIndex = 0;
            this.indices.add(0, minIndex);
        } else {
            this.minIndex++;
            this.indices.add(0, minIndex);
        }
    }
    
    public void pop() {
        this.values.remove(0);
        this.indices.remove(0);
        if (indices.size() > 0) {
            this.min = this.values.get(indices.get(0));
            this.minIndex = indices.get(0);
            // this.min = this.values.get(minIndex);
        } else {
            this.minIndex = -1;
            this.min = Integer.MAX_VALUE;
        }
    }
    
    public int top() {
        return this.values.get(0);
    }
    
    public int getMin() {
        return this.values.get(this.indices.get(0));
    }

}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(val);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */