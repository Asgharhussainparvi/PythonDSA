"""
Queue Implementation in Python
-----------------------------
A queue is a linear data structure that follows the FIFO (First In First Out) principle.
Common operations:
- enqueue: Add an element to the rear of the queue
- dequeue: Remove and return the front element
- front: View the front element without removing it
- rear: View the rear element without removing it
- is_empty: Check if the queue is empty
- size: Get the number of elements in the queue
"""

from collections import deque

class Queue:
    def __init__(self):
        """
        Initialize an empty queue using deque.
        Using deque instead of list for better performance in queue operations.
        """
        self.items = deque()
    
    def enqueue(self, item):
        """
        Add an element to the rear of the queue.
        Time Complexity: O(1)
        """
        self.items.append(item)
    
    def dequeue(self):
        """
        Remove and return the front element from the queue.
        Time Complexity: O(1)
        Raises IndexError if queue is empty
        """
        if not self.is_empty():
            return self.items.popleft()
        raise IndexError("Queue is empty")
    
    def front(self):
        """
        Return the front element without removing it.
        Time Complexity: O(1)
        Raises IndexError if queue is empty
        """
        if not self.is_empty():
            return self.items[0]
        raise IndexError("Queue is empty")
    
    def rear(self):
        """
        Return the rear element without removing it.
        Time Complexity: O(1)
        Raises IndexError if queue is empty
        """
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("Queue is empty")
    
    def is_empty(self):
        """
        Check if the queue is empty.
        Time Complexity: O(1)
        """
        return len(self.items) == 0
    
    def size(self):
        """
        Return the number of elements in the queue.
        Time Complexity: O(1)
        """
        return len(self.items)
    
    def clear(self):
        """
        Remove all elements from the queue.
        Time Complexity: O(1)
        """
        self.items.clear()

def main():
    # Create a new queue
    queue = Queue()
    
    # Demonstrate queue operations
    print("Queue Operations Demo:")
    print("-" * 20)
    
    # Enqueue elements
    print("\nEnqueueing elements...")
    queue.enqueue("First")
    queue.enqueue("Second")
    queue.enqueue("Third")
    print(f"Queue after enqueueing: {list(queue.items)}")
    
    # View front and rear
    print(f"\nFront element: {queue.front()}")
    print(f"Rear element: {queue.rear()}")
    
    # Dequeue elements
    print("\nDequeueing elements...")
    while not queue.is_empty():
        print(f"Dequeued: {queue.dequeue()}")
    
    # Try to dequeue from empty queue
    print("\nTrying to dequeue from empty queue...")
    try:
        queue.dequeue()
    except IndexError as e:
        print(f"Error: {e}")
    
    # Enqueue more elements
    print("\nEnqueueing more elements...")
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(f"Queue: {list(queue.items)}")
    print(f"Queue size: {queue.size()}")
    
    # Clear the queue
    print("\nClearing the queue...")
    queue.clear()
    print(f"Queue is empty: {queue.is_empty()}")

if __name__ == "__main__":
    main() 