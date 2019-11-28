from gameoflife import GameOfLife
from typing import Tuple
from time import sleep

def underpopulation(gl: GameOfLife, value: int, index: Tuple[int, int]):
    neighbors = gl.get_neighbors(index)
    count = gl.count_neighbors(neighbors)
    if count <= 2:
        return 0
    return value

def overpopulation(gl: GameOfLife, value: int, index: Tuple[int, int]):
    neighbors = gl.get_neighbors(index)
    count = gl.count_neighbors(neighbors)
    if count > 3:
        return 0 if value <= 0 else value -1
    return value

def birth(gl: GameOfLife, value: int, index: Tuple[int, int]):
    neighbors = gl.get_neighbors(index)
    count = gl.count_neighbors(neighbors)
    
    if count == 3:
        return 1
    return value

def aging(gl: GameOfLife, value: int, index: Tuple[int, int]):
    value = gl.world[index]
    if value > gl.min_age:
        value = value + 1
    
    if value >= gl.max_age:
        value = 0
    return value

if __name__ == "__main__":
    gl = GameOfLife([underpopulation, overpopulation, birth, aging], world=None, world_shape=(10,10))
    while True:
        for i in range(len(gl.world)):
            for j in range(len(gl.world[0])):
                gl.world[i][j] = gl.new_value((i,j))
        print(gl.world)
        sleep(5)
