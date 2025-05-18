"""
Hash Table Implementation in Python
---------------------------------
A hash table is a data structure that implements an associative array abstract data type,
a structure that can map keys to values. It uses a hash function to compute an index
into an array of buckets or slots, from which the desired value can be found.
"""

class HashTable:
    def __init__(self, size=10):
        """
        Initialize a hash table with a given size.
        Args:
            size (int): The size of the hash table (number of buckets)
        """
        self.size = size
        self.table = [[] for _ in range(size)]  # List of lists for handling collisions
        self.count = 0  # Number of key-value pairs
    
    def _hash_function(self, key):
        """
        Compute the hash value for a given key.
        Time Complexity: O(1)
        """
        if isinstance(key, int):
            return key % self.size
        # For string keys, sum ASCII values
        return sum(ord(c) for c in str(key)) % self.size
    
    def insert(self, key, value):
        """
        Insert a key-value pair into the hash table.
        Time Complexity: O(1) average case, O(n) worst case
        """
        hash_value = self._hash_function(key)
        bucket = self.table[hash_value]
        
        # Check if key already exists
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)  # Update existing key
                return
        
        # Insert new key-value pair
        bucket.append((key, value))
        self.count += 1
        
        # Resize if load factor exceeds 0.7
        if self.count / self.size > 0.7:
            self._resize()
    
    def get(self, key):
        """
        Retrieve the value associated with a key.
        Time Complexity: O(1) average case, O(n) worst case
        Returns:
            The value associated with the key, or None if key not found
        """
        hash_value = self._hash_function(key)
        bucket = self.table[hash_value]
        
        for k, v in bucket:
            if k == key:
                return v
        return None
    
    def delete(self, key):
        """
        Remove a key-value pair from the hash table.
        Time Complexity: O(1) average case, O(n) worst case
        Returns:
            True if key was found and deleted, False otherwise
        """
        hash_value = self._hash_function(key)
        bucket = self.table[hash_value]
        
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                self.count -= 1
                return True
        return False
    
    def _resize(self):
        """
        Resize the hash table when load factor exceeds threshold.
        Time Complexity: O(n)
        """
        old_table = self.table
        self.size *= 2
        self.table = [[] for _ in range(self.size)]
        self.count = 0
        
        # Rehash all existing key-value pairs
        for bucket in old_table:
            for key, value in bucket:
                self.insert(key, value)
    
    def get_size(self):
        """
        Get the number of key-value pairs in the hash table.
        Time Complexity: O(1)
        """
        return self.count
    
    def is_empty(self):
        """
        Check if the hash table is empty.
        Time Complexity: O(1)
        """
        return self.count == 0
    
    def display(self):
        """
        Display the contents of the hash table.
        Time Complexity: O(n)
        """
        print("\nHash Table Contents:")
        print("-" * 30)
        for i, bucket in enumerate(self.table):
            if bucket:
                print(f"Bucket {i}: {bucket}")

def main():
    # Create a new hash table
    ht = HashTable()
    
    # Demonstrate hash table operations
    print("Hash Table Operations Demo:")
    print("-" * 30)
    
    # Insert key-value pairs
    print("\nInserting key-value pairs...")
    ht.insert("name", "John")
    ht.insert("age", 25)
    ht.insert("city", "New York")
    ht.insert(1, "One")
    ht.insert(2, "Two")
    ht.display()
    
    # Get values
    print("\nRetrieving values...")
    print(f"Value for 'name': {ht.get('name')}")
    print(f"Value for 'age': {ht.get('age')}")
    print(f"Value for 'city': {ht.get('city')}")
    print(f"Value for key 1: {ht.get(1)}")
    
    # Try to get non-existent key
    print(f"\nValue for non-existent key 'country': {ht.get('country')}")
    
    # Delete a key-value pair
    print("\nDeleting key 'age'...")
    if ht.delete("age"):
        print("Key 'age' deleted successfully")
    ht.display()
    
    # Get size
    print(f"\nNumber of key-value pairs: {ht.get_size()}")
    
    # Check if empty
    print(f"Is hash table empty? {ht.is_empty()}")

if __name__ == "__main__":
    main() 