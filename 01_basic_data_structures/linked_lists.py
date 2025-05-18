"""
Singly Linked List Implementation in Python
-----------------------------------------
A linked list is a linear data structure where elements are stored in nodes,
and each node points to the next node in the sequence.
Each node contains:
- data: The value stored in the node
- next: Reference to the next node
"""

class Node:
    def __init__(self, data):
        """
        Initialize a new node with given data.
        """
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        """
        Initialize an empty linked list.
        """
        self.head = None
        self.size = 0
    
    def is_empty(self):
        """
        Check if the linked list is empty.
        Time Complexity: O(1)
        """
        return self.head is None
    
    def insert_at_beginning(self, data):
        """
        Insert a new node at the beginning of the list.
        Time Complexity: O(1)
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
    
    def insert_at_end(self, data):
        """
        Insert a new node at the end of the list.
        Time Complexity: O(n)
        """
        new_node = Node(data)
        
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        
        self.size += 1
    
    def insert_after(self, prev_node, data):
        """
        Insert a new node after a given node.
        Time Complexity: O(1)
        """
        if prev_node is None:
            print("Previous node cannot be None")
            return
        
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        self.size += 1
    
    def delete_node(self, key):
        """
        Delete the first occurrence of a node with given key.
        Time Complexity: O(n)
        """
        if self.is_empty():
            print("List is empty")
            return
        
        # If head node holds the key
        if self.head.data == key:
            self.head = self.head.next
            self.size -= 1
            return
        
        # Search for the key
        current = self.head
        while current.next:
            if current.next.data == key:
                current.next = current.next.next
                self.size -= 1
                return
            current = current.next
        
        print(f"Key {key} not found in the list")
    
    def search(self, key):
        """
        Search for a key in the linked list.
        Time Complexity: O(n)
        Returns the node if found, None otherwise
        """
        current = self.head
        while current:
            if current.data == key:
                return current
            current = current.next
        return None
    
    def get_size(self):
        """
        Get the size of the linked list.
        Time Complexity: O(1)
        """
        return self.size
    
    def display(self):
        """
        Display the linked list.
        Time Complexity: O(n)
        """
        if self.is_empty():
            print("List is empty")
            return
        
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

def main():
    # Create a new linked list
    ll = LinkedList()
    
    # Demonstrate linked list operations
    print("Linked List Operations Demo:")
    print("-" * 30)
    
    # Insert elements
    print("\nInserting elements...")
    ll.insert_at_beginning(10)
    ll.insert_at_beginning(20)
    ll.insert_at_end(30)
    ll.insert_at_end(40)
    print("List after insertions:")
    ll.display()
    
    # Search for elements
    print("\nSearching for elements...")
    key = 30
    node = ll.search(key)
    if node:
        print(f"Found {key} in the list")
    else:
        print(f"{key} not found in the list")
    
    # Insert after a node
    print("\nInserting after a node...")
    node = ll.search(30)
    if node:
        ll.insert_after(node, 35)
        print("List after insertion:")
        ll.display()
    
    # Delete nodes
    print("\nDeleting nodes...")
    ll.delete_node(20)
    print("List after deleting 20:")
    ll.display()
    
    ll.delete_node(40)
    print("List after deleting 40:")
    ll.display()
    
    # Get size
    print(f"\nSize of the list: {ll.get_size()}")

if __name__ == "__main__":
    main() 