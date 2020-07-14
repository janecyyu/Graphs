"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)  # v1 points to v2
        else:
            return IndexError("nonexistent vert")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Breadth-First Traversal:
        # create a queue
        q = Queue()
        # create a visited set
        visited = set()
        # add vertexes to queue
        q.enqueue(starting_vertex)
        # visit every vert
        while q.size() > 0:
            v = q.dequeue()  # FIFO
            if v not in visited:
                # add to visited
                visited.add(v)
                print(v)
                for next_v in self.get_neighbors(v):
                    q.enqueue(next_v)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # create a stack
        s = Stack()
        # create a visited set
        visited = set()
        # add vertexes to queue
        s.push(starting_vertex)
        # visit every vert
        while s.size() > 0:
            v = s.pop()  # FILO
            if v not in visited:
                # add to visited
                visited.add(v)

                print(v)

                for next_v in self.get_neighbors(v):
                    s.push(next_v)

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        def dft_indoor(node, visited):
            if node is None or node in visited:
                return

            visited.add(node)
            print(node)
            for next_v in self.get_neighbors(node):
                dft_indoor(next_v, visited)

        visited = set()

        dft_indoor(starting_vertex, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create an empty queue and enqueue A PATH TO the starting vertex ID
        q = Queue()
        for next_v in self.get_neighbors(starting_vertex):
            arr = []
            arr.append(starting_vertex)
            arr.append(next_v)
            q.enqueue(arr)

        # Create a Set to store visited vertices
        visited = set()
        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue the first PATH
            path = q.dequeue()
            # Grab the last vertex from the PATH
            last_v = path[len(path)-1]
            # If that vertex has not been visited...
            if last_v not in visited:
                # CHECK IF IT'S THE TARGET
                if last_v == destination_vertex:
                    # IF SO, RETURN PATH
                    return path
                # Mark it as visited...
                visited.add(last_v)
                # Then add A PATH TO its neighbors to the back of the queue
                for next_v in self.get_neighbors(last_v):
                    new_arr = path.copy()
                    new_arr.append(next_v)
                    q.enqueue(new_arr)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create an empty queue and enqueue A PATH TO the starting vertex ID
        s = Stack()
        for next_v in self.get_neighbors(starting_vertex):
            arr = [starting_vertex]
            arr.append(next_v)
            s.push(arr)

        # Create a Set to store visited vertices
        visited = set()
        # While the queue is not empty...
        while s.size() > 0:
            # Dequeue the lat PATH
            path = s.pop()
            # Grab the last vertex from the PATH
            last_v = path[len(path)-1]
            # If that vertex has not been visited...
            if last_v not in visited:
                # CHECK IF IT'S THE TARGET
                if last_v == destination_vertex:
                    # IF SO, RETURN PATH
                    return path
                # Mark it as visited...
                visited.add(last_v)
                # Then add A PATH TO its neighbors to the back of the queue
                for next_v in self.get_neighbors(last_v):
                    new_arr = path.copy()
                    new_arr.append(next_v)
                    s.push(new_arr)

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        def dfs_indoor(node, visited, path):
            if node in visited:
                return False

            visited.add(node)
            path.append(node)
            if node == destination_vertex:
                return True

            for next_v in self.get_neighbors(node):
                if dfs_indoor(next_v, visited, path):
                    return True

            path.pop()
            return False

        visited = set()
        path = []
        dfs_indoor(starting_vertex, visited, path)
        return path


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
