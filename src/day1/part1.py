f = open("./src/day1/input.txt", "r")
input = f.read().split("\n")

list_left = []
list_right = []

for item in input:
    parts = item.split('   ')
    list_left.append(int(parts[0]))
    list_right.append(int(parts[1]))

list_left.sort()
list_right.sort()

diff = 0

for i, item in enumerate(list_left):
    diff += abs(item - list_right[i])

print(diff)