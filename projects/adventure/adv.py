from room import Room
from player import Player
from world import World
from util import Stack, Queue

import random
from ast import literal_eval


class Path:
    def __init__(self, room, path):
        self.room = room
        self.path = path


OPPOSITE = {'n': 's', 's': 'n', 'w': 'e', 'e': 'w'}


def get_closest_path(start, graph):
    # Create an empty queue and enqueue A PATH TO the starting vertex ID
    q = Queue()
    q.enqueue(start)

    # Create a Set to store visited vertices
    visited = set()

    # While the queue is not empty...
    while q.size() > 0:

        # Dequeue the first PATH
        path = q.dequeue()
        # print(graph[start])
        for dir, neighbor_v in graph[path.room].items():
            neighbor = '?' if neighbor_v == '?' else str(neighbor_v.id)
            print("cur_room: %d, dir: %s, neighbor:%s" %
                  (path.room.id, dir, str(neighbor)))
            if neighbor_v == "?":
                return path.path + [dir]
            if neighbor_v not in visited:
                q.enqueue(Path(neighbor_v, path.path + [dir]))
                visited.add(neighbor_v)
    return []


# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n', "s", "s", "s", "s", "s"]
traversal_path = []
cur_room = player.current_room
graph = {}
unvisited = 1

while unvisited > 0:
    # add room to graph
    dir_graph = graph[cur_room] if cur_room in graph else {}
    # print(dir_graph)
    for dir in cur_room.get_exits():
        if dir not in dir_graph:
            dir_graph[dir] = "?"
            unvisited += 1
    graph[cur_room] = dir_graph

    unvisited -= 1
    closest_path = get_closest_path(Path(cur_room, []), graph)
    # print(closest_path)
    for dir in closest_path:
        traversal_path.append(dir)
        old_room = cur_room
        player.travel(dir)
        cur_room = player.current_room
        dir_graph[dir] = cur_room

        # get dir_graph of room we are in now
        dir_graph = graph[cur_room] if cur_room in graph else {}
        dir_graph[OPPOSITE[dir]] = old_room
        graph[cur_room] = dir_graph

        print("room", cur_room.id)


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)


if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
