from S3_Data_Structures.CH11_HashTables.HashTable import *

class Employee:

    def __init__(self, id, name, age):
        self.key = id
        self.name = name
        self.age = age

class DirectAddressingHT(HashTable):

    def __init__(self, table_size):
        self.ht = [None] * table_size
        self.size = table_size

    def search(self, k):
        # return the object if found, else return None

        if not self.is_valid_key(k):
            return None

        return self.ht[k]

    def insert(self, x):
        if not self.is_valid_key(x.key):
            print('Cannot store in hash table, out of bounds')

        self.ht[x.key] = x

    def delete(self, x):

        if not self.is_valid_key(x.key):
            print('Object not found')
            return None

        self.ht[x.key] = None

    def is_valid_key(self, k):
        return k < self.size

