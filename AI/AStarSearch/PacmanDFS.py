pacman_position = input().split()
food_position = input().split()
graph_dimensions = input().split()

graph = []
for rows in range(0, int(graph_dimensions[0])):
    graph.append(list(input()))

nodes_explored = 0
stack = []

# push the starting node
stack.append(pacman_position)
# print(graph[int(current_node[0])][int(current_node[1])]) Verifies pacman starting position

# push the visitable neigbors
while len(stack) > 0:
    current_node = stack.pop(0)
    print(current_node)
    # look up
    if graph[int(current_node[0]) + 1][int(current_node[1])] == '-':
        stack.append(graph[int(current_node[0]) + 1][int(current_node[1])])
    #look left
    if graph[int(current_node[0])][int(current_node[1]) - 1] == '-':
        stack.append(graph[int(current_node[0])][int(current_node[1]) - 1])
    #look right FIX THIS FIRST
    if graph[int(current_node[0])][int(current_node[1]) + 1] == '-':
        stack.append()
    #look down
    if graph[int(current_node[0]) - 1][int(current_node[1])] == '-':
        stack.append(graph[int(current_node[0]) - 1][int(current_node[1])])
