count = 0



with open("input.txt", "r") as f:
    for line in f:
        line = line.rstrip()
        line = line.split(" ")

        for i in range(len(line)):
            line[i] = int(line[i])

        inc_dec = (line==sorted(line) or line==sorted(line, reverse=True))
        safe = True

        for i in range(len(line)-1):
            difference = abs(int(line[i]) - int(line[i + 1]))

            if not 1<=difference<=3:
                safe = False
        
        print(inc_dec, safe)
        if safe and inc_dec:
            count += 1


print(count)

