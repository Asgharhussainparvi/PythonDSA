class Hash:
    def __init__(self) -> None:
        self.MAX = 10
        self.arr = [None for i in range (self.MAX)]

    def get_hash(self,key):
        hash = 0
        for char in key:
            hash += ord(char) 
        return hash % self.MAX
    
    def __getitem__(self,index):
        h = self.get_hash(index)
        return self.arr[h]
    
    def __setitem__(self,key,val):
        h = self.get_hash(key)
        self.arr[h] =val