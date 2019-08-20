from s2_sorting_and_order_statistics.ch06_heap_sort.priority_queue import MinPriorityQueue
import math

class HuffmanNode:
    def __init__(self, key, freq):
        self.key = key
        self.freq = freq
        self.left = None
        self.right = None

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.key == other.key and self.freq == other.freq

    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return self.key != other.key or  self.freq != other.freq

    def __lt__(self, other):
        if isinstance(other, self.__class__):
            return self.freq < other.freq

    def __gt__(self, other):
        if isinstance(other, self.__class__):
            return self.freq > other.freq

    def __le__(self, other):
        if isinstance(other, self.__class__):
            return self.freq <= other.freq

    def __ge__(self, other):
        if isinstance(other, self.__class__):
            return self.freq >= other.freq

    def __str__(self):
        return self.key + ':' + str(self.freq)

def build_huffman(k, f):
    '''
    build a huffman compression tree
    :param k: keys
    :param f: frequency of occurence
    :return:
    '''

    # steps:
    # - use a priority queue
    # - extract minimum 2 values
    # - add them, combine and put the new value back in queue

    n = len(k)
    arr = list()
    for i in range(n):
        node = HuffmanNode(k[i], f[i])
        arr.append(node)

    dummy_node = HuffmanNode('dummy', math.inf)

    pq = MinPriorityQueue(arr, initial_val=dummy_node)     # arrange all objects as per their priority

    for i in range(n-1):
        a, b = pq.extract_minimum(), pq.extract_minimum()
        node = HuffmanNode(str(a.key)+str(b.key), a.freq+b.freq)
        node.left = a
        node.right = b
        pq.min_heap_insert(node)

    return pq.extract_minimum()

def build_codemap(node, s, enc_map, dec_map):
    # build a map of each character -> bits

    if node is None:
        # empty node
        return
    elif node.left is None and node.right is None:
        # leaf node
        enc_map[node.key] = s
        dec_map[s] = node.key
    else:
        build_codemap(node.left, s + '0', enc_map, dec_map)
        build_codemap(node.right, s + '1', enc_map, dec_map)

    return enc_map, dec_map

def encode(s, enc_map):
    res = ''
    for ch in s:
        res += enc_map[ch]

    return res

def decode(s, dec_map):

    res = ''
    tmp = ''
    for b in s:
        tmp += b
        if tmp in dec_map:
            res += dec_map[tmp]
            tmp = ''

    return res

if __name__ == '__main__':

    k = ['a', 'b', 'c', 'd', 'e', 'f']
    f = [45, 13, 12, 16, 9, 5]

    root = build_huffman(k, f)
    # print_binary_tree(root)
    enc_map, dec_map = build_codemap(node=root, s='', enc_map={}, dec_map={})

    s = 'abdcebcf'

    encoded_s = encode(s, enc_map)
    print('Encoded String {} -> {}'.format(s, encoded_s))

    decoded_s = decode(encoded_s, dec_map)
    print('Decoded String {} -> {}'.format(encoded_s, decoded_s))

    print(s == decoded_s)


    pass
