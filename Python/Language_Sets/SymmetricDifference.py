number_of_inputs = input()
M_integers = set(map(int, input().split()))
number_of_inputs = input()
N_integers = set(map(int, input().split()))

symmetric_difference = list(M_integers ^ N_integers)

symmetric_difference = sorted(symmetric_difference)

for number in symmetric_difference:
    print(number)