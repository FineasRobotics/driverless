import matplotlib.pyplot as plt
import numpy as np
from sklearn.neighbors import NearestNeighbors
import networkx as nx

def opt_order(array):
    # start by creating a nearest neighbour graph to connect each of the nodes to its 2 nearest neighbors
    clf = NearestNeighbors(2).fit(array)
    G = clf.kneighbors_graph()

    # use networkx to construct a graph from this sparse matrix
    T = nx.from_scipy_sparse_matrix(G)

    # get the best order for all the nodes
    paths = [list(nx.dfs_preorder_nodes(T, i)) for i in range(len(array))]

    # find the one that minimizes the distances between the connections
    mindist = np.inf
    minidx = 0

    for i in range(len(array)):
        p = paths[i]           # order of nodes
        ordered = array[p]    # ordered nodes
        # find cost of that order by the sum of euclidean distances between array (i) and (i+1)
        cost = (((ordered[:-1] - ordered[1:])**2).sum(1)).sum()
        if cost < mindist:
            mindist = cost
            minidx = i
    
    order = paths[minidx]

    return np.array([[x, y] for x, y in zip( array[order, 0], array[order, 1] )])

def main():
    # produce a sin function
    x = np.linspace(0, 2 * np.pi, 100)
    y = np.sin(x)

    # shuffles the points
    idx = np.random.permutation(x.size)
    x = x[idx]
    y = y[idx]

    # makes an array [x, y]
    array = np.array([[x, y] for x, y in zip(x, y)])

    # orders the points
    sorted_array = opt_order(array)

    plt.plot(sorted_array[:, 0], sorted_array[:, 1])
    plt.show()

if __name__ == "__main__":
    main()