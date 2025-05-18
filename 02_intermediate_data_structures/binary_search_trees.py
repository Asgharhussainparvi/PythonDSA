"""
Binary Search Tree (BST) Implementation in Python
----------------------------------------------
A binary search tree is a binary tree where for each node:
- All nodes in the left subtree have values less than the node's value
- All nodes in the right subtree have values greater than the node's value
This property enables efficient searching, insertion, and deletion operations.
"""

class BSTNode:
    def __init__(self, value):
        """
        Initialize a BST node with a value.
        """
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        """
        Initialize an empty binary search tree.
        """
        self.root = None
    
    def insert(self, value):
        """
        Insert a value into the BST.
        Time Complexity: O(h) where h is the height of the tree
        """
        if not self.root:
            self.root = BSTNode(value)
            return
        
        self._insert_recursive(self.root, value)
    
    def _insert_recursive(self, node, value):
        """
        Helper method for recursive insertion.
        """
        if value < node.value:
            if node.left is None:
                node.left = BSTNode(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = BSTNode(value)
            else:
                self._insert_recursive(node.right, value)
    
    def search(self, value):
        """
        Search for a value in the BST.
        Time Complexity: O(h) where h is the height of the tree
        Returns:
            The node if found, None otherwise
        """
        return self._search_recursive(self.root, value)
    
    def _search_recursive(self, node, value):
        """
        Helper method for recursive search.
        """
        if node is None or node.value == value:
            return node
        
        if value < node.value:
            return self._search_recursive(node.left, value)
        return self._search_recursive(node.right, value)
    
    def delete(self, value):
        """
        Delete a value from the BST.
        Time Complexity: O(h) where h is the height of the tree
        """
        self.root = self._delete_recursive(self.root, value)
    
    def _delete_recursive(self, node, value):
        """
        Helper method for recursive deletion.
        """
        if node is None:
            return node
        
        if value < node.value:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)
        else:
            # Node with only one child or no child
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            
            # Node with two children: Get the inorder successor (smallest in right subtree)
            node.value = self._min_value(node.right)
            node.right = self._delete_recursive(node.right, node.value)
        
        return node
    
    def _min_value(self, node):
        """
        Find the minimum value in a subtree.
        """
        current = node
        while current.left:
            current = current.left
        return current.value
    
    def inorder_traversal(self, node=None):
        """
        Perform inorder traversal (Left -> Root -> Right).
        Time Complexity: O(n)
        """
        if node is None:
            node = self.root
        
        if node:
            self.inorder_traversal(node.left)
            print(node.value, end=" ")
            self.inorder_traversal(node.right)
    
    def is_valid_bst(self, node=None, min_val=float('-inf'), max_val=float('inf')):
        """
        Check if the tree is a valid BST.
        Time Complexity: O(n)
        """
        if node is None:
            node = self.root
        
        if node is None:
            return True
        
        if not (min_val < node.value < max_val):
            return False
        
        return (self.is_valid_bst(node.left, min_val, node.value) and
                self.is_valid_bst(node.right, node.value, max_val))
    
    def get_height(self, node=None):
        """
        Calculate the height of the BST.
        Time Complexity: O(n)
        """
        if node is None:
            node = self.root
        
        if not node:
            return -1
        
        left_height = self.get_height(node.left)
        right_height = self.get_height(node.right)
        
        return max(left_height, right_height) + 1

def main():
    # Create a new BST
    bst = BinarySearchTree()
    
    # Demonstrate BST operations
    print("Binary Search Tree Operations Demo:")
    print("-" * 40)
    
    # Insert values
    print("\nInserting values...")
    values = [50, 30, 70, 20, 40, 60, 80]
    for value in values:
        bst.insert(value)
        print(f"Inserted {value}")
    
    # Perform inorder traversal
    print("\nInorder traversal (should be sorted):")
    bst.inorder_traversal()
    
    # Search for values
    print("\n\nSearching for values...")
    search_values = [40, 90]
    for value in search_values:
        result = bst.search(value)
        if result:
            print(f"Found {value} in the BST")
        else:
            print(f"{value} not found in the BST")
    
    # Delete a value
    print("\nDeleting value 30...")
    bst.delete(30)
    print("Inorder traversal after deletion:")
    bst.inorder_traversal()
    
    # Check if valid BST
    print("\n\nChecking if tree is a valid BST:")
    print(f"Is valid BST: {bst.is_valid_bst()}")
    
    # Get height
    print(f"\nHeight of the BST: {bst.get_height()}")

if __name__ == "__main__":
    main() 