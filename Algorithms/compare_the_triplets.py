triplet_a = input().split()
triplet_b = input().split()

alice_points = 0
bob_points = 0

for num in range(0, len(triplet_a)):
    if int(triplet_a[num]) > int(triplet_b[num]):
        alice_points += 1
    elif int(triplet_a[num]) < int(triplet_b[num]):
        bob_points += 1

print(str(alice_points) + ' ' + str(bob_points))
        
