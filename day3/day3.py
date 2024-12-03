import re
total = 0

file = "input.txt"

def open_file(file):
    with open(file, "r") as f:
        line = f.read().strip()

    return line

line = open_file(file)


match = re.findall(r"mul\((\d+),(\d+)\)", line)
print(match)


for i in match:
    total += int(i[0]) * int(i[1])


print(total)
