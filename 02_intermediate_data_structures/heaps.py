"""
Heap Implementation in Python
---------------------------
A heap is a specialized tree-based data structure that satisfies the heap property:
- In a Max Heap: Parent nodes are greater than or equal to their children
- In a Min Heap: Parent nodes are less than or equal to their children
Heaps are commonly used to implement priority queues and for heap sort.
"""

class Heap:
    def __init__(self, heap_type="min"):
        """
        Initialize a heap.
        Args:
            heap_type (str): "min" for min heap, "max" for max heap
        """
        self.heap = []
        self.heap_type = heap_type
        self.size = 0
    
    def _parent(self, i):
        """
        Get the index of the parent of node at index i.
        """
        return (i - 1) // 2
    
    def _left_child(self, i):
        """
        Get the index of the left child of node at index i.
        """
        return 2 * i + 1
    
    def _right_child(self, i):
        """
        Get the index of the right child of node at index i.
        """
        return 2 * i + 2
    
    def _swap(self, i, j):
        """
        Swap elements at indices i and j.
        """
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    
    def _heapify_up(self, i):
        """
        Maintain heap property by bubbling up the element at index i.
        Time Complexity: O(log n)
        """
        parent = self._parent(i)
        
        if self.heap_type == "min":
            if i > 0 and self.heap[i] < self.heap[parent]:
                self._swap(i, parent)
                self._heapify_up(parent)
        else:  # max heap
            if i > 0 and self.heap[i] > self.heap[parent]:
                self._swap(i, parent)
                self._heapify_up(parent)
    
    def _heapify_down(self, i):
        """
        Maintain heap property by bubbling down the element at index i.
        Time Complexity: O(log n)
        """
        left = self._left_child(i)
        right = self._right_child(i)
        smallest_or_largest = i
        
        if self.heap_type == "min":
            if left < self.size and self.heap[left] < self.heap[smallest_or_largest]:
                smallest_or_largest = left
            if right < self.size and self.heap[right] < self.heap[smallest_or_largest]:
                smallest_or_largest = right
        else:  # max heap
            if left < self.size and self.heap[left] > self.heap[smallest_or_largest]:
                smallest_or_largest = left
            if right < self.size and self.heap[right] > self.heap[smallest_or_largest]:
                smallest_or_largest = right
        
        if smallest_or_largest != i:
            self._swap(i, smallest_or_largest)
            self._heapify_down(smallest_or_largest)
    
    def insert(self, value):
        """
        Insert a value into the heap.
        Time Complexity: O(log n)
        """
        self.heap.append(value)
        self.size += 1
        self._heapify_up(self.size - 1)
    
    def extract_top(self):
        """
        Remove and return the top element from the heap.
        Time Complexity: O(log n)
        """
        if self.size == 0:
            raise IndexError("Heap is empty")
        
        if self.size == 1:
            self.size -= 1
            return self.heap.pop()
        
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.size -= 1
        self._heapify_down(0)
        
        return root
    
    def peek(self):
        """
        Return the top element without removing it.
        Time Complexity: O(1)
        """
        if self.size == 0:
            raise IndexError("Heap is empty")
        return self.heap[0]
    
    def get_size(self):
        """
        Get the number of elements in the heap.
        Time Complexity: O(1)
        """
        return self.size
    
    def is_empty(self):
        """
        Check if the heap is empty.
        Time Complexity: O(1)
        """
        return self.size == 0
    
    def build_heap(self, arr):
        """
        Build a heap from an array.
        Time Complexity: O(n)
        """
        self.heap = arr
        self.size = len(arr)
        
        # Start from the last non-leaf node and heapify down
        for i in range(self.size // 2 - 1, -1, -1):
            self._heapify_down(i)

def main():
    # Demonstrate Min Heap
    print("Min Heap Operations Demo:")
    print("-" * 30)
    min_heap = Heap("min")
    
    # Insert values
    print("\nInserting values into min heap...")
    values = [5, 3, 7, 1, 4, 6, 2]
    for value in values:
        min_heap.insert(value)
        print(f"Inserted {value}")
    
    # Extract minimum values
    print("\nExtracting minimum values:")
    while not min_heap.is_empty():
        print(f"Extracted: {min_heap.extract_top()}")
    
    # Demonstrate Max Heap
    print("\nMax Heap Operations Demo:")
    print("-" * 30)
    max_heap = Heap("max")
    
    # Build heap from array
    print("\nBuilding max heap from array...")
    max_heap.build_heap(values)
    print(f"Heap size: {max_heap.get_size()}")
    
    # Extract maximum values
    print("\nExtracting maximum values:")
    while not max_heap.is_empty():
        print(f"Extracted: {max_heap.extract_top()}")
    
    # Demonstrate heap sort using min heap
    print("\nHeap Sort Demo (using min heap):")
    print("-" * 30)
    arr = [5, 3, 7, 1, 4, 6, 2]
    print(f"Original array: {arr}")
    
    # Build min heap
    min_heap = Heap("min")
    min_heap.build_heap(arr)
    
    # Extract elements in sorted order
    sorted_arr = []
    while not min_heap.is_empty():
        sorted_arr.append(min_heap.extract_top())
    
    print(f"Sorted array: {sorted_arr}")

if __name__ == "__main__":
    main() 