# s = []
# s.append(1)
# s.append(2)
# s.append(3)
# s.append(4)
# print(s)

# s.pop()
# print(s)

# s.insert(2,1)

# print(s)

from collections import deque

class stack:
    def __init__(self):
        self.container = deque()

    def push(self , val):
        self.container.append(val)
    
    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return self.container[-1]
    
    def is_empty(self):
        return len(self.container)==0
    
    def size(self):
        return len(self.container)
    
    def output(self):
        return self.container[stack]

s = stack()

s.push(23)
s.push(3)
s.push(63)
s.push(83)
s.push(73)

s.pop()
s.pop()


s.peek()

print(s.output())