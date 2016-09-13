start_position = input().split()
food_position = input().split()
graph_dimensions = input().split()

graph = []
for rows in range(0, int(graph_dimensions[0])):
    graph.append((list(input()), False))

nodes_explored = 0
stack = []

# push the starting node
stack.append(start_position)

# push the visitable neigbors
while len(stack) > 0:
    print(stack)
    current_node = stack.pop(0)
    print(current_node)
    # look up
    if graph[int(current_node[0]) + 1][int(current_node[1])] == '-':
        new_node = []
        new_node.append(str(int(current_node[0]) + 1))
        new_node.append(str(current_node[1]))
        stack.append(new_node)
    #look left
    if graph[int(current_node[0])][int(current_node[1]) - 1] == '-':
        new_node = []
        new_node.append(str(current_node[0]))
        new_node.append(str(int(current_node[1]) - 1))
        stack.append(new_node)
    #look right
    if graph[int(current_node[0])][int(current_node[1]) + 1] == '-':
        new_node = []
        new_node.append(str(current_node[0]))
        new_node.append(str(int(current_node[1]) + 1))
        stack.append(new_node)
    #look down
    if graph[int(current_node[0]) - 1][int(current_node[1])] == '-':
        new_node = []
        new_node.append(str(int(current_node[0]) - 1))
        new_node.append(str(current_node[1] ))
        stack.append(new_node)
