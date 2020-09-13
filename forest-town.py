from random import *
from copy import copy, deepcopy

length = 10
height = 10

class Plain():
    def __init__(self):
        self.age = 0
    def __str__(self):
        return '#'
    def Evolve(self, nearby_tiles):
        if any(isinstance(tile, Tree) for tile in nearby_tiles):
            ran = random()
            if ran > 0.9:
                return Tree()
        return Plain()


class Seedling():
    def __init__(self):
        self.age = 0
    def __str__(self):
        return'.'
    def Evolve(self,nearby_tiles):
        self.age += 1
        grow = self.age * .2 + random()
        if grow > 1:
            evolved = Sapling()
            return evolved
        else:
            return self.clone()

class Sapling():
    def __init__(self):
        self.age = 0
    def __str__(self):
        return 't'
    def Evolve(self, nearby_tiles):
        self.age += 1
        grow = self.age * .05 + random()
        if grow > 1:
            evolved = Tree()
            return evolved
        else:
            return self.clone()

class Tree():
    def __init__(self):
        self.age = 0
    def __str__(self):
        return'T'
    def Evolve(self, nearby_tiles):
        return Tree()

class Map():
    def __init__(self):                         # defines initialization function that takes para 'N'
        self.grid = []                          # sets self.grid to an empty list
        for r in range(0, length):                   # for loop, for every row in range 0 to para N
            row = []                            # create an empty list
            for c in range(0, height):               # nested loop, for every column in range 0 to para N
                row.append(Plain())             # adds whatever to the list 'row'
            self.grid.append(row)               # appends the entire row to the self.grid list
        # for testing purposes
        self.grid[4][4] = Tree()
        self.grid[4][5] = Tree()
        self.grid[5][4] = Tree()
        self.grid[5][5] = Tree()

    def __str__(self):                          # this returns the defined string representation of an object (map here)
        s = ''                                  # sets s equal to a blank space
        for row in self.grid:                   # for every row (nested list) in self.grid (map)
            for tile in row:                    # for each tile (column) in that row
                s += str(tile)                  # s adds the object, called as a string
            s += '\n'                           # adds a new line break after each row
        return s                                # returns the Map

    def Turn(self):
        newgrid = deepcopy(self.grid)
        for r in range(0, length):
            for c in range(0, height):
                tile = self.grid[c][r]
                nearby_tiles = []
                for x in range(r-1, r+2):
                    for y in range(c-1, c+2):
                        if (x >= 0 or x < length) or (y >= 0 or y < width): #check if index is in bounds of grid
                            nearby_tiles.append(self.grid[x][y])
                newtile = tile.Evolve(nearby_tiles)
                newgrid[c][r] = newtile
        self.grid = newgrid
        return

m = Map()
for t in range(0,1):
    print(t)
    m.Turn()
    print(m)

#updating random tile in nearby_tiles
