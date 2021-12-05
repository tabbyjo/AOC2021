def split_coord_to_xy(coord):
    coord = coord.split(",")
    coords = {"x": int(coord[0]),"y": int(coord[1])}
    return coords

text_file = open("day5.txt", "r")
lines = text_file.read().split('\n')
coords_list = []
for line in lines:
    pair = line.split(" -> ")
    start = split_coord_to_xy(pair[0])
    end = split_coord_to_xy(pair[1])
    # Include next two lines to filter out the diagonals
    ##if (start["x"] != end["x"]) and (start["y"] != end["y"]):
    ##    continue
    coords_list.append({"start": start, "end": end})
visited_map = {}

for coord_pair in coords_list:
    startx = coord_pair["start"]["x"]
    starty = coord_pair["start"]["y"]
    endx = coord_pair["end"]["x"]
    endy = coord_pair["end"]["y"]
    if startx == endx:
        if starty > endy:
            _range = range(starty, endy - 1, -1)
        else:
            _range = range(starty, endy + 1)
        for i in _range:
            if not visited_map.get(startx, False):
                visited_map[startx] = {}
            visited_map[startx][i] = visited_map[startx].get(i, 0) + 1  
    elif starty == endy:
        if startx > endx:
            _range = range(startx, endx - 1, -1)
        else:            
            _range = range(startx, endx + 1)
        for i in _range:
            if not visited_map.get(i, False):
                visited_map[i] = {}
            visited_map[i][starty] = visited_map[i].get(starty, 0) + 1
    else:
        if starty > endy:
            _rangey = range(starty, endy - 1, -1)
        else:
            _rangey = range(starty, endy + 1)
        if startx > endx:
            _rangex = range(startx, endx - 1, -1)
        else:            
            _rangex = range(startx, endx + 1)
        for x, y in zip(_rangex, _rangey):
            if not visited_map.get(x, False):
                visited_map[x] = {}
            visited_map[x][y] = visited_map[x].get(y, 0) + 1

overlap_total = 0
for k, v in visited_map.items():
    overlap_total += sum(overlap > 1 for overlap in v.values())
print(overlap_total)
    