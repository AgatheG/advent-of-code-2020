with open("input.txt", "r") as file:
    tiles = file.read().split("\n\n")

import re

PATTERN = "^Tile\s(\d+)\:$"

class Tile(object):
    def __init__(self, tile_id, borders):
        self.tile_id = tile_id
        self.borders = borders

    def get_all(self):
        return self.borders | set(b[::-1] for b in self.borders)

d = {}
for tile in tiles:
    tile = tile.split("\n")
    borders = set()
    borders.add(tile[1])
    borders.add(tile[-1])
    s, ss = "", ""
    for i, line in enumerate(tile):
        if i == 0:
            tile_id = re.search(PATTERN, line).group(1)
        else:
            s += line[0]
            ss += line[-1]
    borders.add(s)
    borders.add(ss)
    d[tile_id] = Tile(tile_id, borders)

product = 1
for k in d:
    s = 0
    tile = d[k]
    for kk in d:
        other_tile = d[kk]
        if k != kk:
            check = tile.get_all() & other_tile.get_all()
            if check:
                s += 1
        if s > 2:
            break
    if s == 2:
        product *= int(tile.tile_id)

print(product)