from collections import defaultdict, deque


def bfs(start, checked, adjacency_list):
    """Perform BFS to find all connected lands starting from the 'start' land."""
    queue = deque([start])
    connected_lands = []

    while queue:
        current_land = queue.popleft()
        if current_land not in checked:
            checked.add(current_land)
            connected_lands.append(current_land)
            queue.extend(adjacency_list[current_land])

    return connected_lands


def build_adjacency_list(lands):
    """Create an adjacency list for the lands based on their coordinates."""
    adjacency_list = defaultdict(list)

    for x1, y1 in lands:
        for x2, y2 in lands:
            if (x1 == x2 and abs(y1 - y2) == 1) or (y1 == y2 and abs(x1 - x2) == 1):
                adjacency_list[(x1, y1)].append((x2, y2))

    return adjacency_list


def find_neighbors(lands):
    """Find all groups of connected lands."""
    adjacency_list = build_adjacency_list(lands)
    visited = set()
    groups = []

    for land in lands:
        if land not in visited:
            group = bfs(land, visited, adjacency_list)
            groups.append(group)

    return groups


def find_new_neighbors(existing_lands, new_lands):
    """Find new lands that are neighbors to existing lands."""
    adjacency_list = build_adjacency_list(existing_lands + new_lands)
    new_groups = []

    for new_land in new_lands:
        for existing_land in existing_lands:
            if new_land in adjacency_list[existing_land]:
                new_groups.append(new_land)
                break

    return new_groups


def print_groups(groups):
    """Print groups of connected lands if the group size is greater than 1."""
    for group in groups:
        if len(group) > 1:
            print(f'Count [{len(group)}] : {group}')


input_params = [
    (106, 183), (107, 185), (110, 186), (195, 52), (177, 78), (232, 101), (233, 101), (192, 74), (204, 82), (94, 95), (186, 132), (138, 133), (140, 133),
    (138, 134), (140, 134), (137, 135), (138, 135), (139, 135), (140, 135), (137, 136), (138, 136), (139, 136), (140, 136), (141, 136), (138, 137), (139, 137),
    (140, 137), (139, 138), (143, 133), (144, 138), (145, 138), (145, 139), (126, 186), (125, 186), (160, 72), (161, 72), (160, 73), (161, 73), (148, 34),
    (148, 35), (51, 88), (133, 179), (94, 53), (79, 90), (167, 26), (174, 31), (135, 130), (240, 60), (239, 64), (239, 65), (235, 66), (224, 80), (216, 15),
    (213, 16), (214, 16), (215, 16), (216, 16), (213, 17), (214, 17), (215, 17), (216, 17), (217, 17), (51, 34), (51, 35), (53, 35), (49, 35), (50, 35),
    (49, 34), (53, 33), (53, 32), (54, 32), (54, 31), (49, 30), (50, 30), (52, 30), (53, 30), (54, 30), (57, 29), (56, 29), (56, 30), (55, 30), (52, 34)
]
common_lands = [(103, 56), (168, 64), (64, 190), (179, 77), (232, 100), (42, 36), (47, 17), (34, 5), (81, 74), (165, 57), (22, 17), (106, 175), (107, 175),
                (118, 189), (106, 174), (40, 74), (128, 63), (118, 40), (119, 40), (82, 164), (82, 163), (82, 162), (87, 135), (86, 134)]

rare_lands = [(98, 185), (205, 136), (206, 136), (206, 135), (218, 152), (219, 152), (222, 149), (223, 148), (213, 128), (210, 127), (215, 31), (28, 79),
              (164, 59), (193, 38)]

result_groups = find_neighbors(input_params)
# print_groups(result_groups)

new_neighbors = find_new_neighbors(input_params, common_lands)
print_groups(new_neighbors)
