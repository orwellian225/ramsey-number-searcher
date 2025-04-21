import sys

graph_size = int(sys.argv[1])
num_colors = int(sys.argv[2])

node_count = 0
def recursive_coloring(depth: int, color: str, list_of_colors: list[str]):
    global node_count
    node_count += 1

    print((depth - 1) * "\t" + "|-------" + color[-1] if depth != 0 else "root")

    if depth == (graph_size**2 - graph_size) // 2 - 1:
        for i in range(1, num_colors + 1):
            new_color = str(color)
            new_color += str(i)
            list_of_colors.append(new_color)
        return

    for i in range(1, num_colors + 1):
        new_color = str(color)
        new_color += str(i)
        recursive_coloring(depth + 1, new_color, list_of_colors)

colorings = []
recursive_coloring(0, "", colorings)
print("Number of visits:", node_count)
print("Number of generated colorings:", len(colorings))
print("Colorings:", colorings)