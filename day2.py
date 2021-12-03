

text_file = open("day2.txt", "r")
lines = text_file.read().split('\n')

hor = 0
dep = 0
aim = 0

for line in lines:
    if "forward" in line:
        line = line.replace("forward","")
        hor += int(line)
        dep = dep + (int(line) * aim)
    elif "down" in line:
        line = line.replace('down ','')
        #dep += int(line)
        aim += int(line)
    elif "up" in line:
        line = line.replace('up ','')
        #dep -= int(line)
        aim -= int(line)
    else:
        continue
print(hor * dep)