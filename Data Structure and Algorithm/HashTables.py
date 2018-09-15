class HashTables(object):

    def __init__(self):
        self.size = 10
        self.keys = [None]*self.size
        self.values = [None]*self.size

    def put(self, key, data):

        index = self.hashfunction(key)

        while self.keys[index] is not None:
            if self.values[index] == key:
                self.values[index] = data  # update
                return

            # rehash try to find another slot
            index = (index+1)%self.size

        # insert
        self.keys[index] = key
        self.values[index] = data

    def get(self, key):
        index = self.hashfunction(key)

        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.values[index]

            index = (index+1)%self.size
        # It means the key is not present in the associative
        return None

    def hashfunction(self, key):
        sum0 = 0
        for i in range(len(key)):
            sum0 += ord(key[i])
        return sum0%self.size


if __name__ == "__main__":
    table = HashTables()
    table.put("apple", 10)
    table.put("orange", 50)
    table.put("car", 20)
    table.put("table", 100)

    print(table.get("car"))
