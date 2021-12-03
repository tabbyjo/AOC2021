

def calculate(value_):
    text_file = open("day3.txt", "r")
    lines = text_file.read().split('\n')
    gamma = []
    eps = []
    x=0
    _count = len(lines[0])
    while x < _count:
        all = []
        for line in lines:
            all.append(line[x])
        print(all)
        gamma.append(max(set(all), key = all.count))
        eps.append(min(set(all), key = all.count))
        #print(int("".join(gamma), 2) * int("".join(eps), 2))
        high = max(set(all), key = all.count)
        low = min(set(all), key = all.count)
        oxg_co2 = []
        for line in lines:
            if value_ == "1":
                if high == low:
                    if line[x] == value_:
                        oxg_co2.append(line)
                elif line[x] == high:
                    oxg_co2.append(line)  
            else:
                if high == low:
                    if line[x] == value_:
                        oxg_co2.append(line)
                elif line[x] == low:
                    oxg_co2.append(line)  
        lines = oxg_co2
        print(lines)
        if len(lines) == 1:
            return lines
        x += 1

oxg_co2 = calculate("1")
co2 = calculate("0")
print(int("".join(oxg_co2), 2) * int("".join(co2), 2))

