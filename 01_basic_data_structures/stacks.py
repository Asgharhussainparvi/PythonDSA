"""
Stack Implementation in Python
-----------------------------
A stack is a linear data structure that follows the LIFO (Last In First Out) principle.
Common operations:
- push: Add an element to the top of the stack
- pop: Remove and return the top element
- peek: View the top element without removing it
- is_empty: Check if the stack is empty
- size: Get the number of elements in the stack
"""

class Stack:
    def __init__(self):
        """Initialize an empty stack using a list."""
        self.items = []
    
    def push(self, item):
        """
        Add an element to the top of the stack.
        Time Complexity: O(1)
        """
        self.items.append(item)
    
    def pop(self):
        """
        Remove and return the top element from the stack.
        Time Complexity: O(1)
        Raises IndexError if stack is empty
        """
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("Stack is empty")
    
    def peek(self):
        """
        Return the top element without removing it.
        Time Complexity: O(1)
        Raises IndexError if stack is empty
        """
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("Stack is empty")
    
    def is_empty(self):
        """
        Check if the stack is empty.
        Time Complexity: O(1)
        """
        return len(self.items) == 0
    
    def size(self):
        """
        Return the number of elements in the stack.
        Time Complexity: O(1)
        """
        return len(self.items)
    
    def clear(self):
        """
        Remove all elements from the stack.
        Time Complexity: O(1)
        """
        self.items.clear()

def main():
    # Create a new stack
    stack = Stack()
    
    # Demonstrate stack operations
    print("Stack Operations Demo:")
    print("-" * 20)
    
    # Push elements
    print("\nPushing elements onto the stack...")
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print(f"Stack after pushing: {stack.items}")
    
    # Peek at top element
    print(f"\nTop element (peek): {stack.peek()}")
    
    # Pop elements
    print("\nPopping elements from the stack...")
    while not stack.is_empty():
        print(f"Popped: {stack.pop()}")
    
    # Try to pop from empty stack
    print("\nTrying to pop from empty stack...")
    try:
        stack.pop()
    except IndexError as e:
        print(f"Error: {e}")
    
    # Push more elements
    print("\nPushing more elements...")
    stack.push("A")
    stack.push("B")
    stack.push("C")
    print(f"Stack: {stack.items}")
    print(f"Stack size: {stack.size()}")
    
    # Clear the stack
    print("\nClearing the stack...")
    stack.clear()
    print(f"Stack is empty: {stack.is_empty()}")

if __name__ == "__main__":
    main() 