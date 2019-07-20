from S3_Data_Structures.CH11_HashTables.HashTable import *
from S3_Data_Structures.ch10_elementary_ds.LinkedList.singly_linked_list import *

class Car(HTObject):
    def __init__(self, n, color, power):
        super().__init__(n) # set the key
        self.color = color
        self.power = power

    def __str__(self):
        return '(Key: {}, Color: {}, Power: {})'.format(self.key, self.color, self.power)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.key == other.key

    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return self.key != other.key

class ChainingHT(HashTable):

    def __init__(self, capacity):
        super().__init__(capacity=capacity)
        self.ht = [SinglyLinkedList() for i in range(self.size)]

    def put(self, x):
        hash_key = self.hash_div(x.key)

        # self.ht[hash_key].insert(x)
        # we cannot directly insert into this list
        # because chaining simply adds a chain of nodes (each with a k/v pair)
        # so we must search the list to see if a node exists with the same key

        z = self.ht[hash_key].search(x)
        if z:
            z.data = x
            # just replace the existing object (overwrite)
        else:
            z = SLLNode(x)
            self.ht[hash_key].insert(z)

    def delete(self, x):
        pass

    def get(self, key):
        # return None if not found, else return the object having key

        hash_key = self.hash_div(key)  # using division method of hashing(k%m)
        list = self.ht[hash_key]
        if not list.is_empty():
            z = list.search(key)
            return z
        else:
            print('Element not found!')
            return None

    def print_ht(self):
        print('[')
        for i, lst in enumerate(self.ht):
            print(i, ': [', lst, ']')
        print(']')


if __name__ == '__main__':

    capacity = 10
    ht_chaining = ChainingHT(capacity)

    x = Car(10, 'red', 720)
    ht_chaining.put(x)
    x = Car(20, 'green', 1500)
    ht_chaining.put(x)
    x = Car(30, 'blue', 1000)
    ht_chaining.put(x)
    x = Car(33, 'peach', 150)
    ht_chaining.put(x)
    x = Car(10, 'yellow', 7200)
    ht_chaining.put(x)

    print(ht_chaining.get(key=10))
    ht_chaining.print_ht()

