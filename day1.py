

text_file = open("day1.txt", "r")
lines = text_file.read().split('\n')

dec = 0
inc = 0
equal = 0
windows = []

while len(lines) >= 3:
    window= int(lines[0]) + int(lines[1]) + int(lines[2])
    windows.append(window)
    del lines[0]

current = "0"
for line in windows:
    if current == "0":
        current = line
        continue
    next = line
    if int(next) > int(current):
        inc += 1
    elif int(next) < int(current):
        dec += 1
    else:
        equal += 1
    current = next

print(dec)
print(inc)


