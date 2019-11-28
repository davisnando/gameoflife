import pytest
import numpy as np
from gameoflife import GameOfLife

@pytest.fixture
def world_single():
    world = np.array([[1, 0, 0], 
                      [1, 1, 0], 
                      [1, 0, 0]])
    return world

@pytest.fixture
def world():
    world = np.array(
        [
            [1, 0, 0, 0, 0, 1, 0,],
            [1, 1, 0, 1, 0, 0, 0,],
            [1, 0, 1, 0, 0, 0, 0,],
            [1, 1, 0, 0, 1, 0, 0,],
            [1, 0, 1, 0, 1, 0, 0,],
            [1, 0, 0, 0, 0, 1, 0,],
            [1, 0, 1, 0, 0, 1, 0,],
            [1, 0, 0, 1, 0, 0, 0,],
        ]
    )
    return world


@pytest.fixture
def rules():
    def give_1(gl, value, index):
        return 1
    return [give_1]

def test_get_neighbors(rules, world, world_single):
    gl = GameOfLife(rules, world_single)

    neighbors = gl.get_neighbors((1, 1))
    assert world_single.all() == np.array(neighbors).all()
    assert world_single.shape == (3, 3)


def test_count_neighbors(rules, world, world_single):
    gl = GameOfLife(rules, world_single)
    neighbors = gl.get_neighbors((1, 1))
    count = gl.count_neighbors(neighbors)

    assert count == 3

    gl.world = world
    neighbors = gl.get_neighbors((0,0))
    count = gl.count_neighbors(neighbors)
    assert count == 2

def test_gen_world(rules):
    gl = GameOfLife(rules)
    shape = (50, 50)
    w = gl.gen_world(shape)
    assert w.shape == shape

    shape = (20, 50)
    w = gl.gen_world(shape)
    assert w.shape == shape


def test_new_value(rules):
    gl = GameOfLife(rules)
    assert gl.new_value((1, 1)) == 1
    assert gl.new_value((0, 0)) == 1