"""
Binary Tree Implementation in Python
----------------------------------
A binary tree is a tree data structure in which each node has at most two children,
referred to as the left child and the right child.
"""

class TreeNode:
    def __init__(self, value):
        """
        Initialize a tree node with a value.
        """
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        """
        Initialize an empty binary tree.
        """
        self.root = None
    
    def insert(self, value):
        """
        Insert a value into the binary tree.
        Time Complexity: O(n) in worst case
        """
        if not self.root:
            self.root = TreeNode(value)
            return
        
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            
            if not node.left:
                node.left = TreeNode(value)
                return
            queue.append(node.left)
            
            if not node.right:
                node.right = TreeNode(value)
                return
            queue.append(node.right)
    
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
    
    def preorder_traversal(self, node=None):
        """
        Perform preorder traversal (Root -> Left -> Right).
        Time Complexity: O(n)
        """
        if node is None:
            node = self.root
        
        if node:
            print(node.value, end=" ")
            self.preorder_traversal(node.left)
            self.preorder_traversal(node.right)
    
    def postorder_traversal(self, node=None):
        """
        Perform postorder traversal (Left -> Right -> Root).
        Time Complexity: O(n)
        """
        if node is None:
            node = self.root
        
        if node:
            self.postorder_traversal(node.left)
            self.postorder_traversal(node.right)
            print(node.value, end=" ")
    
    def level_order_traversal(self):
        """
        Perform level order traversal (Breadth-First).
        Time Complexity: O(n)
        """
        if not self.root:
            return
        
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            print(node.value, end=" ")
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    
    def height(self, node=None):
        """
        Calculate the height of the tree.
        Time Complexity: O(n)
        """
        if node is None:
            node = self.root
        
        if not node:
            return -1
        
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        
        return max(left_height, right_height) + 1
    
    def count_nodes(self, node=None):
        """
        Count the total number of nodes in the tree.
        Time Complexity: O(n)
        """
        if node is None:
            node = self.root
        
        if not node:
            return 0
        
        return 1 + self.count_nodes(node.left) + self.count_nodes(node.right)
    
    def is_leaf(self, node):
        """
        Check if a node is a leaf node.
        Time Complexity: O(1)
        """
        return node and not node.left and not node.right
    
    def count_leaves(self, node=None):
        """
        Count the number of leaf nodes in the tree.
        Time Complexity: O(n)
        """
        if node is None:
            node = self.root
        
        if not node:
            return 0
        
        if self.is_leaf(node):
            return 1
        
        return self.count_leaves(node.left) + self.count_leaves(node.right)

def main():
    # Create a new binary tree
    tree = BinaryTree()
    
    # Demonstrate tree operations
    print("Binary Tree Operations Demo:")
    print("-" * 30)
    
    # Insert values
    print("\nInserting values...")
    values = [1, 2, 3, 4, 5, 6, 7]
    for value in values:
        tree.insert(value)
    
    # Perform different traversals
    print("\nTree Traversals:")
    print("Inorder traversal (Left -> Root -> Right):")
    tree.inorder_traversal()
    print("\n\nPreorder traversal (Root -> Left -> Right):")
    tree.preorder_traversal()
    print("\n\nPostorder traversal (Left -> Right -> Root):")
    tree.postorder_traversal()
    print("\n\nLevel order traversal (Breadth-First):")
    tree.level_order_traversal()
    
    # Tree properties
    print("\n\nTree Properties:")
    print(f"Height of the tree: {tree.height()}")
    print(f"Total number of nodes: {tree.count_nodes()}")
    print(f"Number of leaf nodes: {tree.count_leaves()}")

if __name__ == "__main__":
    main() 