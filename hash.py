class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]  

    
    def hash_function(self, key):
        return key % self.size


    def insert(self, key, value):
        index = self.hash_function(key)
        
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                print(f"Updated key {key} with value {value}")
                return
        self.table[index].append([key, value])
        print(f"Inserted ({key}, {value}) at index {index}")

    # Search for a key
    def search(self, key):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                print(f"Key {key} found with value {pair[1]}")
                return pair[1]
        print(f"Key {key} not found")
        return None

    # Delete a key-value pair
    def delete(self, key):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                self.table[index].remove(pair)
                print(f"Key {key} deleted from index {index}")
                return
        print(f"Key {key} not found, cannot delete")

    # Display hash table
    def display(self):
        print("\nHash Table:")
        for i, bucket in enumerate(self.table):
            print(f"Index {i}: {bucket}")



if __name__ == "__main__":
    ht = HashTable()

    ht.insert(15, "Apple")
    ht.insert(25, "Banana")
    ht.insert(35, "Cherry")
    ht.insert(7, "Mango")

    ht.display()

    ht.search(25)
    ht.search(99)

    ht.delete(15)
    ht.delete(99)

    ht.display()