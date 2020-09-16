import pygame
from random import *
from copy import copy, deepcopy

width = 800
height = 600
black = (0,0,0)
white = (255,255,255)
s_tree = pygame.image.load("images/tree.png")
s_plain = pygame.image.load("images/plain.png")
tile_size = 10

class Plain():
    def __init__(self):
        self.age = 0
    def __str__(self):
        return '#'
    def Evolve(self, nearby_tiles):
        count = 0
        for tile in nearby_tiles:
            if isinstance(tile, Tree):
                count += 1
                if count >= 2:
                    ran = random()
                    if ran > 0.9:
                        return Tree()
        return Plain()

class Tree():
    def __init__(self):
        self.age = 0
    def __str__(self):
        return'T'
    def Evolve(self, nearby_tiles):
        return Tree()

class WorldMap():
    def __init__(self, grid = None, length = 72, height = 128):
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
            self.grid[0][0] = Tree()
            self.grid[0][1] = Tree()
            self.grid[1][0] = Tree()
            self.grid[1][1] = Tree()

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

def game_init():

    global screen, game_map

    pygame.init()

    screen = pygame.display.set_mode([width,height])

    game_map = WorldMap()

    game_map = game_map.Turn()

def game_loop():

    running = True
    while running:

        events_list = pygame.event.get()

        for event in events_list:
            if event.type == pygame.QUIT:
                running = False

        draw_game()

    pygame.quit()

def draw_game():

    global screen

    screen.fill((black))

    draw_map(game_map)

    print(game_map)

    pygame.display.flip()

def draw_map(map):
    str_map = str(map)
    cx = 0
    cy = 0
    for tile in str_map:
        if tile == '#':
            screen.blit(s_plain, (cx, cy))
            cx += 10
            if cx >= 1280:
                cx = 0
                cy += 10
        elif tile == 'T':
            screen.blit(s_tree, (cx, cy))
            if cx >= 720:
                cx = 0
                cy += 10

game_init()
game_loop()
