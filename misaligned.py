def get_color_map():
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    color_map = []
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            pair_number = i * len(minor_colors) + j
            color_map.append((pair_number, major, minor))
    return color_map

def print_color_map(color_map):
    for tuples in color_map:
        print(f'{tuples[0]} | {tuples[1]} | {tuples[2]}')

# Usage and testing
color_map = get_color_map()
print_color_map(color_map)
assert len(color_map) == 25
print("All is well (maybe!)")
