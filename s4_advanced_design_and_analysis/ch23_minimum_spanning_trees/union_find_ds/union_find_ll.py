from typing import Any, Optional, DefaultDict, Dict, Hashable
from collections import defaultdict
from s3_data_structures.ch10_elementary_ds.linked_list_ds.doubly_linked_list import *
from s4_advanced_design_and_analysis.ch23_minimum_spanning_trees.union_find_ds.union_find import UnionFind
from s4_advanced_design_and_analysis.ch22_elementary_graph_algorithms.graph import Graph, GraphNode


class SetObject():

    def __init__(self, id: int):
        self.id = id
        self.dll = DoublyLinkedList()

    def get_head(self) -> DLLNode:  # this object is also the representative of this set
        return self.dll.head

    def get_tail(self) -> DLLNode:
        return self.dll.tail

    def add(self, x: DLLNode):
        x.prev = self
        self.dll.append(x)

    def __str__(self):
        return 'S' + str(self.id) + ': ' + str(self.dll)


RepresentativeNode = DLLNode


class UFLinkedListImpl(UnionFind):

    def __init__(self):

        self.id: int = 0        # incremental id

        # maps set id -> set object
        self.set_map: Dict[int, SetObject] = dict()

        # maps element -> dll node object
        self.node_map: Dict[Hashable, DLLNode] = dict()

    def make_set(self, x: Hashable) -> None:

        # maintain an ID for each set
        self.id += 1

        # create a set object, and add x to the set
        s = SetObject(self.id)
        node = DLLNode(x)
        s.add(node)

        # store a mapping of elements to DLL objects
        self.node_map[x] = node

        # store a mapping of set id to set object
        self.set_map[self.id] = s

    def find_set(self, x: Hashable) -> Optional[RepresentativeNode]:

        if x not in self.node_map:
            # print('Element not found in data structure')
            return None

        x = self.node_map[x]

        if x.prev is None:
            print('Not a part of any set / not initialized')
            return None

        s = x.prev                    # points to the set object
        if s.id in self.set_map:
            s = self.set_map[s.id]  # get the set object
            rep = s.get_head()        # get the representative object of this set
            return rep
        else:
            print('Set object not found')
            return None

    def union(self, x: Hashable, y: Hashable) -> None:
        # assumes that s1 and s2 are distinct

        # append s1 + s2
        # purge s2
        # make all elements in s2 to point to s1

        s1: SetObject = self.node_map[x].prev
        s2: SetObject = self.node_map[y].prev

        if s1 is None or s2 is None:
            print('One of the input elements dont exist in this UF data structure')
            return

        ptr = s2.get_head()
        s1.get_tail().next = ptr

        while ptr:
            ptr.prev = s1   # reset the prev pointer
            ptr = ptr.next

        s1.dll.tail = s2.get_tail()     # update s1's tail pointer

        del self.set_map[s2.id]     # purge s2

    def __str__(self):
        s = ''
        for k, v in self.set_map.items():
            s += str(v) + '\n'

        return s


if __name__ == '__main__':

    uf = UFLinkedListImpl()

    uf.make_set('a')
    uf.make_set('b')
    uf.make_set('c')
    uf.make_set('d')
    uf.make_set('e')

    print(uf.find_set('c'))     # c
    print(uf.find_set('t'))     # None

    uf.union('a', 'b')
    uf.union('b', 'c')
    uf.union('e', 'd')

    print(uf)

    uf.union('b', 'd')
    print(uf)