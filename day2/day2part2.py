count = 0



def is_safe(line):
        inc_dec = (line==sorted(line) or line==sorted(line, reverse=True))    
        if not inc_dec:
            return False

        for i in range(len(line)-1):
            difference = abs(int(line[i]) - int(line[i + 1]))

            if not 1<=difference<=3:
                return False

        return True
         

def double_check(line):
    if is_safe(line):
        return True
    for x in range(len(line)):
        if is_safe(line[:x] + line[x+1:]):
            return True
    
    return False


with open("input.txt", "r") as f:
    for line in f:
        line = line.rstrip()
        line = line.split(" ")

        for i in range(len(line)):
            line[i] = int(line[i])


        safe = double_check(line)
        
        
        if safe:
            count += 1


print(count)

