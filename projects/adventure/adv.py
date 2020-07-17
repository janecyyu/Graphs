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


# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n', "s", "s", "s", "s", "s"]
traversal_path = []
count_n = 0
count_n_w = 0
NoneType = type(None)
q = Queue()
visited = set()
# print(type(player.current_room))
q.enqueue(player.current_room)
while q.size() > 0:
    path = q.dequeue()
    # str = type(path)
    # print(type(path) is NoneType)
    # if(type(path) is NoneType):
    #     print("break??")
    #     break
    # q.enqueue(path.get_room_in_direction("n"))
    # u = path[-1]

    if path not in visited:
        print(path)
        visited.add(path)
        # get neighbors
        directions = path.get_exits_string()
        # grab n,e,s,w only
        directions = directions[8:-1]
        directions = directions.replace(',', '').replace(' ', '')
        for d in directions:
            #         path_copy = path

            if d == "n":
                # go n until touch wall
                path_n_copy = path

                while path_n_copy.get_room_in_direction("n"):
                    # count_n += 1
                    traversal_path.append("n")
                    path_n_copy = path_n_copy.get_room_in_direction("n")
                # go south check if the room has neighbors
                while len(get_neighbors(path_n_copy)) > 0 and path_n_copy.id != 0:
                    # w or e
                    w_copy = path_n_copy
                    count_w = 0
                    while "w" in get_neighbors(w_copy):
                        count_w += 1
                        traversal_path.append("w")
                        w_copy = w_copy.get_room_in_direction("w")
                    for i in range(count_w):
                        traversal_path.append("e")
                    e_copy = path_n_copy
                    count_e = 0
                    while "e" in get_neighbors(e_copy):
                        count_e += 1
                        traversal_path.append("e")
                        e_copy = e_copy.get_room_in_direction("e")
                    for i in range(count_e):
                        traversal_path.append("w")

                    traversal_path.append("s")
                    path_n_copy = path_n_copy.get_room_in_direction("s")

            if d == "s":
                # go n until touch wall
                path_n_copy = path

                while path_n_copy.get_room_in_direction("s"):
                    # count_n += 1
                    traversal_path.append("s")
                    path_n_copy = path_n_copy.get_room_in_direction("s")
                # go south check if the room has neighbors
                while len(get_neighbors(path_n_copy)) > 0 and path_n_copy.id != 0:
                    # w or e
                    w_copy = path_n_copy
                    count_w = 0
                    while "w" in get_neighbors(w_copy):
                        count_w += 1
                        traversal_path.append("w")
                        w_copy = w_copy.get_room_in_direction("w")
                    for i in range(count_w):
                        traversal_path.append("e")
                    e_copy = path_n_copy
                    count_e = 0
                    while "e" in get_neighbors(e_copy):
                        count_e += 1
                        traversal_path.append("e")
                        e_copy = e_copy.get_room_in_direction("e")
                    for i in range(count_e):
                        traversal_path.append("w")

                    traversal_path.append("n")
                    path_n_copy = path_n_copy.get_room_in_direction("n")

            if d == "w":
                # go west until touch wall
                path_w_copy = path

                while path_w_copy.get_room_in_direction("w"):
                    # count_n += 1
                    traversal_path.append("w")
                    path_w_copy = path_w_copy.get_room_in_direction("w")
                # go south check if the room has neighbors
                while len(get_neighbors(path_w_copy)) > 0 and path_w_copy.id != 0:
                    # n or s
                    n_copy = path_w_copy
                    count_n = 0
                    while "n" in get_neighbors(n_copy):
                        count_n += 1
                        traversal_path.append("n")
                        n_copy = n_copy.get_room_in_direction("n")
                    for i in range(count_n):
                        traversal_path.append("s")
                    s_copy = path_w_copy
                    count_s = 0
                    while "s" in get_neighbors(s_copy):
                        count_s += 1
                        traversal_path.append("s")
                        s_copy = s_copy.get_room_in_direction("s")
                    for i in range(count_s):
                        traversal_path.append("n")

                    traversal_path.append("e")
                    path_w_copy = path_w_copy.get_room_in_direction("e")

            if d == "e":
                # go west until touch wall
                path_w_copy = path

                while path_w_copy.get_room_in_direction("e"):
                    # count_n += 1
                    traversal_path.append("e")
                    path_w_copy = path_w_copy.get_room_in_direction("e")
                # go south check if the room has neighbors
                while len(get_neighbors(path_w_copy)) > 0 and path_w_copy.id != 0:
                    # n or s
                    n_copy = path_w_copy
                    count_n = 0
                    while "n" in get_neighbors(n_copy):
                        count_n += 1
                        traversal_path.append("n")
                        n_copy = n_copy.get_room_in_direction("n")
                    for i in range(count_n):
                        traversal_path.append("s")
                    s_copy = path_w_copy
                    count_s = 0
                    while "s" in get_neighbors(s_copy):
                        count_s += 1
                        traversal_path.append("s")
                        s_copy = s_copy.get_room_in_direction("s")
                    for i in range(count_s):
                        traversal_path.append("n")

                    traversal_path.append("w")
                    path_w_copy = path_w_copy.get_room_in_direction("w")


print("count_n", count_n)
print("t_p", traversal_path)


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
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
