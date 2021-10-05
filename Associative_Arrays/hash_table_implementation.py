class HashTable:
    def __init__(self):
        # Based on the load factor we can change the size (dynamic resizing)
        # Load factor: n/m where n is the number of items and m is the size of the array
        self.capacity = 10
        self.keys = [None] * self.capacity
        self.values = [None] * self.capacity

    def insert(self, key, value):
        # Find a location
        index = self.hash_function(key)

        # Check if the index is already taken
        while self.keys[index]:
            # Update the value
            if self.keys[index] == key:
                self.values[index] = value
                return

            # Linear probing (try the next slot)
            index = (index + 1) % self.capacity

        # Valid slot found => insert data
        self.keys[index] = key
        self.values[index] = value

    def get(self, key):
        index = self.hash_function(key)

        while self.keys[index]:
            if self.keys[index] == key:
                return self.values[index]

            index = (index + 1) % self.capacity

        return None

    def hash_function(self, key):
        hash_sum = 0
        for letter in key:
            hash_sum += ord(letter)

        return hash_sum % self.capacity
