from room import Room
from player import Player
from world import World
from util import Stack, Queue

import random
from ast import literal_eval


def get_neighbors(path):
    direc = path.get_exits_string()
    direc = direc[8:-1]
    direc = direc.replace(',', '').replace(' ', '')

    return direc


def go_dep(path, n, e, w, s):
    path_n_copy = path

    while path_n_copy.get_room_in_direction(n):
        # count_n += 1
        traversal_path.append(n)
        path_n_copy = path_n_copy.get_room_in_direction(n)
    # go south check if the room has neighbors
    while len(get_neighbors(path_n_copy)) > 0 and path_n_copy.id != 0:
        # w or e
        w_copy = path_n_copy
        count_w = 0
        while w in get_neighbors(w_copy):
            count_w += 1
            traversal_path.append(w)
            w_copy = w_copy.get_room_in_direction(w)
        # 走到底後檢查每個房間有沒有n方向的房間
        check_n = w_copy
        count_check_n = 0
        while n in get_neighbors(check_n):
            count_check_n += 1
            traversal_path.append(n)
            check_n = check_n.get_room_in_direction(n)

        for i in range(count_w):
            traversal_path.append(e)
        e_copy = path_n_copy
        count_e = 0
        while e in get_neighbors(e_copy):
            count_e += 1
            traversal_path.append(e)
            e_copy = e_copy.get_room_in_direction(e)
        for i in range(count_e):
            traversal_path.append(w)

        traversal_path.append(s)
        path_n_copy = path_n_copy.get_room_in_direction(s)


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
# t = player.current_room  # Exits: [n, s, w, e]
# print("t", type(t))
# t = player.current_room.get_exits_string() # Exits: [n, s, w, e]
# t = player.current_room.name  # Room 0
# t = player.current_room.id  # 0
# t = player.current_room.get_room_in_direction("n")
# Room 1

#    (3,6)

# Exits: [n, s]

player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")


# NoneType = type(None)
# q = Queue()
# visited = set()
# # print(type(player.current_room))
# q.enqueue(player.current_room)
# while q.size() > 0:
#     path = q.dequeue()

#     if path not in visited:
#         print(path)
#         visited.add(path)
#         # get neighbors
#         directions = path.get_exits_string()
#         # grab n,e,s,w only
#         directions = directions[8:-1]
#         directions = directions.replace(',', '').replace(' ', '')
#         for d in directions:
#             #         path_copy = path

#             if d == "n":
#                 # go n until touch wall
#                 go_dep(path, "n", "e", "w", "s")

#             if d == "s":
#                 # go n until touch wall
#                 go_dep(path, "s", "e", "w", "n")

#             if d == "w":
#                 # go west until touch wall
#                 go_dep(path, "w", "n", "s", "e")

#             if d == "e":
#                 # go west until touch wall
#                 go_dep(path, "e", "n", "s", "w")


# print("t_p", traversal_path)
