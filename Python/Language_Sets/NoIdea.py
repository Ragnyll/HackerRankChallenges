# the contents of the first line don't matter if you split the input correctly
input()
n_integers = list(map(int, input().split()))
set_A = set(map(int, input().split()))
set_B = set(map(int, input().split()))
happiness = 0

for i in n_integers:
    if i in set_A:
        happiness = happiness + 1
    if i in set_B:
        happiness = happiness - 1
        
# and now print the net happiness
print(happiness)