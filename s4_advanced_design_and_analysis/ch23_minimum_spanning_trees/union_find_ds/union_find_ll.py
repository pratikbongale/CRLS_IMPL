from typing import Any
from s3_data_structures.ch10_elementary_ds.linked_list_ds.singly_linked_list import SinglyLinkedList, SLLNode
from s4_advanced_design_and_analysis.ch23_minimum_spanning_trees.union_find_ds.union_find import UnionFind


class LinkedListUF(UnionFind):

    def make_set(self, x: Any):
        s = SinglyLinkedList()
        node = SLLNode(x)
        s.head = node
        s.tail = node
        node.parent = s.head
        s.append(x)

    def find_set(self, x: Any):
        pass

    def union(self, s1, s2):
        pass