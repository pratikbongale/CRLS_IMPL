from s4_advanced_design_and_analysis.ch22_elementary_graph_algorithms.graph import Graph, Color
from s3_data_structures.ch10_elementary_ds.linked_list_ds.singly_linked_list import SinglyLinkedList
from s4_advanced_design_and_analysis.ch22_elementary_graph_algorithms.cycle_detector import is_cyclic_color
from utilities.node_factory import GraphNode

time = 0


def topological_sort(g: Graph):
    '''
    Gives a dependency graph where
    :param g: directed acyclic graph
    :return: linked list of vertices (showing a linear ordering of vertices in graph)
    '''

    # steps:
    # run a dfs on graph
    # when updating a node's Finish Time, add it to the front of linked list
    # the linked list thus formed will have all the nodes in a linear order sequence

    if not isinstance(g, Graph):
        print('Not a graph object')
        return

    if not is_dag(g):
        print('Linear ordering cannot be defined if graph has cycles')
        return

    ll = SinglyLinkedList()

    for v in g.vertices.values():
        v.color = Color.WHITE
        v.parent = None
        v.d = 0
        v.f = 0

    # write your own dfs
    for v in g.vertices.values():
        if v.color == Color.WHITE:
            dfs_visit(g, v, ll)

    return ll


def dfs_visit(g: Graph, u: GraphNode, ll: SinglyLinkedList):

    global time

    time += 1
    u.color = Color.GRAY
    u.d = time

    for v in g.edges[u.data]:
        if v.color == Color.WHITE:
            v.parent = u
            dfs_visit(g, v, ll)

    time += 1
    u.f = time
    u.color = Color.BLACK
    ll.insert(u)    # adds to the front of ll


def is_dag(g: Graph):
    return not is_cyclic_color(g)


if __name__ == '__main__':

    dag = {
        'Undershorts': ['Pants', 'Shoes'],
        'Pants': ['Shoes', 'Belt'],
        'Belt': ['Jacket'],
        'Shirt': ['Belt', 'Tie'],
        'Tie': ['Jacket'],
        'Socks': ['Shoes'],
        'Watch': []
    }

    g = Graph()
    g.build_graph(dag)

    ll: SinglyLinkedList = topological_sort(g)
    ll.print_list()

