"""
Arrays and Lists in Python
--------------------------
This module demonstrates the basic operations and concepts of arrays and lists in Python.
Lists in Python are dynamic arrays that can hold elements of different types.
"""

class ArrayOperations:
    def __init__(self):
        """Initialize an empty list."""
        self.arr = []
    
    def insert_at_end(self, element):
        """
        Insert an element at the end of the array.
        Time Complexity: O(1) amortized
        """
        self.arr.append(element)
    
    def insert_at_index(self, index, element):
        """
        Insert an element at a specific index.
        Time Complexity: O(n) in worst case
        """
        if 0 <= index <= len(self.arr):
            self.arr.insert(index, element)
        else:
            raise IndexError("Index out of range")
    
    def delete_at_index(self, index):
        """
        Delete an element at a specific index.
        Time Complexity: O(n) in worst case
        """
        if 0 <= index < len(self.arr):
            return self.arr.pop(index)
        raise IndexError("Index out of range")
    
    def get_element(self, index):
        """
        Get element at specific index.
        Time Complexity: O(1)
        """
        if 0 <= index < len(self.arr):
            return self.arr[index]
        raise IndexError("Index out of range")
    
    def search_element(self, element):
        """
        Search for an element in the array.
        Time Complexity: O(n)
        """
        try:
            return self.arr.index(element)
        except ValueError:
            return -1
    
    def get_length(self):
        """
        Get the length of the array.
        Time Complexity: O(1)
        """
        return len(self.arr)
    
    def is_empty(self):
        """
        Check if the array is empty.
        Time Complexity: O(1)
        """
        return len(self.arr) == 0

# Example usage
def main():
    # Create an instance of ArrayOperations
    arr_ops = ArrayOperations()
    
    # Insert elements
    print("Inserting elements...")
    arr_ops.insert_at_end(10)
    arr_ops.insert_at_end(20)
    arr_ops.insert_at_end(30)
    print(f"Array after insertions: {arr_ops.arr}")
    
    # Insert at specific index
    print("\nInserting at index 1...")
    arr_ops.insert_at_index(1, 15)
    print(f"Array after insertion at index 1: {arr_ops.arr}")
    
    # Get element
    print("\nGetting element at index 2...")
    element = arr_ops.get_element(2)
    print(f"Element at index 2: {element}")
    
    # Search element
    print("\nSearching for element 20...")
    index = arr_ops.search_element(20)
    print(f"Element 20 found at index: {index}")
    
    # Delete element
    print("\nDeleting element at index 1...")
    deleted = arr_ops.delete_at_index(1)
    print(f"Deleted element: {deleted}")
    print(f"Array after deletion: {arr_ops.arr}")
    
    # Get length
    print(f"\nArray length: {arr_ops.get_length()}")
    
    # Check if empty
    print(f"Is array empty? {arr_ops.is_empty()}")

if __name__ == "__main__":
    main() 