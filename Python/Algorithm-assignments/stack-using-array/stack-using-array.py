

class Stack:
    def __init__(self):
        self.arr = []
        self.available = 1000

    def is_empty(self):
        if self.available == 1000:
            return True
        return False

    def is_full(self):
        if self.available == 0:
            return True
        return False

    def push(self, val):
        if self.available == 0:
            print("sorry, the stack is full")
            return
        self.arr.append(val)
        self.available -= 1

    def pop(self):
        if self.available == 1000:
            print("the stack is empty")
            return
        removed = self.arr[-1]
        self.arr.pop()
        self.available += 1
        return removed

    def peek(self):
        if self.available == 1000:
            return None
        return self.arr[-1]

    def size(self):
        n = 0
        for i in self.arr:
            n += 1
        return n

s = Stack()

print(s.is_empty())
print(s.is_full())

s.push(10)
s.push(20)
s.push(30)

print(s.peek())

s.pop()
print(s.peek())

print(s.size())