class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)

        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()

        return self.stack.pop()

    def top(self):
        return self.stack[-1]

    def get_min(self):
        return self.min_stack[-1]


stack = MinStack()

stack.push(5)
stack.push(3)
stack.push(7)
stack.push(2)

print("Minimum:", stack.get_min())

stack.pop()

print("Top:", stack.top())
print("Minimum:", stack.get_min())