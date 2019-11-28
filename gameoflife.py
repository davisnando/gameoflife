import numpy as np
import random
from typing import Tuple, List, Any

class GameOfLife:

    def __init__(self,rules: List[Any], world = None, world_shape: Tuple[int, int]=(50, 50)):
        if world is None:
            world = self.gen_world(world_shape)
        self.world = world
        self.rules = rules
        self.max_age = 6
        self.min_age = 0

    def gen_world(self, world_shape: Tuple[int, int]):
        world = []
        for i in range(world_shape[0]):
            line = []
            for j in range(world_shape[1]):
                line.append(random.randint(0, 1))
            world.append(line)
        return np.array(world)
    

    def get_neighbors(self, index: Tuple[int, int]):
        rowNumber = index[0]
        columnNumber = index[1]
        neighbors = []
        for i in range(columnNumber-1, columnNumber+2):
            row = []
            for j in range(rowNumber-1, rowNumber+2):
                if i >= 0 and i < len(self.world) and j >= 0 and j < len(self.world):
                    if self.world[i][j] > 0:
                        row.append(1)
                    else:
                        row.append(0)
                else:
                    row.append(0)
            neighbors.append(row)
        return np.array(neighbors)
    

    def count_neighbors(self, neighbours_matrix):
        count = neighbours_matrix.sum()
        # remove middle because thats the object self
        count = count - neighbours_matrix[1][1]
        return count
    

    def new_value(self, index=Tuple[int, int]):
        value = self.world[index]
        for rule in self.rules:
            value = rule(self, value, index)
        
        return value