from util import Stack, Queue  # These may come in handy


def earliest_ancestor(ancestors, starting_node):
    # transfer ancestors to dict type
    dict = {}
    for x, y in ancestors:
        if x not in dict:
            dict[x] = [y]
        else:
            dict[x].append(y)

    q = Queue()
    q.enqueue([starting_node])
    visited = set()
    v = starting_node
    while q.size() > 0:
        path = q.dequeue()
        v = path[-1]
        if v not in visited:
            visited.add(v)
            # print("visited:", v)
            for next_node in get_neighbors(dict, v):
                new_arr = path.copy()
                new_arr.append(next_node)
                q.enqueue(new_arr)

    if v == starting_node:
        # print(-1)
        return -1
    # print(v)
    return v


def get_neighbors(dict, node):
    neighbors = []
    two_parents = 0
    for x, y in dict.items():
        if node in y:
            # add to neighbors
            neighbors.append(x)
    # check if two parents
    for n in neighbors:
        if len(get_neighbors(dict, n)) == 0:
            two_parents += 1
        if two_parents == 2:
            neighbors = [min(neighbors)]
    return neighbors


# test_ancestors = [(1, 3), (2, 3), (10, 1)]
test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
                  (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]


earliest_ancestor(test_ancestors, 8)
earliest_ancestor(test_ancestors, 9)

# print(get_neighbors(test_ancestors, 3))
