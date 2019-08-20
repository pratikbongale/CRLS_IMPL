from s4_advanced_design_and_analysis.ch22_elementary_graph_algorithms.graph import *

def bfs(g, s, t=None):
    '''
    Primarily used to find the shortest distance of all nodes from a given start node
    :param g: graph
    :return:
    '''



    q = [s]

    while q:
        u = q.pop(0)

        for v in g.adj[u]:
            if v.color == Color.WHITE:
                pass


        pass



    pass


if __name__ == '__main__':
    pass


