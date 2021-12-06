
# Part 1
text_file = open("day6.txt", "r")
fish_list = [int(fish) for fish in text_file.read().split(',')]
days = 80
for day in range(days):
    updated_fish = []
    for fish in fish_list:
        if fish == 0:
            updated_fish.append(6)
            updated_fish.append(8)
        else:
            updated_fish.append( fish - 1)
        fish_list = updated_fish
print(len(updated_fish))

# Part 2 (up the efficiency!)
days = 256
text_file = open("day6.txt", "r")
fish_list = [int(fish) for fish in text_file.read().split(',')]
fish_dict = {age : 0 for age in range(9)}
for fish in fish_list:
    fish_dict[fish] += 1
for day in range(days):
    dead_fish = fish_dict[0]
    for fish in range(8):
        fish_dict[fish] = fish_dict[fish + 1]
    fish_dict[8] = dead_fish
    fish_dict[6] +=  dead_fish   
print(sum(fish_dict.values()))
