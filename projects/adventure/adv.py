from room import Room
from player import Player
from world import World
from util import Stack, Queue

import random
from ast import literal_eval

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
                path_copy = path

                while path_copy.get_room_in_direction("n"):
                    count_n += 1
                    traversal_path.append("n")
                    path_copy = path_copy.get_room_in_direction("n")

            #     traversal_path.append("s")
            # if d == "s":
            #     traversal_path.append("n")
            # if d == "w":
            #     traversal_path.append("e")
            # if d == "e":
            #     traversal_path.append("w")
            # new_room = path.get_room_in_direction(d)
            # path.append(new_room)
            # q.enqueue(new_room)
            # print(q.queue)

print("count_n", count_n)
print("t_p", traversal_path)

# if u not in visited:
#     visited.add(u)
#     for neighbor in u.get_exits():
#         print("u", u)
#         path_copy = list(u)
#         room_name = u.get_room_in_direction(neighbor)
#         path_copy.append(room_name)
#         q.enqueue(path_copy)
#         print(q.queue)


def get_neighbors(room):
    return room.get_exits()


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
