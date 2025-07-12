class MyQueue(object):

    def __init__(self):
        # Write your code here
        self.stck1 = []
        self.stck2 = []

    def push(self, x):
        # Write your code here
        while self.stck1:
            self.stck2.append(self.stck1.pop())
        self.stck1.append(x)
        while self.stck2:
            self.stck1.append(self.stck2.pop())

    def pop(self):
        # Write your code here
        return None if self.empty() else self.stck1.pop()

    def peek(self):
        # Write your code here
        return None if not self.stck1 else self.stck1[-1]

    def empty(self):
        # Write your code here
        return not self.stck1


q = MyQueue()
print(q.empty())
q.push(2)
print(q.peek())
q.push(3)
print(q.peek())
q.push(4)
print(q.peek())
q.push(5)
print(q.peek())