#Day 1 solution Advent of Code

total_distance = 0
list_1 = []
list_2 = []

distances = []

with open("input.txt", "r") as f:

    for line in f:
        current_line = []
        current_line.append(line.split("   "))
        list_1.append(current_line[0][0])
        list_2.append(current_line[0][1].rstrip())

print(type(list_1))

list_1 = sorted(list_1)
list_2 = sorted(list_2)
print(type(list_1))

for i in range(len(list_1)):
    distances.append(abs(int(list_1[i]) - int(list_2[i])))


for i in distances:
    total_distance += i



print(total_distance)