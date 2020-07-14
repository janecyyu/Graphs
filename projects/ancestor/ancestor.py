from util import Stack, Queue  # These may come in handy


def earliest_ancestor(ancestors, starting_node):
    q = Queue()
    q.enqueue([starting_node])
    visited = set()
    while q.size() > 0:
        path = q.dequeue()
        v = path[-1]
        if v not in visited:
            visited.add(v)
            print("visited:", v)
            # for next_node in get_neighbors(ancestors, v):


def get_neighbors(ancestors, node):
    neighbors = []
    dict = {}
    for x, y in ancestors:
        if x not in dict:
            dict[x] = y

    for x, y in dict.items():
        if y == node:
            # add to neighbors
            neighbors.append(x)
        else:
            return None
    print("my neighbors", neighbors)
    return neighbors


test_ancestors = [(1, 3), (2, 3), (10, 1)]
earliest_ancestor(test_ancestors, 3)

# get_neighbors(test_ancestors, 3)
