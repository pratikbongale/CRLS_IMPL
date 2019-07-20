from abc import ABCMeta, abstractmethod

class HTObject():
    # each hash table object must have a key

    def __init__(self, k):
        self.key = k

class HashTable:
    __metaclass__ = ABCMeta

    def __init__(self, capacity):
        self.size = capacity

    @abstractmethod
    def put(self, x):
        raise NotImplementedError

    @abstractmethod
    def delete(self, x):
        raise NotImplementedError

    @abstractmethod
    def get(self, key):
        raise NotImplementedError

    def hash_simple(self, k):
        # precondition: 0 <= k < 1
        if k > 1:
            k = 1/k
        elif k < 0:
            k = abs(k)
            k = 1/k
        else:
            # k = 0 or k = 1
            # fails for k = 1
            pass

        return k*self.size

    def hash_div(self, k):
        # precondition: hash table size m != 2^p
        # choose m to be a prime number far from powers of 2
        h = k % self.size
        return h

    def hash_mult(self, k):
        # choose a constant 0 < A < 1
        A = 0.3
        return int(self.size * (k*A % 1))

    def hash_universal(self, k):
        # choose a hash function from a set H
        pass

    def hash_linear(self, k, i):
        # use any of the hash functions given above
        # and then do probing linear
        h = (self.hash_mult(k) + i) % self.size
        return h

    def hash_quadratic(self, k, i):
        # define constants c1 and c2
        c1 = 3
        c2 = 4

        h = (self.hash_mult(k) + c1*i + c2*(i**2)) % self.size
        return h

    def hash_double_hashing(self, k, i):
        # choose m1 = prime
        # h1(k) = k mod m1
        # h2(k) = 1 + k mod m2
        # m2 = m1-2   (pos no. slightly less than m1)

        m1 = self.size
        m2 = m1 - 2

        def h1(k):
            return k % m1

        def h2(k):
            return 1 + k % m2

        return (h1(k) + i*h2(k)) % m1  # sequence probed depends on k in two ways
