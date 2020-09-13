from random import *
from copy import copy, deepcopy

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

class WorldMap():
    def __init__(self, grid = None, length = 10, height = 10):
        self.grid = grid
        self.length = length
        self.height = height

        if grid == None:
            self.grid = []
            for r in range(0, self.length):
                row = []
                for c in range(0, self.height):
                    row.append(Plain())
                self.grid.append(row)
                # for testing purposes
            self.grid[4][4] = Tree()
            self.grid[4][5] = Tree()
            self.grid[5][4] = Tree()
            self.grid[5][5] = Tree()

    def __str__(self):
        s = ''
        for row in self.grid:
            for tile in row:
                s += str(tile)
            s += '\n'
        return s


    def Turn(self):
        newgrid = deepcopy(self.grid)
        for r in range(0, self.length):
            for c in range(0, self.height):
                tile = self.grid[r][c]
                nearby_tiles = []
                for x in range(r-1, r+2):
                    for y in range(c-1, c+2):
                        if ((x >= 0 and x < self.length) and (y >= 0 and y < self.height)):
                            nearby_tiles.append(self.grid[x][y])
                newtile = tile.Evolve(nearby_tiles)
                newgrid[r][c] = newtile

        return WorldMap(newgrid)

worldMap = WorldMap()
print(worldMap)
while True:
    input()
    worldMap = worldMap.Turn()
    print(worldMap)
