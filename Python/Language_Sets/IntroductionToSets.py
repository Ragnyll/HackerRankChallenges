number_of_inputs = input()

heights = set(map(int, input().split()))


height_sums = sum(heights)
num_heights = len(heights)

average_height = height_sums / num_heights
print(average_height)
