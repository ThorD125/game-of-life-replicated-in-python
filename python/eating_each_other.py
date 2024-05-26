import random
from collections import Counter as counter
import time
import sys

def show(grid):
    for row in grid:
        for col in row:
            print(f"{col} ", end="")
        print(f"")

def get_location(x, y):
    if x < 0:
        x = 0
    if x >= size_x:
        x = size_x - 1
    if y < 0:
        y = 0
    if y >= size_y:
        y = size_y - 1
    return (x, y)

def get_color_location(x, y):
    return grid_array[y][x]

def count_in_list(list):
    return counter(list)

def get_neighbors(x, y):
    neighbor_list = []
    for dx, dy in neighbors:
        nx, ny = get_location(x + dx, y + dy)
        if (nx, ny) != (x, y):
            neighbor_list.append(get_color_location(nx, ny))
    return count_in_list(neighbor_list)
        
def create_evolve_grid(grid):
    new_grid = []
    for y in range(size_y):
        row = []
        for x in range(size_x):
            row.append(get_neighbors(x, y).most_common(1)[0][0])
        new_grid.append(row)
    return new_grid

def count_grid(grid):
    count = {}
    for char in chars:
        count[char] = 0
    for row in grid:
        for col in row:
            count[col] += 1
    return count

def generate_grid(size_y, size_x, chars):
    grid_array = []
    for y in range(size_y):
        row = []
        for x in range(size_x):
            char = chars[random.randint(0, len(chars)-1)]
            row.append(char)
        grid_array.append(row)
    return grid_array

neighbors = (
    (-1, -1),  
    (-1, 0),  
    (-1, 1),  
    (0, -1),  
    (0, 1),  
    (1, -1),  
    (1, 0),  
    (1, 1),  
)

frames_per_second = 30
chars = ["\033[31mr\033[0m", "\033[32mg\033[0m", "\033[33mb\033[0m", "\033[34my\033[0m", "\033[35mo\033[0m", "\033[36mp\033[0m", "\033[37mc\033[0m", "\033[30mm\033[0m"]

size_x = 50
size_y = 10

if len(sys.argv) > 1:
    size_x = int(sys.argv[1])
    size_y = int(sys.argv[2])

grid_array = generate_grid(size_y, size_x, chars)

show(grid_array)

old_counts = []


print("\033[H\033[J", end="")
show(grid_array)



while True:
    print("\033[H\033[J", end="")
    new_grid = create_evolve_grid(grid_array)
    show(new_grid)
    grid_array = new_grid

    new_count = count_grid(grid_array)
    if new_count in old_counts:
        break
    old_counts.append(new_count)
    old_counts = old_counts[-2:]

    time.sleep(1 / frames_per_second)
