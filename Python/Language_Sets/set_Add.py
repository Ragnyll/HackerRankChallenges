num_stamps = int(input())
unique_stamps = set()

for i in range(0, num_stamps):
    unique_stamps.add(input())

print(len(unique_stamps))