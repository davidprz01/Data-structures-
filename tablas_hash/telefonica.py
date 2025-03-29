from typing import Optional

class Node:
    def __init__(self, key: str, value: str) -> None:
        self.key = key
        self.value = value
        self.next: Optional[Node] = None

class Hashtable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.table = [None] * capacity
        self.size = 0

     #Get an index for each key   
    def _hash(self, key):
        return hash(key) % self.capacity
    
    # insert an element into the hash table with a key and value
    def insert(self, key, value):
        index = self._hash(key)

        if self.table[index] is None:
            self.table[index] = Node(key, value)
        else: 
            current = self.table[index]
            while current:
                if current.key == key:
                    current.value = value
                    return
                current = current.next
            newnode = Node(key,value)
            newnode.next = self.table[index]
            self.table[index] = newnode
    
    def search(self, key):
        index = self._hash(key)
        current = self.table[index]
        
        while current:
            if current.key == key:
                return current.value
            current = current.next
            return print("no se ha encontrado el elemento")
        

sistema = Hashtable(5)

sistema.insert("Nombre", "David")
sistema.insert("Telefono","304-6528-9433")

print(sistema.search("Nombre"))
print(sistema.search("Telefono"))
print(sistema._hash("Nombre"))

    






