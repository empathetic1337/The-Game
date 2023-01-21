import sqlite3

import pygame as pg

_ = False
mini_map = [
    [4, 4, 4, 1, 1, 4, 1, 2, 3, 3, 2, 1, 2, 1, 4, 1],
    [1, 1, 1, 1, _, _, _, _, 3, _, _, _, _, _, _, 1],
    [2, 1, 1, _, _, 2, _, _, _, _, 2, 2, 2, _, _, 1, 1, 1],
    [1, _, _, _, _, _, 2, _, _, 2, _, _, 2, _, _, _, _, 1],
    [1, _, _, _, _, _, 2, _, _, 1, _, _, 2, _, _, 1, 1, 1],
    [1, 1, 1, _, _, _, 1, _, _, _, _, _, _, _, _, 4],
    [1, 1, 1, 1, 1, _, _, _, 1, _, _, 4, _, _, 1, 3],
    [1, 1, 1, 1, 4, _, _, _, 4, _, _, _, 3, 2, 1, 1],
    [1, 2, 1, 3, 1, 3, 1, 1, 2, _, _, _, 3, 1, 1, 2],
    [1, 1, 1, 1, 1, 1, 1, 1, _, _, _, _, 3, 1, 1, 2],
    [1, 1, 1, 1, 1, 1, 1, 1, _, _, _, _, 3, 1, 1, 3],
    [1, 1, 3, 1, 1, 1, 1, 1, _, _, _, _, 3, 1, 1, 1],
    [1, 4, _, _, _, _, _, _, _, _, _, _, _, _, 1, 2],
    [3, _, _, _, _, 2, _, 3, _, 1, 1, 2, _, 1, _, 1],
    [4, _, 2, 2, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, 1, _, _, _, 1, 2, _, _, _, _, _, 2],
    [4, _, _, _, 2, _, _, _, _, _, _, _, 1, _, _, 1],
    [1, _, _, _, 3, _, _, _, 2, _, _, _, _, _, _, 3],
    [4, _, 2, _, _, 4, _, 2, _, _, _, 2, _, _, _, 1],
    [3, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, 4, _, _, _, _, _, _, 4, _, _, 4, _, _, _, 1],
    [1, 1, 3, 3, _, _, _, _, _, _, _, _, 3, 1, 1, 1],
    [1, 1, 1, 3, _, _, _, _, _, _, _, _, 1, 1, 1, 1],
    [1, 3, 3, 4, _, _, _, _, _, _, _, _, 3, 3, 3, 1],
    [1, _, _, _, _, _, _, 4, _, _, _, _, _, _, _, 1],
    [2, _, _, 1, 4, _, _, _, 2, _, 2, _, _, _, _, 2],
    [3, _, _, _, 2, _, _, _, 4, _, _, 4, _, _, _, 3],
    [2, _, _, 2, _, 2, _, 2, _, _, _, 2, _, _, _, 1],
    [1, _, _, _, _, 4, _, 2, _, _, _, _, 2, _, _, 2],
    [3, _, _, _, _, _, _, _, _, _, 2, _, _, _, _, 3],
    [2, _, _, _, _, _, _, _, _, _, _, 4, _, _, 5, 3],
    [1, 3, 2, 1, 3, 2, 4, 3, 3, 2, 4, 1, 3, 3, 5, 2],
]
mini_map2 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, _, _, _, _, _, _, _, 2, _, _, _, _, _, _, 1],
    [1, _, _, 4, 4, 1, 3, _, 3, _, 2, 3, 1, _, _, 1],
    [1, _, _, _, _, _, 4, _, 1, _, _, _, 1, _, _, 1],
    [1, _, _, 3, _, _, 2, _, 3, _, 2, _, 2, _, _, 1],
    [1, _, _, 4, 4, 4, 4, _, 2, _, _, _, _, _, 3, 1],
    [1, _, _, _, _, _, _, _, 4, _, 1, 4, _, _, _, 1],
    [1, _, _, _, 4, _, _, _, 4, _, _, _, 1, _, _, 1],
    [1, 1, _, _, 1, 3, 1, 1, 1, 3, _, _, 3, 1, 1, 1],
    [1, 1, _, _, 1, 1, 1, 1, 1, 3, _, _, 3, 1, 1, 1],
    [1, 1, _, _, 1, 1, 1, 1, 1, 3, _, _, 3, 1, 1, 1],
    [1, 1, _, _, 1, 1, 1, 1, 1, 3, _, _, 3, 1, 1, 1],
    [1, 4, _, _, _, _, 3, _, _, _, _, _, _, _, _, 1],
    [3, _, _, _, _, _, 2, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, 4, 2, 2, _, _, _, _, 3, _, _, _, 3, _, 1],
    [1, _, _, 2, _, _, _, _, 1, _, 3, _, 3, _, 3, 1],
    [1, _, _, 1, _, _, _, _, 1, _, _, _, _, _, 3, 1],
    [1, _, _, _, _, 2, _, 4, _, 2, _, _, _, 1, _, 1],
    [3, _, _, _, _, _, _, _, _, _, 3, _, 2, _, _, 1],
    [1, 4, _, _, _, _, _, _, 4, _, _, 4, _, _, _, 1],
    [1, 1, 3, 3, _, _, 3, 3, 1, 3, 3, 1, 3, 1, 1, 1],
    [1, 1, 1, 3, _, _, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [3, 3, 3, 3, 5, 5, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
]
mini_map3 = [
    [7, 8, 9, 6, 10, 8, 6, 7, 9, 6, 7, 8, 8, 7, 9, 10],
    [9, _, _, _, _, _, _, 9, _, _, _, _, _, _, _, 7],
    [8, _, _, _, 7, _, _, 10, _, _, _, _, 8, _, _, 9],
    [7, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 8],
    [6, _, _, 6, _, _, _, _, _, 10, _, _, _, _, _, 10],
    [8, _, _, _, _, _, _, _, _, 6, _, _, 6, _, _, 6],
    [7, _, _, _, _, _, 6, _, _, 8, _, _, _, 9, _, 7],
    [9, _, _, _, 6, _, 9, _, 6, 9, _, _, _, _, _, 8],
    [10, 6, 7, 9, 6, 7, 8, 9, 6, 7, _, _, 7, 9, 10, 6],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 6, _, _, 6, 6, 7, 8],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 9, _, _, 9, 6, 8, 9],
    [9, 8, 9, 8, 10, 7, 6, 9, 8, 10, _, _, 10, 9, 8, 7],
    [6, 6, _, 6, _, 10, _, _, 8, _, _, _, _, 9, _, 9],
    [8, _, _, _, _, _, _, _, 7, _, _, _, _, 8, _, 7],
    [7, _, _, _, _, _, _, _, 9, _, 10, 9, 6, 7, _, 8],
    [9, _, _, 9, _, 8, 7, _, 10, _, _, _, _, _, _, 7],
    [10, _, _, 8, _, _, _, _, 6, 8, 9, 6, 9, _, _, 6],
    [6, _, _, 10, _, _, _, _, _, _, _, _, _, _, _, 10],
    [7, _, _, 6, _, _, _, _, _, _, 9, _, _, _, _, 6],
    [8, _, _, 7, _, _, _, _, _, _, 9, _, _, _, _, 8],
    [10, _, _, 8, _, _, _, _, _, _, _, _, _, _, _, 9],
    [6, 8, 6, 7, _, _, 9, 10, 7, 9, 6, 8, 6, 8, 9, 7],
    [8, 1, 1, 8, _, _, 7, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [7, 7, 7, 6, _, _, 8, 7, 6, 10, 9, 7, 6, 7, 8, 9],
    [9, _, _, 10, _, _, _, _, _, _, 7, _, _, _, _, 6],
    [6, _, _, 9, _, _, _, _, _, _, 8, _, _, _, _, 7],
    [8, _, _, 8, _, _, _, 8, _, _, _, _, _, _, _, 9],
    [7, _, _, 6, _, _, _, 9, _, _, _, 8, _, _, _, 8],
    [9, _, _, _, _, _, _, 7, _, _, _, 9, _, _, _, 6],
    [10, _, _, _, 8, _, _, _, _, _, _, 6, _, _, _, 9],
    [10, _, _, _, _, _, _, _, _, _, _, 10, _, _, _, 11],
    [6, 9, 8, 7, 10, 6, 7, 8, 9, 8, 7, 6, 10, 8, 11, 11],
]
mini_map4 = [
    [8, 7, 8, 9, 7, 7, 9, 8, 7, 9, 8, 7, 8, 9, 8, 9],
    [8, _, _, _, _, 9, 9, _, 10, _, _, _, _, _, _, 9],
    [6, _, _, _, 6, _, _, _, _, _, 10, _, _, _, _, 7],
    [7, _, _, _, _, 7, _, _, _, _, _, _, _, _, _, 8],
    [9, _, _, _, _, 7, _, 8, _, _, _, 10, _, _, _, 9],
    [8, _, _, _, 8, _, _, _, 10, _, 8, _, _, 10, _, 8],
    [8, _, _, 9, _, _, _, _, 10, _, _, _, _, _, _, 7],
    [7, _, _, _, 10, _, _, _, _, _, _, _, _, _, _, 8],
    [9, _, _, _, _, 6, _, _, _, 10, _, _, 8, _, _, 7],
    [8, _, _, 6, _, 7, _, _, _, _, _, _, _, _, _, 9],
    [8, _, 8, _, 8, _, 10, _, _, _, 8, _, _, _, _, 8],
    [9, _, 9, _, _, _, _, _, _, _, _, _, 8, _, _, 9],
    [6, _, _, _, 10, _, _, _, 8, _, _, _, _, _, _, 9],
    [8, _, _, _, _, 10, _, _, _, _, _, _, _, 10, _, 8],
    [7, _, 10, _, _, _, _, _, 8, 8, 8, _, 10, _, _, 8],
    [7, _, _, 9, _, _, _, _, _, _, _, _, _, 10, _, 9],
    [8, _, _, _, 10, _, _, _, _, _, _, _, _, _, _, 8],
    [8, _, 10, _, _, _, 7, _, 7, _, _, _, _, _, _, 7],
    [8, _, _, _, 10, _, _, _, _, 7, _, 7, _, _, _, 9],
    [7, _, _, _, 4, _, _, _, 4, _, _, _, _, _, _, 8],
    [8, 8, 9, _, _, _, _, _, _, _, _, _, 7, 9, 8, 7],
    [8, 1, 8, _, _, _, 8, _, 7, _, _, _, 8, 1, 1, 1],
    [9, 1, 6, _, _, _, _, _, _, _, _, _, 8, 1, 1, 6],
    [7, 7, 8, _, _, 6, _, 7, _, 6, _, _, 9, 9, 8, 1],
    [6, 8, _, _, _, _, _, _, _, _, 9, 9, _, _, _, 8],
    [8, 9, _, _, _, _, _, _, _, 9, _, _, _, _, _, 7],
    [9, _, 6, _, _, _, _, _, _, _, 9, _, _, _, _, 6],
    [8, _, _, 8, _, 7, _, _, 9, 9, 6, _, 8, 7, _, 7],
    [6, _, _, 6, _, 6, _, _, 9, _, 6, _, 6, _, _, 8],
    [9, _, _, 6, _, _, 9, _, 7, _, _, _, _, _, _, 8],
    [7, _, _, _, 8, _, _, 9, _, _, _, _, _, _, _, 9],
    [8, _, _, _, _, 9, _, _, _, _, _, _, _, _, _, 8],
    [8, 8, _, 7, _, _, _, _, 9, _, _, 6, _, _, _, 7],
    [8, 9, 6, 8, _, _, _, 7, _, _, 7, _, 8, 8, 8, 9],
    [8, 1, 1, 7, _, _, _, _, _, 9, _, _, _, 7, 1, 1],
    [8, 8, 9, 7, _, _, _, _, _, _, _, 9, _, 9, 7, 1],
    [8, _, _, _, _, _, _, 8, _, _, _, 8, _, _, _, 8],
    [7, _, 6, _, _, _, _, _, _, _, 8, _, _, _, _, 7],
    [8, _, _, _, _, _, 6, _, _, _, _, _, _, _, _, 6],
    [6, _, _, 9, _, 7, _, 8, _, _, _, 6, _, _, _, 8],
    [7, _, _, _, _, _, 8, _, _, _, _, _, _, _, _, 7],
    [9, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 6],
    [8, _, _, _, _, _, _, _, 9, _, _, _, _, _, _, 6],
    [8, 7, 8, 6, 7, 8, 9, 6, 10, 10, 7, 6, 8, 9, 10, 3],
]
mini_map5 = [
    [1, 1, 1, 1, 1, 1],
    [1, _, _, _, _, 1],
    [1, _, _, _, _, 1],
    [1, 1, 1, 1, 1, 1],
    [1, _, _, _, _, 1],
    [1, _, _, _, _, 1],
    [1, 1, 1, 1, 1, 1],
]

class Map:
    def __init__(self, game):
        self.game = game
        self.mini_map = mini_map
        self.world_map = {}
        self.rows = len(self.mini_map)
        self.cols = len(self.mini_map[0])
        self.maps = (
            mini_map,
            mini_map2,
            mini_map3,
            mini_map4,
            mini_map5,
        )
        self.get_map()

    def get_map(self):
        for j, row in enumerate(self.maps[self.game.current_lvl]):
            for i, value in enumerate(row):
                if value:
                    self.world_map[(i, j)] = value

    def draw(self):
        [pg.draw.rect(self.game.screen, 'darkgray', (pos[0] * 100, pos[1] * 100, 100, 100), 2)
         for pos in self.world_map]