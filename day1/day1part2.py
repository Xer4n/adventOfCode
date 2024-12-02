total_score = 0

list_1 = []
list_2 = []

similarity_scores = []


with open("input.txt", "r") as f:

    for line in f:
        current_line = []
        current_line.append(line.split("   "))
        list_1.append(current_line[0][0])
        list_2.append(current_line[0][1].rstrip())


for i in list_1:
    current = 0
    for k in list_2:
        if (i == k):
            current += 1
    if (current != 0):
        current_score = 0
        current_score = int(i) * int(current)
        similarity_scores.append(current_score)

for x in similarity_scores:
    total_score += int(x)


print(total_score)