set_size = input()
set_A = set(map(int, input().split()))
num_operations = int(input())

for operations in range(0, num_operations):
    operation = input().split()
    if len(operation) == 1:
        set_A.pop()
    else:
        if operation[0] == "remove":
            set_A.remove(int(operation[1]))
        if operation[0] == "discard":
            set_A.discard(int(operation[1]))

print(sum(set_A))
        