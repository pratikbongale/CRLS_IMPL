from S3_Data_Structures.CH11_HashTables.HashTable import *

class Employee:

    def __init__(self, id, name, age):
        self.key = id
        self.name = name
        self.age = age

    def __str__(self):
        return '[Key: {}, Name: {}, Age: {}]'.format(self.key, self.name, self.age)

class DirectAddressingHT(HashTable):

    def __init__(self, table_size):
        self.ht = [None] * table_size
        self.size = table_size

    def search(self, k):
        # return the object if found, else return None

        if not self.is_valid_key(k):
            print('Not a valid key')
            return None

        elif not self.ht[k]:
            print('Object not found')
            return None

        return self.ht[k]

    def insert(self, x):
        if not self.is_valid_key(x.key):
            print('Not a valid key')

        self.ht[x.key] = x

    def delete(self, x):

        if not self.is_valid_key(x.key):
            print('Not a valid key')
            return None

        elif not self.ht[x.key]:
            print('Object not found')
            return None

        z = self.ht[x.key]
        self.ht[x.key] = None

        return z

    def is_valid_key(self, k):
        return k < self.size

if __name__ == '__main__':

    x = Employee(1, 'abc', 30)
    y = Employee(4, 'pqr', 25)
    ht = DirectAddressingHT(10)
    z = ht.search(15)             # => invalid key
    print(z) if z else ''           # => ''

    ht.insert(x)                   # =>
    z = ht.search(1)
    print(z) if z else ''        # => (1, 'abc', 30)

    z = ht.delete(y)        # => not found
    print(z) if z else ''   # => ''

    ht.insert(y)
    z = ht.delete(y)        # => found
    print(z) if z else ''  # => (4, 'pqr', 25)

    ht.search(4)        # => not found


