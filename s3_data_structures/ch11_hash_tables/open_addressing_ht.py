from S3_Data_Structures.CH11_HashTables.HashTable import HashTable, HTObject


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

class OpenAddressingHT(HashTable):

    def __init__(self, capacity):
        super().__init__(capacity=capacity)
        self.ht = [None]*capacity   # hash table

    def put(self, x):
        # x: <k,v> pair
        i = 0
        inserted = False
        for i in range(self.size):
            y = self.hash_linear(x.key, i)
            if self.ht[y] is None or self.ht[y] == 'DELETED':
                self.ht[y] = x
                inserted = True
            elif self.ht[y] == x:  # uses the __eq__ method for comparison
                # match their keys
                self.ht[y] = x
                inserted = True

            if inserted:
                return

        print('Hash table is full')
        return None

    def get(self, k):
        for i in range(self.size):
            y = self.hash_linear(k, i)
            if self.ht[y] is None:
                break
            elif self.ht[y] is not 'DELETED' and self.ht[y].key == k:
                return self.ht[y]

        print('Element not found')
        return None

    def delete(self, k):
        for i in range(self.size):
            y = self.hash_linear(k, i)
            if self.ht[y] is None:
                # reached None, search unsuccessfull
                break
            elif self.ht[y] is not 'DELETED' and self.ht[y].key == k:
                res = self.ht[y]
                self.ht[y] = 'DELETED'
                return res

        print('Element not found')
        return None

    def print_ht(self):
        print('[')
        for i, x in enumerate(self.ht):
            print(i, ': [', x, ']')
        print(']')

if __name__ == '__main__':
    m = 10
    open_addressing_ht = OpenAddressingHT(m)

    x = Car(10, 'red', 720)
    open_addressing_ht.put(x)
    x = Car(20, 'green', 1500)
    open_addressing_ht.put(x)
    x = Car(30, 'blue', 1000)
    open_addressing_ht.put(x)
    x = Car(33, 'peach', 150)
    open_addressing_ht.put(x)
    x = Car(10, 'yellow', 7200)
    open_addressing_ht.put(x)

    print('GET:', open_addressing_ht.get(10))
    open_addressing_ht.print_ht()

    print('Deleted:', open_addressing_ht.delete(10))

