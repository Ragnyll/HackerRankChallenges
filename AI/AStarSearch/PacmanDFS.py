pacman_position = input().split()
food_position = input().split()
# graph dimensions = [rows, column]
graph_dimensions = input().split()

graph = []
for rows in range(0, int(graph_dimensions[0])):
    graph.append(list(input()))

for row in graph:
    print(row)
